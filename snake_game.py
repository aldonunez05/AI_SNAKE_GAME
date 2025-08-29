# pylint: disable=no-member

import pygame
import random
import heapq

pygame.init()

WIDTH, HEIGHT = 500, 500
CELL_SIZE = 20
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

DIRECTIONS = {"UP": (0, -1), "DOWN": (0, 1), "LEFT": (-1, 0), "RIGHT": (1, 0)}

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AI Snake Game")

snake = [(5, 5)]
direction = "RIGHT"
food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

# A* Pathfinding Function
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star_path(start, goal, obstacles):
    frontier = []
    heapq.heappush(frontier, (0, start))
    came_from = {start: None}
    cost_so_far = {start: 0}

    while frontier:
        _, current = heapq.heappop(frontier)
        
        if current == goal:
            break
        
        for move in DIRECTIONS.values():
            neighbor = (current[0] + move[0], current[1] + move[1])
            
            if (0 <= neighbor[0] < GRID_WIDTH and 0 <= neighbor[1] < GRID_HEIGHT and
                    neighbor not in obstacles and neighbor not in cost_so_far):
                cost_so_far[neighbor] = cost_so_far[current] + 1
                priority = cost_so_far[neighbor] + heuristic(neighbor, goal)
                heapq.heappush(frontier, (priority, neighbor))
                came_from[neighbor] = current
    
    path = []
    current = goal
    while current in came_from and came_from[current] is not None:
        path.append(current)
        current = came_from[current]
    path.reverse()
    return path

def get_next_move():
    path = a_star_path(snake[0], food, set(snake))
    if path:
        next_step = path[0]
        for key, move in DIRECTIONS.items():
            if (snake[0][0] + move[0], snake[0][1] + move[1]) == next_step:
                return key
    return direction  # Default to current direction if no path

clock = pygame.time.Clock()
running = True
while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    direction = get_next_move()
    
    new_head = (snake[0][0] + DIRECTIONS[direction][0], snake[0][1] + DIRECTIONS[direction][1])
    if new_head in snake or not (0 <= new_head[0] < GRID_WIDTH and 0 <= new_head[1] < GRID_HEIGHT):
        print("Game Over!")
        running = False
    else:
        snake.insert(0, new_head)
        if new_head == food:
            food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
            while food in snake:
                food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        else:
            snake.pop()
    
    pygame.draw.rect(screen, RED, (food[0] * CELL_SIZE, food[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    
    
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    
    pygame.display.flip()

    clock.tick(10)

pygame.quit()
