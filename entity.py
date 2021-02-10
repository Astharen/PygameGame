import pygame


class entity:
    def __init__(self, x, y, width, height, acc, timeJumping, timeSliding):
        self.x = x
        self.y = y
        # self.vel_x = vel_x
        self.vel_y = int(timeJumping/2 * acc)
        self.acc = acc
        self.width = width
        self.height = height
        self.timeJumping = timeJumping
        self.timeSliding = timeSliding
        self.isJumping = False
        self.isSliding = False
        self.slideCount = 0
        self.jumpCount = 0
        self.runCount = 0
        self.angle = 90
        self.hitbox = pygame.Rect((x, y, width, height))

    def action(self):
        if self.isJumping:
            if self.timeJumping%2!=0:
                print("Error: timeJunping must be even")
            self.y -= self.vel_y
            self.vel_y -= self.acc
            self.jumpCount += 1
            if self.jumpCount > self.timeJumping:
                self.jumpCount = 0
                self.isJumping = False
                self.vel_y = int(self.timeJumping/2 * self.acc)
            self.hitbox = pygame.Rect((self.x, self.y, self.width, self.height))
        elif self.isSliding:
            speed = 90/10
            self.hitbox = pygame.Rect((self.x, self.y, self.width, self.height))
            if self.slideCount < 10:
                self.angle = (self.angle + speed) % 360
            elif self.slideCount > 30:
                self.slideCount = 0
                self.isSliding = False
            elif self.slideCount > 20:
                self.angle = (self.angle - speed) % 360
            else:
                self.angle = 0
            
            if self.slideCount < (self.timeSliding-5) and self.slideCount>5:
                self.hitbox = pygame.Rect((60, 500-30-self.width, self.height, self.width))
            self.slideCount += 1


    def draw(self, screen):
        if self.isSliding:
            image_orig = pygame.Surface((self.height, self.width))
            image_orig.set_colorkey((0, 0, 0))  
            image_orig.fill((130,10,10))
            image = image_orig.copy()
            image.set_colorkey((0,0,0))
            rect = image.get_rect()
            rect.bottomright = (self.x +  self.width, 470)#self.height)
            old_br = rect.bottomright
            new_image = pygame.transform.rotate(image_orig , self.angle)
            rect = new_image.get_rect()
            rect.bottomright = old_br
            screen.blit(new_image , rect)
            pygame.display.flip()
        else:
            pygame.draw.rect(screen, (130,10,10), (self.x, self.y, self.width, self.height))