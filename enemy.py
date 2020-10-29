"IMPORTS"
from ebullet import Ebullet


class Enemy:
    "Enemy class"

    def __init__(self, x, y, screen, pygame):
        self.image = pygame.image.load("enemy.png")
        self.screen = screen
        self.pygame = pygame
        self.previous_time = pygame.time.get_ticks()
        self.rect = pygame.Rect(x, y, 33, 30)
        self.hitbox = (self.rect.x, self.rect.y, 33, 30)
        self.enemyx_change = 1
        self.enemyy_change = 25
        self.enemy_bullet = Ebullet(
            self.rect.x, self.rect.y, self.screen, self.pygame)
        self.isgame_over = False

    def draw(self):
        "drawing method"
        self.screen.blit(self.image, (self.rect.x, self.rect.y))
        self.hitbox = (self.rect.x, self.rect.y, 33, 30)
        self.rect = self.pygame.Rect(self.rect.x, self.rect.y, 33, 30)
        self.pygame.draw.rect(self.screen, (255, 0, 0), self.hitbox, 2)
        self.enemy_bullet.draw()
        self.enemy_bullet.move(self.rect.x, self.rect.y)

    def move(self):
        "moving method"
        if not self.isgame_over:
            if self.rect.x <= 0:
                self.rect.y += self.enemyy_change
                self.enemyx_change = 1
            elif self.rect.x >= 730:
                self.rect.y += self.enemyy_change
                self.enemyx_change = -1
            self.rect.x += self.enemyx_change
        else:
            self.rect.x = 550
            self.rect.y = 50

    def check_collision(self, bullet_x, bullet_y):
        "collision check method"
        return self.rect.collidedict(bullet_x, bullet_y)

    def reset(self, is_hit):
        "enemy reset method"
        if is_hit is True:
            self.rect = self.pygame.Rect(550, 50, 33, 30)

    def get_enemy_bullet_rect(self):
        return self.enemy_bullet.rect

    def set_game_over(self, isgame_over):
        self.isgame_over = isgame_over
        self.enemy_bullet.isgame_over = isgame_over
