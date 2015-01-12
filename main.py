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
enemySpeed = 3
    
clock = pygame.time.Clock()

width, height = pygame.display.Info().current_w, pygame.display.Info().current_h

screen = pygame.display.set_mode( (1000, 380) )

background = pygame.image.load( "grass_jk.png" ).convert_alpha()
hero = pygame.image.load( "sprites/archer_main.png" ).convert_alpha()
rock = pygame.image.load( "rock.png" ).convert_alpha()
enemy = pygame.image.load( "Dragon_Mouth_Closed.png" ).convert_alpha()
arrow = pygame.image.load( "arrow.png" ).convert_alpha()
target = pygame.image.load( "missing.png" ).convert_alpha()

#making the target move
pygame.event.pump()
if pygame.mouse.get_focused():
    pygame.mouse.set_visible(False)

mpos = pygame.mouse.get_pos()
target_Rect = target.get_rect().move( mpos[0], mpos[1] )


#Hero movement sprites
time = 0
counter = 0

'''down'''
herod0 =  pygame.image.load( "sprites/archer_down1.png" ).convert_alpha()
herod1 = hero
herod2 =  pygame.image.load( "sprites/archer_down2.png" ).convert_alpha()
herod3 = hero
herod = [herod0, herod1, herod2, herod3]
'''right'''
heror0 =  pygame.image.load( "sprites/archer_right1.png" ).convert_alpha()
heror1 =  pygame.image.load( "sprites/archer_right.png" ).convert_alpha()
heror2 =  pygame.image.load( "sprites/archer_right2.png" ).convert_alpha()
heror3 =  heror1
heror = [heror0, heror1, heror2, heror3]
'''up'''
herou0 =  pygame.image.load( "sprites/archer_up1.png" ).convert_alpha()
herou1 =  pygame.image.load( "sprites/archer_up.png" ).convert_alpha()
herou2 =  pygame.image.load( "sprites/archer_up2.png" ).convert_alpha()
herou3 =  herou1
herou = [herou0, herou1, herou2, herou3]
'''left'''
herol0 =  pygame.image.load( "sprites/archer_left1.png" ).convert_alpha()
herol1 =  pygame.image.load( "sprites/archer_left.png" ).convert_alpha()
herol2 =  pygame.image.load( "sprites/archer_left2.png" ).convert_alpha()
herol3 =  herol1
herol = [herol0, herol1, herol2, herol3]
'''down left'''
herodl0 =  pygame.image.load( "sprites/archer_dl1.png" ).convert_alpha()
herodl1 =  pygame.image.load( "sprites/archer_dl.png" ).convert_alpha()
herodl2 =  pygame.image.load( "sprites/archer_dl2.png" ).convert_alpha()
herodl3 =  herodl1
herodl = [herodl0, herodl1, herodl2, herodl3]
'''down right'''
herodr0 =  pygame.image.load( "sprites/archer_dr1.png" ).convert_alpha()
herodr1 =  pygame.image.load( "sprites/archer_dr.png" ).convert_alpha()
herodr2 =  pygame.image.load( "sprites/archer_dr2.png" ).convert_alpha()
herodr3 =  herodr1
herodr = [herodr0, herodr1, herodr2, herodr3]
'''up left'''
heroul0 =  pygame.image.load( "sprites/archer_ul1.png" ).convert_alpha()
heroul1 =  pygame.image.load( "sprites/archer_ul.png" ).convert_alpha()
heroul2 =  pygame.image.load( "sprites/archer_ul2.png" ).convert_alpha()
heroul3 =  heroul1
heroul = [heroul0, heroul1, heroul2, heroul3]
'''up right'''
herour0 =  pygame.image.load( "sprites/archer_ur1.png" ).convert_alpha()
herour1 =  pygame.image.load( "sprites/archer_ur.png" ).convert_alpha()
herour2 =  pygame.image.load( "sprites/archer_ur2.png" ).convert_alpha()
herour3 =  herour1
herour = [herour0, herour1, herour2, herour3]



#remember which direction hero was facing
direction = herod

def timeReset():
    counter=0
    time=-1

def reset(bkground):
    screen.blit( bkground, (0,0) )
    screen.blit( rock, (500, 180) )

screen.blit( hero, (50, 50) )
screen.blit( enemy, (500, 100) )
screen.blit( background, (0,0) )
screen.blit( rock, (500, 180) )

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
            if target_Rect.centerx - hero_Rect.centerx == 0:
                arrowSpeedX = 0
                arrowSpeedY = 10
            elif target_Rect.centery - hero_Rect.centery == 0:
                arrowSpeedX = 10
                arrowSpeedY = 0
            else:
                temp_tan_var = ((target_Rect.centerx - hero_Rect.centerx)/(target_Rect.centery - hero_Rect.centery))
                print( temp_tan_var )
                angle = math.atan( temp_tan_var )
                angle = angle * 52.29
                print (angle)
                pygame.transform.rotate(target, angle)
                arrow_Rect = arrow.get_rect().move(hero_Rect.center)
                arrowOn = True
                if hero_Rect.centery > mpos[1]:
                    arrowSpeedY = - (90 - angle) / 9.0
                elif hero_Rect.centery < mpos[1]:
                    arrowSpeedY =((90 - angle) / 9.0)
                else:
                    arrowSpeedY = 0
                print ( arrowSpeedY )
                if hero_Rect.centerx > mpos[0]:
                    arrowSpeedX = - (angle) / 9.0
                elif hero_Rect.centerx < mpos[0]:
                    arrowSpeedX = ((angle) / 9.0)
                else:
                    arrowSpeedX = 0
                print ( arrowSpeedX )
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
                hero = pygame.image.load( "sprites/archer_main.png" ).convert_alpha()
                enemy = pygame.image.load( "Dragon_Mouth_Closed.png" ).convert_alpha()
                enemyDead = False
                dead = False
                hero_Rect.top = 50
                hero_Rect.left = 50
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
            hero = direction[1]
        else:
            time += 1
            if time == 29 :
                time = 0
        if time % 5 == 0:
            if vertSpeed > 0 and hoSpeed == 0:
                templeft = hero_Rect.left
                temptop = hero_Rect.top
                hero = herod[counter]
                hero_Rect = herod[counter].get_rect().move( templeft, temptop )
                counter = (counter + 1) % 4
                direction=herod
            
            elif vertSpeed == 0 and hoSpeed > 0:
                templeft = hero_Rect.left
                temptop = hero_Rect.top
                hero = heror[counter]
                hero_Rect = heror[counter].get_rect().move( templeft, temptop )
                counter = (counter + 1) % 4
                direction=heror
            
            elif vertSpeed < 0 and hoSpeed == 0:
                templeft = hero_Rect.left
                temptop = hero_Rect.top
                hero = herou[counter]
                hero_Rect = herou[counter].get_rect().move( templeft, temptop )
                counter = (counter + 1) % 4
                direction=herou
               
            elif vertSpeed == 0 and hoSpeed < 0:
                templeft = hero_Rect.left
                temptop = hero_Rect.top
                hero = herol[counter]
                hero_Rect = herol[counter].get_rect().move( templeft, temptop )
                counter = (counter + 1) % 4
                direction=herol
 
            elif vertSpeed > 0 and hoSpeed < 0:
                templeft = hero_Rect.left
                temptop = hero_Rect.top
                hero = herodl[counter]
                hero_Rect = herodl[counter].get_rect().move( templeft, temptop )
                counter = (counter + 1) % 4
                direction=herodl
            elif vertSpeed > 0 and hoSpeed > 0:
                templeft = hero_Rect.left
                temptop = hero_Rect.top
                hero = herodr[counter]
                hero_Rect = herodr[counter].get_rect().move( templeft, temptop )
                counter = (counter + 1) % 4
                direction=herodr
            elif vertSpeed < 0 and hoSpeed < 0:
                templeft = hero_Rect.left
                temptop = hero_Rect.top
                hero = heroul[counter]
                hero_Rect = heroul[counter].get_rect().move( templeft, temptop )
                counter = (counter + 1) % 4
                direction=heroul
            elif vertSpeed < 0 and hoSpeed > 0:
                templeft = hero_Rect.left
                temptop = hero_Rect.top
                hero = herour[counter]
                hero_Rect = herour[counter].get_rect().move( templeft, temptop )
                counter = (counter + 1) % 4
                direction=herour
                
    screen.blit( hero, (hero_Rect) )
    screen.blit( enemy, (enemy_Rect) )
    screen.blit( target, (target_Rect) )
    if arrowOn == True:
       screen.blit( arrow, (arrow_Rect) )       
        

    pygame.display.update( refresh )
    
    refresh = []
    
    clock.tick(30)

print "terminating"
