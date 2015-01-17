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

# collision checker 
def pathCollide( object_rect, agent_rect, refresh_List ):
	if agent_rect.colliderect( object_rect ):
		# print( "colliding" )
		if agent_rect.left >= object_rect.right - 18:
			#hoSpeed = 0
			refresh_List.append( (agent_rect.x-30, agent_rect.y-30, agent_rect.width+60, agent_rect.height+60) )
			agent_rect.left = object_rect.right
		elif agent_rect.right <= object_rect.left + 18:
			#hoSpeed = 0
			refresh_List.append( (agent_rect.x-30, agent_rect.y-30, agent_rect.width+60, agent_rect.height+60) )
			agent_rect.right = object_rect.left
		elif agent_rect.top <= object_rect.bottom - 18:
			#vertSpeed = 0
			refresh_List.append( (agent_rect.x-30, agent_rect.y-30, agent_rect.width+60, agent_rect.height+60) )
			agent_rect.bottom = object_rect.top
			#print( "colliding with bottom" )
			refresh_List.append( object_rect )
		elif agent_rect.bottom >= object_rect.top + 18:
			#vertSpeed = 0
			refresh_List.append( (agent_rect.x-30, agent_rect.y-30, agent_rect.width+60, agent_rect.height+60) )
			#print( "colliding with top" )
			agent_rect.top = object_rect.bottom

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
	
	

print "terminating"
