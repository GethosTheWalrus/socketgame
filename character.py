import pygame, socket, json

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

class Player(CharacterClient):
    def __init__(self, screen, strips, host, port, x, y, width, height):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.host, self.port = host, port

        super().__init__(screen, strips, x, y, width, height)

    def render(self):
        super().render()
        self.move()

    # control moving the player
    def move(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        self._update_server("move", {"action": "move", "x": self.rect.x, "y": self.rect.y})

    def _update_server(self, action, data):
        json_data = json.dumps(data)
        self.s.sendto(json_data.encode("utf-8"), (self.host, self.port))
