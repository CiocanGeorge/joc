#"Imports"
import random
import pygame
import math

# initializare pygame
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


def player(x, y):
    screen.blit(playerImg, (x, y))

#score
score=0

# inamic
enemyImg = pygame.image.load("enemy.png")
enemyX = random.randint(10, 780)
enemyY = 50
enemyX_change = 0.5
enemyY_change = 25
bullet_state = "ready"


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


# bullet
# ready - you can't see the bullet on the screen
# fire  -the bullet is currently moving
bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 0
bulletX_change = 0
bulletY_change = 10


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def updatePlayer(changeX, changeY):
    global playerX
    global playerY
    playerX += changeX
    playerY += changeY


def updatePlayer2(plX, plY, changeX, changeY):
    plX = plX + changeX
    plY = plY + changeY
    return (plX, plY)

def isColision(eneX,eneY,bullX,bullY):
    distanta=math.sqrt(math.pow((eneX-bullX),2) + (math.pow((eneY-bullY),2)))
    if distanta<27:
        return True
    else:
        return False




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

        # miscare player
        # stanga dreapta
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
                    bulletY = playerY
                    fire_bullet(playerX, playerY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            # sus jos
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                playerY_change = -5
            if event.key == pygame.K_DOWN:
                playerY_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0

    # update pozitie
    updatePlayer(playerX_change,playerY_change)
    #playerX, playerY = updatePlayer2(playerX, playerY, playerX_change, playerY_change)

    # limite
    if playerX <= 5:
        playerX = 5
    elif playerX >= 730:
        playerX = 730
    if playerY >= 520:
        playerY = 520
    elif playerY <= 10:
        playerY = 10

    # miscare inamic
    enemyX += enemyX_change

    if enemyX <= 0:
        enemyY += enemyY_change
        enemyX_change = 0.5
    elif enemyX >= 730:
        enemyY += enemyY_change
        enemyX_change = -0.5

    # bullet movement
    if bulletY <= 0:
        # update position needed
        bulletY = playerY
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    #colision
    colision=isColision(enemyX,enemyY,bulletX,bulletY)
    if colision:

        bullet_state="ready"
        score+=1
        print(score)
        enemyX = random.randint(10, 780)



    player(playerX, playerY)
    enemy(enemyX, enemyY)


    pygame.display.update()