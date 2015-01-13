'''
written by Mathias Dyssegaard Kallick
1/8/2015
main.py - holds the code necessary to display a background and the hero, for now.
'''

# imports
import sys, pygame, math

# initialize
pygame.init()

# initialize the fonts
try:
    pygame.font.init()
except:
    print "Fonts unavailable"
    sys.exit()

dead = False
arrowOn = False
enemyDead = False
vertSpeed = 0
hoSpeed = 0
frame = 0
# defines speed of enemy
enemySpeed = 0
    
clock = pygame.time.Clock()

width, height = pygame.display.Info().current_w, pygame.display.Info().current_h

screen = pygame.display.set_mode( (1000, 380) )

background = pygame.image.load( "RockGround2.png" ).convert_alpha()
heroSprites = pygame.image.load( "sprites/archer_main.png" ).convert_alpha()
rock = pygame.image.load( "rock.png" ).convert_alpha()
enemy = pygame.image.load( "dsprite/Dragon_Mouth_Closed.png" ).convert_alpha()
arrow = pygame.image.load( "arrow.png" ).convert_alpha()
target = pygame.image.load( "Pointer.png" ).convert_alpha()

#making the target move
pygame.event.pump()


mpos = pygame.mouse.get_pos()
target_Rect = target.get_rect().move( mpos[0], mpos[1] )


#Hero movement sprites
time = 0
counter = 0

'''down'''
herod = [(0, 102, 87, 102), (0, 0, 87, 102), (0, 204, 87, 102), (0, 0, 87, 102)]
'''right'''
heror = [(87, 102, 87, 102), (87, 0, 87, 102), (87, 204, 87, 102), (87, 0, 87, 102)]
'''up'''
herou = [(174, 102, 87, 102), (174, 0, 87, 102), (174, 204, 87, 102), (174, 0, 87, 102)]
'''left'''
herol = [(261, 102, 87, 102), (261, 0, 87, 102), (261, 204, 87, 102), (261, 0, 87, 102)]
'''down left'''
herodl = [(348, 102, 87, 101), (348, 0, 87, 102), (348, 204, 87, 102), (348, 0, 87, 102)]
'''down right'''
herodr = [(435, 102, 87, 102), (435, 0, 87, 102), (435, 204, 87, 102), (435, 0, 87, 102)]
'''up left'''
heroul = [(522, 102, 87, 102), (522, 0, 87, 102), (522, 204, 87, 102), (522, 0, 87, 102)]
'''up right'''
herour = [(609, 102, 87, 102), (609, 0, 87, 102), (609, 204, 87, 102), (609, 0, 87, 102)]


#remember which direction hero was facing
direction = herod
dFrame=herod[1]
def timeReset():
    counter=0
    time=-1

def reset(bkground):
    screen.blit( bkground, (0,0) )
    screen.blit( bkground, (648,0) )
    screen.blit( rock, (500, 180) )

screen.blit( heroSprites, (50, 50), dFrame  )
screen.blit( enemy, (500, 100) )
screen.blit( background, (0,0) )
screen.blit( background, (648,0) )
screen.blit( rock, (500, 180) )

refresh = []

rock_Rect = rock.get_rect().move(500, 180)
hero_Rect = pygame.Rect(50, 50, 87, 102)
enemy_Rect = enemy.get_rect().move(500, 100)

pygame.display.update()
#Control limits 
wOn=True
aOn=True
sOn=True
dOn=True
while (10 == 10):
    if pygame.mouse.get_focused():
        pygame.mouse.set_visible(False)
    frame = frame + 1
    # adding all the rectangles to the refresh list
    refresh.append( hero_Rect )
    #refresh.append( background.get_rect() )
    refresh.append( enemy_Rect )
    refresh.append( target_Rect )
    if arrowOn == True:
        refresh.append( arrow_Rect )
        
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:  
            mpos = pygame.mouse.get_pos()
            target_Rect = target.get_rect().move( mpos[0], mpos[1] )
    
        if event.type == pygame.MOUSEBUTTONDOWN:
            arrow = pygame.image.load( "arrow.png" ).convert_alpha() 
            if target_Rect.centerx - hero_Rect.centerx == 0:
                arrowSpeedX = 0
                arrowSpeedY = 10
            elif target_Rect.centery - hero_Rect.centery == 0:
                arrowSpeedX = 10
                arrowSpeedY = 0
            else:
                temp_tan_var = ((float(target_Rect.centery) - float(hero_Rect.centery))/(float(target_Rect.centerx) - float(hero_Rect.centerx)))
                print( "temp_tan_var" )
                print( temp_tan_var )
                print( "############" )
                angle = (math.atan( temp_tan_var ))
                print( "angle" )
                print( angle )
                print( "############" )

                if (hero_Rect.centerx > target_Rect.centerx):
                    arrow = pygame.transform.rotate(arrow, ( - (angle * 57.29) + 180 ))
                else:
                    arrow = pygame.transform.rotate(arrow, ( - (angle * 57.29) ))
                arrow_Rect = arrow.get_rect().move( hero_Rect.centerx - (arrow.get_rect().width/2), hero_Rect.centery - (arrow.get_rect().height/2) )
                arrowOn = True
                arrowSpeedY =  ( math.sin(angle) * 10.0 )
                print( "arrowSpeedY" )
                print( arrowSpeedY )
                print( "############" )
                arrowSpeedX =  ( math.cos(angle) * 10.0 )
                if (hero_Rect.centerx > target_Rect.centerx):
                    arrowSpeedX = -arrowSpeedX
                    arrowSpeedY = -arrowSpeedY
                print( "arrowSpeedX" )
                print( arrowSpeedX )
                print( "############" )
                screen.blit( arrow, (arrow_Rect) )

          
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
            if catch[pygame.K_w] and not keyAfter[pygame.K_w] and wOn != True:
                print "UPW"
                vertSpeed+=1
                wOn=True
                timeReset()
            if catch[pygame.K_a] and not keyAfter[pygame.K_a] and aOn != True:
                print "UPA"
                hoSpeed+=1
                aOn=True
                timeReset()
            if catch[pygame.K_s] and not keyAfter[pygame.K_s] and sOn != True:
                print "UPS"
                vertSpeed-=1
                sOn=True
                timeReset()
            if catch[pygame.K_d] and not keyAfter[pygame.K_d] and dOn != True:
                print "UPD"
                hoSpeed-=1
                dOn=True
                timeReset()

        # reset button
        if event.type == pygame.KEYDOWN:
            key = pygame.key.get_pressed()
            if key[pygame.K_r]:
                print ( "r is hit" )
                reset(background)
                dFrame = herod[1]
                enemy = pygame.image.load( "dsprite/Dragon_Mouth_Closed.png" ).convert_alpha()
                enemyDead = False
                dead = False
                hero_Rect = pygame.Rect(50, 50, 87, 102)
                enemy_Rect.top = 100
                enemy_Rect.left = 500
                timeReset()
                direction=herod
                refresh.append( background.get_rect() )

    #Catches pygame event errors
    catch=pygame.key.get_pressed()
    if catch[pygame.K_w] == False and catch[pygame.K_a] == False and catch[pygame.K_s] == False and catch[pygame.K_d] == False:
        hoSpeed=0
        vertSpeed=0


    # collision checker
    if hero_Rect.colliderect( rock_Rect ):
        # print( "colliding" )
        if hero_Rect.left >= rock_Rect.right - 18:
            #hoSpeed = 0
            refresh.append( hero_Rect )
            hero_Rect.left = rock_Rect.right
        elif hero_Rect.right <= rock_Rect.left + 18:
            #hoSpeed = 0
            refresh.append( hero_Rect )
            hero_Rect.right = rock_Rect.left
        elif hero_Rect.top <= rock_Rect.bottom - 18:
            #vertSpeed = 0
            refresh.append( hero_Rect )
            hero_Rect.bottom = rock_Rect.top
            #print( "colliding with bottom" )
            refresh.append( hero_Rect )
        elif hero_Rect.bottom >= rock_Rect.top + 18:
            #vertSpeed = 0
            refresh.append( hero_Rect )
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
    if enemy_Rect.bottom < hero_Rect.centery and enemyDead != True:
        vertVar = 1
    elif enemy_Rect.top > hero_Rect.centery and enemyDead != True:
        vertVar = -1
    else:
        vertVar = 0
    if enemy_Rect.right < hero_Rect.centerx and enemyDead != True:
        hoVar = 1
    elif enemy_Rect.left > hero_Rect.centerx and enemyDead != True:
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

    # arrow collision with enemy checker
    if arrowOn == True:
        if arrow_Rect.colliderect( enemy_Rect ):
            enemy = pygame.image.load( "dead.png" ).convert_alpha()
            hoVar = 0
            vertVar = 0
            enemyDead = True
                
    # movement code
    hero_Rect = hero_Rect.move( hoSpeed * 5, vertSpeed * 5)
    enemy_Rect = enemy_Rect.move( hoVar * enemySpeed, vertVar * enemySpeed )
    if arrowOn == True:
        arrow_Rect = arrow_Rect.move( arrowSpeedX, arrowSpeedY )

    # adding all the rectangles to the refresh list
    refresh.append( hero_Rect )
    refresh.append( rock_Rect )
    refresh.append( enemy_Rect )
    refresh.append( target_Rect )
    if frame % 60 == 0:
        refresh.append( background.get_rect() )
    
    if arrowOn == True:
        refresh.append( arrow_Rect )
    
    # redrawing everything
    reset(background)
    
    #sprite control
    if not dead:
        if vertSpeed == 0 and hoSpeed == 0:
            time = -1
            counter = 0
            dFrame = direction[1]
        else:
            time += 1
            if time == 29 :
                time = 0
        if time % 5 == 0:
            if vertSpeed > 0 and hoSpeed == 0:
                dFrame = herod[counter]
                counter = (counter + 1) % 4
                direction=herod
            elif vertSpeed == 0 and hoSpeed > 0:
                dFrame = heror[counter]
                counter = (counter + 1) % 4
                direction=heror
            elif vertSpeed < 0 and hoSpeed == 0:
                dFrame = herou[counter]
                counter = (counter + 1) % 4
                direction=herou
               
            elif vertSpeed == 0 and hoSpeed < 0:
                dFrame = herol[counter]
                counter = (counter + 1) % 4
                direction=herol
 
            elif vertSpeed > 0 and hoSpeed < 0:
                dFrame = herodl[counter]
                counter = (counter + 1) % 4
                direction=herodl
            elif vertSpeed > 0 and hoSpeed > 0:
                dFrame = herodr[counter]
                counter = (counter + 1) % 4
                direction=herodr
            elif vertSpeed < 0 and hoSpeed < 0:
                dFrame = heroul[counter]
                counter = (counter + 1) % 4
                direction=heroul
            elif vertSpeed < 0 and hoSpeed > 0:
                dFrame = herour[counter]
                counter = (counter + 1) % 4
                direction=herour
      
    if dead:
        screen.blit( hero, (hero_Rect))
    else:
        screen.blit( heroSprites, (hero_Rect.x,hero_Rect.y), dFrame )
    screen.blit( enemy, (enemy_Rect) )
    screen.blit( target, (target_Rect) )
    if arrowOn == True:
       screen.blit( arrow, (arrow_Rect) )       
        

    pygame.display.update( refresh )
    
    refresh = []
    
    clock.tick(30)

print "terminating"
