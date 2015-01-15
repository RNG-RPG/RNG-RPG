import pygame, sys, glob, ntpath
from random import shuffle
from pygame.locals import *
from image import *

pygame.init()

clock = pygame.time.Clock()
LENGTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((LENGTH,HEIGHT))

BKG = []

for bkg in glob.glob("./images/bkg-*.png"):
  BKG.append(ntpath.basename(bkg))
 
y = 0 

while True:
    for event in pygame.event.get():
         if event.type == QUIT:
             pygame.quit()
             sys.exit()
    for i in range(len(BKG)): 
         back= load_image(BKG[i], 'images',LENGTH,HEIGHT)
         screen.blit(back, (0,y-(i*HEIGHT)))
    
    y = y + HEIGHT
    print y
    if y == (len(BKG)-1)*HEIGHT:
        y = 0

    msElapsed = clock.tick(10)
    pygame.display.flip()
