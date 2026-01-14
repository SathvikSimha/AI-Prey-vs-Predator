# ai_predator.py
from math import inf
from settings import *
from grid import Grid
from player import Player

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

class AIPredator(Player):
    """
    AI-controlled Predator.
    Uses minimax with alpha-beta pruning to chase the human prey.
    """

    def decide_and_move(self, grid: Grid, prey_pos, depth=2):
        start_state = (self.x, self.y, prey_pos[0], prey_pos[1])

        best_score = -inf
        best_move = (self.x, self.y)

        # For predator's possible moves (MAX player)
        for nx, ny in grid.get_neighbors((self.x, self.y)) + [(self.x, self.y)]:
            score = minimax(
                grid,
                (nx, ny, prey_pos[0], prey_pos[1]),
                depth - 1,
                alpha=-inf,
                beta=inf,
                maximizing=False
            )
            if score > best_score:
                best_score = score
                best_move = (nx, ny)

        self.x, self.y = best_move


def get_neighbors_including_stay(grid: Grid, pos):
    return grid.get_neighbors(pos) + [pos]


def evaluate_state(state):
    """
    State = (pred_x, pred_y, prey_x, prey_y)
    Lower distance is better for predator.
    """
    px, py, hx, hy = state
    d = manhattan((px, py), (hx, hy))
    # Predator wants distance small, so score = -d
    return -d


def minimax(grid: Grid, state, depth, alpha, beta, maximizing):
    """
    Simple minimax for predator (MAX) vs prey (MIN).
    State = (pred_x, pred_y, prey_x, prey_y)
    """
    pred_x, pred_y, prey_x, prey_y = state

    # Terminal: predator caught prey
    if (pred_x, pred_y) == (prey_x, prey_y):
        return 1000  # big win for predator

    if depth == 0:
        return evaluate_state(state)

    if maximizing:
        # Predator's turn (MAX)
        max_eval = -inf
        for nx, ny in get_neighbors_including_stay(grid, (pred_x, pred_y)):
            new_state = (nx, ny, prey_x, prey_y)
            eval = minimax(grid, new_state, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        # Prey's turn (MIN) – assumes prey tries to maximize distance
        min_eval = inf
        for nx, ny in get_neighbors_including_stay(grid, (prey_x, prey_y)):
            new_state = (pred_x, pred_y, nx, ny)
            eval = minimax(grid, new_state, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval
