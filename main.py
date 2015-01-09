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

vertSpeed = 0
hoSpeed = 0
	
clock = pygame.time.Clock()

screen = pygame.display.set_mode( (1000, 380) )

background = pygame.image.load( "grass_jk.png" ).convert_alpha()
hero = pygame.image.load( "archer_main.png" ).convert_alpha()
rock = pygame.image.load( "rock.png" ).convert_alpha()
def reset():
    screen.fill( (255, 255, 255) )
    screen.blit( background, (0,0) )
    screen.blit( rock, (500, 180) )

screen.blit( hero, (50, 50) )

refresh = []

rock_Rect = rock.get_rect().move(500, 180)
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
                if vertSpeed == 1:
                    vertSpeed = 0
                else:
                    vertSpeed = -1
            if key[pygame.K_a]:
                print "A"
                if hoSpeed == 1:
                    hoSpeed = 0
                else:
                    hoSpeed = -1
            if key[pygame.K_s]:
                print "S"
                if vertSpeed == -1:
                    vertSpeed = 0
                else:
                    vertSpeed = 1
            if key[pygame.K_d]:
                print "D"
                if hoSpeed == -1:
                    hoSpeed = 0
                else:
                    hoSpeed = 1

        if event.type == pygame.KEYUP:
            if key[pygame.K_w]:
                print "UPW"
                if vertSpeed == -1:
                    vertSpeed = 0
                else:
                    vertSpeed = 1
            if key[pygame.K_a]:
                print "UPA"
                if hoSpeed == -1:
                    hoSpeed = 0
                else:
                    hoSpeed = 1
            if key[pygame.K_s]:
                print "UPS"
                if vertSpeed == 1:
                    vertSpeed = 0
                else:
                    vertSpeed = -1
            if key[pygame.K_d]:
                print "UPD"
                if hoSpeed == 1:
                    hoSpeed = 0
                else:
                    hoSpeed = -1

        if event.type == pygame.QUIT:
            sys.exit()
	
	if hero_Rect.colliderect( rock_Rect ):
		if hero_Rect.left == rock_Rect.right:
			if hoSpeed >= 0:
				hoSpeed = hoSpeed
			else:
				hoSpeed = 0
		if hero_Rect.right == rock_Rect.left:
			if hoSpeed <= 0:
				hoSpeed = hoSpeed
			else:
				hoSpeed = 0
		if hero_Rect.top == rock_Rect.bottom:
			if vertSpeed >= 0:
				hoSpeed = hoSpeed
			else:
				vertSpeed = 0
		if hero_Rect.bottom == rock_Rect.top:
			if vertSpeed <= 0:
				hoSpeed = hoSpeed
			else:
				vertSpeed = 0

    hero_Rect = hero_Rect.move( hoSpeed, vertSpeed )
	
    refresh.append( hero_Rect )
    refresh.append( background.get_rect() )

    reset()
    screen.blit( hero, (hero_Rect) )
	
    pygame.display.update( refresh )
	
    refresh = []
	
    clock.tick(30)

print "terminating"
