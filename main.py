import pygame
pygame.init()

class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 8

    def update(self):
        self.y -= self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 0), (self.x, self.y, 4, 12))

screen = pygame.display.set_mode ((800, 600))
pygame.display.set_caption("Space Shooter")
running = True

ship_x = 375
ship_y = 520
ship_speed = 5
clock = pygame.time.Clock()

bullets = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bullets.append(Bullet(ship_x + 25, ship_y))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        ship_x -= ship_speed

    if keys[pygame.K_RIGHT]:
        ship_x += ship_speed

    if ship_x < 0:
        ship_x = 0
    if ship_x > 750:
        ship_x = 750

    screen.fill((0, 0, 20))
    pygame.draw.rect(screen, (255, 255, 255), (ship_x, ship_y, 50, 30))

    for bullet in bullets[:]:
            bullet.update()
            bullet.draw(screen)
            if bullet.y < 0:
                bullets.remove(bullet)

    pygame.display.flip()
    clock.tick(60)

    


pygame.quit()