#"Imports"
import random
import pygame
import math
from player import *
from enemy import *
from bullet import *


# initializare pygame
#from Python.joc.enemy import Enemy
#from Python.joc.joc.bullet import Bullet
#from Python.joc.player import Player

pygame.init()

# creare screen
screen = pygame.display.set_mode((800, 600))

# backgournd
background = pygame.image.load("background.jpg")

# titlu si logo
pygame.display.set_caption("Invazia Spatiala")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("player.png")
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

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


#new enemy
enemy01 =  Enemy(550,50,enemyImg,screen,pygame)


#def enemy(x, y):
#    screen.blit(enemyImg, (x, y))


# bullet
# ready - you can't see the bullet on the screen
# fire  -the bullet is currently moving
bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 0
bulletX_change = 0
bulletY_change = 10

bullet01=Bullet(player1.rect.x,player1.rect.y,bulletImg,screen,pygame)

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

def isColision(eneX,eneY,bullX,bullY):
    distanta=math.sqrt(math.pow((eneX-bullX),2) + (math.pow((eneY-bullY),2)))
    if distanta<27:
        return True
    else:
        return False
 #test

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
#stackoverflow
    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_LEFT]:
        player1.rect.x -= 5

    if keys_pressed[pygame.K_RIGHT]:
        player1.rect.x += 5

    if keys_pressed[pygame.K_UP]:
        player1.rect.y -= 5

    if keys_pressed[pygame.K_DOWN]:
        player1.rect.y += 5
    if keys_pressed[pygame.K_SPACE]:
        bullet01.state = "fire"
        bullet01.setBullet(player1.rect.x,player1.rect.y)
        
    if(bullet01.state is "fire"):
        bullet01.draw()
        bullet01.move()
        
    player1.rect.clamp_ip(screen_rect)

    enemy01.move()

    # bullet movement
    if bulletY <= 0:
        bulletY = player1.rect.y
        bullet_state = "ready"

    if bullet_state is "fire":
        #bullet01.move()
        bulletY -= bulletY_change

    #colision
    colision=isColision(enemyX,enemyY,bulletX,bulletY)
    if colision:
        bullet_state="ready"
        score+=1
        enemyX = random.randint(10, 780)

    player1.draw()
    enemy01.draw()
    #bullet01.draw()
    pygame.display.flip()
    pygame.display.update()