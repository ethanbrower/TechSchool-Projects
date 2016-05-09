
  #wizard_take_down.py
#Ethan Brower
#3/10/16

import pygame
import random
from tkinter import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
LBLUE = (125, 188, 209)
YELLOW = (210, 217, 28)
ORANGE = (217, 138, 28)
PURPLE = (135, 28, 217)
DGREEN = (3, 140, 14)
BROWN = (64, 46, 27)
DBROWN = (51, 33, 15)
GRAY = (70, 70, 70)

pygame.init()
 

size = (1000, 563)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("WIZARD TAKE DOWN!")

pygame.key.set_repeat(30, 30)

done = False


x_speed = 0
y_speed = 0
 
x_coord = 100
y_coord = 375

x_speed2 = 0
y_speed2 = 0

x_coord2 = 800
y_coord2 = 375

x_speed3 = 0
y_speed3 = 0
 
x_coord3 = x_coord + 35
y_coord3 = y_coord + 40



w1_a1_spd = 3
w1_a1_x = x_coord + 50
w1_a1_y = y_coord + 40

#atk1 = 'false'

#create characters
def wiz1(screen, x_c, y_c):
    screen.blit(w1, (x_c, y_c))

def wiz2(screen, x_c, y_c):
    screen.blit(w2, (x_c, y_c))

def wiz1_atk1(screen, wiz1_xcoord, wiz1_ycoord):
    screen.blit(w1_a1, (wiz1_xcoord, wiz1_ycoord))
  
    

clock = pygame.time.Clock()

w1 = pygame.image.load('game stuff/wiz1.png')
w2 = pygame.image.load('game stuff/wiz2.png')
w1_a1 = pygame.image.load('game stuff/FIREblast.png')
music = pygame.mixer.Sound('game stuff/game.ogg')
background = pygame.image.load('game stuff/bckgd.png')

# -------- Main Program Loop -----------
while not done:
    music.play()
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
            
        #player 1 controls
        elif event.type == pygame.KEYDOWN:
        
            if event.key == pygame.K_a:
                x_speed = -3
            elif event.key == pygame.K_d:
                x_speed = 3
            elif event.key == pygame.K_w:
                y_speed = -3
            elif event.key == pygame.K_s:
                y_speed = 3
            elif event.key == pygame.K_v:
                pass
                    
                
        
                
 
    
        elif event.type == pygame.KEYUP:
        
            if event.key == pygame.K_a or event.key == pygame.K_d:
                x_speed = 0
            elif event.key == pygame.K_w or event.key == pygame.K_s:
                y_speed = 0
            elif event.key == pygame.K_v:
                pass
                

        #player 2 controls
        if event.type == pygame.KEYDOWN:
        
            if event.key == pygame.K_LEFT:
                x_speed2 = -3
            elif event.key == pygame.K_RIGHT:
                x_speed2 = 3
            elif event.key == pygame.K_UP:
                y_speed2 = -3
            elif event.key == pygame.K_DOWN:
                y_speed2 = 3
 
    
        elif event.type == pygame.KEYUP:
        
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed2 = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed2 = 0
 

        x_coord += x_speed
        y_coord += y_speed

        x_coord2 += x_speed2
        y_coord2 += y_speed2
        
    #draw all graphics
    screen.fill(WHITE)
    '''pygame.draw.rect(screen, BROWN, [0, 300, 1000, 400], 0)
    pygame.draw.rect(screen, DBROWN, [0, 700, 1000, 50], 0)'''

    screen.blit(background, (0,0))

    #screen.blit(w1_a1, (x_coord3, y_coord3))
    #x_coord3 = x_coord + 35
    #y_coord3 = y_coord + 40

    wiz1_atk1(screen, x_coord3 , y_coord3)
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_v:
            x_coord3 += 10


    wiz1(screen, x_coord, y_coord)
    if x_coord < 1: 
        x_coord = 1
    if x_coord > 460:
        x_coord = 460
    if y_coord < 301:
        y_coord = 301
    if y_coord > 463:
        y_coord = 463
        
    wiz2(screen, x_coord2, y_coord2)
    if x_coord2 < 500: 
        x_coord2 = 500
    if x_coord2 > 900:
        x_coord2 = 900
    if y_coord2 < 301:
        y_coord2 = 301
    if y_coord2 > 463:
        y_coord2 = 463

    
            

    
    pygame.display.flip()


    clock.tick(60)
 

pygame.quit()
