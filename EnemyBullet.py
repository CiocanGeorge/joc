class EnemyBullet:
    def __init__(self, x, y, screen, pygame):
        self.image = pygame.transform.scale(pygame.image.load("egg1.png"), (40, 30))
        self.screen = screen
        self.pygame = pygame
        self.rect = pygame.Rect(x, y, 33, 30)
        self.hitbox = (self.rect.x, self.rect.y, 33, 30)

    def draw(self):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))
        self.hitbox = (self.rect.x, self.rect.y, 36, 30)
        self.rect = self.pygame.Rect(self.rect.x, self.rect.y, 36, 30)
        self.pygame.draw.rect(self.screen, (255, 0, 0), self.hitbox, 2)

    def move(self, x, y):
        self.rect.y = self.rect.y + 3
        if self.rect.y >= 580:
            self.rect.x = x
            self.rect.y = y

    def setBullet(self, x, y):
        self.rect.x = x + 15
        self.rect.y = y

    def checkCollision(self, player1):
        return self.rect.collidedict(player1.rect.x, player1.rect.y)
