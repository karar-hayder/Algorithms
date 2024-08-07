import pygame
import time
from AStar import create_grid,Point
from random import randint
import math

class A_Star:
    def __init__(self, grid) -> None:
        self.grid: list[list[Point]] = grid
        self.__find_nearby()
        self.open_list = []
        self.closed_list = set()
        self.start_point = None
        self.end_point = None

    def initialize(self, start_cord: tuple[int, int], end_cord: tuple[int, int]):
        self.start_point = self.grid[start_cord[1]][start_cord[0]]
        self.end_point = self.grid[end_cord[1]][end_cord[0]]
        self.start_point.g = 0
        self.start_point.f = self.__calc_heuristic(self.start_point)
        self.open_list.append(self.start_point)
        self.closed_list = set()

    def step(self):
        if not self.open_list:
            return None, True
        self.open_list.sort(key=lambda p: p.f)
        current_point = self.open_list.pop(0)
        if current_point.visited:
            return None, False
        current_point.visited = True

        if current_point == self.end_point:
            return self.__return_path(), True

        for point in current_point.nearby_points:
            if point.blocked or point.visited:
                continue

            tentative_g_score = current_point.g + self.__cost_from_start_to_n(current_point, point)
            if tentative_g_score < point.g:
                point.prev = current_point
                point.g = tentative_g_score
                point.h = self.__calc_heuristic(point)
                point.f = point.g + point.h

                if point not in self.closed_list:
                    self.open_list.append(point)
                    self.closed_list.add(point)

        return None, False

    def __cost_from_start_to_n(self, current: Point, neighbor: Point):
        return math.dist(current.get_cord(), neighbor.get_cord())

    def __calc_heuristic(self, n: Point):
        return math.dist(n.get_cord(), self.end_point.get_cord())

    def __find_nearby(self):
        for y, row in enumerate(self.grid):
            for x, point in enumerate(row):
                for y2 in range(-1, 2):
                    for x2 in range(-1, 2):
                        if x2 == 0 and y2 == 0:
                            continue
                        if not self.__check_bounds(x, y, x2, y2):
                            near_point = self.grid[y + y2][x + x2]
                            point.nearby_points.append(near_point)

    def __check_bounds(self, x, y, x2, y2):
        return y + y2 < 0 or y + y2 >= len(self.grid) or x + x2 < 0 or x + x2 >= len(self.grid[0])

    def __return_path(self):
        path = list()
        current: Point = self.end_point
        while current != self.start_point:
            path.append(current)
            current = current.prev
        path.append(self.start_point)
        return path[::-1]


ROWS, COLS = 50, 50
WIDTH, HEIGHT = 600, 600
CELL_SIZE = WIDTH // COLS

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("A* Algorithm Visualization")

def draw_grid(win, grid, path):
    for row in grid:
        for point in row:
            color = WHITE
            if point.blocked:
                color = BLACK
            elif point == A.start_point:
                color = GREEN
            elif point == A.end_point:
                color = RED
            elif point.visited and point not in path:
                color = YELLOW
            elif point in path:
                color = BLUE
            pygame.draw.rect(win, color, (point.x * CELL_SIZE, point.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(win, BLACK, (point.x * CELL_SIZE, point.y * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

def main():
    global A
    A = A_Star(create_grid(50, 50))
    start_cord = (0, 0)
    end_cord = (38, 49)
    
    # Blocking some points for demonstration
    for i in range(50):
        if randint(0, 50) <= 30:
            x, y = randint(0, 49), randint(0, 49)
            A.grid[y][x].blocked = True
    
    A.initialize(start_cord, end_cord)
    
    path = []
    running = True
    found = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if not found:
            path, found = A.step()

        win.fill(WHITE)
        draw_grid(win, A.grid, path if path else [])
        pygame.display.flip()
        
        time.sleep(0.01)

    pygame.quit()

if __name__ == "__main__":
    main()