import pygame
pygame.init()
w = 800
h = 600
background = pygame.image.load(r"C:\Users\raghd\Downloads\night 2.png")
background = pygame.transform.scale(background,(w,h))

screen = pygame.display.set_mode((w,h))
pygame.display.set_caption("Pong Game")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0, 0, 0))
    pygame.display.flip()
pygame.quit()