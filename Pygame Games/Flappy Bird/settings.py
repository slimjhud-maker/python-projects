import pygame, os

screenwidth = 900
screenheight = 500

screen = None
running = True
gameon = False
FPS = 60
clock = pygame.time.Clock()

DIR = os.path.dirname(__file__)

bg = None
bgImgPath = r"\Flappy Bird Assets\bg.png"
groundImgPath = r"\Flappy Bird Assets\ground.png"
flappyImgPath = r"\Flappy Bird Assets\bird"

ground = None
groundx = 0
groundy = 0
groundspeed = 5

flappy = None
playerGr = pygame.sprite.Group()
