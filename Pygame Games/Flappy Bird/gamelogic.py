import settings as s

def scrollground():
    s.groundx -= s.groundspeed
    if s.groundx <= -s.ground.get_width():
        s.groundx = 0

def blitbg():
    s.screen.blit(s.bg, (0, 0))

def blitground():
    y = s.groundy
    w = s.ground.get_width()
    s.screen.blit(s.ground, (s.groundx, y))
    s.screen.blit(s.ground, (s.groundx + w, y))
