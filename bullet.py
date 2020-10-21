import math
class Bullet:
    def __init__(self,x,y,image,screen,pygame):
        self.image = image
        self.screen =  screen
        self.pygame = pygame
        self.rect =  pygame.Rect(x,y,33,30)
        self.hitbox = (self.rect.x, self.rect.y, 33, 30)
        self.enemyX_change = 1
        self.enemyY_change = 1
    def draw(self):
        self.screen.blit(self.image,(self.rect.x,self.rect.y))
        self.hitbox = (self.rect.x, self.rect.y , 33, 30)
        self.rect =  self.pygame.Rect(self.rect.x, self.rect.y,33,30)
        self.pygame.draw.rect(self.screen, (255,0,0), self.hitbox,2)
    def move(self):
        while(1):
            if self.rect.y > 10:
                self.rect.y -= 1
            else:
                break;



    def checkCollision(self,bulletX,bulletY):
       return self.rect.collidedict(bulletX,bulletY)