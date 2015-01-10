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
#Control limits 
wOn=True
aOn=True
sOn=True
dOn=True
while (10 == 10):
    for event in pygame.event.get():
        #if event.type == pygame.MOUSEMOTION:   
    
        if event.type == pygame.MOUSEBUTTONDOWN:
            sys.exit()
           
        
        if event.type == pygame.KEYDOWN:
            key = pygame.key.get_pressed()
            if key[pygame.K_w] and wOn:
                print "W"
                vertSpeed=-5
                wOn=False
            if key[pygame.K_a] and aOn:
                print "A"
                hoSpeed=-5
                aOn=False
            if key[pygame.K_s] and sOn:
                print "S"
                vertSpeed=5
                sOn=False
            if key[pygame.K_d] and dOn:
                print "D"
                hoSpeed=5
                dOn=False
        if event.type == pygame.KEYUP:
            if key[pygame.K_w] and wOn != True:
                print "UPW"
                vertSpeed+=5
                wOn=True
            if key[pygame.K_a] and aOn != True:
                print "UPA"
                hoSpeed+=5
                aOn=True
            if key[pygame.K_s] and sOn != True:
                print "UPS"
                vertSpeed-=5
                sOn=True
            if key[pygame.K_d] and dOn != True:
                print "UPD"
                hoSpeed-=5
                dOn=True
    
    
    
    
    if hero_Rect.colliderect( rock_Rect ):
        print( "colliding" )
        if hero_Rect.left >= rock_Rect.left:
            #hoSpeed = 0
            hero_Rect.left = rock_Rect.right
        elif hero_Rect.right <= rock_Rect.right:
            #hoSpeed = 0
            hero_Rect.right = rock_Rect.left
        elif hero_Rect.top <= rock_Rect.top:
            #vertSpeed = 0
            hero_Rect.top = rock_Rect.bottom
        elif hero_Rect.bottom >= rock_Rect.bottom:
            #vertSpeed = 0
            hero_Rect.bottom = rock_Rect.top

    hero_Rect = hero_Rect.move( hoSpeed * 5, vertSpeed * 5)
	
    refresh.append( hero_Rect )
    refresh.append( background.get_rect() )

    reset()
    screen.blit( hero, (hero_Rect) )
	
    pygame.display.update( refresh )
	
    refresh = []
	
    clock.tick(30)

print "terminating"
