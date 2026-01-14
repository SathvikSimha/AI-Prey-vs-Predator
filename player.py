import pygame
from settings import *
from grid import Grid

class Player:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw(self, surface):
        rect = pygame.Rect(self.x*TILE_SIZE, self.y*TILE_SIZE, TILE_SIZE, TILE_SIZE)
        pygame.draw.rect(surface, self.color, rect)

    def move(self, dx, dy, grid: Grid):
        new_x = self.x + dx
        new_y = self.y + dy

        # Check valid movement
        if grid.is_walkable(new_x, new_y):
            self.x = new_x
            self.y = new_y
            return True  # Movement happened
        return False     # Movement blocked
