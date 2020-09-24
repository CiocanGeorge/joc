import pygame
import random

#initializare pygame
pygame.init()

#creare screen
screen = pygame.display.set_mode((800,600))

#backgournd
background=pygame.image.load("background.jpg")


#titlu si logo
pygame.display.set_caption("Invazia Spatiala")
icon=pygame.image.load("icon.png")
pygame.display.set_icon(icon)

#Player
playerImg=pygame.image.load("player.png")
playerX=370
playerY=480
playerX_change=0
playerY_change=0

def player(x,y):
    screen.blit(playerImg,(x,y))

#inamic
enemyImg=pygame.image.load("enemy.png")
enemyX=random.randint(10,780)
enemyY=50
enemyX_change=0.5
enemyY_change=25
bullet_state="ready"

def enemy(x,y):
    screen.blit(enemyImg,(x,y))

#bullet
# ready - you can't see the bullet on the screen
# fire  -the bullet is currently moving
bulletImg=pygame.image.load("bullet.png")
bulletX=0
bulletY=480
bulletX_change=0
bulletY_change=10

def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletImg,(x+16,y+10))

#game loop
runnig=True
while runnig:
    # RGB --   RED,GREE,BLUE
    screen.fill((0, 0, 0))
    #background image
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnig=False

        #miscare player
            #stanga dreapta
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change=-5
            if event.key == pygame.K_RIGHT:
                playerX_change=5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX=playerX
                    fire_bullet(bulletX,bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change=0
            # sus jos
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                playerY_change=-5
            if event.key == pygame.K_DOWN:
                playerY_change=5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change=0

    #update pozitie
    playerX+=playerX_change
    playerY+=playerY_change

    #limite
    if playerX<=5:
        playerX=5
    elif playerX>=730:
        playerX=730
    if playerY >= 520:
        playerY = 520
    elif playerY <= 10:
        playerY = 10

    #miscare inamic
    enemyX+=enemyX_change

    if enemyX<=0:
        enemyY += enemyY_change
        enemyX_change = 0.5
    elif enemyX>=730:
        enemyY += enemyY_change
        enemyX_change=-0.5

    #bullet movement
    if bulletY<=0:
        bulletY=480
        bullet_state="ready"

    if bullet_state is "fire":
        fire_bullet(bulletX,bulletY)
        bulletY-=bulletY_change


    player(playerX,playerY)
    enemy(enemyX,enemyY)

    pygame.display.update()



