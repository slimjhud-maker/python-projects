import pygame, math, random
pygame.init()

height, width = 500, 600
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()

background = pygame.image.load(r"C:\Users\raghd\Downloads\universeBG2.png")
background = pygame.transform.scale(background,(width,height))

class Star(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.loadedImage = pygame.image.load(r"C:\Users\raghd\Downloads\image (6).png")
        size = random.randint(10,20)
        self.loadedImage = pygame.transform.scale(self.loadedImage,(size,size))
        self.image = self.loadedImage
        self.rect = self.image.get_rect(center=(random.randint(0,width), random.randint(0,height)))
        self.life = random.randint(1,300)
        self.deadTimer = 0
        self.visible = True
    def update(self):
        if self.visible:
            self.life -= 1
            if self.life <= 0:
                self.visible = False
                self.deadTimer = 10
        else:
            self.deadTimer -= 1
            if self.deadTimer <= 0:
                self.__init__()
    def draw(self, surf):
        if self.visible:
            surf.blit(self.image, self.rect)

stars = []
i = 0
while True:
    stars.append(Star())
    i += 1
    if i == 120:
        break

class Sun(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.loadedImage = pygame.image.load(r"C:\Users\raghd\Downloads\sun2.png")
        self.loadedImage = pygame.transform.scale(self.loadedImage,(150,150))
        self.image = self.loadedImage
        self.rect = self.image.get_rect(center=(width//2,height//2))
        self.angle = 1
    def update(self):
        self.angle += 1
        old_center = self.rect.center
        self.image = pygame.transform.rotate(self.loadedImage, self.angle)
        self.image = pygame.transform.rotate(self.image, self.angle)
        self.rect = self.image.get_rect(center=old_center)

class Earth(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.loadedImage = pygame.image.load(r"C:\Users\raghd\Downloads\earth.png")
        self.loadedImage = pygame.transform.scale(self.loadedImage,(100,100))
        self.image = self.loadedImage
        self.rect = self.image.get_rect(center=(0,0))
        self.angle = 1
        self.orbitAngle = 0
        self.orbitRadius = 160
    def update(self):
        self.orbitAngle += 0.8
        x = width//2 + math.cos(math.radians(self.orbitAngle)) * self.orbitRadius
        y = height//2 + math.sin(math.radians(self.orbitAngle)) * self.orbitRadius
        self.rect.center = (x,y)
        self.angle += 1
        old_center = self.rect.center
        self.image = pygame.transform.rotate(self.loadedImage, self.angle)
        self.image = pygame.transform.rotate(self.image, self.angle)
        self.rect = self.image.get_rect(center=old_center)

class Moon(pygame.sprite.Sprite):
    def __init__(self, earth):
        super().__init__()
        self.earth = earth
        self.loadedImage = pygame.image.load(r"C:\Users\raghd\Downloads\moon.png")
        self.loadedImage = pygame.transform.scale(self.loadedImage,(50,50))
        self.image = self.loadedImage
        self.rect = self.image.get_rect(center=(0,0))
        self.angle = 1
        self.orbitAngle = 0
        self.orbitRadius = 50
    def update(self):
        self.orbitAngle += 3
        ex, ey = self.earth.rect.center
        x = ex + math.cos(math.radians(self.orbitAngle)) * self.orbitRadius
        y = ey + math.sin(math.radians(self.orbitAngle)) * self.orbitRadius
        self.rect.center = (x,y)
        self.angle += 1
        old_center = self.rect.center
        self.image = pygame.transform.rotate(self.loadedImage, self.angle)
        self.image = pygame.transform.rotate(self.image, self.angle)
        self.rect = self.image.get_rect(center=old_center)

sun = Sun()
earth = Earth()
moon = Moon(earth)

allSprites = pygame.sprite.Group(sun, earth, moon)

running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background,(0,0))

    j = 0
    while True:
        stars[j].update()
        stars[j].draw(screen)
        j += 1
        if j == len(stars):
            break

    allSprites.update()
    allSprites.draw(screen)

    pygame.display.update()