import pygame
import random
import time

pygame.init()  # Initialization

WIDTH = 400
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Image load
image_background = pygame.image.load('resources/AnimatedStreet.png')
image_player = pygame.image.load('resources/Player.png')
image_enemy = pygame.image.load('resources/Enemy.png')
image_tenge = pygame.transform.scale_by(pygame.image.load('resources/tenge.png'), 0.08)
image_rub = pygame.transform.scale_by(pygame.image.load('resources/ruble.png'), 0.075)
image_dollar = pygame.transform.scale_by(pygame.image.load('resources/dollar.png'), 0.08)
image_euro = pygame.transform.scale_by(pygame.image.load('resources/euro (1).png'), 0.09)
coins_images = [image_tenge, image_rub, image_dollar, image_euro]

# Coins
coin_points = [1, 6, 490, 530]  # tenge, ruble, dollar, euro

pygame.mixer.music.load('resources/background.wav')
pygame.mixer.music.play(-1)

sound_crash = pygame.mixer.Sound('resources/crash.wav')

# Fonts
font_game_over = pygame.font.SysFont("Verdana", 60)
image_game_over = font_game_over.render("Game Over", True, "black")
image_game_over_rect = image_game_over.get_rect(center=(WIDTH // 2, HEIGHT // 2))

font_score = pygame.font.SysFont("Verdana", 30)

# Car speed control
point_increment = 500
next_speed_increase = 1000

# Player's car
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_player
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT
        self.speed = 5

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(self.speed, 0)
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-self.speed, 0)
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

# Enemy
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_enemy
        self.rect = self.image.get_rect()
        self.speed = 10
        self.generate_random_rect()

    def generate_random_rect(self):
        self.rect.left = random.randint(0, WIDTH - self.rect.w)
        self.rect.bottom = 0

    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > HEIGHT:
            self.generate_random_rect()

# Coins
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.currency = random.randint(0, 3)
        self.image = coins_images[self.currency]
        self.rect = self.image.get_rect()
        self.speed = 5
        self.value = coin_points[self.currency]
        self.generate_random_rect()

    def generate_random_rect(self):
        self.currency = random.randint(0, 3)
        self.image = coins_images[self.currency]
        self.value = coin_points[self.currency]
        self.rect.left = random.randint(0, WIDTH - self.rect.w)
        self.rect.bottom = 0

    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > HEIGHT:
            self.generate_random_rect()

running = True

clock = pygame.time.Clock()
FPS = 60

player = Player()
enemy = Enemy()
coin = Coin()

# Sprites
all_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()
coin_sprites = pygame.sprite.Group()

all_sprites.add(player, enemy, coin)
enemy_sprites.add(enemy)
coin_sprites.add(coin)

score = 0

# GAME LOOP
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.move()

    screen.blit(image_background, (0, 0))

    for entity in all_sprites:
        entity.move()
        screen.blit(entity.image, entity.rect)

    # Game Over condition
    if pygame.sprite.spritecollideany(player, enemy_sprites):
        sound_crash.play()
        time.sleep(1)
        running = False
        screen.fill("red")
        screen.blit(image_game_over, image_game_over_rect)
        pygame.display.flip()
        time.sleep(3)

    # Coin taken?
    collided_coins = pygame.sprite.spritecollide(player, coin_sprites, False)
    for coin_obj in collided_coins:
        score += coin_obj.value
        coin_obj.generate_random_rect()

    # Speed up the player's car
    if score >= next_speed_increase:
        enemy.speed *= 1.1
        next_speed_increase += point_increment

    # Score showing
    score_text = font_score.render(f"Score: {score}", True, "black")
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
