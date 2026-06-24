import pygame
import settings as s

class Flappy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.birdImg = []
        self.loadImages()
        self.frame = 0
        self.image = self.birdImg[0]
        self.rect = self.image.get_rect(center=(100, s.screenheight//2))
        self.mask = pygame.mask.from_surface(self.image)
        self.vel = 0
        self.jumpower = -8
        self.gravity = 0.4

    def loadImages(self):
        for i in range(1, 4):
            img = pygame.image.load(s.DIR + s.flappyImgPath + str(i) + ".png")
            img = pygame.transform.scale(img, (50, 50))
            self.birdImg.append(img)

    def handleFrameCount(self):
        self.frame += 0.2
        if self.frame >= len(self.birdImg):
            self.frame = 0
        self.image = self.birdImg[int(self.frame)]
        self.mask = pygame.mask.from_surface(self.image)

    def flap(self):
        self.vel = self.jumpower

    def update(self):
        self.handleFrameCount()
        self.vel += self.gravity
        self.rect.y += self.vel
        if self.rect.bottom >= s.groundy:
            self.rect.bottom = s.groundy
            self.vel = 0
