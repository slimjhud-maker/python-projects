import pygame
import random
import settings as s

class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.pipeImg = pygame.image.load(s.DIR + s.obstacleImgPath)
        self.pipeImg = pygame.transform.scale(self.pipeImg, (80, 500))

        gap = 160
        offset = random.randint(-150, 150)

        self.topPipe = pygame.transform.flip(self.pipeImg, False, True)
        self.bottomPipe = self.pipeImg

        cx = s.screenwidth + 60
        mid = (0 + s.groundy) // 2

        self.topRect = self.topPipe.get_rect(midbottom=(cx, mid - gap//2 + offset))
        self.bottomRect = self.bottomPipe.get_rect(midtop=(cx, mid + gap//2 + offset))

        self.topMask = pygame.mask.from_surface(self.topPipe)
        self.bottomMask = pygame.mask.from_surface(self.bottomPipe)

        self.speed = 5

    def update(self):
        self.topRect.x -= self.speed
        self.bottomRect.x -= self.speed
        if self.topRect.right < 0:
            self.kill()

    def draw(self, screen):
        screen.blit(self.topPipe, self.topRect)
        screen.blit(self.bottomPipe, self.bottomRect)
