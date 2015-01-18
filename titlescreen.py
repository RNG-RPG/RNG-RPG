# written by Raymond Chung
# file  titlescreen.py
#
#-------------------------------------------------------------------------------
#---[ Imports ]-----------------------------------------------------------------
#-------------------------------------------------------------------------------
import sys, pygame, random, os, os.path, glob, itertools, ntpath
from random import shuffle
from pygame.locals import *
from menu import *
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
  pygame.mixer.pre_init()
  rain = pygame.mixer.Sound("sounds/rain.wav")
  beginsound= pygame.mixer.Sound("sounds/begin.wav")
  beginsound.set_volume(1)
  
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
  
  # Create the menus. 
  menu0 = cMenu(HEIGHT/5, WIDTH/5, 20, 5, 'vertical', 100, screen,
              [('Play',      1, None),
              ('Tutorial',      2, None),
              ('Directions',         3, None),
              ('Credits',         4, None),
              ('Exit',           9, None)])

  menu2 = cMenu(0, 0, 5, 5, 'vertical', 20, screen,
              [("W = UP", 3, None),
              ('S = DOWN', 3, None),
              ('D = LEFT', 3, None),
              ('A = RIGHT', 3, None),
              ('R = RETRY', 3, None),
              ('P = PAUSE', 3, None),
              ('Esc = QUIT', 3, None),
              ('Left Click = ATTACK', 3, None),
              ('Back', 0, None)])

  menu3 = cMenu(0, 0, 20, 5, 'vertical', 20, screen,
              [('PRODUCER - Larry Patrizio',               4, None),
              ('LEAD GAME DESIGNER - Shawn Jiang',         4, None),
              ('LEAD PROGRAMMER- Mathias Kallick',         4, None),
              ('LEAD ARTIST- Ed Zhou',                     4, None),
              ('LEAD SOUND SPECIALIST- Raymond Chung',     4, None),
              ('',          4, None),
              ('Back',          0, None),
              ('Exit',               9, None)])

  # Place menus at the center of the screen
  menu2.set_center(True, True)
  menu3.set_center(True, True)

  # Create the state variables (make them different so that the user event is
  # triggered at the start of the "while 1" loop so that the initial display
  # does not wait for user input)
  state = 0
  prev_state = 1

  # rect_list is the list of pygame.Rect's that will tell pygame where to
  # update the screen (there is no point in updating the entire screen if only
  # a small portion of it changed!)
  rect_list = []

  # The main while loop
  y=0
  pygame.mixer.music.load("sounds/BKGmusic/MenuStart/TowardsFate.wav")
  pygame.mixer.music.play(-1,0)
  rain.play(-1)
  rain.set_volume(.5)
  
  while 1:
  # Check if the state has changed, if it has, then post a user event to
  # the queue to force the menu to be shown at least once
    if prev_state != state:
      pygame.event.post(pygame.event.Event(EVENT_CHANGE_STATE, key = 0))
      prev_state = state
    
      if state in [0, 1, 2, 3, 4]:
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
        rain.stop()
        beginsound.play()
        play.main()
      elif state == 2:
        rain.stop()
        play.tutorial()
      elif state == 3:
        rect_list, state = menu2.update(e, state)
      elif state == 4:
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
