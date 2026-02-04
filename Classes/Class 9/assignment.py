import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball")

ball_radius = 20
ball_color = ("Red")
ball_x = WIDTH // 2
ball_y = HEIGHT // 2

dx = 2
dy = 2
angle_deg = 45

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ball_x += dx
    ball_y += dy

    if ball_x - ball_radius <= 0 or ball_x + ball_radius >= WIDTH:
        dx = -dx
        if dx > 0 and dy > 0: angle_deg = 45
        elif dx > 0 and dy < 0: angle_deg = 315
        elif dx < 0 and dy > 0: angle_deg = 135
        else: angle_deg = 225
    else:
        angle_deg = angle_deg

    if ball_y - ball_radius <= 0 or ball_y + ball_radius >= HEIGHT:
        dy = -dy
        if dx > 0 and dy > 0: angle_deg = 45
        elif dx > 0 and dy < 0: angle_deg = 315
        elif dx < 0 and dy > 0: angle_deg = 135
        else: angle_deg = 225
    else:
        angle_deg = angle_deg

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, ball_color, (int(ball_x), int(ball_y)), ball_radius)

    pygame.display.flip()

pygame.quit()