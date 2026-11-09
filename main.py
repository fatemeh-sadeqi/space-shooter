import pygame
pygame.init()

screen = pygame.display.set_mode ((800, 600))
pygame.display.set_caption("Space Shooter")
running = True

ship_x = 375
ship_y = 520
ship_speed = 5

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

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
    pygame.display.flip()

pygame.quit()