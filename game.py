import sys 
import pygame as pg
import time

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
POT_BORDER = pg.Rect(0,0,SCREEN_WIDTH, 1)
BOTTOM_BORDER = pg.Rect (0,SCREEN_HEIGHT,SCREEN_WIDTH,1)
LEFT_BORDER = pg.Rect(0,0,1,SCREEN_HEIGHT)
RIGHT_BORDER = pg.Rect(SCREEN_WIDTH,0,1,SCREEN_HEIGHT)

WHITE = (255, 255, 255)
BLACKE = (0, 0, 0)

PLATFORM_WIDTH = 200
PLATFORM_HEIGHT = 30
PLATFORM_X = (SCREEN_WIDTH - PLATFORM_WIDTH ) //2
PLATFORM_Y = int(SCREEN_HEIGHT * 0.8)
PLATFORM_SPEED =  3 
BALL_X = 270
BALL_Y = 270
BALL_WIDTH = 50
BALL_SPEED = 3
BALL_HEIGHT = 50
BALL_DIRECTION=pg.math.Vector2(0,1).normalize()

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


    speed_vector = BALL_DIRECTION * BALL_SPEED 
    BALL_X +=  speed_vector.x 
    BALL_Y += speed_vector.y 
   

    platform = pg.Rect( PLATFORM_X, PLATFORM_Y, PLATFORM_WIDTH, PLATFORM_HEIGHT)
    pg.draw.rect( screen, BLACKE, platform)
    ball = pg.Rect( BALL_X, BALL_Y, BALL_WIDTH, BALL_HEIGHT)
    pg.draw.rect( screen, BLACKE, ball)
    


    if ball.colliderect(platform):
        BALL_DIRECTION = BALL_DIRECTION.reflect(pg.math.Vector2(0,-1))
    if ball.colliderect(POT_BORDER):
        BALL_DIRECTION = BALL_DIRECTION.reflect(pg.math.Vector2(0,1))
    if ball.colliderect(BOTTOM_BORDER):
        BALL_DIRECTION = BALL_DIRECTION.reflect(pg.math.Vector2(0,-1))
    if ball.colliderect(LEFT_BORDER):
        BALL_DIRECTION = BALL_DIRECTION.reflect(pg.math.Vector2(1,0))
    if ball.colliderect(RIGHT_BORDER):
        BALL_DIRECTION = BALL_DIRECTION.reflect(pg.math.Vector2(-1,0))
    # if ball.colliderect(pg.Rect(0,0,width=SCREEN_WIDTH,height=0)):


    pg.display.flip()
    clock.tick(FPS)
