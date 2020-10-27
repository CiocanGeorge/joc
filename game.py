"Imports"
import pygame
from player import Player
from enemy import Enemy

pygame.init()
pygame.font.init()

# score
myfont = pygame.font.SysFont('Comic Sans MS', 16)


# creare screen
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
previous_time = pygame.time.get_ticks()

# backgournd
background = pygame.image.load("background.jpg")

# titlu si logo
pygame.display.set_caption("Invazia Spatiala")
pygame.display.set_icon(pygame.image.load("icon.png"))

# new player
player1 = Player(390, 480, screen, pygame)

# new enemy
enemy01 = Enemy(550, 50, screen, pygame)

screen_rect = screen.get_rect()
# game loop
RUNNING = True
while RUNNING:
    # RGB --   RED,GREE,BLUE
    screen.fill((0, 0, 0))
    # background image
    screen.blit(background, (0, 0))
    SCORE_DISPLAY = "SCORE: {}".format(player1.score)
    textsurface = myfont.render(SCORE_DISPLAY, False, (255, 0, 0))
    screen.blit(textsurface, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False

    keys_pressed = pygame.key.get_pressed()

    player1.move(keys_pressed, screen_rect)
    player1.pewpew2(keys_pressed)
    if player1.player_collision(enemy01):
        GAME_OVER = "Game Over"
        gameover_surface = myfont.render(GAME_OVER, False, (255, 0, 0))
        screen.blit(gameover_surface, (400, 300))

    enemy01.reset(player1.bullet_collision(enemy01))
    enemy01.move()

    player1.draw(myfont)
    enemy01.draw()
    pygame.display.flip()
    pygame.display.update()
