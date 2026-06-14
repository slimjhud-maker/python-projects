import pygame, math
pygame.init()
height, width = 500, 500
screen = pygame.display.set_mode((width,height))

pygame.display.set_caption("Vertical bouncing")
img = pygame.image.load(r"C:\Users\raghd\Downloads\ftgr.png")
img = pygame.transform.scale(img,(width,height))

class Earth(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # image, rect, update
        self.loadedImage = pygame.image.load(r"C:\Users\raghd\Downloads\rb_.png")
        self.loadedImage = pygame.transform.scale(self.loadedImage,(100,100))
        self.image = self.loadedImage
        self.image = pygame.transform.scale(self.loadedImage,(100,100))
        self.rect = self.image.get_rect(center=(width//2,height//2))
        self.angle = 1
        self.startingscale = 1
    def update(self):
        Oldcenter = self.rect.center
        self.angle = (self.angle + 1) %360
        scale = self.startingscale + 1*math.sin(math.radians(self.angle))
        self.image = pygame.transform.rotozoom(self.loadedImage, self.angle, scale= scale)
        self.rect = self.image.get_rect(center=Oldcenter)
    
        
        
ball = Earth()
earthGr = pygame.sprite.Group()
earthGr.add(ball)

runing = True
while runing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False
            
    screen.blit(img,(0,0))
    earthGr.draw(screen)
    earthGr.update()
    pygame.display.update()