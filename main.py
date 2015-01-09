'''
written by Mathias Dyssegaard Kallick
1/8/2015
main.py - holds the code necessary to display a background and the hero, for now.
'''

# imports
import sys, pygame

# initialize
pygame.init()

# initialize the fonts
try:
	pygame.font.init()
except:
	print "Fonts unavailable"
	sys.exit()

speed = 0
speed1 = 0
	
clock = pygame.time.Clock()

screen = pygame.display.set_mode( (1000, 380) )

background = pygame.image.load( "grass_jk.png" ).convert_alpha()
hero = pygame.image.load( "temp_char.png" ).convert_alpha()
def reset():
    screen.fill( (255, 255, 255) )
    screen.blit( background, (0,0) )

screen.blit( hero, (50, 50) )

refresh = []

hero_Rect = hero.get_rect().move(50, 50)

pygame.display.update()

while (10 == 10):
    for event in pygame.event.get():
        #if event.type == pygame.MOUSEMOTION:   
    
        if event.type == pygame.MOUSEBUTTONDOWN:
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            key = pygame.key.get_pressed()
            if key[pygame.K_w]:
                print "W"
                if speed == 1:
                    speed = 0
                else:
                    speed = -1
            if key[pygame.K_a]:
                print "A"
                if speed1 == 1:
                    speed1 = 0
                else:
                    speed1 = -1
            if key[pygame.K_s]:
                print "S"
                if speed == -1:
                    speed = 0
                else:
                    speed = 1
            if key[pygame.K_d]:
                print "D"
                if speed1 == -1:
                    speed1 = 0
                else:
                    speed1 = 1

        if event.type == pygame.KEYUP:
            if key[pygame.K_w]:
                print "UPW"
                if speed == -1:
                    speed = 0
                else:
                    speed = 1
            if key[pygame.K_a]:
                print "UPA"
                if speed1 == -1:
                    speed1 = 0
                else:
                    speed1 = 1
            if key[pygame.K_s]:
                print "UPS"
                if speed == 1:
                    speed = 0
                else:
                    speed = -1
            if key[pygame.K_d]:
                print "UPD"
                if speed1 == 1:
                    speed1 = 0
                else:
                    speed1 = -1

        if event.type == pygame.QUIT:
            sys.exit()
			
    hero_Rect = hero_Rect.move( speed1, speed )
	
    refresh.append( hero_Rect )
    refresh.append( background.get_rect() )

    reset()
    screen.blit( hero, (hero_Rect) )
	
    pygame.display.update( refresh )
	
    refresh = []
	
    clock.tick(30)

print "terminating"
