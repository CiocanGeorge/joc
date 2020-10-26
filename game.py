#"Imports"
import pygame
from player import *
from enemy import *

pygame.init()
pygame.font.init()

#score
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

#new player
player1 = Player(390,480,screen,pygame)

#new enemy
enemy01 =  Enemy(550,50,screen,pygame)

screen_rect = screen.get_rect()
# game loop
runnig = True
while runnig:
    # RGB --   RED,GREE,BLUE
    screen.fill((0, 0, 0))
    # background image
    screen.blit(background, (0, 0))
    to_display = "SCORE: {}".format(player1.score)
    textsurface = myfont.render(to_display, False, (255, 0, 0))
    screen.blit(textsurface, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnig = False

    keys_pressed = pygame.key.get_pressed()

    player1.move(keys_pressed,screen_rect)
    player1.pewpew2(keys_pressed)
    isrunnig=player1.playerCollision(enemy01)
    if(isrunnig):
        to_display = "Game Over"
        textsurface = myfont.render(to_display, False, (255, 0, 0))
        screen.blit(textsurface, (400, 300))



    enemy01.reset(player1.collision(enemy01))
    enemy01.move()


    player1.draw(myfont)
    enemy01.draw()
    pygame.display.flip()
    pygame.display.update()