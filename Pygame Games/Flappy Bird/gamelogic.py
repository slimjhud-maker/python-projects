import pygame
import settings as s

def scrollground():
    s.groundx -= s.groundspeed
    if s.groundx <= -s.ground.get_width():
        s.groundx = 0

def moveOnGameStarts():
    scrollground()
    s.playerGr.update()
    s.obstacleGr.update()
    checkCollision()

def blitGameComponents():
    s.screen.blit(s.bg, (0, 0))
    drawObstacles()
    blitground()
    s.playerGr.draw(s.screen)

    textRender = s.font.render(f"Score: {s.score//15}", True, "black")
    s.screen.blit(textRender, (10,10))

def blitground():
    y = s.groundy
    w = s.ground.get_width()
    s.screen.blit(s.ground, (s.groundx, y))
    s.screen.blit(s.ground, (s.groundx + w, y))

def drawObstacles():
    for obs in s.obstacleGr:
        obs.draw(s.screen)

def checkCollision():
    logicflappy = s.flappy
    for obs in s.obstacleGr:
        if s.flappy.rect.left > obs.topRect.right:
            s.score +=1

            
        offsetTop = (obs.topRect.x - logicflappy.rect.x, obs.topRect.y - logicflappy.rect.y)
        offsetBottom = (obs.bottomRect.x - logicflappy.rect.x, obs.bottomRect.y - logicflappy.rect.y)

        if logicflappy.mask.overlap(obs.topMask, offsetTop):
            s.gameon = False
        if logicflappy.mask.overlap(obs.bottomMask, offsetBottom):
            s.gameon = False


