'''
written by Mathias Dyssegaard Kallick
1/8/2015
main.py - holds the code necessary to display a background and the hero, for now.
'''

# imports
import sys, pygame, math, agent, os
import titlescreen, engine, room

# initialize
pygame.mixer.pre_init()
pygame.init()
pygame.mixer.init()

# initialize the fonts
try:
	pygame.font.init()
except:
	print "Fonts unavailable"
	sys.exit()

#width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
WIDTH = 1200
HEIGHT = 700
screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
os.environ['SDL_VIDEO_CENTERED'] = '1'

# START SCREEN FUNCTION

def start():

	images = []
	clock = pygame.time.Clock()
	start_Frame = 0
	current_Frame = 0
	x = 0
	i = 0
	screen.fill((0,0,0))
	pygame.display.update()
	
	crickets = pygame.mixer.Sound("sounds/crickets.wav")
	pygame.mixer.music.load("sounds/BKGmusic/MenuTitle/Sunnybreeze.wav")
	pygame.mixer.music.play(-1,0)
	
	while i < 72:
		images.append( str(i) )
		if i < 10:
			images[i] = pygame.image.load( "Title_Screen_Gif/frame_00" + str(i) + ".gif" ).convert_alpha()
			images[i] = pygame.transform.smoothscale( images[i], (WIDTH/2, HEIGHT) )
		else:
			images[i] = pygame.image.load( "Title_Screen_Gif/frame_0" + str(i) + ".gif" ).convert_alpha()
			images[i] = pygame.transform.smoothscale( images[i], (WIDTH/2, HEIGHT) )
		i += 1
	
	while 10 == 10:
		refresh = []
		start_Frame += 1
		crickets.play()
		crickets.fadeout(500)
		crickets.play()
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				key = pygame.key.get_pressed()
				if key[pygame.K_SPACE]:
					crickets.stop()
					titlescreen.main(WIDTH,HEIGHT)

		refresh.append ( images[0].get_rect().move(287,0) )
		
		if start_Frame % 2 == 0:
			screen.blit( images[current_Frame], (287,0) )
			current_Frame += 1
			if current_Frame == 71:
				current_Frame = 0

		pygame.display.update( refresh )
		clock.tick(30)
	
# SANDBOX ROOM FUNCTION					
def sandbox():
	clock = pygame.time.Clock()
	mainengine	= engine.engine("sandbox", screen, clock, WIDTH,HEIGHT)
	mainengine.main()

# TUTORIAL ROOM FUNCTION
def tutorial():
	clock = pygame.time.Clock()
	mainengine	= engine.engine("tutorial", screen, clock, WIDTH,HEIGHT)
	mainengine.main()


# MAIN ROOM FUNCTION
def main():
	clock = pygame.time.Clock()
	mainengine	= engine.engine("main", screen, clock, WIDTH,HEIGHT)
	mainengine.main()
	
# main loop:
if __name__ == "__main__":
	while 1 == 1:
		start()