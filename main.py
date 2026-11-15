import pygame
import random
pygame.init()

class Enemy:
    def __init__(self):
        self.x = random.randint(0, 760)
        self.y = -40
        self.speed = 2


    def update(self):
        self.y += self.speed

    def draw(self, screen):
        screen.blit(enemy_img, (self.x, self.y))

class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 8

    def update(self):
        self.y -= self.speed

    def draw(self, screen):
        screen.blit(bullet_img, (self.x, self.y))

screen = pygame.display.set_mode ((800, 600))
pygame.display.set_caption("Space Shooter")
ship_img = pygame.image.load("images/ship.png").convert_alpha()
ship_img = pygame.transform.scale(ship_img, (50, 30))
enemy_img = pygame.image.load("images/enemy.png").convert_alpha()
enemy_img = pygame.transform.scale(enemy_img, (40, 30))
bullet_img = pygame.image.load("images/bullet.png").convert_alpha()
bullet_img = pygame.transform.scale(bullet_img, (10, 24))
running = True

ship_x = 375
ship_y = 520
ship_speed = 5
clock = pygame.time.Clock()

bullets = []
enemies = []

score = 0
lives = 3
game_over = False
font = pygame.font.Font(None, 36)
big_font = pygame.font.Font(None, 72)

 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bullets.append(Bullet(ship_x + 20, ship_y))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        ship_x -= ship_speed

    if keys[pygame.K_RIGHT]:
        ship_x += ship_speed

    if ship_x < 0:
        ship_x = 0
    if ship_x > 750:
        ship_x = 750

    if random.randint(1, 60) == 1 and not game_over:
        enemies.append(Enemy())

    screen.fill((0, 0, 20))
    screen.blit(ship_img, (ship_x, ship_y))

    for bullet in bullets[:]:
        bullet.update()
        bullet.draw(screen)
        if bullet.y < 0:
            bullets.remove(bullet)

    ship_rect = pygame.Rect(ship_x, ship_y, 50, 30)

    for enemy in enemies[:]:
        enemy.update()
        enemy.draw(screen)

        enemy_rect = pygame.Rect(enemy.x, enemy.y, 40, 30)

        if enemy_rect.colliderect(ship_rect):
            lives -= 1
            enemies.remove(enemy)

        elif enemy.y > 600:
            lives -= 1
            enemies.remove(enemy)

    for bullet in bullets[:]:
        for enemy in enemies[:]:
            bullet_rect = pygame.Rect(bullet.x, bullet.y, 10, 24)
            enemy_rect = pygame.Rect(enemy.x, enemy.y, 40, 30)

            if bullet_rect.colliderect(enemy_rect):
                bullets.remove(bullet)
                enemies.remove(enemy)
                score += 10
                break

    if lives <= 0:
        lives = 0
        game_over = True

    text = font.render(f"Score: {score} Lives: {lives}", True, (255, 255, 255))
    screen.blit(text, (10, 10))

    if game_over:
        over_text = big_font.render("GAME OVER", True, (255, 255, 255))
        screen.blit(over_text, (250, 250))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()