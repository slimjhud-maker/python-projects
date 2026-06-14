import pygame
import settings as s
import gamelogic as g

pygame.init()
s.screen = pygame.display.set_mode((s.screenwidth, s.screenheight))

while s.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            s.running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                s.gameon = not s.gameon

    if s.gameon:
        g.scrollground()

    g.blitbg()
    g.blitground()
    pygame.display.update()
