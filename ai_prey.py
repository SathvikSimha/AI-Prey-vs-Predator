# ai_prey.py
import heapq
from settings import *
from grid import Grid
from player import Player

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

class AIPrey(Player):
    """
    AI-controlled Prey.
    Escapes from the human predator using A* pathfinding.
    """

    def decide_and_move(self, grid: Grid, predator_pos):
        start = (self.x, self.y)

        # Choose a goal: farthest free tile from predator
        best_goal = None
        best_dist = -1

        for x in range(GRID_SIZE):
            for y in range(GRID_SIZE):
                if grid.is_walkable(x, y):
                    d = manhattan((x, y), predator_pos)
                    if d > best_dist:
                        best_dist = d
                        best_goal = (x, y)

        if best_goal is None or best_goal == start:
            # No better place to go
            return

        path = a_star(grid, start, best_goal)
        if path and len(path) > 1:
            # path[0] is current pos, path[1] is next step
            nx, ny = path[1]
            # Move one step along path
            self.x, self.y = nx, ny


def a_star(grid: Grid, start, goal):
    """Basic A* search on the grid."""
    open_set = []
    heapq.heappush(open_set, (0, start))

    came_from = {}
    g_score = {start: 0}

    def h(pos):
        return manhattan(pos, goal)

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            # reconstruct path
            return reconstruct_path(came_from, current)

        for neighbor in grid.get_neighbors(current):
            tentative_g = g_score[current] + 1
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score = tentative_g + h(neighbor)
                heapq.heappush(open_set, (f_score, neighbor))

    return None  # no path


def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path
