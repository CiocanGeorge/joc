from bullet import *
class Player:
    def __init__(self,x,y,image,screen,pygame):
        self.image = image
        self.screen = screen
        self.pygame = pygame
        self.rect = pygame.Rect(x, y, 38,38)
        self.hitbox = (self.rect.x, self.rect.y, 60, 60)
        self.previous_time = pygame.time.get_ticks()
        self.bulletImg = pygame.image.load("bullet.png")
        self.bullet1=Bullet(self.rect.x,self.rect.y,self.bulletImg,self.screen,self.pygame)
        self.bullet2=Bullet(self.rect.x,self.rect.y,self.bulletImg,self.screen,self.pygame)
        self.bullets=[self.bullet1,self.bullet2]
        self.contor = 0
    def draw(self):
        self.screen.blit(self.image,(self.rect.x,self.rect.y))
        self.hitbox = (self.rect.x , self.rect.y , 64, 62)
        self.rect = self.pygame.Rect( self.rect.x, self.rect.y, 64,62)
        self.pygame.draw.rect(self.screen, (255,0,0), self.hitbox,2)
        #test bullet
        for bull in self.bullets:
            if bull.state is "fire":
                bull.draw()
                bull.move()
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
    def get_rect(self):
        return  self.rect
    def pewpew(self,keys_pressed):
        if keys_pressed[self.pygame.K_SPACE]:
            current_time = self.pygame.time.get_ticks()
            if self.contor is 2:
                self.contor=0
            bull=self.bullets[self.contor]
            if bull.state is not "fire" and (current_time - self.previous_time > 380):
                self.previous_time = current_time
                bull.state="fire"
                bull.setBullet(self.rect.x,self.rect.y)
                self.contor+=1
    def collision(self,enemy):
         for bull in self.bullets:
            if bull.state is "fire":
                if bull.rect.collidepoint(enemy.rect.x,enemy.rect.y):
                    print("headshot!!")
