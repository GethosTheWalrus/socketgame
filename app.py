import pygame
import keyboard
import socket
from spritesheet import SpriteStripAnim
from character import Character, Player

# networking
port = 12345
s = socket.socket()

# connect to the server
s.connect(('127.0.0.1', port))

# receive data from server
print(s.recv(1024))

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((600, 600))
running = True

strips = {
    "down": SpriteStripAnim('assets/goblin.png', (0,0,65,65), 7, 1, True, 5),
    "right": SpriteStripAnim('assets/goblin.png', (0,65,65,65), 7, 1, True, 5),
    "up": SpriteStripAnim('assets/goblin.png', (0,130,65,65), 7, 1, True, 5),
    "left": SpriteStripAnim('assets/goblin.png', (0,195,65,65), 7, 1, True, 5)
}
p = Player(screen, strips, 100, 100, 65, 65)

image = strips["down"].next()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            s.close()

        # detect user key events
        keyboard.detect_key_press(event, p)

    p.render()

    pygame.display.flip()
    clock.tick(60)