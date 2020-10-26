import math
class Bullet:
    def __init__(self,x,y,image,screen,pygame):
        self.image = image
        self.screen =  screen
        self.pygame = pygame
        self.rect =  pygame.Rect(x,y,33,30)
        self.hitbox = (self.rect.x, self.rect.y, 33, 30)
        self.state = "ready"
    def draw(self):
        if(self.state == "fire"):
            self.screen.blit(self.image,(self.rect.x,self.rect.y))
            self.hitbox = (self.rect.x, self.rect.y , 33, 30)
            self.rect =  self.pygame.Rect(self.rect.x, self.rect.y,33,30)
            self.pygame.draw.rect(self.screen, (255,0,0), self.hitbox,2)
    def move(self):
        if self.state == "fire":
            self.rect.y  =  self.rect.y-3
            if self.rect.y < 10:
                self.state = "gone"
    def  setBullet(self,x,y):
        self.rect.x = x+18
        self.rect.y = y
    def checkCollision(self,player1):
       return self.rect.collidedict(player1.rect.x,player1.rect.y)