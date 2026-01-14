import pygame
import random
from settings import *

class Grid:
    def __init__(self):
        self.obstacles = set()
        self.generate_obstacles()

    def generate_obstacles(self, count=40):
        """Generate random obstacles."""
        self.obstacles.clear()
        for _ in range(count):
            x = random.randint(0, GRID_SIZE-1)
            y = random.randint(0, GRID_SIZE-1)
            self.obstacles.add((x, y))

    def draw(self, surface):
        for x in range(GRID_SIZE):
            for y in range(GRID_SIZE):
                rect = pygame.Rect(x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE)

                if (x, y) in self.obstacles:
                    pygame.draw.rect(surface, DARK_GREY, rect)
                else:
                    pygame.draw.rect(surface, GREY, rect, 1)

    def is_walkable(self, x, y):
        return (0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE and (x, y) not in self.obstacles)

    def get_neighbors(self, pos):
        x, y = pos
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        neighbors = []
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if self.is_walkable(nx, ny):
                neighbors.append((nx, ny))
        return neighbors
