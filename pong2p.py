# Import the required imports
import pygame as pg
from pygame.locals import *
import pygame.mixer as mixer
import sys
import time

#define variables
window_width, window_height = 1500, 1000
pscore = 0
cscore = 0
move_speed = 7
playerPosX = 10
playerPosY = 0
playerWidth = 20
playerHeight = 130
cpuPosX = 1470
cpuPosY = 400
cpuWidth = 20
cpuHeight = 130

#define the player class
class Player1(object):
    def __init__(self):
        self.color = (255,255,255)
        self.width = 20
        self.height = 130
        self.positionx, self.positiony = 10, 400
    #function for drawing the player
    def draw(self, surface):
        r = pg.Rect((self.positionx, self.positiony), (self.width, self.height))
        pg.draw.rect(surface, self.color, r)
    #move the player
    def move(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w] and self.positiony > 0:
            self.positiony -= move_speed
        if keys[pg.K_s] and self.positiony < 860:
            self.positiony += move_speed
        #Horizontal Movement for testing
        #if keys[pg.K_LEFT] and self.positionx > 0:
         #   self.positionx -= move_speed
        #if keys[pg.K_RIGHT] and self.positionx < 1480:
         #   self.positionx += move_speed

class CPU(object):
    def __init__(self):
        self.color = (255,255,255)
        self.width = 20
        self.height = 130
        self.positionx, self.positiony = 1470, 400
    #function for drawing the player
    def draw(self, surface):
        r = pg.Rect((self.positionx, self.positiony), (self.width, self.height))
        pg.draw.rect(surface, self.color, r)
    def move(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_UP] and self.positiony > 0:
            self.positiony -= move_speed
        if keys[pg.K_DOWN] and self.positiony < 860:
            self.positiony += move_speed
        


class Ball(object):
    def __init__(self):
        self.color = (255, 255, 255)
        self.width = 10
        self.height = 10
        self.positionx, self.positiony = 750, 400
        self.velocityx, self.velocityy = 0, 0
        self.max_speed = 10
    def draw(self, surface):
        r = pg.Rect((self.positionx, self.positiony), (self.width, self.height))
        pg.draw.rect(surface, self.color, r)
    def reset(self):
        self.positionx, self.positiony = 750, 400

class DottedLine(object):
    def __init__(self):
        self.color = (255, 255, 255)
        self.width = 10
        self.height = 50
        self.positionx, self.positiony = 740, 25
    def draw(self, surface):
        r = pg.Rect((self.positionx, self.positiony), (self.width, self.height))
        pg.draw.rect(surface, self.color, r)
        rr = pg.Rect((self.positionx, self.positiony + 100), (self.width, self.height))
        pg.draw.rect(surface, self.color, rr)
        rrr = pg.Rect((self.positionx, self.positiony + 200), (self.width, self.height))
        pg.draw.rect(surface, self.color, rrr)
        rrrr = pg.Rect((self.positionx, self.positiony + 300), (self.width, self.height))
        pg.draw.rect(surface, self.color, rrrr)
        rrrrr = pg.Rect((self.positionx, self.positiony + 400), (self.width, self.height))
        pg.draw.rect(surface, self.color, rrrrr)
        rrrrrr = pg.Rect((self.positionx, self.positiony + 500), (self.width, self.height))
        pg.draw.rect(surface, self.color, rrrrrr)
        rrrrrrr = pg.Rect((self.positionx, self.positiony + 600), (self.width, self.height))
        pg.draw.rect(surface, self.color, rrrrrrr)
        rrrrrrrr = pg.Rect((self.positionx, self.positiony + 700), (self.width, self.height))
        pg.draw.rect(surface, self.color, rrrrrrrr)
        rrrrrrrrr = pg.Rect((self.positionx, self.positiony + 800), (self.width, self.height))
        pg.draw.rect(surface, self.color, rrrrrrrrr)
        rrrrrrrrrr = pg.Rect((self.positionx, self.positiony + 900), (self.width, self.height))
        pg.draw.rect(surface, self.color, rrrrrrrrrr)

def main():
    pg.init()
    mixer.init()

    mixer.music.load("python/pong/blipSelect.wav")

    #screen stuff
    screen = pg.display.set_mode((window_width, window_height), pg.RESIZABLE)
    pg.display.set_caption("Pong?")
    icon = pg.image.load("python/pong/icon.png")
    pg.display.set_icon(icon)
    surface = pg.Surface(screen.get_size())
    surface = surface.convert()

    #make the variable the class
    player1 = Player1()
    cpu = CPU()
    ball = Ball()
    dotted_line = DottedLine()

    pscore = 0
    cscore = 0

    ball.velocityx += move_speed
    ball.velocityy += move_speed

    myfont = pg.font.SysFont("monospace",16)

    while True:
        #loops and stuff
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        playerPosX = player1.positionx
        playerPosY = player1.positiony
        playerWidth = player1.width
        playerHeight = player1.height
        cpuPosX = cpu.positionx
        cpuPosY = cpu.positiony
        cpuWidth = cpu.width
        cpuHeight = cpu.height
        pg.time.delay(10)
        surface.fill((0, 0, 0))
        pg.display.flip()

        player1.draw(surface)
        player1.move()

        cpu.draw(surface)
        cpu.move()
        ball.draw(surface)
        dotted_line.draw(surface)

        ball.positionx += ball.velocityx
        ball.positiony += ball.velocityy

        #ball collisions
        if ball.positionx > 1470 - ball.width and ball.positiony < cpuPosY + cpuHeight and ball.positiony > cpuPosY - cpuHeight:
            ball.velocityx = -ball.velocityx
            mixer.music.play()
        if ball.positionx < 30 + ball.width and ball.positiony < playerPosY + playerHeight and ball.positiony > playerPosY - playerHeight:
            ball.velocityx = -ball.velocityx
            mixer.music.play()
        if ball.positiony < 0:
            ball.velocityy = -ball.velocityy
            mixer.music.play()
        if ball.positiony > window_height - ball.height:
            ball.velocityy = -ball.velocityy
            mixer.music.play()

        #Scores
        if ball.positionx > window_width:
            pscore += 1
            ball.reset()
        if ball.positionx < 0:
            cscore += 1
            ball.reset()
        
        #Winning
        if pscore > 3:
            print('Player1 wins')
            pg.quit()
            sys.exit()
        if pscore > 3:
            print('Player2 wins')
            pg.quit()
            sys.exit()

        #screen stuff
        screen.blit(surface, (0, 0))
        pg.display.update()

main()