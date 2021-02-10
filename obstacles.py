import pygame

class obstacle(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = pygame.Rect((x, y, width, height))

    def draw(self, screen):
        self.hitbox = pygame.Rect((self.x, self.y, self.width, self.height))
        pygame.draw.rect(screen, (10, 10, 130), self.hitbox)

    def test_collision(self, pj):
        self.hitbox = pygame.Rect((self.x, self.y, self.width, self.height))

        if self.hitbox.colliderect(pj.hitbox):
        #if (pj.x < self.x + self.width and pj.x > self.x) and (pj.y < self.y + self.height and pj.y > self.y):
            print(self.hitbox)
            print(pj.hitbox)
            return True
        else:
            return False