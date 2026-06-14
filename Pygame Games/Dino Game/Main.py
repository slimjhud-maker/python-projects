import pygame, time, random
pygame.init()

width, height = 600, 600
groundY = height - 100
groundForDino = height - 80

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

bg = pygame.image.load(r"C:\\Users\\raghd\\OneDrive\\Desktop\\python_projects\\python-projects\\Pygame Games\\Dino Game\\Dino Game Assets\\bg.png")
bg = pygame.transform.scale(bg, (width, height - 100))

groundImg = pygame.image.load(r"C:\\Users\\raghd\\OneDrive\\Desktop\\python_projects\\python-projects\\Pygame Games\\Dino Game\\Dino Game Assets\\ground.png")

obstacle_paths = [
    r"C:\\Users\\raghd\\OneDrive\\Desktop\\python_projects\\python-projects\\Pygame Games\\Dino Game\\Dino Game Assets\\cactus.png",
    r"C:\\Users\\raghd\\OneDrive\\Desktop\\python_projects\\python-projects\\Pygame Games\\Dino Game\\Dino Game Assets\\spikes.png"
]

def collision(a, b):
    for i in b:
        offset = (i.rect.x - a.rect.x, i.rect.y - a.rect.y)
        if a.mask.overlap(i.mask, offset):
            return True
    return False

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, speed):
        super().__init__()
        img = pygame.image.load(random.choice(obstacle_paths))
        w = random.randint(115, 135)
        self.image = pygame.transform.scale(img, (w, 90))
        self.rect = self.image.get_rect()
        self.rect.bottom = groundY
        self.rect.x = width + 100
        self.baseSpeed = speed
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, mult):
        self.rect.x -= self.baseSpeed * mult
        if self.rect.right < 0:
            self.kill()

class Dino(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.runImages = []
        self.idleImages = []
        self.deadImages = []
        self.jumpImages = []
        self.load()
        self.index = 0
        self.wait = 0
        self.image = self.idleImages[0]
        self.rect = self.image.get_rect(center=(200, 0))
        self.rect.bottom = groundForDino
        self.mask = pygame.mask.from_surface(self.image)
        self.state = "idle"
        self.velocity = 0
        self.jumpPower = 20
        self.isJumping = False
        self.xSpeed = 1.45
        self.baseX = 200
        self.deathVel = 0

    def load(self):
        for i in range(1, 9):
            self.runImages.append(pygame.transform.scale(pygame.image.load(fr"C:\\Users\\raghd\\OneDrive\\Desktop\\python_projects\\python-projects\\Pygame Games\\Dino Game\\Dino Game Assets\\Dino Animations\\Run\\Run ({i}).png"), (200, 200)))
        for i in range(1, 9):
            self.idleImages.append(pygame.transform.scale(pygame.image.load(fr"C:\\Users\\raghd\\OneDrive\\Desktop\\python_projects\\python-projects\\Pygame Games\\Dino Game\\Dino Game Assets\\Dino Animations\\Idle\\Idle ({i}).png"), (200, 200)))
        for i in range(1, 9):
            self.deadImages.append(pygame.transform.scale(pygame.image.load(fr"C:\\Users\\raghd\\OneDrive\\Desktop\\python_projects\\python-projects\\Pygame Games\\Dino Game\\Dino Game Assets\\Dino Animations\\Dead\\Dead ({i}).png"), (200, 200)))
        for i in range(1, 13):
            self.jumpImages.append(pygame.transform.scale(pygame.image.load(fr"C:\\Users\\raghd\\OneDrive\\Desktop\\python_projects\\python-projects\\Pygame Games\\Dino Game\\Dino Game Assets\\Dino Animations\\Jump\\Jump ({i}).png"), (200, 200)))

    def animate(self, arr, baseSpeed, mult):
        self.wait += 1
        if self.wait > max(1, int(baseSpeed / mult)):
            self.index += 1
            self.wait = 0
        if self.index >= len(arr):
            self.index = len(arr) - 1 if self.state == "dead" else 0
        self.image = arr[self.index]
        self.mask = pygame.mask.from_surface(self.image)

    def run(self, mult):
        self.animate(self.runImages, 4, mult)

    def idle(self, mult):
        self.animate(self.idleImages, 4, mult)

    def dead(self, mult):
        self.animate(self.deadImages, 4, mult)
        self.rect.y += self.deathVel
        self.deathVel += 1
        if self.rect.bottom >= groundForDino:
            self.rect.bottom = groundForDino

    def jump(self, mult):
        self.animate(self.jumpImages, 6, mult)
        self.rect.y += self.velocity
        self.velocity += 1
        if self.velocity < 0:
            self.rect.x += self.xSpeed * mult
        if self.rect.bottom >= groundForDino:
            self.rect.bottom = groundForDino
            self.isJumping = False
            self.index = 0
            self.state = "run"
        if not self.isJumping:
            self.rect.x -= (self.rect.x - self.baseX) * 0.25

    def update(self, mult):
        if self.state == "run":
            self.run(mult)
        elif self.state == "idle":
            self.idle(mult)
        elif self.state == "dead":
            self.dead(mult)
        elif self.state == "jump":
            self.jump(mult)

groundX = 0
def scrollGround(mult):
    global groundX
    groundX -= 4 * mult
    if groundX <= -40:
        groundX = 0

font = pygame.font.Font(None, 48)
deathFont = pygame.font.Font(None, 60)

score = 0
scoreStarted = False
freezeScore = False
spawnTimer = 0
gameOn = False
speedMultiplier = 1

dino = Dino()
dinoGroup = pygame.sprite.Group(dino)
obstacles = pygame.sprite.Group()

running = True
while running:
    clock.tick(60)
    spawnTimer += 1

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False

        if i.type == pygame.KEYDOWN:

            if dino.state == "dead":
                if i.key == pygame.K_SPACE:
                    dino = Dino()
                    dinoGroup = pygame.sprite.Group(dino)
                    obstacles.empty()
                    score = 0
                    scoreStarted = False
                    freezeScore = False
                    spawnTimer = 0
                    speedMultiplier = 1
                    gameOn = False
                continue

            if i.key == pygame.K_SPACE:
                gameOn = True
                if not scoreStarted:
                    start_time = time.time()
                    scoreStarted = True
                if not dino.isJumping:
                    dino.state = "run"

            if i.key == pygame.K_UP and not dino.isJumping:
                dino.isJumping = True
                dino.state = "jump"
                dino.index = 0
                dino.velocity = -dino.jumpPower

    if gameOn and dino.state != "dead":
        speedMultiplier += 0.0008
        if spawnTimer > 90:
            obstacles.add(Obstacle(4))
            spawnTimer = 0
        scrollGround(speedMultiplier)

    for i in obstacles:
        i.update(speedMultiplier)

    if collision(dino, obstacles) and dino.state != "dead":
        dino.state = "dead"
        dino.index = 0
        dino.deathVel = 0
        freezeScore = True
        gameOn = False

    if scoreStarted and not freezeScore:
        score = int(time.time() - start_time)

    screen.blit(bg, (0, 0))
    screen.blit(groundImg, (groundX, groundY))

    dinoGroup.update(speedMultiplier)
    dinoGroup.draw(screen)
    obstacles.draw(screen)

    s = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(s, (20, 20))

    if dino.state == "dead":
        t1 = deathFont.render("you died", True, (0, 0, 0))
        t2 = deathFont.render(f"your score was {score}", True, (0, 0, 0))
        t3 = deathFont.render("press space to play again", True, (0, 0, 0))
        screen.blit(t1, (width//2 - t1.get_width()//2, 200))
        screen.blit(t2, (width//2 - t2.get_width()//2, 270))
        screen.blit(t3, (width//2 - t3.get_width()//2, 340))

    pygame.display.update()

pygame.quit()
