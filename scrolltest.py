import pygame, sys, glob, ntpath
from random import shuffle
from pygame.locals import *
from image import *

pygame.init()

clock = pygame.time.Clock()
LENGTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((LENGTH,HEIGHT))

BKG= []

for bkg in glob.glob("./images/bkg-*.png"):
  back= load_image(bkg,"",LENGTH,HEIGHT)
  BKG.append(back)
 
y = 0 

curr = 0
while True:
    for event in pygame.event.get():
         if event.type == QUIT:
             pygame.quit()
             sys.exit()
    screen.blit(BKG[curr],(0,0))
    
    y = y + HEIGHT
    print y
    if y == (len(BKG)-1)*HEIGHT:
        y = 0
    
    curr+=1
    curr = curr%len(BKG)
    
    msElapsed = clock.tick(10)
    pygame.display.flip()
