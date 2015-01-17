# created by Raymond Chung
# file  engine.py

# imports
import sys, pygame, math, agent, os
import titlescreen, room

class engine:
	
	def __init__ (self, state, screen, clock, width, height):
		self.state = state
		self.width = width
		self.height = height
		self.screen = screen
		self.clock = clock
		self.level = 0
		
		#Character stats
		self.attspeed = 10 
		
	# collision checker 
	def pathCollide(self, object_rect, agent_rect, refresh_List ):
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
	
	def setState(self):
	    if self.state == "tutorial":
	        self.room = room.tutorial(self.screen, self.width, self.height)
	    if self.state == "main":
	        if self.level == 0:
	            self.room = room.firstroom(self.screen, self.width, self.height)
	        elif self.level == 1:
	            self.room = room.secondroom(self.screen, self.width, self.height)
	
	def reset(self):
		   self.room.reset()
		   
	def main(self):    
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
	    
	    #make sounds	
	    arrowhit = pygame.mixer.Sound( "sounds/arrowhit.wav" )
	    arrowshot = pygame.mixer.Sound("sounds/arrowshot.wav")
	    arrowready = pygame.mixer.Sound("sounds/arrowready.wav")
	    footsteps = pygame.mixer.Sound("sounds/footsteps.wav")
	    deathsound = pygame.mixer.Sound("sounds/death.wav")

	    #sound volume
	    deathsound.set_volume(.6)
	    arrowshot.set_volume(.6)
	    arrowready.set_volume(.5)
	    footsteps.set_volume(1)
	    arrowhit.set_volume(.5)
	    
	    #making the target move
	    pygame.event.pump()
	    mpos = pygame.mouse.get_pos()
	    
	    arrowLoadImage = pygame.image.load( "sprites/particle_main.png" ).convert_alpha()
	    arrow = [arrowLoadImage, arrowLoadImage, arrowLoadImage, arrowLoadImage, arrowLoadImage, arrowLoadImage, arrowLoadImage, arrowLoadImage, arrowLoadImage, arrowLoadImage]
	    arrow_rects = [arrow[0].get_rect(),arrow[1].get_rect(),arrow[2].get_rect(),arrow[3].get_rect(),arrow[4].get_rect(),arrow[5].get_rect(),arrow[6].get_rect(),arrow[7].get_rect(),arrow[8].get_rect(),arrow[9].get_rect()]
	    
	    heroSprites = pygame.image.load( "sprites/archer_main.png" ).convert_alpha()
	    
	    target = pygame.image.load( "sprites/AimingPointer.png" ).convert_alpha()
	    target = pygame.transform.scale(target, (50, 50))
	    target_Rect = target.get_rect().move( mpos[0], mpos[1] )
	    
	    self.setState()
	    self.reset()
	             
	    pygame.mixer.music.load(self.room.music)
    	    pygame.mixer.music.play(-1,0)
	    
	    
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

	    #remember which direction hero was facing
	    direction = herod
	    dFrame=herod[1]
	    def timeReset():
		   counter=0
		   time=-1
		   
	    self.screen.blit( heroSprites, (50, 50), dFrame  )
		   
	    for enem in self.room.enemies:
		   self.screen.blit( self.room.enemySprites, (enem.getRect().x, enem.getRect().y), enem.getCurrentSprite())
	    
	    self.reset()

	    hero_Rect = pygame.Rect(150, 150, 58, 68)
	    
	    top_Rect = None
	    bottom_Rect = None
	    left_Rect = None
	    right_Rect = None
	    
	    rock_Rects = []
	    if self.room.rock != None:
	        for i in range(len(self.room.rockx)):
	            rock_Rect = self.room.rock.get_rect().move(self.room.rockx[i], self.room.rocky[i])
	            rock_Rects.append(rock_Rect)
	    if self.room.top_side != None:
	        top_Rect = self.room.top_side.get_rect()
	    if self.room.bottom_side != None:
	        bottom_Rect = self.room.bottom_side.get_rect().move(0, self.height-50)
	    if self.room.left_side != None:
	        left_Rect = self.room.left_side.get_rect()
	    if self.room.right_side != None:
	        right_Rect = self.room.right_side.get_rect().move(self.width-50, 0)

	    pygame.display.update()
	    #Control limits 
	    wOn=True
	    aOn=True
	    sOn=True
	    dOn=True

	    while 1 == 1:
		   
		   #counts frames for animations
		   self.room.frameCounter += 1
		   if self.room.frameCounter == 29:
			  self.room.frameCounter = -1
	    
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
		   
			  if event.type == pygame.MOUSEBUTTONDOWN and attacktimer >= self.attspeed and dead == False:

				 chan= pygame.mixer.find_channel(True)
				 chan.play(arrowready)
				 #arrowready.play()
				 print "arrowready",arrowready.get_num_channels()
				 attackDelay = True
				 attacktimer = 0
				 if arrownum < 9:
				     arrownum += 1
				 else:
				     arrownum = 0

				 arrow[arrownum] = pygame.image.load( "arrow.png" ).convert_alpha()  
				 arrow[arrownum] = pygame.image.load( "sprites/particle_main.png" ).convert_alpha() 

				 chan= pygame.mixer.find_channel(True)
				 chan.play(arrowshot)
				 #arrowshot.play()
				 print "arrowshot", arrowshot.get_num_channels()
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
				     self.screen.blit( arrow[arrownum], (arrow_rects[arrownum]) )

			    
			  if event.type == pygame.KEYDOWN and dead != True:
				 key = pygame.key.get_pressed()
				 if key[pygame.K_w] and wOn:
				     footsteps.play(maxtime=1200)
				     print "footsteps up", footsteps.get_num_channels()
				     print "W"
				     vertSpeed-=1
				     wOn=False
				 if key[pygame.K_a] and aOn:
				     footsteps.play(maxtime=1200)
				     print "footsteps left", footsteps.get_num_channels()
				     print "A"
				     hoSpeed-=1
				     aOn=False
				 if key[pygame.K_s] and sOn:
				     footsteps.play(maxtime=1200)
				     print "footsteps down", footsteps.get_num_channels()
				     print "S"
				     vertSpeed+=1
				     sOn=False
				 if key[pygame.K_d] and dOn:
				     footsteps.play(maxtime=1200)
				     print "footsteps right", footsteps.get_num_channels()
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
				     refresh.append( self.room.background.get_rect() )
				     print ( "r is hit" )
				     self.reset()
				     loopdeath = 0
				     dFrame = herod[1]
				     hero_Rect = pygame.Rect(50, 50, 87, 102)
				     for enem in self.room.enemies:
				         enem.changeRect(enem.getOriginalRect())
				         enem.ressurect()
				     dead = False
				     timeReset()
				     direction=herod
				     refresh.append( self.room.background.get_rect() )
				     refresh.append( self.room.background.get_rect().move(648, 0) )
				 elif key[pygame.K_ESCAPE]:
				     titlescreen.main(self.width,self.height)
		   


		   # collision checker
		   if rock_Rects[0] != None:
		       for i in range(len(rock_Rects)):
		           self.pathCollide( rock_Rects[i], hero_Rect, refresh )
		   if top_Rect != None:
		       self.pathCollide( top_Rect, hero_Rect, refresh )
		   if bottom_Rect != None:
		       self.pathCollide( bottom_Rect, hero_Rect, refresh )
		   if left_Rect != None:
		       self.pathCollide( left_Rect, hero_Rect, refresh )
		   if right_Rect != None:
		       self.pathCollide( right_Rect, hero_Rect, refresh )
		   
		   for enem in self.room.enemies:
			  if rock_Rects[0] != None:
		           for i in range(len(rock_Rects)):
		               self.pathCollide( rock_Rects[i], enem.Rect, refresh )
		   """
		   pathCollide( top_Rect, enemy_Rect, refresh )
		   pathCollide( bottom_Rect, enemy_Rect, refresh )
		   pathCollide( left_Rect, enemy_Rect, refresh )
		   pathCollide( right_Rect, enemy_Rect, refresh )
		   """
		   
		   # enemy AI, deciding where it needs to move
		   for enem in self.room.enemies:
			  if math.sqrt((enem.getRect().centerx - hero_Rect.centerx)**2 + (enem.getRect().centery - hero_Rect.centery)**2) < 400 or enem.isAggro():
				 if enem.isAggro() != True:
				 	enem.setAggro(True)
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
		   for enem in self.room.enemies:
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
		   for enem in self.room.enemies:
			  k = 0
			  while k < 10:
				 if arrowOn[k] == True:

				     if arrow_rects[k].colliderect( enem.getRect() ) and not enem.isDead():
				         if enem.isAggro() != True:
				             enem.setAggro(True)

				         chan= pygame.mixer.find_channel(True)
				         chan.play(arrowhit)
				         #arrowhit.play()
				         print "arrowhit", arrowhit.get_num_channels()
				         enem.changeHP(-1)
				         refresh.append( (enem.getRect().x+enem.getxDev()*2, enem.getRect().y+enem.getyDev()*2, enem.getRect().width-enem.getxDev()*4, enem.getRect().height-enem.getyDev()*4))
				         enem.changeRect(enem.getRect().move( 2 * (arrowSpeedX[k]), 2 * (arrowSpeedY[k]) ))
				         arrowOn[k] = False
				 k += 1
				     
		   # movement code
		   hero_Rect = hero_Rect.move( hoSpeed * 5, vertSpeed * 5)
		   for enem in self.room.enemies:
			  enem.changeRect(enem.getRect().move( enem.getHSpeed() * enemySpeed, enem.getVSpeed() * enemySpeed ))
		   
		   

		   # adding all the rectangles to the refresh list
		   refresh.append( hero_Rect )
		   if rock_Rects[0] != None:
		       for i in range(len(rock_Rects)):
		           refresh.append( rock_Rects[i] )
		   refresh.append( target_Rect )
		   for enem in self.room.enemies:
			  refresh.append( (enem.getRect().x+enem.getxDev()*2, enem.getRect().y+enem.getyDev()*2, enem.getRect().width-enem.getxDev()*4, enem.getRect().height-enem.getyDev()*4))
	 
		   i = 0
		   while i < 10:
			  if arrowOn[i] == True:
				 arrow_rects[i] = arrow_rects[i].move( arrowSpeedX[i], arrowSpeedY[i] )
			  if arrowOn[i] == True:
				 refresh.append( arrow_rects[i] )
			  i += 1
		   
		   
		   # redrawing everything
		   self.reset()
		   
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
		   	   	 chan= pygame.mixer.find_channel(True)
		   	   	 chan.play(deathsound)
		   	   	 #deathsound.play()
		   	   	 print "deathsound character", deathsound.get_num_channels()
		   	   	 loopdeath += 1
		   	   
		   #enemy animations!
		   for enem in self.room.enemies:
			  if not enem.isDead():
				 if self.room.frameCounter % enem.getFrameSpeed() == 0:
				     enem.changeSprite((enem.getSpriteNumber()+1) % (len(enem.getSprites())-1))
			  else:
				 enem.changeSprite(-1)
				 
				 if enem.deadcount == 0:
				 	#print "deadcount at death", enem.deadcount
				 	chan = pygame.mixer.find_channel(True)
				 	chan.play(enem.deathsound)
				 	#enem.deathsound.play()
				 	print "deathsound enemy",enem.deathsound.get_num_channels()
				 	enem.deadcount += 1
				 	#print "deadcount after death", enem.deadcount
				 	
		   self.screen.blit( heroSprites, (hero_Rect.x,hero_Rect.y), dFrame )
		   for enem in self.room.enemies:
			  self.screen.blit( self.room.enemySprites, (enem.getRect().x+enem.getxDev(),enem.getRect().y+enem.getyDev()), enem.getCurrentSprite()) 
		   self.screen.blit( target, (target_Rect) )
		   i = 0
		   while i < 10:
			  if arrowOn[i] == True:
				self.screen.blit( arrow[i], (arrow_rects[i]) )
			  i += 1
			  

		   pygame.display.update( refresh )
		   
		   refresh = []
		   
		   if hero_Rect.x > self.width or hero_Rect.x < 0 or hero_Rect.y > self.height or hero_Rect.y < 0:
		       self.level += 1
		       print "LEVEL", self.level
		       self.setState()
		       self.reset()
		       pygame.display.update()
		       
		       top_Rect = None
		       bottom_Rect = None
		       left_Rect = None
		       right_Rect = None
		       
		       rock_Rects = []
		       
		       if self.room.rock != None:
			      for i in range(len(self.room.rockx)):
				     rock_Rect = self.room.rock.get_rect().move(self.room.rockx[i], self.room.rocky[i])
				     rock_Rects.append(rock_Rect)
		       if self.room.top_side != None:
		           top_Rect = self.room.top_side.get_rect()
		       if self.room.bottom_side != None:
		           bottom_Rect = self.room.bottom_side.get_rect().move(0, self.height-50)
		       if self.room.left_side != None:
		           left_Rect = self.room.left_side.get_rect()   
		       if self.room.right_side != None:
			      right_Rect = self.room.right_side.get_rect().move(self.width-50, 0)
		       
		       hero_Rect = pygame.Rect(50, 100, 87, 102)
		       
		       pygame.mixer.music.load(self.room.music)
		       pygame.mixer.music.play(-1,0)
		       
		   
		   self.clock.tick(30)
