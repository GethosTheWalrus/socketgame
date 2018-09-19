import pygame

def detect_key_press(event, object):
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
            object.vx = 0

        if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            object.vy = 0
        

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        object.vx = 2
        object.direction = "right"
    elif keys[pygame.K_LEFT]:
        object.vx = -2
        object.direction = "left"

    if keys[pygame.K_UP]:
        object.vy = -2
        object.direction = "up"
    elif keys[pygame.K_DOWN]:
        object.vy = 2
        object.direction = "down"