#! /usr/bin/python
# written by Raymond Chung
# \file  example.py
#
#-------------------------------------------------------------------------------
#---[ Imports ]-----------------------------------------------------------------
#-------------------------------------------------------------------------------
import sys, pygame, random, os, os.path, glob, itertools, ntpath
from random import shuffle
from pygame.locals import *
from menutest import *
from image import *
import play


## ---[ main ]------------------------------------------------------------------
#  This function runs the entire screen and contains the main while loop
#
def main(WIDTH,HEIGHT):
  # Uncomment this to center the window on the computer screen
  os.environ['SDL_VIDEO_CENTERED'] = '1'

  # Initialize Pygame
  pygame.init()

  # Create a window of 800x600 pixels
  clock = pygame.time.Clock()
  LENGTH = WIDTH
  HEIGHT = HEIGHT
  clock = pygame.time.Clock()
  screen = pygame.display.set_mode((LENGTH, HEIGHT))

  # Set the window caption
  pygame.display.set_caption("RNG-RPG")

  # Load some images to use for sample buttons
  BKG = []
  for bkg in glob.glob("./images/bkg-*.png"):
    back= load_image(bkg,"",LENGTH,HEIGHT)
    BKG.append(back)
  
  image1  = load_image('1.png', 'images',50,50)
  image2  = load_image('2.png', 'images',50,50)
  image3  = load_image('3.png', 'images',50,50)
  image4  = load_image('4.png', 'images',5,50)
  
  # Create 3 diffrent menus.  One of them is only text, another one is only
  # images, and a third is -gasp- a mix of images and text buttons!  To
  # understand the input factors, see the menu file
  menu0 = cMenu(50, 50, 20, 5, 'vertical', 100, screen,
              [('Play',      1, None),
              ('Directions',         2, None),
              ('Settings',         3, None),
              ('Exit',           9, None)])

  menu2 = cMenu(0, 0, 5, 5, 'vertical', 7, screen,
              [("UP = W", 2, None),
              ('DOWN = S', 2, None),
              ('LEFT = D', 2, None),
              ('RIGHT = A', 2, None),
              ('ATTACK = Left Click', 2, None),
              ('Back', 0, None)])

  menu3 = cMenu(25, 15, 20, 5, 'vertical', 7, screen,
              [('Directions',         2, None),
              ('Back',          0, None),
              ('Play',            1, None),
              ('Exit',               9, None)])

  # Center menu2 at the center of the draw_surface (the entire screen here)
  menu2.set_center(True, True)

  # Create the state variables (make them different so that the user event is
  # triggered at the start of the "while 1" loop so that the initial display
  # does not wait for user input)
  state = 0
  prev_state = 1

  # rect_list is the list of pygame.Rect's that will tell pygame where to
  # update the screen (there is no point in updating the entire screen if only
  # a small portion of it changed!)
  rect_list = []

  # Ignore mouse motion (greatly reduces resources when not needed)
  pygame.event.set_blocked(pygame.MOUSEMOTION)

  # The main while loop
  y=0
  while 1:
  # Check if the state has changed, if it has, then post a user event to
  # the queue to force the menu to be shown at least once
    
    if prev_state != state:
      pygame.event.post(pygame.event.Event(EVENT_CHANGE_STATE, key = 0))
      prev_state = state
    
      if state in [0, 1, 2, 3]:
      # Reset the screen before going to the next menu.  Also, put a
      # caption at the bottom to tell the user what is going one
        screen.blit(BKG[0],(0,0))
        pygame.display.flip()

    # Get the next event
    e = pygame.event.wait()

    # Update the menu, based on which "state" we are in - When using the menu
    # in a more complex program, definitely make the states global variables
    # so that you can refer to them by a name
    if e.type == pygame.KEYDOWN or e.type == EVENT_CHANGE_STATE:
      if state == 0:
        rect_list, state = menu0.update(e, state)
      elif state == 1:
        play.main()
      elif state == 2:
        rect_list, state = menu2.update(e, state)
      elif state == 3:
        rect_list, state = menu3.update(e, state)
      elif state == 9:
        pygame.quit()
        sys.exit()

    # Quit if the user presses the exit button
    if e.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    if e.type == pygame.KEYDOWN:
      if e.key == pygame.K_ESCAPE:
        pygame.quit()
        sys.exit()

    # Update the screen
    pygame.display.update(rect_list)


## ---[ The python script starts here! ]----------------------------------------
# Run the script
if __name__ == "__main__":
  main()


#---[ END OF FILE ]-------------------------------------------------------------
