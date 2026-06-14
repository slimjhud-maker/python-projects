import pygame, os

screenwidth = 900
screenheight = 500

screen = None
running = True
gameon = False

DIR = os.path.dirname(__file__)

bg = pygame.image.load(DIR + r"\Flappy Bird Assets\bg.png")
bg = pygame.transform.scale(bg, (screenwidth, screenheight))

ground = pygame.image.load(DIR + r"\Flappy Bird Assets\ground.png")
groundx = 0
groundy = screenheight - ground.get_height()
groundspeed = 0.8
