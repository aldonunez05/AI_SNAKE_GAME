#!/usr/bin/env python3
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

score = 0

snake = [(5, 5)]
direction = "RIGHT"
food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

font = pygame.font.SysFont('Arial', 40)

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

def flood_fill_area(start, obstacles):
    visited = {start}
    queue = [start]
    while queue:
        current = queue.pop()
        for move in DIRECTIONS.values():
            neighbor = (current[0] + move[0], current[1] + move[1])
            if (0 <= neighbor[0] < GRID_WIDTH and 0 <= neighbor[1] < GRID_HEIGHT and
                    neighbor not in obstacles and neighbor not in visited):
                visited.add(neighbor)
                queue.append(neighbor)
    return len(visited)

def simulate_eating(snake_body, path, target_food):
    sim = list(snake_body)
    for step in path:
        sim.insert(0, step)
        if step != target_food:
            sim.pop()
    return sim

def is_path_safe(snake_body, target_food, path):
    sim = simulate_eating(snake_body, path, target_food)
    tail = sim[-1]
    body_without_tail = set(sim[:-1])
    return bool(a_star_path(sim[0], tail, body_without_tail))

def safest_move(snake_body):
    body_without_tail = set(snake_body[:-1])
    best_move = direction
    best_area = -1
    for key, move in DIRECTIONS.items():
        neighbor = (snake_body[0][0] + move[0], snake_body[0][1] + move[1])
        if (0 <= neighbor[0] < GRID_WIDTH and 0 <= neighbor[1] < GRID_HEIGHT and
                neighbor not in body_without_tail):
            area = flood_fill_area(neighbor, body_without_tail)
            if area > best_area:
                best_area = area
                best_move = key
    return best_move

def get_next_move():
    path = a_star_path(snake[0], food, set(snake))
    if path and is_path_safe(snake, food, path):
        next_step = path[0]
        for key, move in DIRECTIONS.items():
            if (snake[0][0] + move[0], snake[0][1] + move[1]) == next_step:
                return key
    return safest_move(snake)

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
        print(f"Game Over! Score: {score}")
        running = False
    else:
        snake.insert(0, new_head)
        if new_head == food:
            score += 1
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

with open('snake_scores.txt', 'a') as f:
    f.write(str(score) + '\n')
