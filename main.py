import pygame
import random
import time

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Aim Trainer")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Cosmic", 36)


points = 0
target_radius = 20
target_position = (random.randint(target_radius, SCREEN_WIDTH - target_radius), random.randint(target_radius, SCREEN_HEIGHT - target_radius))
target_start_time = time.time()


def draw_crosshair():
    crosshair_thickness = 2
    crosshair_gap = 6
    crosshair_length = 14
    crosshair_color = "black"

    crosshair_lines_positions = [
        (pygame.mouse.get_pos()[0] - crosshair_gap / 2 - crosshair_length, pygame.mouse.get_pos()[1]),
        (pygame.mouse.get_pos()[0] - crosshair_gap / 2, pygame.mouse.get_pos()[1]),
        (pygame.mouse.get_pos()[0] + crosshair_gap / 2, pygame.mouse.get_pos()[1]),
        (pygame.mouse.get_pos()[0] + crosshair_gap / 2 + crosshair_length, pygame.mouse.get_pos()[1]),
        (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1] - crosshair_gap / 2 - crosshair_length),
        (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1] - crosshair_gap / 2),
        (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1] + crosshair_gap / 2),
        (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1] + crosshair_gap / 2 + crosshair_length)
    ]

    pygame.mouse.set_visible(False)
    for i in range(0, len(crosshair_lines_positions), 2):
        pygame.draw.line(screen, crosshair_color, crosshair_lines_positions[i], crosshair_lines_positions[i + 1], crosshair_thickness)


def draw_target():
    pygame.draw.circle(screen, "red", target_position, target_radius)


def draw_points():
    points_text = font.render(f"Points: {points}", True, "black")
    screen.blit(points_text, (10, 10))


running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            distance = ((mouse_x - target_position[0]) ** 2 + (mouse_y - target_position[1]) ** 2) ** 0.5
            if distance <= target_radius:
                reaction_time = time.time() - target_start_time
                points += max(10 - int(reaction_time * 10), 1)
                target_position = (random.randint(target_radius, SCREEN_WIDTH - target_radius),
                                   random.randint(target_radius, SCREEN_HEIGHT - target_radius))
                target_start_time = time.time()
            else:
                points -= 5
                target_position = (random.randint(target_radius, SCREEN_WIDTH - target_radius),
                                   random.randint(target_radius, SCREEN_HEIGHT - target_radius))
                target_start_time = time.time()

    screen.fill("silver")
    draw_target()
    draw_crosshair()
    draw_points()
    pygame.display.update()
    clock.tick(60)


pygame.quit()
