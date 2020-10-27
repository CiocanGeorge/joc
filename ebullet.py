"imports"


class Ebullet:
    "Enemy Bulet Class"

    def __init__(self, x, y, screen, pygame):
        self.image = pygame.transform.scale(
            pygame.image.load("egg1.png"), (40, 30))
        self.screen = screen
        self.pygame = pygame
        self.rect = pygame.Rect(x, y, 38, 30)
        self.hitbox = (self.rect.x, self.rect.y, 38, 30)

    def draw(self):
        "Enemy Bullet Drawing Method"
        self.screen.blit(self.image, (self.rect.x, self.rect.y))
        self.hitbox = (self.rect.x, self.rect.y, 38, 30)
        self.rect = self.pygame.Rect(self.rect.x, self.rect.y, 38, 30)
        self.pygame.draw.rect(self.screen, (255, 0, 0), self.hitbox, 2)

    def move(self, enemy_x, enemy_y):
        "Enemy Bullet Movement Method"
        self.rect.y = self.rect.y + 3
        if self.rect.y >= 580:
            self.rect.x = enemy_x
            self.rect.y = enemy_y

    def check_collision(self, player1):
        "Collision Check Method"
        return self.rect.collidedict(player1.rect.x, player1.rect.y)
