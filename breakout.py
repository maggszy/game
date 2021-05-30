import sys
import pygame
import random
from wall import Wall

class Breakout():
    def main(self):
        self.xspeed0 = 6
        self.yspeed0 = 6
        self.full_lives = 5
        self.paddle_speed = 30
        self.score = 0 
        bgcolor = 0x08, 0x00, 0x1E  #ciemnygranat
        size = self.width, self.height = 640, 480
        #BLACK= (0,0,0)

        pygame.init()
        pygame.display.set_caption("Breakout!!")
        screen = pygame.display.set_mode(size)
        #clock = pygame.time.Clock()

        paddle = pygame.image.load("images/glasspaddle.png").convert()
        self.paddlerect = paddle.get_rect()  #tutaj tak samo jak w ball

        ball = pygame.image.load("images/myball.png").convert()
        ball.set_colorkey((255, 255, 255)) #zmienić, by nie było ramki dookoła
        self.ballrect = ball.get_rect()

        self.bounce = pygame.mixer.Sound('sound/bounce_sound.wav')
        self.bounce.set_volume(10)

        self.wall = Wall()
        self.wall.build_wall(self.width)

        #initialize for game loop
        self.paddlerect = self.paddlerect.move((self.width/2) - (self.paddlerect.right/2), self.height-20)
        self.ballrect = self.ballrect.move(self.width/2, self.height/2)
        self.xspeed = self.xspeed0
        self.yspeed = self.yspeed0
        self.lives = self.full_lives
        clock = pygame.time.Clock()
        pygame.key.set_repeat(1,30)
        pygame.mouse.set_visible(0)

        while 1:
            clock.tick(60)
            self.key_press()
            self.hit_ball()
            self.move_ball()
            self.lose_life(bgcolor, screen)
            #make visible how many lives left
            
           # if self.xspeed < 0 and self.ballrect.left <0:
            #    self.xspeed = - self.xspeed
             #   self.bounce.play(0)

            #if self.xspeed > 0 and self.ballrect.right > self.width:
             #   self.xspeed = - self.xspeed
              #  self.bounce.play(0)
            self.hit_wall()
                     
            screen.fill(bgcolor)
            scoretext = pygame.font.Font(None, 40).render(str(self.score), True, (0,255,255),bgcolor)
            scoretextrect = scoretext.get_rect()
            scoretextrect = scoretextrect.move(self.width - scoretextrect.right, 0)
            screen.blit(scoretext, scoretextrect)

            self.rebuild_wall()

            for i in range(0,len(self.wall.brickrect)):
                screen.blit(self.wall.brick, self.wall.brickrect[i])

            screen.blit(ball,self.ballrect)
            screen.blit(paddle,self.paddlerect)
            pygame.display.flip()

    #for paddle movement
    def key_press(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                if event.key == pygame.K_LEFT:                        
                    self.paddlerect = self.paddlerect.move(-self.paddle_speed, 0)     
                    if (self.paddlerect.left < 0):                           
                        self.paddlerect.left = 0      
                if event.key == pygame.K_RIGHT:                    
                    self.paddlerect = self.paddlerect.move(self.paddle_speed, 0)
                    if (self.paddlerect.right > self.width):                            
                        self.paddlerect.right = self.width
    
    #check if paddle has hit ball
    def hit_ball(self):
        if self.ballrect.bottom >= self.paddlerect.top and \
            self.ballrect.bottom <= self.paddlerect.bottom and \
            self.ballrect.right >= self.paddlerect.left and \
            self.ballrect.left <= self.paddlerect.right:
            
            self.yspeed = -self.yspeed
            self.bounce.play(0)
            offset = self.ballrect.center[0] - self.paddlerect.center[0]
            #changing angle of ball depending on the place where ball hits paddle
            if offset > 0:
                if offset >30:
                    self.xspeed = 7
                elif offset > 23:
                    self.xspeed = 6
                elif offset > 17:
                    self.xspeed = 5
            else:
                if offset < -30:
                    self.xspeed = -7
                elif offset < -23:
                    self.xspeed = -6
                elif offset < -17:
                    self.xspeed = -5

    def move_ball(self):
        self.ballrect = self.ballrect.move(self.xspeed, self.yspeed)
        if self.ballrect.left < 0 or self.ballrect.right > self.width:
            self.xspeed = - self.xspeed
            self.bounce.play(0)
        if self.ballrect.top < 0:
            self.yspeed = - self.yspeed
            self.bounce.play(0)

    def lose_life(self, bgcolor, screen):
        if self.ballrect.top > self.height:
            self.lives -=1
            self.xspeed = self.xspeed0 #starts new ball
            if random.random() > 0.5:
                self.xspeed = -self.xspeed
            self.yspeed = self.yspeed0
            self.ballrect.center = self.width * random.random(), self.height/3

            if self.lives ==0:  #change this into another screen
                msg = pygame.font.Font(None, 70).render("Game Over", True, (0,255,255), bgcolor)
                msgrect = msg.get_rect()
                msgrect = msgrect.move(self.width/2 - (msgrect.center[0]), self.height/3)
                screen.blit(msg, msgrect)
                pygame.display.flip()

                #process key press, ESC to quit, any other to restart game
                while 1:
                    restart = False
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            sys.exit()
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                sys.exit()
                            if not (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):                                    
                                restart = True  
                    if restart:
                        screen.fill(bgcolor)
                        self.wall.build_wall(self.width)
                        self.lives = self.full_lives
                        self.score = 0
                        break
    
    def hit_wall(self):
        idx = self.ballrect.collidelist(self.wall.brickrect)
        if idx != -1:
            if self.ballrect.center[0] > self.wall.brickrect[idx].right or\
                self.ballrect.center[0] < self.wall.brickrect[idx].left:
                self.xspeed = - self.xspeed
            else:
                self.yspeed = - self.yspeed
            self.bounce.play(0)
            self.wall.brickrect[idx:idx+1] = []
            self.score +=10

    def rebuild_wall(self):
        if self.wall.brickrect == []:
            self.wall.build_wall(self.width)
            self.xspeed = self.xspeed0
            self.yspeed = self.yspeed0
            self.ballrect.center = self.width/2, self.height/3



        
    



            






if __name__ == '__main__':
    br = Breakout()
    br.main()


