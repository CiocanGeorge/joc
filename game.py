#"Imports"
import random

import bullet
import pygame
import math
from player import *
from enemy import *
from bullet import *


pygame.init()

# creare screen
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
previous_time = pygame.time.get_ticks()

# backgournd
background = pygame.image.load("background.jpg")

# titlu si logo
pygame.display.set_caption("Invazia Spatiala")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("player.png")

#new player
player1 = Player(390,480,playerImg,screen,pygame)

#score
score=0

# inamic
enemyImg = pygame.image.load("enemy.png")
enemyX = random.randint(10, 780)
enemyY = 50
enemyX_change = 0.5
enemyY_change = 25
bullet_state = "ready"
contor=0


#new enemy
enemy01 =  Enemy(550,50,enemyImg,screen,pygame)

screen_rect = screen.get_rect()
# game loop
runnig = True
while runnig:
    # RGB --   RED,GREE,BLUE
    screen.fill((0, 0, 0))
    # background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnig = False

    keys_pressed = pygame.key.get_pressed()

    player1.move(keys_pressed,screen_rect)
    player1.pewpew(keys_pressed )
    player1.collision(enemy01)

    enemy01.move()

    #colision
    #colision=isColision(enemyX,enemyY,bulletX,bulletY)
    #if colision:
    #    bullet_state="ready"
    #    score+=1
    #    enemyX = random.randint(10, 780)

    player1.draw()
    enemy01.draw()
    pygame.display.flip()
    pygame.display.update()