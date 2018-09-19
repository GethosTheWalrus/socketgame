import pygame

class Character(pygame.sprite.Sprite):
    def __init__(self, screen, strips, x, y, width, height):
        # call parent constructor
        super().__init__()

        # initialize all variables
        self.direction = "down"
        self.screen = screen
        self.strips = strips
        self.image = self.strips[self.direction].next()
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y, self.rect.width, self.rect.height = x, y, width, height
        self.vx, self.vy = 0, 0

    # draw the character on the screen
    def render(self):
        if self.vx != 0 or self.vy != 0:
            self.image = self.strips[self.direction].next()
        else:
            self.image = self.strips[self.direction].images[0]
            
        self.screen.blit(self.image, (self.rect.x, self.rect.y))

class Player(Character):
    def __init__(self, screen, strips, x, y, width, height):
        super().__init__(screen, strips, x, y, width, height)

    def render(self):
        super().render()
        self.move()

    # control moving the player
    def move(self):
        self.rect.x += self.vx
        self.rect.y += self.vy