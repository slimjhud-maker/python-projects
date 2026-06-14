import pygame
import random

pygame.init()

width = 500
height = 700
lives = 3
score = 0
gameon = False
gameover = False
running = True

basket_width = 90
basket_height = 40
star_size = 40

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

title_font = pygame.font.Font(None, 64)
big_font = pygame.font.Font(None, 48)
medium_font = pygame.font.Font(None, 32)
small_font = pygame.font.Font(None, 28)


class Basket(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        loaded = pygame.image.load(r"python-projects\Pygame Games\Star Catcher Game\Star Catcher game Assets\bask2 (1).png")
        self.image = pygame.transform.scale(loaded, (basket_width, basket_height))
        self.rect = self.image.get_rect(midbottom=(width // 2, height - 120))
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.left -= 7
        if keys[pygame.K_RIGHT]:
            self.rect.right += 7
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > width:
            self.rect.right = width


class Star(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        img = pygame.image.load(r"python-projects\Pygame Games\Star Catcher Game\Star Catcher game Assets\starr (1).png")
        self.original_image = pygame.transform.scale(img, (star_size, star_size))
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.angle = 0
        self.reset()

    def reset(self):
        self.rect.midtop = (random.randint(30, width - 30), -100)
        self.angle = 0

    def update(self):
        self.rect.top += 4
        self.angle = (self.angle + 5) % 360
        center = self.rect.center
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=center)
        self.mask = pygame.mask.from_surface(self.image)


background = pygame.image.load(r"python-projects\Pygame Games\Star Catcher Game\Star Catcher game Assets\night 2 (2).png")
background = pygame.transform.scale(background, (width, height))

player = Basket()
falling_star = Star()
all_sprites = pygame.sprite.Group(player, falling_star)

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if not gameon:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                gameon = True

        if gameover:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                score = 0
                lives = 3
                gameover = False
                player.rect.midbottom = (width // 2, height - 120)
                falling_star.reset()

    if gameon and not gameover:
        player.update()
        falling_star.update()

        if falling_star.rect.top > height:
            lives -= 1
            falling_star.reset()
            if lives == 0:
                gameover = True

        if pygame.sprite.collide_mask(player, falling_star):
            if player.rect.left + 10 < falling_star.rect.centerx < player.rect.right - 10:
                score += 1
                falling_star.reset()

    screen.blit(background, (0, 0))
    all_sprites.draw(screen)

    if not gameon:
        text = big_font.render("PRESS SPACE TO START", True, (255, 255, 255))
        screen.blit(text, text.get_rect(center=(width // 2, height // 2)))
    else:
        score_surf = medium_font.render(f"Score: {score}", True, (255, 255, 255))
        lives_surf = medium_font.render(f"Lives: {lives}", True, (255, 80, 80))
        screen.blit(score_surf, (10, 40))
        screen.blit(lives_surf, (width - lives_surf.get_width() - 10, 40))

    if gameover:
        overlay = pygame.Surface((width, height), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        screen.blit(overlay, (0, 0))

        t = title_font.render("GAME OVER", True, (255, 255, 255))
        s = medium_font.render(f"Final Score: {score}", True, (255, 255, 255))
        r = small_font.render("Press SPACE to Restart", True, (200, 200, 200))

        screen.blit(t, t.get_rect(center=(width // 2, height // 2 - 60)))
        screen.blit(s, s.get_rect(center=(width // 2, height // 2)))
        screen.blit(r, r.get_rect(center=(width // 2, height // 2 + 60)))

    pygame.display.flip()

pygame.quit()