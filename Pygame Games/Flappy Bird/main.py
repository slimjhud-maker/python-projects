import pygame
import settings as s
import gamelogic as g
import flappy as f
import obstacles as o

pygame.init()

s.screen = pygame.display.set_mode((s.screenwidth, s.screenheight))

s.bg = pygame.image.load(s.DIR + s.bgImgPath)
s.bg = pygame.transform.scale(s.bg, (s.screenwidth, s.screenheight))

s.ground = pygame.image.load(s.DIR + s.groundImgPath)
s.ground = pygame.transform.scale(s.ground, (s.screenwidth + 100, 100))
s.groundy = s.screenheight - s.ground.get_height()

s.flappy = f.Flappy()
s.playerGr.add(s.flappy)

SPAWNPIPE = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWNPIPE, s.pipeSpawnSpeed)

while s.running:
    s.clock.tick(s.FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            s.running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if s.gameon:
                    s.flappy.flap()
                else:
                    s.gameon = True

        if event.type == SPAWNPIPE and s.gameon:
            s.obstacleGr.add(o.Obstacle())

    if s.gameon:
        g.moveOnGameStarts()

    g.blitGameComponents()
    pygame.display.update()
