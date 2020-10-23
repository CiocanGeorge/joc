import math
class Enemy:
    def __init__(self,x,y,screen,pygame):
        self.image = pygame.image.load("enemy.png")
        self.screen =  screen
        self.pygame = pygame
        self.rect =  pygame.Rect(x,y,33,30)
        self.hitbox = (self.rect.x, self.rect.y, 33, 30)
        self.enemyX_change = 1
        self.enemyY_change = 25
    def draw(self):
        self.screen.blit(self.image,(self.rect.x,self.rect.y))
        self.hitbox = (self.rect.x, self.rect.y , 33, 30)
        self.rect =  self.pygame.Rect(self.rect.x, self.rect.y,33,30)
        self.pygame.draw.rect(self.screen, (255,0,0), self.hitbox,2)
    def move(self):
        if self.rect.x <= 0:
            self.rect.y += self.enemyY_change
            self.enemyX_change = 1
        elif self.rect.x >= 730:
            self.rect.y += self.enemyY_change
            self.enemyX_change = -1
        self.rect.x += self.enemyX_change
    def checkCollision(self,bulletX,bulletY):
       return self.rect.collidedict(bulletX,bulletY)

    def reset(self,isHit):
        if isHit is True:
            #enemy01 = Enemy(550, 50,  screen, pygame)
            self.rect=self.pygame.Rect(550,50,33,30)