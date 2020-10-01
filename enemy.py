class Enemy:
    def __init__(self,x,y,image,screen,pygame):
        self.x = x
        self.y = y
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.image = image
        self.screen =  screen
        self.pygame = pygame
    def draw(self):
        self.screen.blit(self.image,(self.x,self.y))
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.pygame.draw.rect(self.screen, (255,0,0), self.hitbox,2)

    def move(self,speedx,speedy):
        self.x += speedx
        self.y += speedy
