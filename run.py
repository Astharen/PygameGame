from entity import entity
import pygame, sys
from obstacles import obstacle
import random

pygame.init()

win_x = 1000
clock = pygame.time.Clock()
screen = pygame.display.set_mode((win_x, 500))
FPS = 30
acc = 3
timeJumping = 20
timeSliding = 30


pygame.font.init()
myfont = pygame.font.SysFont(None, 30)

pygame.time.set_timer(pygame.USEREVENT+1, 1000)
pygame.time.set_timer(pygame.USEREVENT+2, 500)
pygame.time.set_timer(pygame.USEREVENT+3, random.randrange(1500, 2500))

def draw_window(screen, obstacles, pj):
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (10,130,10), (0, 470, win_x, 30))
    pj.draw(screen)
    for obs in obstacles:
        obs.draw(screen)

def end(window_x, window_y, screen, points):

    lostTxt = 'You lost. Points: ' + str(points)
    lost_font = pygame.font.SysFont(None, 25)
    again_font = pygame.font.SysFont(None, 25)
    screen.fill((0, 0, 0))

    label = lost_font.render(lostTxt, 1, (255,255,255))

    screen.blit(label, (window_x / 2 - label.get_width() / 2, window_y / 2 - label.get_height() / 2))
    pygame.display.update()

    pygame.time.delay(2000)

    run = True
    while run:
        screen.fill((0,0,0))
        text = 'Press any key to play again'
        label = again_font.render(text, 1, (255,255,255))
        screen.blit(label, (window_x / 2 - label.get_width() / 2, window_y / 2 - label.get_height() / 2))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                run = False

    main_run()


def main_run():

    run = True
    vel_x = 3
    points = 0
    obstacles = []
    displayed_points = points
    collision = False
    pj = entity(60, 500-30-80, 50, 80, acc, timeJumping, timeSliding)

    while run:

        clock.tick(FPS)

        points += vel_x

        pj.action()
        draw_window(screen, obstacles, pj)

        for ind, obs in sorted(enumerate(obstacles)):
            if obs.test_collision(pj):
                end(win_x, 500, screen, displayed_points)
            obs.x -= vel_x
            if obs.x < -30:
                obstacles.remove(obs)

        textsurface = myfont.render('Points:' + str(displayed_points), False, (255, 255, 255))
        screen.blit(textsurface, (win_x - 20 - textsurface.get_width(), 20 + textsurface.get_height()))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and not pj.isSliding:
            pj.isJumping = True
        if keys[pygame.K_DOWN] and not pj.isJumping:
            pj.isSliding = True

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.USEREVENT+1:
                vel_x += 1
            if event.type == pygame.USEREVENT+2:
                displayed_points = points
            if event.type == pygame.USEREVENT+3:
                r = random.randint(0, 1)
                if r == 0:
                    obstacles.append(obstacle(win_x, 500-(30+50), 70, 50))
                elif r == 1:
                    obstacles.append(obstacle(win_x, 0, 40, 395))

        pygame.display.update()

main_run()