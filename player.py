"Imports"
from bullet import Bullet


class Player:
    "player class"

    def __init__(self, x, y, screen, pygame):
        self.image = pygame.image.load("player.png")
        self.screen = screen
        self.pygame = pygame
        self.rect = pygame.Rect(x, y, 38, 38)
        self.hitbox = (self.rect.x, self.rect.y, 60, 60)
        self.previous_time = pygame.time.get_ticks()
        self.bullet_img = pygame.image.load("bullet.png")
        self.bullets = []
        self.reloading = False
        self.contor = 0
        self.score = 0
        self.is_over = False

    def draw(self, myfont):
        "Player and player bullet drawing"
        self.screen.blit(self.image, (self.rect.x, self.rect.y))
        self.hitbox = (self.rect.x, self.rect.y, 64, 62)
        self.rect = self.pygame.Rect(self.rect.x, self.rect.y, 64, 62)
        self.pygame.draw.rect(self.screen, (255, 0, 0), self.hitbox, 2)
        for bull in self.bullets:
            if bull.state == "fire":
                bull.draw()
                bull.move()
                if self.reloading:
                    textsurface = myfont.render(
                        'reloading!', False, (255, 0, 0))
                    self.screen.blit(textsurface, (self.rect.x, self.rect.y))
        if self.is_over:
            game_over = "Game Over"
            gameover_surface = myfont.render(game_over, False, (255, 0, 0))
            self.screen.blit(gameover_surface, (400, 300))

    def move(self, keys_pressed, screen_rect):
        "Player movement method"
        if not self.is_over:
            if keys_pressed[self.pygame.K_LEFT]:
                self.rect.x -= 5
            if keys_pressed[self.pygame.K_RIGHT]:
                self.rect.x += 5
            if keys_pressed[self.pygame.K_UP]:
                self.rect.y -= 5
            if keys_pressed[self.pygame.K_DOWN]:
                self.rect.y += 5
        else:
            self.rect.x = 390
            self.rect.y = 480

        self.rect.clamp_ip(screen_rect)

    def pewpew2(self, keys_pressed):
        "Player shooting method"
        current_time = self.pygame.time.get_ticks()
        if(self.contor == 9 and (current_time - self.previous_time) > 1000):
            self.reloading = False
            self.previous_time = current_time
            self.contor = 0
        if (keys_pressed[self.pygame.K_SPACE] and
            (current_time - self.previous_time > 380) and
                self.reloading is False and not self.is_over):
            if self.contor < 10:
                self.bullets.append(
                    Bullet(self.rect.x, self.rect.y, self.bullet_img, self.screen, self.pygame))
            for bull in self.bullets:
                if bull.state == "ready":
                    if bull.state != "fire":
                        self.previous_time = current_time
                        bull.state = "fire"
                        bull.set_bullet(self.rect.x, self.rect.y)
                        self.contor += 1
                        if self.contor == 9:
                            self.reloading = True
        for bull in self.bullets:
            if bull.state == "gone":
                self.bullets.remove(bull)

    def bullet_collision(self, enemy):
        "Bullet with enemy collisision method"
        for bull in self.bullets:
            if bull.state == "fire":
                if bull.rect.colliderect(enemy.rect):
                    bull.state = "gone"
                    self.score += 1
                    return True

    def player_collision(self, enemy):
        "Player collision with enemy method"
        if self.rect.colliderect(enemy.rect):
            self.is_over = True

    def check_enemy_bullet_collision(self, enemy_bullet):
        "Check enemy bullet collision with player method"
        if enemy_bullet.colliderect(self.rect):
            self.is_over = True

    def return_isOver(self):
        return self.is_over
