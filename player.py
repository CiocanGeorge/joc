from bullet import *
from enemy import *
class Player:
    def __init__(self,x,y,screen,pygame):
        self.image = pygame.image.load("player.png")
        self.screen = screen
        self.pygame = pygame
        self.rect = pygame.Rect(x, y, 38,38)
        self.hitbox = (self.rect.x, self.rect.y, 60, 60)
        self.previous_time = pygame.time.get_ticks()
        self.bulletImg = pygame.image.load("bullet.png")
        self.bulletsTest= []
        self.reloading = False
        self.contor = 0
        self.score  = 0
        self.IsOver=False
    def draw(self,myfont):
        self.screen.blit(self.image,(self.rect.x,self.rect.y))
        self.hitbox = (self.rect.x , self.rect.y , 64, 62)
        self.rect = self.pygame.Rect( self.rect.x, self.rect.y, 64,62)
        self.pygame.draw.rect(self.screen, (255,0,0), self.hitbox,2)
        for bull in self.bulletsTest:
            if bull.state == "fire":
                bull.draw()
                bull.move()
                if self.reloading:
                    textsurface = myfont.render('reloading!',False,(255,0,0))
                    self.screen.blit(textsurface,(self.rect.x,self.rect.y))
    def move(self,keys_pressed,screen_rect):
        if keys_pressed[self.pygame.K_LEFT]:
            self.rect.x -= 5
        if keys_pressed[self.pygame.K_RIGHT]:
            self.rect.x += 5
        if keys_pressed[self.pygame.K_UP]:
            self.rect.y -= 5
        if keys_pressed[self.pygame.K_DOWN]:
           self.rect.y += 5
        self.rect.clamp_ip(screen_rect)
    def pewpew2(self,keys_pressed):
        current_time = self.pygame.time.get_ticks()
        if(self.contor == 9 and (current_time - self.previous_time) > 1000):
            self.reloading = False
            self.previous_time = current_time
            self.contor = 0
        if keys_pressed[self.pygame.K_SPACE]  and  (current_time - self.previous_time > 380)and self.reloading is False:
            if(self.contor <10):
                self.bulletsTest.append(Bullet(self.rect.x,self.rect.y,self.bulletImg,self.screen,self.pygame))
            for bull in self.bulletsTest:
                if(bull.state == "ready"):
                    if bull.state != "fire":
                        self.previous_time = current_time
                        bull.state="fire"
                        bull.setBullet(self.rect.x,self.rect.y)
                        self.contor+=1
                        if(self.contor == 9):
                            self.reloading = True
        for bull in self.bulletsTest:
            if(bull.state == "gone"):
                self.bulletsTest.remove(bull)
    def collision(self,enemy):
         for bull in self.bulletsTest:
            if bull.state == "fire":
                if bull.rect.colliderect(enemy.rect):
                    bull.state="gone"
                    self.score +=1
                    return True
    def playerCollision(self,enemy):
        if self.rect.colliderect(enemy.rect):
            self.IsOver=True
            return self.IsOver