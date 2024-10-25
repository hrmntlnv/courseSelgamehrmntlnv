import sys
import pygame as pg
import time

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

PLATFORM_WIDTH = 200
PLATFORM_HEIGHT = 30
PLATFORM_X = (SCREEN_WIDTH - PLATFORM_WIDTH ) //2
PLATFORM_Y = int(SCREEN_HEIGHT * 0.8)
PLATFORM_SPEED =  3 
BALL_X = 10
BALL_Y = 10
BALL_WIDTH = 50
BALL_SPEED = 3
BALL_HEIGHT = 50

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("tilauncher")
clock = pg.time.Clock()

FPS = 120

while True:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()
    
    keys = pg.key.get_pressed()

    if keys[pg.K_LEFT]:
        PLATFORM_X -= PLATFORM_SPEED
        PLATFORM_X = max (0, PLATFORM_X )
    if keys[pg.K_RIGHT]:
        PLATFORM_X += PLATFORM_SPEED
        PLATFORM_X =min (SCREEN_WIDTH - PLATFORM_WIDTH, PLATFORM_X)
    screen.fill(WHITE)

   

    platform = pg.Rect( PLATFORM_X, PLATFORM_Y, PLATFORM_WIDTH, PLATFORM_HEIGHT)
    pg.draw.rect( screen, BLACK, platform)
    ball = pg.Rect( BALL_X, BALL_Y, BALL_WIDTH, BALL_HEIGHT)
    pg.draw.rect( screen, BLACK, ball)

    BALL_Y += 3
    



    pg.display.flip()
    clock.tick(FPS)
