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

dead = False
vertSpeed = 0
hoSpeed = 0
# defines speed of enemy
enemySpeed = 3
	
clock = pygame.time.Clock()

screen = pygame.display.set_mode( (1000, 380) )

background = pygame.image.load( "grass_jk.png" ).convert_alpha()
hero = pygame.image.load( "archer_main.png" ).convert_alpha()
rock = pygame.image.load( "rock.png" ).convert_alpha()
enemy = pygame.image.load( "enemy_temp.png" ).convert_alpha()

def reset(bkground):
    screen.fill( (255, 255, 255) )
    screen.blit( bkground, (0,0) )
    screen.blit( rock, (500, 180) )

screen.blit( hero, (50, 50) )
screen.blit( enemy, (500, 100) )

refresh = []

rock_Rect = rock.get_rect().move(500, 180)
hero_Rect = hero.get_rect().move(50, 50)
enemy_Rect = enemy.get_rect().move(500, 100)

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
           
        
        if event.type == pygame.KEYDOWN and dead != True:
            key = pygame.key.get_pressed()
            if key[pygame.K_w] and wOn:
                print "W"
                vertSpeed-=1
                wOn=False
            if key[pygame.K_a] and aOn:
                print "A"
                hoSpeed-=1
                aOn=False
            if key[pygame.K_s] and sOn:
                print "S"
                vertSpeed+=1
                sOn=False
            if key[pygame.K_d] and dOn:
                print "D"
                hoSpeed+=1
                dOn=False
        if event.type == pygame.KEYUP:
            keyAfter = pygame.key.get_pressed()
            if key[pygame.K_w] != keyAfter[pygame.K_w] and wOn != True:
                print "UPW"
                vertSpeed+=1
                wOn=True
            if key[pygame.K_a] != keyAfter[pygame.K_a] and aOn != True:
                print "UPA"
                hoSpeed+=1
                aOn=True
            if key[pygame.K_s] != keyAfter[pygame.K_s] and sOn != True:
                print "UPS"
                vertSpeed-=1
                sOn=True
            if key[pygame.K_d] != keyAfter[pygame.K_d] and dOn != True:
                print "UPD"
                hoSpeed-=1
                dOn=True

        # reset button
        if event.type == pygame.KEYDOWN and dead == True:
            key = pygame.key.get_pressed()
            if key[pygame.K_r]:
                print ( "r is hit" )
                reset(background)
                hero = pygame.image.load( "archer_main.png" ).convert_alpha()
                dead = False
                hero_Rect.top = 50
                hero_Rect.left = 50
                enemy_Rect.top = 100
                enemy_Rect.left = 500
     
    #Catches pygame event errors
    catch=pygame.key.get_pressed()
    if catch[pygame.K_w] == False and catch[pygame.K_a] == False and catch[pygame.K_s] == False and catch[pygame.K_d] == False:
        hoSpeed=0
        vertSpeed=0
    
    # collision checker
    if hero_Rect.colliderect( rock_Rect ):
        # print( "colliding" )
        if hero_Rect.left >= rock_Rect.right - 6:
            #hoSpeed = 0
            hero_Rect.left = rock_Rect.right
        elif hero_Rect.right <= rock_Rect.left + 6:
            #hoSpeed = 0
            hero_Rect.right = rock_Rect.left
        elif hero_Rect.top <= rock_Rect.bottom - 6:
            #vertSpeed = 0
            hero_Rect.bottom = rock_Rect.top
            #print( "colliding with bottom" )
        elif hero_Rect.bottom >= rock_Rect.top + 6:
            #vertSpeed = 0
            #print( "colliding with top" )
            hero_Rect.top = rock_Rect.bottom

    # enemy collision checking
    if enemy_Rect.colliderect( rock_Rect ):
        # print( "colliding" )
        if enemy_Rect.left >= rock_Rect.right - 6:
            #hoSpeed = 0
            enemy_Rect.left = rock_Rect.right
        elif enemy_Rect.right <= rock_Rect.left + 6:
            #hoSpeed = 0
            enemy_Rect.right = rock_Rect.left
        elif enemy_Rect.top <= rock_Rect.bottom - 6:
            #vertSpeed = 0
            enemy_Rect.bottom = rock_Rect.top
            #print( "colliding with bottom" )
        elif enemy_Rect.bottom >= rock_Rect.top + 6:
            #vertSpeed = 0
            #print( "colliding with top" )
            enemy_Rect.top = rock_Rect.bottom
            
    
    # enemy AI, deciding where it needs to move
    if enemy_Rect.bottom < hero_Rect.centery:
        vertVar = 1
    elif enemy_Rect.top > hero_Rect.centery:
        vertVar = -1
    else:
        vertVar = 0
    if enemy_Rect.right < hero_Rect.centerx:
        hoVar = 1
    elif enemy_Rect.left > hero_Rect.centerx:
        hoVar = -1
    else:
        hoVar = 0
        
    # enemy collision with hero checker
    if enemy_Rect.colliderect( hero_Rect ):
        hero = pygame.image.load( "dead.png" ).convert_alpha()
        hoSpeed = 0
        vertSpeed = 0
        dead = True
        for event in pygame.event.get(): 
            if event.type == pygame.KEYDOWN:
                key = pygame.key.get_pressed()
    
    # movement code
    hero_Rect = hero_Rect.move( hoSpeed * 5, vertSpeed * 5)
    enemy_Rect = enemy_Rect.move( hoVar * enemySpeed, vertVar * enemySpeed )

    # adding all the rectangles to the refresh list
    refresh.append( hero_Rect )
    refresh.append( background.get_rect() )
    refresh.append( enemy_Rect )

    # redrawing everything
    reset(background)
    screen.blit( hero, (hero_Rect) )
    screen.blit( enemy, (enemy_Rect) )

    pygame.display.update( refresh )
    
    refresh = []
    
    clock.tick(30)

print "terminating"
