'''
written by Mathias Dyssegaard Kallick
1/8/2015
main.py - holds the code necessary to display a background and the hero, for now.
'''

# imports
import sys, pygame, math, agent, os
import titlescreen

# initialize
pygame.init()

# initialize the fonts
try:
    pygame.font.init()
except:
    print "Fonts unavailable"
    sys.exit()

#width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
WIDTH = 1300
HEIGHT = 648
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
    screen.fill((255,255,255))
    pygame.display.update()

    
    while i < 72:
            images.append( str(i) )
            if i < 10:
                images[i] = pygame.image.load( "Title_Screen_Gif/frame_00" + str(i) + ".gif" ).convert_alpha()
                images[i] = pygame.transform.smoothscale( images[i], (800, 700) )
            else:
                images[i] = pygame.image.load( "Title_Screen_Gif/frame_0" + str(i) + ".gif" ).convert_alpha()
                images[i] = pygame.transform.smoothscale( images[i], (800, 700) )
            i += 1
    
    while 10 == 10:
        refresh = []
        start_Frame += 1
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                key = pygame.key.get_pressed()
                if key[pygame.K_SPACE]:
                    titlescreen.main(WIDTH,HEIGHT)

        refresh.append ( images[0].get_rect().move(287,0) )
        
        if start_Frame % 2 == 0:
            screen.blit( images[current_Frame], (287,0) )
            current_Frame += 1
            if current_Frame == 71:
                current_Frame = 0

        pygame.display.update( refresh )
        clock.tick(30)
        
            
# MAIN ROOM FUNCTION (temp)
def main():
    pygame.event.set_allowed(pygame.MOUSEMOTION)
    pygame.mouse.get_focused
    dead = False
    arrowOn = [False,False,False,False,False,False,False,False,False,False]
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
    target = pygame.image.load( "sprites/AimingPointer.png" ).convert_alpha()
    target = pygame.transform.scale(target, (50, 50))
    arrow_rects = [arrow[0].get_rect(),arrow[1].get_rect(),arrow[2].get_rect(),arrow[3].get_rect(),arrow[4].get_rect(),arrow[5].get_rect(),arrow[6].get_rect(),arrow[7].get_rect(),arrow[8].get_rect(),arrow[9].get_rect()]

    arrowhit = pygame.mixer.Sound( "sounds/arrowhit.wav" )
    arrowshot = pygame.mixer.Sound("sounds/arrowshot.wav")
    arrowready = pygame.mixer.Sound("sounds/arrowshot.wav")
    	
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

    #Add DA enemies HERE
    frameCounter = -1
    dragond = [(0, 0, 114, 154), (114, 0, 114, 154), (214, 0, 114, 154)]
    #hitbox note: subtract double of |dev| from respective x, y -- width and height of rect
    enemyDragon = agent.Enemy(10, [(0, 0, 114, 154), (114, 0, 114, 154), (228, 0, 114, 154)], pygame.Rect(500, 100, 34, 74), 10)
    enemyDragon.setDev(-40, -40)
    enemySlime = agent.Enemy(3,  [(0, 154, 75, 75), (75, 154, 75, 75), (0, 154, 75, 75), (150, 154, 75, 75), (225, 154, 75, 75)], pygame.Rect(700, 400, 35, 35), 5)
    enemySlime.setDev(-20, -20)
    enemySlime2 = agent.Enemy(3,  [(0, 154, 75, 75), (75, 154, 75, 75), (0, 154, 75, 75), (150, 154, 75, 75), (225, 154, 75, 75)], pygame.Rect(800, 350, 35, 35), 5)
    enemySlime2.setDev(-20, -20)
    enemySlime3 = agent.Enemy(3,  [(0, 154, 75, 75), (75, 154, 75, 75), (0, 154, 75, 75), (150, 154, 75, 75), (225, 154, 75, 75)], pygame.Rect(900, 350, 35, 35), 5)
    enemySlime3.setDev(-20, -20)
    enemySlime4 = agent.Enemy(3,  [(0, 154, 75, 75), (75, 154, 75, 75), (0, 154, 75, 75), (150, 154, 75, 75), (225, 154, 75, 75)], pygame.Rect(900, 450, 35, 35), 5)
    enemySlime4.setDev(-20, -20)
    enemySlime5 = agent.Enemy(3,  [(0, 154, 75, 75), (75, 154, 75, 75), (0, 154, 75, 75), (150, 154, 75, 75), (225, 154, 75, 75)], pygame.Rect(700, 300, 35, 35), 5)
    enemySlime5.setDev(-20, -20)
    enemySlime6 = agent.Enemy(3,  [(0, 154, 75, 75), (75, 154, 75, 75), (0, 154, 75, 75), (150, 154, 75, 75), (225, 154, 75, 75)], pygame.Rect(800, 500, 35, 35), 5)
    enemySlime6.setDev(-20, -20)
    enemyVoodoo = agent.Enemy(5, [(0, 229, 55, 66), (0, 229, 55, 66), (56, 229, 55, 66), (112, 229, 55, 66), (168, 229, 55, 66), (224, 229, 55, 66), (280, 229, 55, 66),
                                 (336, 229, 55, 66), (392, 229, 55, 66), (448, 229, 55, 66)], pygame.Rect(1000, 100, 36, 46), 6, True)
    enemyVoodoo.setDev(-10,-10)            
    
    enemies = [enemyDragon, enemySlime, enemySlime2, enemySlime3, enemySlime4, enemySlime5, enemySlime6, enemyVoodoo]

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
    if enemies == None:
        endgame = pygame.image.load( "images/congrats.png" ).convert_alpha()
        endgame = pygame.transform.scale(endgame, (WIDTH, HEIGHT))
        
    for enem in enemies:
        screen.blit( enemySprites, (enem.getRect().x, enem.getRect().y), enem.getCurrentSprite())
    screen.blit( background, (0,0) )
    screen.blit( background, (648,0) )
    screen.blit( rock, (500, 180) )
    screen.blit( left_side, (0,0) )
    screen.blit( right_side, (1242, 0) )
    screen.blit( top_side, (0,0) )
    screen.blit( bottom_side, (0, 594) )

    

    rock_Rect = rock.get_rect().move(500, 180)
    hero_Rect = pygame.Rect(50, 50, 87, 102)
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
        #counts frames for animations
        frameCounter += 1
        if frameCounter == 29:
            frameCounter = -1
    
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
                arrowready.play()
                attackDelay = True
                attacktimer = 0
                if arrownum < 9:
                    arrownum += 1
                else:
                    arrownum = 0
                arrow[arrownum] = pygame.image.load( "arrow.png" ).convert_alpha() 
                arrowshot.play()
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
                    for enem in enemies:
                        enem.changeRect(enem.getOriginalRect())
                        enem.ressurect()
                    dead = False
                    hero_Rect = pygame.Rect(50, 50, 87, 102)
                    timeReset()
                    direction=herod
                    refresh.append( background.get_rect() )
                elif key[pygame.K_ESCAPE]:
                    titlescreen.main(WIDTH,HEIGHT)
        


        # collision checker
        pathCollide( rock_Rect, hero_Rect, refresh )
        pathCollide( top_Rect, hero_Rect, refresh )
        pathCollide( bottom_Rect, hero_Rect, refresh )
        pathCollide( left_Rect, hero_Rect, refresh )
        pathCollide( right_Rect, hero_Rect, refresh )
        for enem in enemies:
            pathCollide( rock_Rect, enem.getRect(), refresh )
        """
        pathCollide( top_Rect, enemy_Rect, refresh )
        pathCollide( bottom_Rect, enemy_Rect, refresh )
        pathCollide( left_Rect, enemy_Rect, refresh )
        pathCollide( right_Rect, enemy_Rect, refresh )
        """
        
        # enemy AI, deciding where it needs to move
        for enem in enemies:
            if enem.getRect().bottom < hero_Rect.centery and enem.isDead() != True:
                enem.setVSpeed(1)
            elif enem.getRect().top > hero_Rect.centery and enem.isDead() != True:
                enem.setVSpeed(-1)
            else:
                enem.setVSpeed(0)
            if enem.getRect().right < hero_Rect.centerx and enem.isDead() != True:
                enem.setHSpeed(1)
            elif enem.getRect().left > hero_Rect.centerx and enem.isDead() != True:
                enem.setHSpeed(-1)
            else:
                enem.setHSpeed(0)
            
        # enemy collision with hero checker
        for enem in enemies:
            if enem.getRect().colliderect( hero_Rect ) and enem.isDead() == False :
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
        for enem in enemies:
            k = 0
            while k < 10:
                if arrowOn[k] == True:
                    if arrow_rects[k].colliderect( enem.getRect() ) and enem.isDead() != True:
                        arrowhit.play()
                        enem.changeHP(-1)
                        enem.changeRect(enem.getRect().move( 2 * (arrowSpeedX[k]), 2 * (arrowSpeedY[k]) ))
                        arrowOn[k] = False
                k += 1
                    
        # movement code
        hero_Rect = hero_Rect.move( hoSpeed * 5, vertSpeed * 5)
        for enem in enemies:
            enem.changeRect(enem.getRect().move( enem.getHSpeed() * enemySpeed, enem.getVSpeed() * enemySpeed ))
        
        

        # adding all the rectangles to the refresh list
        refresh.append( hero_Rect )
        refresh.append( rock_Rect )
        refresh.append( target_Rect )
        for enem in enemies:
            refresh.append( (enem.getRect().x+enem.getxDev()*2, enem.getRect().y+enem.getyDev()*2, enem.getRect().width-enem.getxDev()*4, enem.getRect().height-enem.getyDev()*4))
 
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
        #enemy animations!
        for enem in enemies:
            if not enem.isDead():
                if frameCounter % enem.getFrameSpeed() == 0:
                    enem.changeSprite((enem.getSpriteNumber()+1) % (len(enem.getSprites())-1))
            else:
                enem.changeSprite(-1)
            
        screen.blit( heroSprites, (hero_Rect.x,hero_Rect.y), dFrame )
        for enem in enemies:
            screen.blit( enemySprites, (enem.getRect().x+enem.getxDev(),enem.getRect().y+enem.getyDev()), enem.getCurrentSprite()) 
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
if __name__ == "__main__":
    while 1 == 1:
        start()
        main()
    
    

print "terminating"
