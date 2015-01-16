'''
written by Mathias Dyssegaard Kallick
1/8/2015
main.py - holds the code necessary to display a background and the hero, for now.
'''

# imports
import sys, pygame, math, agent, os
import titlescreen

# initialize
pygame.mixer.pre_init()
pygame.init()

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
        
            
# MAIN ROOM FUNCTION (temp)
def main():
    
    pygame.mixer.music.load("sounds/BKGmusic/TownBoss/VictoryAtLast.wav")
    pygame.mixer.music.play(-1,0)
    
    pygame.event.set_allowed(pygame.MOUSEMOTION)
    pygame.mouse.get_focused
    dead = False
    arrowOn = [False]*10
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
    loopdeath= 0
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
    arrowLoadImage = pygame.image.load( "sprites/particle_main.png" ).convert_alpha()
    arrow = [arrowLoadImage, arrowLoadImage, arrowLoadImage, arrowLoadImage, arrowLoadImage, arrowLoadImage, arrowLoadImage, arrowLoadImage, arrowLoadImage, arrowLoadImage]
    target = pygame.image.load( "sprites/AimingPointer.png" ).convert_alpha()
    target = pygame.transform.scale(target, (50, 50))
    arrow_rects = [arrow[0].get_rect(),arrow[1].get_rect(),arrow[2].get_rect(),arrow[3].get_rect(),arrow[4].get_rect(),arrow[5].get_rect(),arrow[6].get_rect(),arrow[7].get_rect(),arrow[8].get_rect(),arrow[9].get_rect()]

    arrowhit = pygame.mixer.Sound( "sounds/arrowhit.wav" )
    arrowshot = pygame.mixer.Sound("sounds/arrowshot.wav")
    arrowready = pygame.mixer.Sound("sounds/arrowshot.wav")
    footsteps = pygame.mixer.Sound("sounds/footsteps.wav")
    deathsound = pygame.mixer.Sound("sounds/death.wav")

    bloodexplode = pygame.mixer.Sound("sounds/bloodexplode.wav")

    slimedeath = pygame.mixer.Sound("sounds/slimedeath.wav")

    	
    #making the target move
    pygame.event.pump()
    mpos = pygame.mouse.get_pos()
    target_Rect = target.get_rect().move( mpos[0], mpos[1] )


    #Hero movement sprites
    time = -1
    counter = 0

    '''down'''
    herod = [(0, 68, 58, 68), (0, 0, 58, 68), (0, 136, 58, 68), (0, 0, 58, 68), (0, 204, 58, 68)]
    '''right'''
    heror = [(58, 68, 58, 68), (58, 0, 58, 68), (58, 136, 58, 68), (58, 0, 58, 68), (58, 204, 58, 68)]
    '''up'''
    herou = [(116, 68, 58, 68), (116, 0, 58, 68), (116, 136, 58, 68), (116, 0, 58, 68), (116, 204, 58, 68)]
    '''left'''
    herol = [(174, 68, 58, 68), (174, 0, 58, 68), (174, 136, 58, 68), (174, 0, 58, 68), (174, 204, 58, 68)]
    '''down left'''
    herodl = [(232, 68, 58, 68), (232, 0, 58, 68), (232, 136, 58, 68), (232, 0, 58, 68), (232, 204, 58, 68)]
    '''down right'''
    herodr = [(290, 68, 58, 68), (290, 0, 58, 68), (290, 136, 58, 68), (290, 0, 58, 68), (290, 204, 58, 68)]
    '''up left'''
    heroul = [(348, 68, 58, 68), (348, 0, 58, 68), (348, 136, 58, 68), (348, 0, 58, 68), (348, 204, 58, 68)]
    '''up right'''
    herour = [(406, 68, 58, 68), (406, 0, 58, 68), (406, 136, 58, 68), (406, 0, 58, 68), (406, 204, 58, 68)]

    #Add DA enemies HERE
    frameCounter = -1
    dragond = [(0, 0, 114, 154), (114, 0, 114, 154), (214, 0, 114, 154)]
    #hitbox note: subtract double of |dev| from respective x, y -- width and height of rect
    enemyDragon = agent.Dragon(10, [(0, 0, 114, 154), (114, 0, 114, 154), (228, 0, 114, 154)], pygame.Rect(500, 100, 34, 74), 10)
    enemyDragon.setDev(-40, -40)

    enemySlime = agent.Slime(3,  [(0, 154, 75, 75), (75, 154, 75, 75), (0, 154, 75, 75), (150, 154, 75, 75), (225, 154, 75, 75)], pygame.Rect(700, 400, 35, 35), 5)
    enemySlime.setDev(-20, -20)
    enemySlime2 = agent.Slime(3,  [(75, 154, 75, 75), (0, 154, 75, 75), (150, 154, 75, 75), (0, 154, 75, 75), (225, 154, 75, 75)], pygame.Rect(800, 350, 35, 35), 5)
    enemySlime2.setDev(-20, -20)
    enemySlime3 = agent.Slime(3,  [(0, 154, 75, 75), (75, 154, 75, 75), (0, 154, 75, 75), (150, 154, 75, 75), (225, 154, 75, 75)], pygame.Rect(900, 350, 35, 35), 5)
    enemySlime3.setDev(-20, -20)
    enemySlime4 = agent.Slime(3,  [(75, 154, 75, 75), (0, 154, 75, 75), (150, 154, 75, 75), (0, 154, 75, 75), (225, 154, 75, 75)], pygame.Rect(900, 450, 35, 35), 5)
    enemySlime4.setDev(-20, -20)
    enemySlime5 = agent.Slime(3,  [(0, 154, 75, 75), (75, 154, 75, 75), (0, 154, 75, 75), (150, 154, 75, 75), (225, 154, 75, 75)], pygame.Rect(700, 300, 35, 35), 5)
    enemySlime5.setDev(-20, -20)
    enemySlime6 = agent.Slime(3,  [(0, 154, 75, 75), (75, 154, 75, 75), (0, 154, 75, 75), (150, 154, 75, 75), (225, 154, 75, 75)], pygame.Rect(800, 500, 35, 35), 5)

    enemySlime = agent.Slime(3,  [(0, 154, 50, 50), (50, 154, 50, 50), (0, 154, 50, 50), (100, 154, 50, 50), (150, 154, 50, 50)], pygame.Rect(700, 400, 10, 10), 5)
    enemySlime.setDev(-20, -20)
    enemySlime2 = agent.Slime(3,  [(0, 154, 50, 50), (50, 154, 50, 50), (0, 154, 50, 50), (100, 154, 50, 50), (150, 154, 50, 50)], pygame.Rect(800, 350, 10, 10), 5)
    enemySlime2.setDev(-20, -20)
    enemySlime3 = agent.Slime(3,  [(0, 154, 50, 50), (50, 154, 50, 50), (0, 154, 50, 50), (100, 154, 50, 50), (150, 154, 50, 50)], pygame.Rect(900, 350, 10, 10), 5)
    enemySlime3.setDev(-20, -20)
    enemySlime4 = agent.Slime(3,  [(0, 154, 50, 50), (50, 154, 50, 50), (0, 154, 50, 50), (100, 154, 50, 50), (150, 154, 50, 50)], pygame.Rect(900, 450, 10, 10), 5)
    enemySlime4.setDev(-20, -20)
    enemySlime5 = agent.Slime(3,  [(0, 154, 50, 50), (50, 154, 50, 50), (0, 154, 50, 50), (100, 154, 50, 50), (150, 154, 50, 50)], pygame.Rect(700, 300, 10, 10), 5)
    enemySlime5.setDev(-20, -20)
    enemySlime6 = agent.Slime(3,  [(0, 154, 50, 50), (50, 154, 50, 50), (0, 154, 50, 50), (100, 154, 50, 50), (150, 154, 50, 50)], pygame.Rect(800, 500, 10, 10), 5)

    enemySlime6.setDev(-20, -20)
    
    #directional facing sprites require more complexity
    enemyVoodoo = agent.Voodoo(5, [(0, 229, 55, 66), (0, 229, 55, 66), (56, 229, 55, 66), (112, 229, 55, 66), (168, 229, 55, 66), (224, 229, 55, 66), (280, 229, 55, 66),
                                 (336, 229, 55, 66), (392, 229, 55, 66), (448, 229, 55, 66)], pygame.Rect(1000, 100, 36, 46), 6, True)
    enemyVoodoo.setDev(-10,-10)        
    enemySquirrel = agent.Squirrel( 2, [(0, 295, 33, 36), (33, 295, 33, 36), (66, 295, 33, 36), (99, 295, 33, 36), (66, 295, 33, 36),(66, 295, 33, 36), (66, 295, 33, 36),
                                    (99, 295, 34, 36), (99, 295, 34, 36), (99, 295, 34, 36)], pygame.Rect(950, 500, 10, 12), 20, True)
    enemySquirrel.setDev(-12,-12)
    enemySquirrel.setSpeed(5)
    
    enemies = [enemyDragon, enemySlime, enemySlime2, enemySlime3, enemySlime4, enemySlime5, enemySlime6, enemyVoodoo, enemySquirrel]

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
        screen.blit( bottom_side, (0, 648) )

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
    screen.blit( bottom_side, (0, 648) )

    

    rock_Rect = rock.get_rect().move(500, 180)
    hero_Rect = pygame.Rect(50, 50, 58, 68)
    top_Rect = top_side.get_rect()
    bottom_Rect = bottom_side.get_rect().move(0, 648)
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
                pygame.mouse.set_visible(False)
                mpos = pygame.mouse.get_pos()
                target_Rect = target.get_rect().move( mpos[0], mpos[1] )
        
            if event.type == pygame.MOUSEBUTTONDOWN and attacktimer >= 30 and dead == False:
                arrowready.set_volume(.5)
                arrowready.play()
                attackDelay = True
                attacktimer = 0
                if arrownum < 9:
                    arrownum += 1
                else:
                    arrownum = 0

                arrow[arrownum] = pygame.image.load( "arrow.png" ).convert_alpha() 
                arrowshot.set_volume(.5)

                arrow[arrownum] = pygame.image.load( "sprites/particle_main.png" ).convert_alpha() 

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
                    footsteps.set_volume(1)
                    footsteps.play()
                    print "W"
                    vertSpeed-=1
                    wOn=False
                if key[pygame.K_a] and aOn:
                    footsteps.play()
                    print "A"
                    hoSpeed-=1
                    aOn=False
                if key[pygame.K_s] and sOn:
                    footsteps.play()
                    print "S"
                    vertSpeed+=1
                    sOn=False
                if key[pygame.K_d] and dOn:
                    footsteps.play()
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
                    refresh.append( background.get_rect() )
                    print ( "r is hit" )
                    reset(background)
                    loopdeath = 0
                    dFrame = herod[1]
                    hero_Rect = pygame.Rect(50, 50, 87, 102)
                    for enem in enemies:
                        enem.changeRect(enem.getOriginalRect())
                        enem.ressurect()
                    dead = False
                    timeReset()
                    direction=herod
                    refresh.append( background.get_rect() )
                    refresh.append( background.get_rect().move(648, 0) )
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
            if math.sqrt((enem.getRect().centerx - hero_Rect.centerx)**2 + (enem.getRect().centery - hero_Rect.centery)**2) < 400 or enem.isAggro():
                enem.setAggro(True)
                if enem.getRect().bottom < hero_Rect.centery and enem.isDead() != True:
                    enem.setVSpeed(1)
                    enem.movesound.play()
                elif enem.getRect().top > hero_Rect.centery and enem.isDead() != True:
                    enem.setVSpeed(-1)
                else:
                    enem.setVSpeed(0)
                if enem.getRect().right < hero_Rect.centerx and enem.isDead() != True:
                    enem.setHSpeed(1)
                    enem.movesound.play()
                elif enem.getRect().left > hero_Rect.centerx and enem.isDead() != True:
                    enem.setHSpeed(-1)
                else:
                    enem.setHSpeed(0)
            
        # enemy collision with hero checker
        for enem in enemies:
            if enem.getRect().colliderect( hero_Rect ) and enem.isDead() == False :
                dFrame = (464, 0, 58, 68)
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
                        print "before", enem.isAggro()
                        if enem.isAggro() != True:
                            enem.setAggro(True)
                            print "after", enem.isAggro()
                        arrowhit.set_volume(.5)

                    if arrow_rects[k].colliderect( enem.getRect() ) and not enem.isDead():
                        enem.setAggro(True)

                        arrowhit.play()
                        enem.changeHP(-1)
                        refresh.append( (enem.getRect().x+enem.getxDev()*2, enem.getRect().y+enem.getyDev()*2, enem.getRect().width-enem.getxDev()*4, enem.getRect().height-enem.getyDev()*4))
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
        else:
        	   if loopdeath == 0:
        	   	 deathsound.set_volume(.5)
        	   	 deathsound.play()
        	   	 loopdeath += 1
        	   
        #enemy animations!
        for enem in enemies:
            if not enem.isDead():
                if frameCounter % enem.getFrameSpeed() == 0:
                    enem.changeSprite((enem.getSpriteNumber()+1) % (len(enem.getSprites())-1))
            else:
                enem.changeSprite(-1)
                enem.deadcount += 1
                if enem.deadcount == 1:
                	enem.deathsound.set_volume(1)
                	bloodexplode.set_volume(.5)
                	bloodexplode.play()
                	enem.deathsound.play()
                	
            
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
