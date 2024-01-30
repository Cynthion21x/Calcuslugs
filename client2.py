import pygame
import socket
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

s = socket.socket()
s.connect(('127.0.0.1',54321))


"""while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    print(player_pos)

    screen.fill("purple")

    pygame.draw.circle(screen, "red", player_pos, 40)

    pygame.display.flip()


    dt = clock.tick(60) / 1000
    """
pygame.quit()
