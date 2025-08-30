import numpy as np
import heapq
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# -----------------------
# Parámetros del entorno
# -----------------------
WORLD_MIN = 0.0
WORLD_MAX = 15.0
GRID_RES = 0.25            # resolución del grid (menor => A* más caro)
ROBOT_RADIUS = 0.4        # radio para inflar obstáculos
INFLATION = ROBOT_RADIUS + 0.1

# Potenciales / seguimiento local
K_ATTR = 0.9              # ganancia hacia waypoint
K_REP = 1.8               # ganancia repulsiva local
REPULSION_RAD = 1.2       # radio de influencia repulsiva (m)
MAX_STEP = 0.18           # paso máximo por iteración

# Replan / stuck detection
STUCK_WINDOW = 14         # ventana para detectar estancamiento
STUCK_POS_MOV = 0.15      # movimiento mínimo esperado en ventana
REPLAN_LIMIT = 8          # cuántas replanificaciones máximo antes de fallback

# -----------------------
# Obstáculos: herradura (usa tus puntos)
# -----------------------
def create_herradura_obstacles():
    return np.array([
        [2, 2],[2, 3], [2, 4],[2, 5],[2, 6],[2, 7],[2, 8],[2, 9], [2, 10],
        [10, 10],[10, 9],[10, 8],[10, 7],[10, 6],[10, 5],[10, 4],[10, 3],[10, 2],
        [9, 2], [9, 3],[9, 4],[9, 5],[9, 6],[9, 7],[9, 8],[9, 9],
        [3, 9],[3, 8],[3, 7],[3, 6],[3, 5],[3, 4],[3, 3], [3, 2],
        [4,9],[5,9],[6,9],[7,9],[8,9],[3,10],[4,10],[5,10],[6,10],
        [7,10],[8,10],[9,10]
    ])

# -----------------------
# Grid utilities
# -----------------------
def build_grid(obstacles_world, grid_res=GRID_RES, inflation=INFLATION):
    nx = int((WORLD_MAX - WORLD_MIN) / grid_res) + 1
    ny = nx
    occ = np.zeros((nx, ny), dtype=np.bool_)
    xs = np.linspace(WORLD_MIN, WORLD_MAX, nx)
    ys = np.linspace(WORLD_MIN, WORLD_MAX, ny)
    # marcar celdas ocupadas por puntos de obstáculo (inflados)
    xv = np.repeat(xs[:, None], ny, axis=1)
    yv = np.repeat(ys[None, :], nx, axis=0)
    for ox, oy in obstacles_world:
        dist = np.sqrt((xv - ox)**2 + (yv - oy)**2)
        occ |= (dist <= inflation)
    return occ, xs, ys

def world_to_grid(p, xs, ys):
    ix = int(np.round((p[0] - WORLD_MIN) / (xs[1] - xs[0])))
    iy = int(np.round((p[1] - WORLD_MIN) / (ys[1] - ys[0])))
    ix = np.clip(ix, 0, len(xs)-1)
    iy = np.clip(iy, 0, len(ys)-1)
    return ix, iy

def grid_to_world(ix, iy, xs, ys):
    return np.array([xs[ix], ys[iy]])

# -----------------------
# A* planner (8-connected)
# -----------------------
def astar(occ, start_world, goal_world, xs, ys):
    sx, sy = world_to_grid(start_world, xs, ys)
    gx, gy = world_to_grid(goal_world, xs, ys)
    nx, ny = occ.shape

    if occ[sx, sy] or occ[gx, gy]:
        return None

    def heuristic(a, b):
        return np.hypot(b[0]-a[0], b[1]-a[1])

    start = (sx, sy)
    goal = (gx, gy)

    open_set = []
    heapq.heappush(open_set, (0.0, start))
    came_from = {}
    gscore = {start: 0.0}
    fscore = {start: heuristic(start, goal)}

    neighbors = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]
    while open_set:
        _, current = heapq.heappop(open_set)
        if current == goal:
            # reconstruct path
            path = []
            node = current
            while node in came_from:
                path.append(node)
                node = came_from[node]
            path.append(start)
            path.reverse()
            path_world = [grid_to_world(ix, iy, xs, ys) for ix, iy in path]
            return np.array(path_world)
        for dx, dy in neighbors:
            nxp = current[0] + dx
            nyp = current[1] + dy
            if nxp < 0 or nxp >= nx or nyp < 0 or nyp >= ny:
                continue
            if occ[nxp, nyp]:
                continue
            step_cost = np.hypot(dx, dy)
            tentative_g = gscore[current] + step_cost
            neighbor = (nxp, nyp)
            if tentative_g < gscore.get(neighbor, 1e12):
                came_from[neighbor] = current
                gscore[neighbor] = tentative_g
                f = tentative_g + heuristic(neighbor, goal)
                fscore[neighbor] = f
                heapq.heappush(open_set, (f, neighbor))
    return None

# -----------------------
# Local control: mezcla waypoint-seeking + repulsión local
# -----------------------
def local_control_towards(agent_pos, waypoint, obstacles, k_attr=K_ATTR, k_rep=K_REP,
                          rep_radius=REPULSION_RAD, max_step=MAX_STEP):
    to_wp = waypoint - agent_pos
    dist_wp = np.linalg.norm(to_wp) + 1e-9
    dir_to_wp = to_wp / dist_wp

    rep_vec = np.zeros(2)
    for o in obstacles:
        v = agent_pos - o
        d = np.linalg.norm(v) + 1e-9
        if d < rep_radius:
            rep_strength = (1.0/d - 1.0/rep_radius)
            rep_strength = max(rep_strength, 0.0)
            rep_dir = v / d
            rep_vec += rep_strength * (rep_dir / (d + 1e-9))
    desired = k_attr * dir_to_wp + k_rep * rep_vec
    norm = np.linalg.norm(desired) + 1e-9
    step = desired / norm * min(max_step, norm * max_step)
    return step

# -----------------------
# Stuck detection
# -----------------------
def detect_stuck(pos_history, window=STUCK_WINDOW, mov_thresh=STUCK_POS_MOV):
    if len(pos_history) < window+1:
        return False
    p_old = pos_history[-(window+1)]
    p_new = pos_history[-1]
    moved = np.linalg.norm(p_new - p_old)
    return moved < mov_thresh

# -----------------------
# Main ejecución y animación
# -----------------------
if __name__ == "__main__":
    obstacles = create_herradura_obstacles()
    start = np.array([1.0, 1.0])
    goal = np.array([12.0, 12.0])

    occ, xs, ys = build_grid(obstacles, grid_res=GRID_RES, inflation=INFLATION)

    path = astar(occ, start, goal, xs, ys)
    if path is None:
        raise RuntimeError("No se encontró camino inicial con A*. Revisa inflación/obstáculos.")

    def simplify_path(path_world, step=3):
        if path_world is None:
            return None
        return np.array([path_world[i] for i in range(0, len(path_world), step)] + [path_world[-1]])

    waypoints = simplify_path(path, step=3)

    # Variables a nivel módulo (global para update)
    agent_pos = start.copy()
    pos_history = [agent_pos.copy()]
    hist_modes = []
    hist_pot = []

    current_wp_idx = 0
    replan_count = 0

    fig, (ax, ax2) = plt.subplots(1, 2, figsize=(13,5))
    ax.set_xlim(WORLD_MIN, WORLD_MAX)
    ax.set_ylim(WORLD_MIN, WORLD_MAX)
    ax.set_aspect('equal')

    mode = "FOLLOW_PATH"

    def update(frame):
        # CORRECCIÓN: usar 'global' porque las variables están en el scope del módulo
        global agent_pos, waypoints, current_wp_idx, path, replan_count, mode, pos_history

        # si alcanzó el objetivo
        if np.linalg.norm(agent_pos - goal) < 0.45:
            mode = "ARRIVED"
            pass
        else:
            if waypoints is None or current_wp_idx >= len(waypoints):
                path = astar(occ, agent_pos, goal, xs, ys)
                if path is not None:
                    waypoints = simplify_path(path, step=3)
                    current_wp_idx = 0
                    mode = "REPLAN_OK"
                    replan_count += 1
                else:
                    mode = "REPLAN_FAIL"
                    if replan_count > REPLAN_LIMIT:
                        agent_pos += np.random.randn(2) * 0.15
            else:
                wp = waypoints[current_wp_idx]
                if np.linalg.norm(wp - agent_pos) < 0.5:
                    current_wp_idx += 1
                    mode = "ADVANCE_WP"
                else:
                    step = local_control_towards(agent_pos, wp, obstacles,
                                                 k_attr=K_ATTR, k_rep=K_REP,
                                                 rep_radius=REPULSION_RAD,
                                                 max_step=MAX_STEP)
                    agent_pos = agent_pos + step
                    mode = "FOLLOW_PATH"

        pos_history.append(agent_pos.copy())
        hist_modes.append(mode)

        # detectar stuck -> replan
        if detect_stuck(pos_history, window=STUCK_WINDOW, mov_thresh=STUCK_POS_MOV):
            new_path = astar(occ, agent_pos, goal, xs, ys)
            if new_path is not None:
                waypoints = simplify_path(new_path, step=3)
                current_wp_idx = 0
                replan_count += 1
                mode = "REPLANNED"
            else:
                agent_pos += (np.random.randn(2) * 0.12)
                mode = "PERTURB"

        # Dibujo
        ax.clear()
        ax.set_xlim(WORLD_MIN, WORLD_MAX)
        ax.set_ylim(WORLD_MIN, WORLD_MAX)
        ax.set_title(f"Modo: {mode}  | Replans: {replan_count}")
        ax.scatter(obstacles[:,0], obstacles[:,1], s=65, marker='s', color='black', label='Obstáculos (puntos)')
        occ_x, occ_y = np.where(occ)
        occ_coords = np.array([ [xs[ix], ys[iy]] for ix, iy in zip(occ_x, occ_y)])
        if occ_coords.size > 0:
            ax.scatter(occ_coords[:,0], occ_coords[:,1], s=8, alpha=0.09, color='gray')

        if path is not None:
            ax.plot(path[:,0], path[:,1], linestyle='--', linewidth=1.0, label='Path A*')

        if waypoints is not None:
            ax.scatter(waypoints[:,0], waypoints[:,1], marker='x', color='blue', s=50, label='Waypoints')
            if current_wp_idx < len(waypoints):
                ax.scatter(waypoints[current_wp_idx][0], waypoints[current_wp_idx][1], marker='o', color='cyan', s=80, label='WP actual')

        traj = np.array(pos_history)
        ax.plot(traj[:,0], traj[:,1], color='red', linewidth=1.3, label='Trayectoria')
        ax.scatter(agent_pos[0], agent_pos[1], color='red', s=120, label='Agente')
        ax.scatter(start[0], start[1], marker='D', color='green', s=90, label='Start')
        ax.scatter(goal[0], goal[1], marker='*', color='gold', s=140, label='Goal')
        ax.legend(loc='upper left', fontsize='small')

        ax2.clear()
        dists = [np.linalg.norm(p - goal) for p in pos_history]
        ax2.plot(dists, label='Distancia a goal')
        ax2.set_xlabel('Iteración')
        ax2.set_ylabel('Distancia (m)')
        ax2.set_title('Progreso hacia meta')
        ax2.legend()

    ani = FuncAnimation(fig, update, frames=1200, interval=60)
    plt.tight_layout()
    plt.show()
