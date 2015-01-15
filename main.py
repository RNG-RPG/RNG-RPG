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

#width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
screen = pygame.display.set_mode( (1296, 648) )


# collision checker 
def pathCollide( object_rect, agent_rect, refresh_List ):
    if agent_rect.colliderect( object_rect ):
        # print( "colliding" )
        if agent_rect.left >= object_rect.right - 18:
            #hoSpeed = 0
            refresh_List.append( agent_rect )
            agent_rect.left = object_rect.right
        elif agent_rect.right <= object_rect.left + 18:
            #hoSpeed = 0
            refresh_List.append( agent_rect )
            agent_rect.right = object_rect.left
        elif agent_rect.top <= object_rect.bottom - 18:
            #vertSpeed = 0
            refresh_List.append( agent_rect )
            agent_rect.bottom = object_rect.top
            #print( "colliding with bottom" )
            refresh_List.append( object_rect )
        elif agent_rect.bottom >= object_rect.top + 18:
            #vertSpeed = 0
            refresh_List.append( agent_rect )
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
    screen.fill((255,255,255))
    pygame.display.update()

    
    while i < 72:
            images.append( str(i) )
            if i < 10:
                images[i] = pygame.image.load( "Title_Screen_Gif/frame_00" + str(i) + ".gif" ).convert_alpha()
            else:
                images[i] = pygame.image.load( "Title_Screen_Gif/frame_0" + str(i) + ".gif" ).convert_alpha()
            i += 1
    
    while x == 0:
        refresh = []
        start_Frame += 1
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                key = pygame.key.get_pressed()
                if key[pygame.K_SPACE]:
                    main()

        refresh.append ( images[0].get_rect())
        
        if start_Frame % 2 == 0:
            screen.blit( images[current_Frame], (0,0) )
            current_Frame += 1
            if current_Frame == 71:
                current_Frame = 0

        pygame.display.update( refresh )
         
        clock.tick(30)
        
            
# MAIN ROOM FUNCTION (temp)
def main():

    dead = False
    arrowOn = [False,False,False,False,False,False,False,False,False,False]
    enemyDead = False
    vertSpeed = 0
    hoSpeed = 0
    frame = 0
    attacktimer = 30
    attackDelay = False
    # defines speed of enemy
    enemySpeed = 1
    arrowSpeedX = [0,0,0,0,0,0,0,0,0,0]
    arrowSpeedY = [0,0,0,0,0,0,0,0,0,0]
    arrownum = 0
    refresh = []
        
    clock = pygame.time.Clock()

    

    background = pygame.image.load( "RockGround2.png" ).convert_alpha()
    left_side = pygame.image.load( "rock_sides.png" ).convert_alpha()
    right_side = pygame.image.load( "rock_sides.png" ).convert_alpha()
    top_side = pygame.image.load( "rock_top.png" ).convert_alpha()
    bottom_side = pygame.image.load( "rock_top.png" ).convert_alpha()
    heroSprites = pygame.image.load( "sprites/archer_main.png" ).convert_alpha()
    rock = pygame.image.load( "rock.png" ).convert_alpha()
    enemySprites = pygame.image.load( "sprites/enemy_main.png" ).convert_alpha()
    arrowLoadImage = pygame.image.load( "arrow.png" ).convert_alpha()
    arrow = [arrowLoadImage, arrowLoadImage, arrowLoadImage, arrowLoadImage, arrowLoadImage, arrowLoadImage, arrowLoadImage, arrowLoadImage, arrowLoadImage, arrowLoadImage]
    target = pygame.image.load( "Pointer.png" ).convert_alpha()
    arrow_rects = [arrow[0].get_rect(),arrow[1].get_rect(),arrow[2].get_rect(),arrow[3].get_rect(),arrow[4].get_rect(),arrow[5].get_rect(),arrow[6].get_rect(),arrow[7].get_rect(),arrow[8].get_rect(),arrow[9].get_rect()]

    #making the target move
    pygame.event.pump()
    mpos = pygame.mouse.get_pos()
    target_Rect = target.get_rect().move( mpos[0], mpos[1] )


    #Hero movement sprites
    time = -1
    counter = 0

    '''down'''
    herod = [(0, 102, 87, 102), (0, 0, 87, 102), (0, 204, 87, 102), (0, 0, 87, 102), (0, 306, 87, 102)]
    '''right'''
    heror = [(87, 102, 87, 102), (87, 0, 87, 102), (87, 204, 87, 102), (87, 0, 87, 102), (87, 306, 87, 102)]
    '''up'''
    herou = [(174, 102, 87, 102), (174, 0, 87, 102), (174, 204, 87, 102), (174, 0, 87, 102), (174, 306, 87, 102)]
    '''left'''
    herol = [(261, 102, 87, 102), (261, 0, 87, 102), (261, 204, 87, 102), (261, 0, 87, 102), (261, 306, 87, 102)]
    '''down left'''
    herodl = [(348, 102, 87, 101), (348, 0, 87, 102), (348, 204, 87, 102), (348, 0, 87, 102), (348, 306, 87, 102)]
    '''down right'''
    herodr = [(435, 102, 87, 102), (435, 0, 87, 102), (435, 204, 87, 102), (435, 0, 87, 102), (435, 306, 87, 102)]
    '''up left'''
    heroul = [(522, 102, 87, 102), (522, 0, 87, 102), (522, 204, 87, 102), (522, 0, 87, 102), (522, 306, 87, 102)]
    '''up right'''
    herour = [(609, 102, 87, 102), (609, 0, 87, 102), (609, 204, 87, 102), (609, 0, 87, 102), (609, 306, 87, 102)]

    #dragon
    counter1 = 0
    frameCounter = -1
    dragond = [(0, 0, 114, 154), (114, 0, 114, 154)]
    eFrame = dragond[0]
    #remember which direction hero was facing
    direction = herod
    dFrame=herod[1]
    def timeReset():
        counter=0
        time=-1

    def reset(bkground):
        screen.blit( bkground, (0,0) )
        screen.blit( bkground, (648,0) )
        #draw on top of the background
        screen.blit( rock, (500, 180) )
        screen.blit( left_side, (0,0) )
        screen.blit( right_side, (1242, 0) )
        screen.blit( top_side, (0,0) )
        screen.blit( bottom_side, (0, 594) )

    screen.blit( heroSprites, (50, 50), dFrame  )
    screen.blit( enemySprites, (500, 100), eFrame)
    screen.blit( background, (0,0) )
    screen.blit( background, (648,0) )
    screen.blit( rock, (500, 180) )
    screen.blit( left_side, (0,0) )
    screen.blit( right_side, (1242, 0) )
    screen.blit( top_side, (0,0) )
    screen.blit( bottom_side, (0, 594) )

    

    rock_Rect = rock.get_rect().move(500, 180)
    hero_Rect = pygame.Rect(50, 50, 87, 102)
    enemy_Rect = pygame.Rect(500, 100, 114, 154)
    top_Rect = top_side.get_rect()
    bottom_Rect = bottom_side.get_rect().move(0, 594)
    left_Rect = left_side.get_rect()
    right_Rect = right_side.get_rect().move(1242, 0)

    pygame.display.update()
    #Control limits 
    wOn=True
    aOn=True
    sOn=True
    dOn=True

    while 1 == 1:
    
        #Catches pygame event errors
        catch=pygame.key.get_pressed()
        if catch[pygame.K_w] == False and catch[pygame.K_a] == False and catch[pygame.K_s] == False and catch[pygame.K_d] == False:
            hoSpeed=0
            vertSpeed=0
    
        if pygame.mouse.get_focused():
            pygame.mouse.set_visible(False)
        frame = frame + 1
        attacktimer = attacktimer + 1
        # adding all the rectangles to the refresh list
        refresh.append( hero_Rect )
        #refresh.append( background.get_rect() )
        refresh.append( enemy_Rect )
        refresh.append( target_Rect )
        j = 0
        while j < 10:
            if arrowOn[j] == True:
                refresh.append( arrow_rects[j] )
            j += 1
            
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:  
                mpos = pygame.mouse.get_pos()
                target_Rect = target.get_rect().move( mpos[0], mpos[1] )
        
            if event.type == pygame.MOUSEBUTTONDOWN and attacktimer >= 30 and dead == False:
                attackDelay = True
                attacktimer = 0
                if arrownum < 9:
                    arrownum += 1
                else:
                    arrownum = 0
                arrow[arrownum] = pygame.image.load( "arrow.png" ).convert_alpha() 
                if target_Rect.centerx - hero_Rect.centerx == 0:
                    arrowSpeedX[arrownum] = 0
                    arrowSpeedY[arrownum] = 10
                elif target_Rect.centery - hero_Rect.centery == 0:
                    arrowSpeedX[arrownum] = 10
                    arrowSpeedY[arrownum] = 0
                else:
                    temp_tan_var = ((float(target_Rect.centery) - float(hero_Rect.centery))/(float(target_Rect.centerx) - float(hero_Rect.centerx)))
                    #print( "temp_tan_var" )
                    #print( temp_tan_var )
                    #print( "############" )
                    angle = (math.atan( temp_tan_var ))
                    #print( "angle" )
                    #print( angle )
                    #print( "############" )

                    if (hero_Rect.centerx > target_Rect.centerx):
                        arrow[arrownum] = pygame.transform.rotate(arrow[arrownum], ( - (angle * 57.29) + 180 ))
                    else:
                        arrow[arrownum] = pygame.transform.rotate(arrow[arrownum], ( - (angle * 57.29) ))
                    arrow_rects[arrownum] = arrow[arrownum].get_rect().move( hero_Rect.centerx - (arrow[arrownum].get_rect().width/2), hero_Rect.centery - (arrow[arrownum].get_rect().height/2) )
                    arrowOn[arrownum] = True
                    arrowSpeedY[arrownum] =  ( math.sin(angle) * 10.0 )
                    #print( "arrowSpeedY" )
                    #print( arrowSpeedY )
                    #print( "############" )
                    arrowSpeedX[arrownum] =  ( math.cos(angle) * 10.0 )
                    if (hero_Rect.centerx > target_Rect.centerx):
                        arrowSpeedX[arrownum] = -arrowSpeedX[arrownum]
                        arrowSpeedY[arrownum] = -arrowSpeedY[arrownum]
                    #print( "arrowSpeedX" )
                    #print( arrowSpeedX )
                    #print( "############" )
                    screen.blit( arrow[arrownum], (arrow_rects[arrownum]) )

              
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

            # reset button and reset to menu
            if event.type == pygame.KEYDOWN:
                key = pygame.key.get_pressed()
                if key[pygame.K_r]:
                    print ( "r is hit" )
                    reset(background)
                    dFrame = herod[1]
                    enemyDead = False
                    dead = False
                    hero_Rect = pygame.Rect(50, 50, 87, 102)
                    enemy_Rect = pygame.Rect(500, 100, 114, 154)
                    timeReset()
                    direction=herod
                    refresh.append( background.get_rect() )
                elif key[pygame.K_ESCAPE]:
                    start()
        


        # collision checker
        pathCollide( rock_Rect, hero_Rect, refresh )
        pathCollide( top_Rect, hero_Rect, refresh )
        pathCollide( bottom_Rect, hero_Rect, refresh )
        pathCollide( left_Rect, hero_Rect, refresh )
        pathCollide( right_Rect, hero_Rect, refresh )
        pathCollide( rock_Rect, enemy_Rect, refresh )
        """
        pathCollide( top_Rect, enemy_Rect, refresh )
        pathCollide( bottom_Rect, enemy_Rect, refresh )
        pathCollide( left_Rect, enemy_Rect, refresh )
        pathCollide( right_Rect, enemy_Rect, refresh )
        """
        
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
        if enemy_Rect.colliderect( hero_Rect ) and enemyDead == False :
            dFrame = (696, 0, 87, 102)
            hoSpeed = 0
            vertSpeed = 0
            dead = True
            """
            for event in pygame.event.get(): 
                if event.type == pygame.KEYDOWN:
                    key = pygame.key.get_pressed()
            """

                    
        # arrow collision with enemy checker
        k = 0
        while k < 10:
            if arrowOn[k] == True:
                if arrow_rects[k].colliderect( enemy_Rect ) and enemyDead != True:
                    eFrame = (228, 0, 114, 154)
                    hoVar = 0
                    vertVar = 0
                    enemyDead = True
                    arrowOn[k] = False
            k += 1
                    
        # movement code
        hero_Rect = hero_Rect.move( hoSpeed * 5, vertSpeed * 5)
        enemy_Rect = enemy_Rect.move( hoVar * enemySpeed, vertVar * enemySpeed )
        
        

        # adding all the rectangles to the refresh list
        refresh.append( hero_Rect )
        refresh.append( rock_Rect )
        refresh.append( enemy_Rect )
        refresh.append( target_Rect )
        if frame % 60 == 0:
            refresh.append( background.get_rect() )
            refresh.append( background.get_rect().move(648, 0) )

        i = 0
        while i < 10:
            if arrowOn[i] == True:
                arrow_rects[i] = arrow_rects[i].move( arrowSpeedX[i], arrowSpeedY[i] )
            if arrowOn[i] == True:
                refresh.append( arrow_rects[i] )
            i += 1
        
        
        # redrawing everything
        reset(background)
        
        #sprite control
        if not dead:
            if attacktimer > 5:
                if vertSpeed == 0 and hoSpeed == 0:
                    time = -1
                    counter = 0
                    dFrame = direction[1]
                else:
                     time += 1
                     if time == 29:
                        time = -1
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
                #attack frames
            elif attackDelay == True:
                if target_Rect.centerx < hero_Rect.centerx:
                    if angle < 1.6 and angle > 1.15:
                        dFrame = herou[4]
                    elif angle <= 1.15 and angle > 0.42:
                        dFrame = heroul[4]
                    elif angle <= 0.42 and angle >= -0.42:
                        dFrame = herol[4]
                    elif angle < -0.42 and angle >= -1.15:
                        dFrame = herodl[4]
                    elif angle < -1.15 and angle > -1.58:
                        dFrame = herod[4]
                elif target_Rect.centerx > hero_Rect.centerx:
                    if angle < 1.6 and angle >  1.15:
                        dFrame = herod[4]
                    elif angle <= 1.15 and angle > 0.42:
                        dFrame = herodr[4]
                    elif angle <= 0.42 and angle >= -0.42:
                        dFrame = heror[4]
                    elif angle < -0.42 and angle >= -1.15:
                        dFrame = herour[4]
                    elif angle < -1.15 and angle > -1.58:
                        dFrame = herou[4]
                else:
                    if target_Rect.centery <= hero_Rect.centery:
                        dFrame = herou[4]
                    else:
                        dFrame = herod[4]
                attackDelay=False
        #enemy!
        if not enemyDead:
            frameCounter += 1
            if frameCounter == 29:
                frameCounter = -1
            if frameCounter % 10 == 0:
                eFrame = dragond[counter1]
                counter1 = (counter1 + 1) % 2
            
        screen.blit( heroSprites, (hero_Rect.x,hero_Rect.y), dFrame )
        screen.blit( enemySprites, (enemy_Rect.x,enemy_Rect.y), eFrame) 
        screen.blit( target, (target_Rect) )
        i = 0
        while i < 10:
            if arrowOn[i] == True:
               screen.blit( arrow[i], (arrow_rects[i]) )
            i += 1
            

        pygame.display.update( refresh )
        
        refresh = []
        
        clock.tick(30)

# main loop:

while 1 == 1:
    start()
    main()
    
    

print "terminating"
