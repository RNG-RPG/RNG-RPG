# created by Raymond Chung
# file	engine.py

# imports
import sys, pygame, math, agent, item, os
import titlescreen, room
import levels.grasslands as grasslands
import levels.bosslands as bosslands

class engine:
	
	def __init__ (self, state, screen, clock, width, height):
		self.state = state
		self.width = width
		self.height = height
		self.screen = screen
		self.clock = clock
		self.rooms = []
		self.roomNum = 0
		self.level = 1
		self.pause = False
		self.talking = False
		self.winVar = False
		self.checkAvoid = False
		self.enemySprites = pygame.image.load( "sprites/enemy_main.png" ).convert_alpha()
		
		#Character stats
		self.attspeed = 10 
		
	def getScreen(self):
		return self.screen
	def getWidth(self):
		return self.width
	def getHeight(self):
		return self.height
		
	def setTalk(self, bool):
		self.talking = bool
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
	
	# deals with inventory stuff
	inventoryItems = {(1,1):None,(1,2):None,(1,3):None,(1,4):None,(2,1):None,(2,2):None,(2,3):None,(2,4):None,(3,1):None,(3,2):None,(3,3):None,(3,4):None,(4,1):None,(4,2):None,(4,3):None,(4,4):None,(5,1):None,(5,2):None,(5,3):None,(5,4):None}
	# test of stuff
	inventoryItems[(1,1)] = item.healthPotion()
	def inventoryFunc(self, level, num, agent, inventoryList):
		if isinstance(inventoryList[(level,num)], item.healthPotion):
			if agent.getHP() <= (agent.getMaxHP() - 3):
				agent.changeHP(3)
			else:
				agent.changeHP((agent.getMaxHP() - agent.getHP()))
		print( "level:", level, " num:", num )
	
	# deals with upgrade stuff (for now, I have decided that this should just happen in the function itself.
	# upgradeItems = {(1,1):None,(2,1):None,(2,2):None,(3,1):None,(3,2):None,(3,3):None,(4,1):None,(4,2):None,(4,3):None,(4,4):None,(5,1):None,(5,2):None,(5,3):None,(5,4):None}
	# def upgradeFunc(self, level, num):
	#	print( "level:", level, " num:", num )
	
	#caches to remember room states
	def setUpRooms(self):
             
		self.rooms = []
		if self.level == 0:
			temp = pygame.image.load( "RockGround2.png" ).convert_alpha()
			spritos = [pygame.transform.scale(temp, (self.width, self.height)), pygame.image.load('sprites/rockwall_main.png').convert_alpha(), pygame.image.load( "sprites/enemy_main.png" ).convert_alpha()]
			self.rooms.append(room.cavefirstroom(self.getScreen(), self.getWidth(), self.getHeight(), spritos))
			self.rooms.append(room.cavesecondroom(self.getScreen(), self.getWidth(), self.getHeight(), spritos))
			self.rooms.append(room.cavebossroom(self.getScreen(), self.getWidth(), self.getHeight(), spritos))
			self.rooms.append(room.voodooroom(self.getScreen(), self.getWidth(), self.getHeight(), spritos))
		if self.level == 1:
			temp = pygame.image.load( "GrassGround.png" ).convert_alpha()
			spritos = [pygame.transform.scale(temp, (self.width, self.height)), pygame.image.load('sprites/treewall_main.png').convert_alpha(), pygame.image.load( "sprites/enemy_main.png" ).convert_alpha(),
						pygame.image.load('sprites/rockwall_main.png').convert_alpha()]
			self.rooms = grasslands.gatherRooms(self.getScreen(), self.getWidth(), self.getHeight(), spritos)
		if self.level == 2:
			temp = pygame.image.load( "RockGround2.png" ).convert_alpha()
			spritos = [pygame.transform.scale(temp, (self.width, self.height)), pygame.image.load('sprites/rockwall_main.png').convert_alpha(), pygame.image.load( "sprites/enemy_main.png" ).convert_alpha()]
			self.rooms.append(room.cavefirstroom(self.getScreen(), self.getWidth(), self.getHeight(), spritos))
			self.rooms.append(room.cavesecondroom(self.getScreen(), self.getWidth(), self.getHeight(), spritos))
			self.rooms.append(room.cavebossroom(self.getScreen(), self.getWidth(), self.getHeight(), spritos))
			self.rooms.append(room.voodooroom(self.getScreen(), self.getWidth(), self.getHeight(), spritos))
		if self.level == 3:
			temp = pygame.image.load( "GrassGround.png" ).convert_alpha()
			spritos = [pygame.transform.scale(temp, (self.width, self.height)), pygame.image.load('sprites/treewall_main.png').convert_alpha(), pygame.image.load( "sprites/enemy_main.png" ).convert_alpha(),
						pygame.image.load('sprites/rockwall_main.png').convert_alpha()]
			self.rooms = bosslands.gatherRooms(self.getScreen(), self.getWidth(), self.getHeight(), spritos)
            
	
	def setState(self):
		if self.state == "sandbox":
			self.room = room.sandbox(self.screen, self.width, self.height)
		if self.state == "tutorial":
			self.level = 0
			self.room = self.rooms[self.roomNum]
		if self.state == "main":
			self.level = 1
			self.room = self.rooms[self.roomNum]
		if self.state == "main1":
			self.level = 2
			self.room = self.rooms[self.roomNum]
		if self.state == "main2":
			self.level = 3
			self.room = self.rooms[self.roomNum]
	
	def reset(self):
			self.room.reset()
	
	def paused(self):
		while self.pause:
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_p:
						self.pause = False
						self.paused()
	 
			pygame.display.update()
			self.clock.tick(15) 


	
	def main(self):		
		pygame.event.set_allowed(pygame.MOUSEMOTION)
		pygame.mouse.get_focused
		dead = False
		arrowOn = [False]*10
		vertSpeed = 0
		hoSpeed = 0
		frame = 0
		attacktimer = 30
		inventoryOn = False
		hero_invincible = False
		invincible_counter = 0
		attackDelay = False
		# defines speed of enemy
		enemySpeed = 1
		arrowSpeedX = [0,0,0,0,0,0,0,0,0,0]
		arrowSpeedY = [0,0,0,0,0,0,0,0,0,0]
		arrownum = 0
		loopdeath= 0
		refresh = [] 
		displayText = None
		bestFont = pygame.font.SysFont("Helvetica", 25)
		#load inventory image
		inventory = pygame.image.load( "upgrades.png" ).convert_alpha()
		texture_missing_upgrades = pygame.image.load( "texture_missing_upgrades.png" ).convert_alpha()
		description = ""
		attackSecondary = 1
		attackRadius = 200
		AOE = False
		DPS = False
		
		LEFT = 1
		MIDDLE = 2
		RIGHT = 3
		SCROLL_UP = 4
		SCROLL_DOWN = 5
		
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
		
		
		# arrow initializing
		arrowLoadImage = pygame.image.load( "sprites/particle_main.png" ).convert_alpha()
		arrow = [arrowLoadImage, arrowLoadImage, arrowLoadImage, arrowLoadImage, arrowLoadImage, arrowLoadImage, arrowLoadImage, arrowLoadImage, arrowLoadImage, arrowLoadImage]
		arrow_rects = [arrow[0].get_rect(),arrow[1].get_rect(),arrow[2].get_rect(),arrow[3].get_rect(),arrow[4].get_rect(),arrow[5].get_rect(),arrow[6].get_rect(),arrow[7].get_rect(),arrow[8].get_rect(),arrow[9].get_rect()]
		arrow_posX = [None,None,None,None,None,None,None,None,None,None]
		arrow_posY = [None,None,None,None,None,None,None,None,None,None]
		
		# enemy projectile initializing
		projectileLoadImage = pygame.image.load( "dsprite/FireBall.png" ).convert_alpha()
		projectilenum = 0
		projectile = []
		projectile_rects = []
		projectile_posX = []
		projectile_posY = []
		projectileSpeedX = []
		projectileSpeedY = []
		enemy_projectiles = []
		i = 0
		while i < 20:
			projectile.append(projectileLoadImage)
			projectile_rects.append(projectile[i].get_rect())
			projectile_posX.append(None)
			projectile_posY.append(None)
			enemy_projectiles.append(False)
			projectileSpeedX.append(None)
			projectileSpeedY.append(None)
			i += 1
		
		# hero health stuff
		healthBar = pygame.image.load( "HP_Bar.png" ).convert_alpha()
		healthBar_Rect = healthBar.get_rect().move(0, 539)
		health_Rect = pygame.Rect((4, 574), (17, 91))
		agent_hero = agent.Agent(10, 4, 0, 1)

		# hero mana stuff
		manaBar = pygame.image.load( "HP_Bar.png" ).convert_alpha()
		manaBar_Rect = healthBar.get_rect().move(26, 539)
		mana_Rect = pygame.Rect((30, 574), (17, 91))
		
		heroSprites = pygame.image.load( "sprites/archer_main.png" ).convert_alpha()
		npcSprites = pygame.image.load( "sprites/npc_main.png" ).convert_alpha()
		target = pygame.image.load( "sprites/AimingPointer.png" ).convert_alpha()
		target = pygame.transform.scale(target, (45, 50))
		target_Rect = target.get_rect().move( mpos[0] - 25, mpos[1] - 25)
		
		self.setUpRooms()
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
			
		self.screen.blit( heroSprites, (50, 50), dFrame	 )
			
		for enem in self.room.enemies:
			self.screen.blit( self.enemySprites, (enem.getRect().x, enem.getRect().y), enem.getCurrentSprite())
		
		self.reset()

		hero_Rect = pygame.Rect(150, 150, 58, 68)
		
		wall_Rects = []
		rock_Rects = []
		if self.room.rock != None:
			for i in range(len(self.room.rockx)):
				rock_Rect = self.room.rock.get_rect().move(self.room.rockx[i], self.room.rocky[i])
				rock_Rects.append(rock_Rect)
                        
		for wall in self.room.walls:
			wall_Rects.append(wall)
            
		pygame.display.update()
		#Control limits 
		wOn=True
		aOn=True
		sOn=True
		dOn=True
		
		self.tutorialcount = 0
		
		while 1 == 1:
		
			# health_bar calculator
			health_Rect = pygame.Rect((4, (574 + ((float(agent_hero.getMaxHP() - agent_hero.getHP())/float(agent_hero.getMaxHP())) * 91))), (17, (float(agent_hero.getHP())/float(agent_hero.getMaxHP())) * 91))
			mana_Rect = pygame.Rect((30, (574 + ((float(agent_hero.getMaxMP() - agent_hero.getMP())/float(agent_hero.getMaxMP())) * 91))), (17, (float(agent_hero.getMP())/float(agent_hero.getMaxMP())) * 91))
			# Stage Changing/win variables - LEVEL DESIGN:
			if self.state == "main":
				if self.rooms[5].bossDead() and self.rooms[9].bossDead() and self.winVar == False:
					self.rooms[7].setNPC(["The forest seems to be at peace..."])
					self.rooms[12].setNPC(["You have conquered the woods...", "Now face your foe within the caves!"])
					self.rooms[12].setPass(True)
					self.winVar = True
			elif self.state == "main1":
				if self.rooms[2].bossDead() and self.winVar == False:
					self.reset()
					wall_Rects = []
					for wall in self.room.walls:
						wall_Rects.append(wall)
					pygame.display.update()
					self.winVar = True
			elif self.state == "main2":
				if self.rooms[6].bossDead() and self.rooms[7].bossDead() and self.rooms[8].bossDead():
					#do shit
					print "THE BOSS EVEN STRIKES IN ROOM 5"
			def tutpaused():
				while self.pause:			  
					if self.tutorialcount < 4:
						for event in pygame.event.get():
							print "looking for movement pause"
							if event.type == pygame.KEYDOWN:
								if event.key == pygame.K_w or event.key == pygame.K_a or event.key == pygame.K_s or event.key == pygame.K_d:
									print "found movement pause"
									self.pause = False
									tutpaused()
									self.tutorialcount += 1
									print "tutorialcount pause", self.tutorialcount
					elif self.tutorialcount < 10:
						for event in pygame.event.get():
							print "looking for movement pause 2"
							if event.type == pygame.MOUSEBUTTONDOWN:
								print "found movement pause 2"
								self.pause = False
								tutpaused()
								self.tutorialcount += 1
								print "tutorialcount pause 2", self.tutorialcount
					elif self.tutorialcount > 9:
						for event in pygame.event.get():
							print "looking for movement pause 3"
							if event.type == pygame.KEYDOWN:
								pygame.display.update()
								print "found movement pause 3"
								self.pause = False
								tutpaused()
								self.tutorialcount += 1
								print "tutorialcount pause 3", self.tutorialcount
								print "tutorial complete"

				pygame.display.update()
				self.clock.tick(15) 
					  
			if self.state == "tutorial":
				tutorial1 = pygame.image.load( "Tutorial/Tutorial1.png" ).convert_alpha()
				tutorial1 = pygame.transform.scale(tutorial1, (self.width, self.height))
				tutorial2 = pygame.image.load( "Tutorial/Tutorial2.png" ).convert_alpha()
				tutorial2 = pygame.transform.scale(tutorial2, (self.width, self.height))
				tutorial3 = pygame.image.load( "Tutorial/Tutorial3.png" ).convert_alpha()
				tutorial3 = pygame.transform.scale(tutorial3, (self.width, self.height)) 
			
				if self.room.identity == 1 and self.tutorialcount == 0:
					print "identified"
					self.screen.blit( tutorial1, (0,0) )
					pygame.display.update()
					self.pause = True
					tutpaused()
				elif self.room.identity == 1 and self.tutorialcount < 6:
					for event in pygame.event.get():
						print "looking for movement"
						if event.type == pygame.KEYDOWN:
							pygame.display.update()
							if event.key == pygame.K_w or event.key == pygame.K_a or event.key == pygame.K_s or event.key == pygame.K_d and not self.talking:
								
								if event.key == pygame.K_w:
									footsteps.play(maxtime=1200)
									print "footsteps up", footsteps.get_num_channels()
									print "W"
									vertSpeed-=1
								if event.key == pygame.K_a:
									footsteps.play(maxtime=1200)
									print "footsteps left", footsteps.get_num_channels()
									print "A"
									hoSpeed-=1
								if event.key == pygame.K_s:
									footsteps.play(maxtime=1200)
									print "footsteps down", footsteps.get_num_channels()
									print "S"
									vertSpeed+=1
								if event.key == pygame.K_d:
									footsteps.play(maxtime=1200)
									print "footsteps right", footsteps.get_num_channels()
									print "D"
									hoSpeed+=1
								
								print "found movement"
								self.tutorialcount += 1
								print "tutorialcount", self.tutorialcount
				elif self.room.identity == 1 and self.tutorialcount == 6:
					print "identified 2"
					self.screen.blit( tutorial2, (0,0) )
					pygame.display.update()
					self.pause = True
					tutpaused()
			
				elif self.room.identity == 1 and self.tutorialcount < 10:
					for event in pygame.event.get():
						print "looking for movement 2"
						if event.type == pygame.MOUSEMOTION:
							pygame.mouse.set_visible(False)
							mpos = pygame.mouse.get_pos()
							target_Rect = target.get_rect().move( mpos[0] - 25, mpos[1] - 25)
							pygame.display.update()
						if event.type == pygame.MOUSEBUTTONDOWN and inventoryOn != True and event.button == LEFT:
							
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
		  
							arrow[arrownum] = pygame.image.load( "sprites/particle_main.png" ).convert_alpha() 

							chan= pygame.mixer.find_channel(True)
							chan.play(arrowshot)
							#arrowshot.play()
							#print "arrowshot", arrowshot.get_num_channels()
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
							if (hero_Rect.centerx > target_Rect.centerx):
								arrow[arrownum] = pygame.transform.rotate(arrow[arrownum], ( - (math.degrees(angle)) + 180 ))
							else:
								arrow[arrownum] = pygame.transform.rotate(arrow[arrownum], ( - (math.degrees(angle)) ))

							arrow_rects[arrownum] = arrow[arrownum].get_rect().move( hero_Rect.centerx - (arrow[arrownum].get_rect().width/2), hero_Rect.centery - (arrow[arrownum].get_rect().height/2) )
							arrow_posX[arrownum] = arrow_rects[arrownum].left
							arrow_posY[arrownum] = arrow_rects[arrownum].top
							print( "arrow_posX : " )
							print( arrow_posX[arrownum] )
							print( "arrow_posY : " )
							print( arrow_posY[arrownum] )
							arrowOn[arrownum] = True
							print 'hibish4'
							arrowSpeedY[arrownum] =	 ( math.sin(angle) * 10.0 )
							#print( "arrowSpeedY" )
							#print( arrowSpeedY )
							#print( "############" )
							arrowSpeedX[arrownum] =	 ( math.cos(angle) * 10.0 )
							if (hero_Rect.centerx > target_Rect.centerx):
								arrowSpeedX[arrownum] = -arrowSpeedX[arrownum]
								arrowSpeedY[arrownum] = -arrowSpeedY[arrownum]
							#print( "arrowSpeedX" )
							#print( arrowSpeedX )
							#print( "############" )
							self.screen.blit( arrow[arrownum], (arrow_rects[arrownum]) )

							
							print "found movement 2"
							self.tutorialcount += 1
							print "tutorialcount 2", self.tutorialcount
				elif self.room.identity == 1 and self.tutorialcount == 10:
					print "identified 3"
					self.screen.blit( tutorial3, (0,0) )
					pygame.display.update()
					self.pause = True
					tutpaused()
				elif self.tutorialcount > 10:
					pygame.display.update()
			
			# dragon shooting code
			for enem in self.room.enemies:
				if isinstance(enem, agent.Dragon) and enem.isDead() != True:
					if self.room.frameCounter == 15:
						if projectilenum < 19:
							projectilenum += 1
						else:
							projectilenum = 0
						if hero_Rect.centerx - enem.getRect().centerx == 0:
							projectileSpeedX[projectilenum] = 0
							projectileSpeedY[projectilenum] = 10
						elif hero_Rect.centery - enem.getRect().centery == 0:
							projectileSpeedX[projectilenum] = 10
							projectileSpeedY[projectilenum] = 0
						else:
							temp_tan_var = ((float(hero_Rect.centery) - float(enem.getRect().centery))/(float(hero_Rect.centerx) - float(enem.getRect().centerx)))
							#print( "temp_tan_var" )
							#print( temp_tan_var )
							#print( "############" )
							angle = (math.atan( temp_tan_var ))
						projectile_rects[projectilenum] = projectile[projectilenum].get_rect().move( enem.getRect().centerx - (projectile[projectilenum].get_rect().width/2), enem.getRect().centery - (projectile[projectilenum].get_rect().height/2) )
						projectile_posX[projectilenum] = projectile_rects[projectilenum].left
						projectile_posY[projectilenum] = projectile_rects[projectilenum].top
						# print( "projectile_posX : " )
						# print( projectile_posX[projectilenum] )
						# print( "projectile_posY : " )
						# print( projectile_posY[projectilenum] )
						# enemy_projectiles[projectilenum] = True
						# print 'hibish4'
						projectileSpeedY[projectilenum] = ( math.sin(angle) * 10.0 )
						#print( "arrowSpeedY" )
						#print( arrowSpeedY )
						#print( "############" )
						projectileSpeedX[projectilenum] = ( math.cos(angle) * 10.0 )
						if (hero_Rect.centerx < target_Rect.centerx):
							projectileSpeedX[projectilenum] = -projectileSpeedX[projectilenum]
							projectileSpeedY[projectilenum] = -projectileSpeedY[projectilenum]
						#print( "arrowSpeedX" )
						#print( arrowSpeedX )
						#print( "############" )
						enemy_projectiles[projectilenum] = True
						self.screen.blit( projectile[projectilenum], (projectile_rects[projectilenum]) )

			
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
			refresh.append( pygame.Rect(hero_Rect.x-20, hero_Rect.y-20, 98, 108 ))
			#refresh.append( background.get_rect() )
			refresh.append( target_Rect )
			#refresh.append( health
			j = 0
			while j < 10:
				if arrowOn[j] == True:
					refresh.append( arrow_rects[j] )
				j += 1
			  
			for event in pygame.event.get():
				if event.type == pygame.MOUSEMOTION:
					pygame.mouse.set_visible(False)
					mpos = pygame.mouse.get_pos()
					target_Rect = target.get_rect().move( mpos[0] - 25, mpos[1] - 25)
				
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_p:
					  self.pause = True
					  self.paused()
					  
				if event.type == pygame.MOUSEBUTTONDOWN and self.talking:
					displayText=activeNPC.getMessage()
				# event = pygame.event.poll()
				if event.type == pygame.MOUSEBUTTONDOWN and attacktimer >= self.attspeed and dead == False and inventoryOn != True and event.button == LEFT and not self.talking:
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

					if (hero_Rect.centerx > target_Rect.centerx):
						arrow[arrownum] = pygame.transform.rotate(arrow[arrownum], ( - (angle * 57.29) + 180 ))
					else:
						arrow[arrownum] = pygame.transform.rotate(arrow[arrownum], ( - (angle * 57.29) ))
					arrow_rects[arrownum] = arrow[arrownum].get_rect().move( hero_Rect.centerx - (arrow[arrownum].get_rect().width/2), hero_Rect.centery - (arrow[arrownum].get_rect().height/2) )
					arrow_posX[arrownum] = arrow_rects[arrownum].left
					arrow_posY[arrownum] = arrow_rects[arrownum].top
					print( "arrow_posX : " )
					print( arrow_posX[arrownum] )
					print( "arrow_posY : " )
					print( arrow_posY[arrownum] )
					arrowOn[arrownum] = True
					arrowSpeedY[arrownum] =	 ( math.sin(angle) * 10.0 )
					#print( "arrowSpeedY" )
					#print( arrowSpeedY )
					#print( "############" )
					arrowSpeedX[arrownum] =	 ( math.cos(angle) * 10.0 )
					if arrowSpeedX[arrownum] == 0 and arrowSpeedY[arrownum] == 0:
						arrowOn[arrownum] = False
					if (hero_Rect.centerx > target_Rect.centerx):
						arrowSpeedX[arrownum] = -arrowSpeedX[arrownum]
						arrowSpeedY[arrownum] = -arrowSpeedY[arrownum]
					#print( "arrowSpeedX" )
					#print( arrowSpeedX )
					#print( "############" )
					self.screen.blit( arrow[arrownum], (arrow_rects[arrownum]) )
				elif event.type == pygame.MOUSEBUTTONDOWN and attacktimer >= self.attspeed and dead == False and inventoryOn != True and event.button == RIGHT and not self.talking:
					print( "right button clicked" )
					if agent_hero.getMP() > 0:
						agent_hero.changeMP( -1 )
						for enem in self.room.enemies:
							if AOE == True and enem.isDead() == False:
								if ((((enem.getRect().centery-hero_Rect.centery)**2) + ((enem.getRect().centerx-hero_Rect.centerx)**2)) ** .5) <= attackRadius:
									enem.changeHP( ( attackSecondary * -1) )
									if enem.aggressive != True:
										enem.setAggress(True)
									if enem.isAggro() != True:
										enem.setAggro(True)
							elif DPS == True:
								print( "big damage arrow fired" )
							# else:
								# print( "we don't have the technology!" )

						   
				if event.type == pygame.KEYDOWN and dead != True:
					key = pygame.key.get_pressed()
					
					if key[pygame.K_w] and wOn:
						if not self.talking:
							footsteps.play(maxtime=1200)
							print "footsteps up", footsteps.get_num_channels()
						print "W"
						vertSpeed-=1
						wOn=False
					if key[pygame.K_a] and aOn:
						if not self.talking:
							footsteps.play(maxtime=1200)
							print "footsteps left", footsteps.get_num_channels()
						print "A"
						hoSpeed-=1
						aOn=False
					if key[pygame.K_s] and sOn:
						if not self.talking:
							footsteps.play(maxtime=1200)
							print "footsteps down", footsteps.get_num_channels()
						print "S"
						vertSpeed+=1
						sOn=False
					if key[pygame.K_d] and dOn:
						if not self.talking:
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
						hero_Rect = pygame.Rect(50, 50, 58, 68)
						self.talking = False
						for enem in self.room.enemies:
							enem.changeRect(enem.getOriginalRect())
							enem.ressurect()
						dead = False
						timeReset()
						direction=herod
						refresh.append( self.room.background.get_rect() )
						refresh.append( self.room.background.get_rect().move(648, 0) )
						agent_hero = agent.Agent(10, 4, 0, 1)
					elif key[pygame.K_ESCAPE]:
						titlescreen.main(self.width,self.height)
					elif key[pygame.K_i]:
						refresh.append( self.room.background.get_rect() )
						print ( "i is hit" )
						#self.reset()
						if inventoryOn != True:
							inventoryOn = True
						else:
							inventoryOn = False
				elif event.type == pygame.MOUSEBUTTONDOWN and inventoryOn == True:
					# inventory slots:
					if pygame.Rect((18+200,17+30), (55,55)).collidepoint( pygame.mouse.get_pos() ):
						self.inventoryFunc(1, 1, agent_hero, self.inventoryItems)
					elif pygame.Rect((18+200,105+30), (55,55)).collidepoint( pygame.mouse.get_pos() ):
						self.inventoryFunc(1, 2, agent_hero, self.inventoryItems)
					elif pygame.Rect((18+200,193+30), (55,55)).collidepoint( pygame.mouse.get_pos() ):
						self.inventoryFunc(1, 3, agent_hero, self.inventoryItems)
					elif pygame.Rect((18+200,281+30), (55,55)).collidepoint( pygame.mouse.get_pos() ):
						self.inventoryFunc(1, 4, agent_hero, self.inventoryItems)
					elif pygame.Rect((18+200,369+30), (55,55)).collidepoint( pygame.mouse.get_pos() ):
						self.inventoryFunc(1, 5, agent_hero, self.inventoryItems)
					elif pygame.Rect((106+200,17+30), (55,55)).collidepoint( pygame.mouse.get_pos() ):
						self.inventoryFunc(2, 1, agent_hero, self.inventoryItems)
					elif pygame.Rect((106+200,105+30), (55,55)).collidepoint( pygame.mouse.get_pos() ):
						self.inventoryFunc(2, 2, agent_hero, self.inventoryItems)
					elif pygame.Rect((106+200,193+30), (55,55)).collidepoint( pygame.mouse.get_pos() ):
						self.inventoryFunc(2, 3, agent_hero, self.inventoryItems)
					elif pygame.Rect((106+200,281+30), (55,55)).collidepoint( pygame.mouse.get_pos() ):
						self.inventoryFunc(2, 4, agent_hero, self.inventoryItems)
					elif pygame.Rect((106+200,369+30), (55,55)).collidepoint( pygame.mouse.get_pos() ):
						self.inventoryFunc(2, 5, agent_hero, self.inventoryItems)
					elif pygame.Rect((194+200,17+30), (55,55)).collidepoint( pygame.mouse.get_pos() ):
						self.inventoryFunc(3, 1, agent_hero, self.inventoryItems)
					elif pygame.Rect((194+200,105+30), (55,55)).collidepoint( pygame.mouse.get_pos() ):
						self.inventoryFunc(3, 2, agent_hero, self.inventoryItems)
					elif pygame.Rect((194+200,193+30), (55,55)).collidepoint( pygame.mouse.get_pos() ):
						self.inventoryFunc(3, 3, agent_hero, self.inventoryItems)
					elif pygame.Rect((194+200,281+30), (55,55)).collidepoint( pygame.mouse.get_pos() ):
						self.inventoryFunc(3, 4, agent_hero, self.inventoryItems)
					elif pygame.Rect((194+200,369+30), (55,55)).collidepoint( pygame.mouse.get_pos() ):
						self.inventoryFunc(3, 5, agent_hero, self.inventoryItems)
					elif pygame.Rect((282+200,17+30), (55,55)).collidepoint( pygame.mouse.get_pos() ):
						self.inventoryFunc(4, 1, agent_hero, self.inventoryItems)
					elif pygame.Rect((282+200,105+30), (55,55)).collidepoint( pygame.mouse.get_pos() ):
						self.inventoryFunc(4, 2, agent_hero, self.inventoryItems)
					elif pygame.Rect((282+200,193+30), (55,55)).collidepoint( pygame.mouse.get_pos() ):
						self.inventoryFunc(4, 3, agent_hero, self.inventoryItems)
					elif pygame.Rect((282+200,281+30), (55,55)).collidepoint( pygame.mouse.get_pos() ):
						self.inventoryFunc(4, 4, agent_hero, self.inventoryItems)
					elif pygame.Rect((282+200,369+30), (55,55)).collidepoint( pygame.mouse.get_pos() ):
						self.inventoryFunc(4, 5, agent_hero, self.inventoryItems)
						# upgrade slots:
					elif pygame.Rect((550+200,22+30), (57,57)).collidepoint( pygame.mouse.get_pos() ):
						print( "1, 1" )
						#self.upgradeFunc(1, 1, agent_hero)
					elif pygame.Rect((492+200,109+30), (57,57)).collidepoint( pygame.mouse.get_pos() ):
						print( "2, 1" )
						AOE = True
						#self.upgradeFunc(2, 1, agent_hero)
					elif pygame.Rect((608+200,109+30), (57,57)).collidepoint( pygame.mouse.get_pos() ):
						print( "2, 2" )
						DPS = True
						#self.upgradeFunc(2, 2, agent_hero)
					elif pygame.Rect((434+200,196+30), (57,57)).collidepoint( pygame.mouse.get_pos() ):
						print( "3, 1" )
						#self.upgradeFunc(3, 1, agent_hero)
					elif pygame.Rect((550+200,196+30), (57,57)).collidepoint( pygame.mouse.get_pos() ):
						print( "3, 2" )
						#self.upgradeFunc(3, 2, agent_hero)
					elif pygame.Rect((666+200,196+30), (57,57)).collidepoint( pygame.mouse.get_pos() ): #devil's button!!! *oooooooooooooooh*
						print( "3, 3" )
						#self.upgradeFunc(3, 3, agent_hero)
					elif pygame.Rect((376+200,283+30), (57,57)).collidepoint( pygame.mouse.get_pos() ):
						print( "4, 1" )
						#self.upgradeFunc(4, 1, agent_hero)
					elif pygame.Rect((492+200,283+30), (57,57)).collidepoint( pygame.mouse.get_pos() ):
						print( "4, 2" )
						#self.upgradeFunc(4, 2, agent_hero)
					elif pygame.Rect((608+200, 283+30), (57,57)).collidepoint( pygame.mouse.get_pos() ):
						print( "4, 3" )
						#self.upgradeFunc(4, 3, agent_hero)
					elif pygame.Rect((724+200, 283+30), (57,57)).collidepoint( pygame.mouse.get_pos() ):
						print( "4, 4" )
						#self.upgradeFunc(4, 4, agent_hero)
					elif pygame.Rect((376+200,370+30), (57,57)).collidepoint( pygame.mouse.get_pos() ):
						print( "5, 1" )
						#self.upgradeFunc(5, 1, agent_hero)
					elif pygame.Rect((492+200,370+30), (57,57)).collidepoint( pygame.mouse.get_pos() ):
						print( "5, 2" )
						#self.upgradeFunc(5, 2, agent_hero)
					elif pygame.Rect((608+200,370+30), (57,57)).collidepoint( pygame.mouse.get_pos() ):
						print( "5, 3" )
						#self.upgradeFunc(5, 3, agent_hero)
					elif pygame.Rect((724+200,370+30), (57,57)).collidepoint( pygame.mouse.get_pos() ):
						print( "5 ,4" )
						#self.upgradeFunc(5, 4, agent_hero)



			# collision checker
			for rock in rock_Rects:
				self.pathCollide( rock, hero_Rect, refresh )
			for wall in wall_Rects:
				self.pathCollide( wall, hero_Rect, refresh)
				for enem in self.room.enemies:
					self.pathCollide(wall, enem.Rect, refresh)
			for NPC in self.room.NPCs:
				if not self.talking and hero_Rect.colliderect( NPC.getRect() ):
					self.setTalk(True)
					talkFrame = direction[1]
					activeNPC = NPC
					displayText=activeNPC.getMessage()
				self.pathCollide( NPC.getRect(), hero_Rect, refresh)
			for enem in self.room.enemies:
				for rock in rock_Rects:
					self.pathCollide( rock, enem.Rect, refresh )

			# enemy AI, deciding where it needs to move
			for enem in self.room.enemies:
				if enem.aggressive == True:
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
				if enem.getRect().colliderect( hero_Rect ) and enem.isDead() == False and hero_invincible == False:
					agent_hero.changeHP( - (enem.getAttack()) )
					health_Rect = pygame.Rect((4, (574 + ((float(agent_hero.getMaxHP() - agent_hero.getHP())/float(agent_hero.getMaxHP())) * 91))), (17, (float(agent_hero.getHP())/float(agent_hero.getMaxHP())) * 91))
					print( "health lost", enem.getAttack(), agent_hero.getHP() )
					hero_invincible = True
					if hero_Rect.top > 70 and hero_Rect.bottom < self.height - 70 and hero_Rect.left > 70 and hero_Rect.right <self.width - 70:
						hero_Rect = hero_Rect.move( enem.getHSpeed() * 5, enem.getVSpeed() * 5 )
					if agent_hero.getHP() <= 0:
						dead = True
						health_Rect = pygame.Rect( (0, 0), (0, 0) )
				if enem.getRect().colliderect(hero_Rect) and enem.isDead() and isinstance(enem, agent.TreeBeard):
					self.pathCollide(enem.getRect(), hero_Rect, refresh)
					"""
					for event in pygame.event.get(): 
					if event.type == pygame.KEYDOWN:
					key = pygame.key.get_pressed()
					"""
			
			# dragon fireball collision with hero checker
			i = 0
			while i < 20:
				if enemy_projectiles[i] == True:
					if projectile_rects[i].colliderect( hero_Rect ) and hero_invincible == False:
						agent_hero.changeHP( - 1 )
						print( "health lost", enem.getAttack(), agent_hero.getHP() )
						hero_invincible = True
						hero_Rect = hero_Rect.move( enem.getHSpeed() * 5, enem.getVSpeed() * 5 )
						if agent_hero.getHP() <= 0:
							dead = True
							health_Rect = pygame.Rect( (0, 0), (0, 0) )
						enemy_projectiles[i] = False
				i += 1
					
			# arrow collision with enemy checker
			for enem in self.room.enemies:
				k = 0
				while k < 10:
					if arrowOn[k] == True:
						if arrow_rects[k].colliderect( enem.getRect() ) and not enem.isDead():
							if enem.aggressive != True:
								enem.setAggress(True)
							if enem.isAggro() != True:
								enem.setAggro(True)
							for enem2 in self.room.enemies:
								if math.sqrt((enem.getRect().centerx - enem2.getRect().centerx)**2 + (enem.getRect().centery - enem2.getRect().centery)**2) < 300:
									if enem2.aggressive != True:
										enem2.setAggress(True)
									if enem2.isAggro() != True:
										enem2.setAggro(True)	
							chan= pygame.mixer.find_channel(True)
							chan.play(arrowhit)
							#arrowhit.play()
							print "arrowhit", arrowhit.get_num_channels()
							enem.changeHP(-1)
							if enem.getHP() <= 0:
								enem.setDead(True)
								enem.setHSpeed(0)
								enem.setVSpeed(0)
								agent_hero.changeEXP(enem.getEXP())
								print("did all the stuff when the thing died")
							refresh.append( (enem.getRect().x+enem.getxDev()*2, enem.getRect().y+enem.getyDev()*2, enem.getRect().width-enem.getxDev()*4, enem.getRect().height-enem.getyDev()*4))
							if not isinstance(enem, agent.TreeBeard):
								if enem.getRect().top > 70 and enem.getRect().bottom < self.height - 70 and enem.getRect().left > 70 and enem.getRect().right <self.width - 70:
									enem.changeRect(enem.getRect().move( 2 * (arrowSpeedX[k]), 2 * (arrowSpeedY[k]) ))
							arrowOn[k] = False
					k += 1
					 
			# movement code
			if not self.talking:
				hero_Rect = hero_Rect.move( hoSpeed * 5, vertSpeed * 5)
			for enem in self.room.enemies:
				enem.changeRect(enem.getRect().move( enem.getHSpeed() * enemySpeed, enem.getVSpeed() * enemySpeed ))

			
			
			# adding all the rectangles to the refresh list
			#refresh.append( 
			refresh.append( target_Rect )
			refresh.append( healthBar_Rect )
			refresh.append( manaBar_Rect )
			refresh.append( mana_Rect )
			refresh.append( health_Rect )
			for enem in self.room.enemies:
				refresh.append( (enem.getRect().x+enem.getxDev()*2, enem.getRect().y+enem.getyDev()*2, enem.getRect().width-enem.getxDev()*4, enem.getRect().height-enem.getyDev()*4))
			for NPC in self.room.NPCs:
				refresh.append(( NPC.getRect().x-2, NPC.getRect().y,NPC.getRect().width, NPC.getRect().height))
			i = 0
			while i < 10:
				if arrowOn[i] == True:
					refresh.append( arrow_rects[i] )
					arrow_posX[i] = arrow_posX[i] + arrowSpeedX[i]
					arrow_posY[i] = arrow_posY[i] + arrowSpeedY[i]
					arrow_rects[i].left = arrow_posX[i]
					arrow_rects[i].top = arrow_posY[i]
					#arrow_rects[i] = arrow_rects[i].move( arrowSpeedX[i], arrowSpeedY[i] )
				if arrowOn[i] == True:
					refresh.append((arrow_rects[i].x-20, arrow_rects[i].y-20,arrow_rects[i].width+40,arrow_rects[i].height+40))
				i += 1
			if self.talking:
				refresh.append((50, 600, 1100, 200))

			# enemy projectile movement
			i = 0
			while i < 20:
				if enemy_projectiles[i] == True:
					refresh.append( projectile_rects[i] )
					projectile_posX[i] = projectile_posX[i] + projectileSpeedX[i]
					projectile_posY[i] = projectile_posY[i] + projectileSpeedY[i]
					projectile_rects[i].left = projectile_posX[i]
					projectile_rects[i].top = projectile_posY[i]
					#arrow_rects[i] = arrow_rects[i].move( arrowSpeedX[i], arrowSpeedY[i] )
				if enemy_projectiles[i] == True:
					refresh.append((projectile_rects[i].x-20, projectile_rects[i].y-20,projectile_rects[i].width+40,projectile_rects[i].height+40))
				i += 1
		   
			# redrawing everything
			self.reset()
		   
			# enemy hp stuff
			i = 0
			enem_health_rects = []
			for enem in self.room.enemies:
				#print( "Appending!" )
				if enem.getHP() != 0:
					
					enem_health_rects.append(pygame.Rect((enem.getRect().left, enem.getRect().top - 20), (((float(enem.getHP())/float(enem.getMaxHP()))*enem.getRect().width*3), 10)))
					pygame.draw.rect(self.screen, (255, 0, 0), enem_health_rects[i], 0)
					refresh_rect = pygame.Rect((enem_health_rects[i].left - 20, enem_health_rects[i].top - 20), (enem_health_rects[i].width + 40, enem_health_rects[i].height + 40))
					refresh.append(refresh_rect)
					i += 1
		   
		   
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
						if angle < 1.6 and angle >	1.15:
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
				dFrame = (464, 0, 58, 68)
				hero_invincible = False
				invincible_counter = 0
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
					
			for enem in self.room.enemies:
				self.screen.blit( self.enemySprites, (enem.getRect().x+enem.getxDev(),enem.getRect().y+enem.getyDev()), enem.getCurrentSprite()) 
			self.screen.blit( target, (target_Rect) )
			if self.talking:
				self.screen.blit( heroSprites, (hero_Rect.x,hero_Rect.y), talkFrame )
			else:
				if hero_invincible == True:
					if invincible_counter % 3 ==0:
						self.screen.blit( heroSprites, (hero_Rect.x,hero_Rect.y), dFrame )
				else:
					self.screen.blit( heroSprites, (hero_Rect.x,hero_Rect.y), dFrame )
			for NPC in self.room.NPCs:
				self.screen.blit( npcSprites, (NPC.getRect().x -2,NPC.getRect().y), NPC.getCurrentSprite(hero_Rect.x,hero_Rect.y))
			i = 0
			while i < 10:
				if arrowOn[i] == True:
					self.screen.blit( arrow[i], (arrow_rects[i]) )
				i += 1
			i = 0
			while i < 20:
				if enemy_projectiles[i] == True:
					#print("drawing!", i)
					self.screen.blit( projectile[i], (projectile_rects[i]) )
				i += 1
			if self.talking:
				if displayText is not None:
					txt = bestFont.render(displayText, True, (255,255,255))
					self.screen.blit(txt, (50, 600))
				else:
					self.setTalk(False)
			
			self.screen.blit(healthBar, (healthBar_Rect) )
			self.screen.blit(manaBar, (manaBar_Rect) )
			pygame.draw.rect(self.screen, (255, 0, 0), health_Rect, 0)
			pygame.draw.rect(self.screen, (0, 0, 255), mana_Rect, 0)
			
			# inventory stuff
			if inventoryOn == True:
				#print ( "inventoryOn", inventoryOn )
				self.screen.blit( inventory, (200, 30) )		#801, 441 (size of inventory image)
				self.screen.blit( texture_missing_upgrades, (550+200,22+30) )
				self.screen.blit( texture_missing_upgrades, (492+200,109+30) )
				self.screen.blit( texture_missing_upgrades, (608+200,109+30) )
				self.screen.blit( texture_missing_upgrades, (434+200,196+30) )
				self.screen.blit( texture_missing_upgrades, (550+200,196+30) )
				self.screen.blit( texture_missing_upgrades, (666+200,196+30) )
				self.screen.blit( texture_missing_upgrades, (376+200,283+30) )
				self.screen.blit( texture_missing_upgrades, (492+200,283+30) )
				self.screen.blit( texture_missing_upgrades, (608+200,283+30) )
				self.screen.blit( texture_missing_upgrades, (724+200,283+30) )
				self.screen.blit( texture_missing_upgrades, (376+200,370+30) )
				self.screen.blit( texture_missing_upgrades, (492+200,370+30) )
				self.screen.blit( texture_missing_upgrades, (608+200,370+30) )
				self.screen.blit( texture_missing_upgrades, (724+200,370+30) )
				upgrade_description = bestFont.render(description, True, (255,255,255))
				self.screen.blit(upgrade_description, (41+200,482+30))
				refresh.append(inventory.get_rect())
				if pygame.Rect((550+200,22+30), (57,57)).collidepoint( pygame.mouse.get_pos() ): #(1,1)
					if description != "train in archery":
						description = "train in archery"
						print( description )
				elif pygame.Rect((492+200,109+30), (57,57)).collidepoint( pygame.mouse.get_pos() ): #(2,1)
					if description != "train for AOE attack":
						description = "train for AOE attack"
						print( description )
				elif pygame.Rect((608+200,109+30), (57,57)).collidepoint( pygame.mouse.get_pos() ): #(2,2)
					if description != "train for big damage attack":
						description = "train for big damage attack"
						print( description )
				elif pygame.Rect((434+200,196+30), (57,57)).collidepoint( pygame.mouse.get_pos() ): #(3,1)
					if description != "increase radius":
						description = "increase radius"
						print( description )
				elif pygame.Rect((550+200,196+30), (57,57)).collidepoint( pygame.mouse.get_pos() ): #(3,2)
					if description != "increase speed":
						description = "increase speed"
						print( description )
				elif pygame.Rect((666+200,196+30), (57,57)).collidepoint( pygame.mouse.get_pos() ): #(3,3)
					if description != "increase attack":
						description = "increase attack"
						print( description )
				elif pygame.Rect((376+200,283+30), (57,57)).collidepoint( pygame.mouse.get_pos() ): #(4,1)
					if description != "increase attack":
						description = "increase attack"
						print( description )
				elif pygame.Rect((492+200,283+30), (57,57)).collidepoint( pygame.mouse.get_pos() ): #(4,2)
					if description != "increase radius":
						description = "increase radius"
						print( description )
				elif pygame.Rect((608+200,283+30), (57,57)).collidepoint( pygame.mouse.get_pos() ): #(4,3)
					if description != "increase attack":
						description = "increase attack"
						print( description )
				elif pygame.Rect((724+200,283+30), (57,57)).collidepoint( pygame.mouse.get_pos() ): #(4,4)
					if description != "increase speed":
						description = "increase speed"
						print( description )
				elif pygame.Rect((376+200,370+30), (57,57)).collidepoint( pygame.mouse.get_pos() ): #(5,1)
					if description != "increase attack":
						description = "increase attack"
						print( description )
				elif pygame.Rect((492+200,370+30), (57,57)).collidepoint( pygame.mouse.get_pos() ): #(5,2)
					if description != "full screen":
						description = "full screen"
						print( description )
				elif pygame.Rect((608+200,370+30), (57,57)).collidepoint( pygame.mouse.get_pos() ): #(5,3)
					if description != "increase attack":
						description = "increase attack"
						print( description )
				elif pygame.Rect((724+200,370+30), (57,57)).collidepoint( pygame.mouse.get_pos() ): #(5,4)
					if description != "increase default attack speed":
						description = "increase default attack speed"
						print( description )
				 
				
				
			
			pygame.display.update( refresh )
		   
			refresh = []
			
			#hero invincible timer
			if hero_invincible == True:
				invincible_counter += 1
				if invincible_counter == 60:
					print("resetting invincibility")
					hero_invincible = False
					invincible_counter = 0

			
			#Room transitions
			if hero_Rect.x > self.width or hero_Rect.x < 0 or hero_Rect.y > self.height or hero_Rect.y < 0:
				arrow = [arrowLoadImage, arrowLoadImage, arrowLoadImage, arrowLoadImage, arrowLoadImage, arrowLoadImage, arrowLoadImage, arrowLoadImage, arrowLoadImage, arrowLoadImage]
				arrow_rects = [arrow[0].get_rect(),arrow[1].get_rect(),arrow[2].get_rect(),arrow[3].get_rect(),arrow[4].get_rect(),arrow[5].get_rect(),arrow[6].get_rect(),arrow[7].get_rect(),arrow[8].get_rect(),arrow[9].get_rect()]
				arrow_posX = [-500]*10
				arrow_posY = [-500]*10
				
				arrowSpeedX = [0,0,0,0,0,0,0,0,0,0]
				arrowSpeedY = [0,0,0,0,0,0,0,0,0,0]
				arrownum = 0
				while i < 10:
					arrowOn[i] = False
				thismusic = self.room.music
				print "ROOM before: ", self.roomNum
				roomCache = self.roomNum
				self.roomNum = self.room.judge(hero_Rect)
				
				#next rooms
				if self.roomNum == 99:
					if self.state == "main":
						self.state = "main1"
					elif self.state == "main1":
						self.state = "main2"
					hero_Rect.x = 60
					self.roomNum = 0
					self.setState()
					self.setUpRooms()
					self.room = self.rooms[0]
					self.reset()
					pygame.display.update()
					self.winVar = False
					self.checkAvoid = True
					
				print "ROOM: ", self.roomNum
				self.setState()
				self.reset()
				if roomCache != self.roomNum:
					pygame.display.update()
				
				wall_Rects = []
				rock_Rects = []
				if self.room.rock != None:
					for i in range(len(self.room.rockx)):
						rock_Rect = self.room.rock.get_rect().move(self.room.rockx[i], self.room.rocky[i])
						rock_Rects.append(rock_Rect)
				for wall in self.room.walls:
					wall_Rects.append(wall)
				if self.checkAvoid:
					self.checkAvoid = False
				else:
					hero_Rect = self.room.checkroom(hero_Rect)
				
				if thismusic != self.room.music:
					pygame.mixer.music.load(self.room.music)
					pygame.mixer.music.play(-1,0)
			  
	   
			self.clock.tick(30)
