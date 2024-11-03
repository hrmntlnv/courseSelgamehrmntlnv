import sys 
import pygame as pg
import time

pg.font.init()
def_font = pg.font.Font(pg.font.get_default_font(), 30)
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
POT_BORDER = pg.Rect(0,0,SCREEN_WIDTH, 1)
BOTTOM_BORDER = pg.Rect (0,SCREEN_HEIGHT,SCREEN_WIDTH,1)
LEFT_BORDER = pg.Rect(0,0,1,SCREEN_HEIGHT)
RIGHT_BORDER = pg.Rect(SCREEN_WIDTH,0,1,SCREEN_HEIGHT)
PLATFORM_WIDTH = 200
PLATFORM_HEIGHT = 30
BALL_WIDTH = 50
BALL_HEIGHT = 50
FPS = 120

def game(screen, clock):

    
    


    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)


    PLATFORM_X = (SCREEN_WIDTH - PLATFORM_WIDTH ) //2
    PLATFORM_Y = int(SCREEN_HEIGHT * 0.8)
    PLATFORM_SPEED =  3 
    BALL_X = 270
    BALL_Y = 270
    BALL_SPEED = 3
    BALL_DIRECTION=pg.math.Vector2(0,1).normalize()
    COUNTER = 0

    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pg.display.set_caption("tilauncher")
    clock = pg.time.Clock()
   

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
        pg.draw.rect( screen, BLACK, platform)
        ball = pg.Rect( BALL_X, BALL_Y, BALL_WIDTH, BALL_HEIGHT)
        pg.draw.rect( screen, BLACK, ball)
        text_surface = def_font.render(str(COUNTER), False, (255,0,0))


        if ball.colliderect(platform):
            BALL_DIRECTION = BALL_DIRECTION.reflect(pg.math.Vector2(0,-1))
            COUNTER += 1
        if ball.colliderect(POT_BORDER):
            BALL_DIRECTION = BALL_DIRECTION.reflect(pg.math.Vector2(0,1))
        if ball.colliderect(BOTTOM_BORDER):
            break
        # BALL_DIRECTION = BALL_DIRECTION.reflect(pg.math.Vector2(0,-1))
        if ball.colliderect(LEFT_BORDER):
            BALL_DIRECTION = BALL_DIRECTION.reflect(pg.math.Vector2(1,0))
        if ball.colliderect(RIGHT_BORDER):
            BALL_DIRECTION = BALL_DIRECTION.reflect(pg.math.Vector2(-1,0))
        # if ball.colliderect(pg.Rect(0,0,width=SCREEN_WIDTH,height=0)):

        screen.blit(text_surface, (20,20))
        pg.display.flip()
        clock.tick(FPS)

if __name__== '__main__':
    screen_out = pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    Clock_out = pg.time.Clock()
    while True:
        game(screen_out,Clock_out)
        finish_text = def_font.render('Game Over', False,(0,0,0))
        screen_out.blit(finish_text, (SCREEN_WIDTH/2-30, SCREEN_HEIGHT/2))
        pg.display.flip()
        while True:
            for i in pg.event.get():
                if i.type == pg.QUIT:
                    sys.exit()
            keys = pg.key.get_pressed()
            if keys [pg.K_r]:
                break