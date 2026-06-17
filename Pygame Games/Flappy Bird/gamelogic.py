import settings as s

def scrollground():
    s.groundx -= s.groundspeed
    if s.groundx <= -s.ground.get_width():
        s.groundx = 0

def moveOnGameStarts():
    scrollground()
    s.playerGr.update()

def blitGameComponents():
    s.screen.blit(s.bg, (0,0))
    blitground()
    s.playerGr.draw(s.screen)

def blitground():
    y = s.groundy
    w = s.ground.get_width()
    s.screen.blit(s.ground, (s.groundx, y))
    s.screen.blit(s.ground, (s.groundx + w, y))
