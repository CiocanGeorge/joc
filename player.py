class Player:
    def __init__(self,x,y,image,screen,pygame):
        self.image = image
        self.screen = screen
        self.pygame = pygame
        self.rect = pygame.Rect(x, y, 38,38)
        self.hitbox = (self.rect.x, self.rect.y, 60, 60)
    def draw(self):
        self.screen.blit(self.image,(self.rect.x,self.rect.y))
        self.hitbox = (self.rect.x , self.rect.y , 64, 62)
        self.rect = self.pygame.Rect( self.rect.x, self.rect.y, 64,62)
        self.pygame.draw.rect(self.screen, (255,0,0), self.hitbox,2)
    def move(self,speedx,speedy):
        #self.x += speedx
        #self.y += speedy
        self.rect.x +=  speedx
        self.rect.y +=  speedy
    def get_rect(self):
        return  self.rect
