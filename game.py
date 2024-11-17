import sys 
import pygame as pg
import pygame.mixer as mixer
mixer.init()
pg.init()

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
sound_back_groung = mixer.Sound('back-ground-music.mp3')
sound_colision = mixer.Sound('Sound.mp3')
sound_platform = mixer.Sound('Sound-platform.mp3')

def game(screen, clock, assets):

    

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
        # pg.draw.rect( screen, BLACK, platform)
        
        ball = assets['ball'].get_rect()

        ball.x = BALL_X

        ball.y = BALL_Y

        # ball = pg.Rect( BALL_X, BALL_Y, BALL_WIDTH, BALL_HEIGHT)
        platform = assets['panel'].get_rect()

        platform.x = PLATFORM_X

        platform.y = PLATFORM_Y

        # pg.draw.rect( screen, BLACK, ball)
        screen.blit(assets['ball'], ball)
        screen.blit(assets['panel'], platform)
        text_surface = def_font.render(str(COUNTER), False, (255,0,0))



        if ball.colliderect(platform):
            sound_platform.play()
            ball_center = (ball.x + ball.width/2, ball.y + ball.height/2)
            platform_center = (platform.x + platform.width/2, platform.y + platform.height/2)
            colision_vector = (ball_center[0]-platform_center[0],ball_center[1]-platform[1])
            BALL_DIRECTION = pg.math.Vector2(colision_vector).normalize()
            COUNTER += 1
        


        if ball.colliderect(POT_BORDER):
            sound_colision.play()
            BALL_DIRECTION = BALL_DIRECTION.reflect(pg.math.Vector2(0,1))



        if ball.colliderect(BOTTOM_BORDER):
            break


        # BALL_DIRECTION = BALL_DIRECTION.reflect(pg.math.Vector2(0,-1))
        if ball.colliderect(LEFT_BORDER):
            sound_colision.play()
            BALL_DIRECTION = BALL_DIRECTION.reflect(pg.math.Vector2(1,0))



        if ball.colliderect(RIGHT_BORDER):
            sound_colision.play()
            BALL_DIRECTION = BALL_DIRECTION.reflect(pg.math.Vector2(-1,0))
        # if ball.colliderect(pg.Rect(0,0,width=SCREEN_WIDTH,height=0)):


        screen.blit(text_surface, (20,20))
        pg.display.flip()
        clock.tick(FPS)

if __name__== '__main__':
    
    screen_out = pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    assets_int = {
        'ball': pg.transform.scale(pg.image.load('ball.png').convert_alpha(), (BALL_WIDTH, BALL_HEIGHT)),
        'panel': pg.transform.scale(pg.image.load('panel.png').convert_alpha(), (PLATFORM_WIDTH, PLATFORM_HEIGHT))
         }

    Clock_out = pg.time.Clock()

    while True:
        sound_back_groung.play()
        game(screen_out,Clock_out, assets_int)
        sound_back_groung.stop()
        finish_text = def_font.render('Game Over', False,(0,0,0))

        screen_out.blit(finish_text, (SCREEN_WIDTH/2-30, SCREEN_HEIGHT/2))

        pg.display.flip()



        while True:


            for i in pg.event.get():
                if i.type == pg.QUIT:
                    sys.exit()
            keys = pg.key.get_pressed()
            if keys [pg.K_0]:
                break