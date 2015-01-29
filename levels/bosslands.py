#Edo frikin KUN
#1/22/2015
#

import agent, room, pygame, random as ra

def gatherRooms(screen, width, height, sprites):
	return [bossland0(screen, width, height, sprites), bossland1(screen, width, height, sprites), bossland2(screen, width, height, sprites), bossland3(screen, width, height, sprites),
			bossland4(screen, width, height, sprites), bossland5(screen, width, height, sprites), bossland6(screen, width, height, sprites), bossland7(screen, width, height, sprites), 
			bossland8(screen, width, height, sprites)]
class bossland0:		   
	def __init__ (self, screen, width, height, sprites):
		self.identity = 0
		self.screen= screen
		
		self.music= "sounds/BKGmusic/ForestCreepy/Clovewood.wav"
		
		self.width = width
		self.height = height
		self.background = sprites[0]
		self.wallSprites = sprites[1]
		self.enemySprites = sprites[2]
		self.cave = sprites[3]
		self.walls = [pygame.Rect(0, 0, 1200, 50), pygame.Rect(0, 50, 50, 600), pygame.Rect(0, 650, 1200, 50)]
		self.rock = None
		self.rockx= []
		self.rocky= []
		
		rockBro = agent.HelpRock(150, 50)
		rockBro1 = agent.HelpRock(200, 50)
		rockBro.setMessage(["[Rock Twat]: Congratulation! You've slain that infernal winged beast!","[Rock Twat]: Now go complete your quest ya scrub."])
		rockBro1.setMessage(["[Rocky Balboa]: You like what you see?","[Rocky Balboa]: These rock hard abs didn't come to be from sitting around all day", "[Rocky Balboa]: .... Oh wait...."])
		self.NPCs = [rockBro, rockBro1]

		
		#Add DA enemies HERE
		self.frameCounter = -1
		#hitbox note: subtract double of |dev| from respective x, y -- width and height of rect

		self.enemies = [agent.Squirrel((self.width*ra.uniform(0.1, 0.9), self.height*ra.uniform(0.2, 0.8))),
						agent.Squirrel((self.width*ra.uniform(0.1, 0.9), self.height*ra.uniform(0.2, 0.8))),
						agent.Squirrel((self.width*ra.uniform(0.1, 0.9), self.height*ra.uniform(0.2, 0.8))),
						agent.Squirrel((self.width*ra.uniform(0.1, 0.9), self.height*ra.uniform(0.2, 0.8)))]
		
	def reset(self):
		self.screen.fill((90,0,0))
		self.screen.blit( self.background, (0,0) )
		self.screen.blit( self.background, (self.height,0) )
		#draw on top of the background
		self.screen.blit( self.wallSprites, (0,0), (0, 0, 1200, 85) )
		self.screen.blit( self.cave, (0, 85), (0, 0, 50, 600))
		self.screen.blit( self.wallSprites, (0, 650), (0, 892, 1200, 50)  )
		
	def checkroom(self,hero_Rect):
		print "room0"
		return pygame.Rect(self.width - 60, hero_Rect.y, 58, 68)

	def judge(self, hero_Rect):
		if hero_Rect.x > 0:
			return 1
			
class bossland1:		   
	def __init__ (self, screen, width, height, sprites):
		self.identity = 1
		self.screen= screen
		
		self.music= "sounds/BKGmusic/ForestCreepy/Clovewood.wav"
		
		self.width = width
		self.height = height
		self.background = sprites[0]
		self.wallSprites = sprites[1]
		self.enemySprites = sprites[2]
		self.cave = sprites[3]
		self.walls = [pygame.Rect(0, 0, 1200, 50), pygame.Rect(0, 650, 1200, 50)]
		self.rock = None
		self.rockx= []
		self.rocky= []
		
		self.NPCs = []

		
		#Add DA enemies HERE
		self.frameCounter = -1
		#hitbox note: subtract double of |dev| from respective x, y -- width and height of rect

		self.enemies = [agent.Squirrel((self.width*ra.uniform(0.1, 0.9), self.height*ra.uniform(0.2, 0.8))),
						agent.Squirrel((self.width*ra.uniform(0.1, 0.9), self.height*ra.uniform(0.2, 0.8))),
						agent.Squirrel((self.width*ra.uniform(0.1, 0.9), self.height*ra.uniform(0.2, 0.8))),
						agent.Squirrel((self.width*ra.uniform(0.1, 0.9), self.height*ra.uniform(0.2, 0.8)))]
		
	def reset(self):
		self.screen.fill((90,0,0))
		self.screen.blit( self.background, (0,0) )
		self.screen.blit( self.background, (self.height,0) )
		#draw on top of the background
		self.screen.blit( self.wallSprites, (0,0), (0, 0, 1200, 85) )
		self.screen.blit( self.wallSprites, (0, 650), (0, 892, 1200, 50)  )
		
	def checkroom(self,hero_Rect):
		print "room1"
		if hero_Rect.x < 0:
			return pygame.Rect(self.width - 60, hero_Rect.y, 58, 68)
		else:
			return pygame.Rect(2, hero_Rect.y,58,68)

	def judge(self, hero_Rect):
		if hero_Rect.x > 0:
			return 2
		else:
			return 0
			
class bossland2:		   
	def __init__ (self, screen, width, height, sprites):
		self.identity = 2
		self.screen= screen
		
		self.music= "sounds/BKGmusic/ForestCreepy/Clovewood.wav"
		
		self.width = width
		self.height = height
		self.background = sprites[0]
		self.wallSprites = sprites[1]
		self.enemySprites = sprites[2]
		self.walls = [pygame.Rect(0, 0, 1200, 50),  pygame.Rect(1150, 50, 50, 600), pygame.Rect(0, 650, 445, 50), pygame.Rect(675, 650, 525, 50)]
		self.rock = None
		self.rockx= []
		self.rocky= []
		self.NPCs = []

		#Add DA enemies HERE
		self.frameCounter = -1

		self.enemies = [agent.Squirrel((self.width*ra.uniform(0.1, 0.9), self.height*ra.uniform(0.2, 0.8))),
						agent.Squirrel((self.width*ra.uniform(0.1, 0.9), self.height*ra.uniform(0.2, 0.8))),
						agent.Squirrel((self.width*ra.uniform(0.1, 0.9), self.height*ra.uniform(0.2, 0.8))),
						agent.Squirrel((self.width*ra.uniform(0.1, 0.9), self.height*ra.uniform(0.2, 0.8))),
						agent.Squirrel((self.width*ra.uniform(0.1, 0.9), self.height*ra.uniform(0.2, 0.8))),
						agent.Squirrel((self.width*ra.uniform(0.1, 0.9), self.height*ra.uniform(0.2, 0.8))),
						agent.Squirrel((self.width*ra.uniform(0.1, 0.9), self.height*ra.uniform(0.2, 0.8))),
						agent.Voodoo((self.width*ra.uniform(0.1, 0.9), self.height*ra.uniform(0.2, 0.8)))]
	
	def reset(self):
		self.screen.fill((90,0,0))
		self.screen.blit( self.background, (0,0) )
		self.screen.blit( self.background, (self.height,0) )
		#draw on top of the background
		self.screen.blit( self.wallSprites, (0,0), (0, 0, 1200, 85) )
		self.screen.blit( self.wallSprites, (1150, 0), (1100, 170, 50, 700)  )
		self.screen.blit( self.wallSprites, (0,650), (55, 895, 445, 50))
		self.screen.blit( self.wallSprites, (675,650), (635, 895, 525, 50))
		
	def checkroom(self,hero_Rect):
		print "room2"
		if hero_Rect.x > self.width:
			return pygame.Rect(2, hero_Rect.y, 58, 68)
		else:
			return pygame.Rect(hero_Rect.x, self.height-70, 58, 68)


			
	def judge(self, hero_Rect):
		if hero_Rect.x < 0:
			return 1
		else:
			return 3
		
class bossland3:		   
	def __init__ (self, screen, width, height, sprites):
		self.identity = 3
		self.screen= screen
		
		self.music= "sounds/BKGmusic/ForestCreepy/Clovewood.wav"
		
		self.width = width
		self.height = height
		self.background = sprites[0]
		self.wallSprites = sprites[1]
		self.enemySprites = sprites[2]
		self.walls = [pygame.Rect(0, 0, 445, 50), pygame.Rect(675, 0, 525, 50),pygame.Rect(0, 0, 50, 700), pygame.Rect(1150, 0, 50, 700),pygame.Rect(0, 650, 445, 50), pygame.Rect(675, 650, 525, 50)]
		self.rock = None
		self.rockx= []
		self.rocky= []
		self.NPCs = []

		#Add DA enemies HERE
		self.frameCounter = -1

		self.enemies = [agent.Voodoo((self.width*ra.uniform(0.1, 0.9), self.height*ra.uniform(0.2, 0.8))),
						agent.Squirrel((self.width*ra.uniform(0.1, 0.9), self.height*ra.uniform(0.2, 0.8))),
						agent.Squirrel((self.width*ra.uniform(0.1, 0.9), self.height*ra.uniform(0.2, 0.8)))]
		
	def reset(self):
		self.screen.fill((90,0,0))
		self.screen.blit( self.background, (0,0) )
		self.screen.blit( self.background, (self.height,0) )
		#draw on top of the background
		self.screen.blit(self.wallSprites, (0,0), (0, 90, 445, 77))
		self.screen.blit(self.wallSprites, (675,0), (675, 90, 525, 77))
		self.screen.blit( self.wallSprites, (0,0), (55, 170, 50, 700))
		self.screen.blit( self.wallSprites, (1150, 0), (1100, 170, 50, 700))
		self.screen.blit( self.wallSprites, (0,650), (55, 895, 445, 50))
		self.screen.blit( self.wallSprites, (675,650), (635, 895, 525, 50))
		
	def checkroom(self,hero_Rect):
		print "room3"
		if hero_Rect.y < 0:
			return pygame.Rect(hero_Rect.x, self.height-70, 58, 68)
		else:
			return pygame.Rect(hero_Rect.x, 2, 58, 68)
			
	def judge(self, hero_Rect):
		if hero_Rect.y < 0:
			return 2
		else:
			return 4
			
class bossland4:		   
	def __init__ (self, screen, width, height, sprites):
		self.identity = 4
		self.screen= screen
		
		self.music= "sounds/BKGmusic/ForestCreepy/Clovewood.wav"
		
		self.width = width
		self.height = height
		self.background = sprites[0]
		self.wallSprites = sprites[1]
		self.enemySprites = sprites[2]
		self.walls = [pygame.Rect(0, 0, 445, 50), pygame.Rect(675, 0, 525, 50),pygame.Rect(0, 0, 50, 700), pygame.Rect(1150, 0, 50, 700),pygame.Rect(0, 650, 445, 50), pygame.Rect(675, 650, 525, 50)]
		self.rock = None
		self.rockx= []
		self.rocky= []
		self.NPCs = []

		#Add DA enemies HERE
		self.frameCounter = -1

		self.enemies = [agent.Voodoo((self.width*ra.uniform(0.1, 0.9), self.height*ra.uniform(0.2, 0.8))),
						agent.Squirrel((self.width*ra.uniform(0.1, 0.9), self.height*ra.uniform(0.2, 0.8))),
						agent.Squirrel((self.width*ra.uniform(0.1, 0.9), self.height*ra.uniform(0.2, 0.8)))]
		
	def reset(self):
		self.screen.fill((90,0,0))
		self.screen.blit( self.background, (0,0) )
		self.screen.blit( self.background, (self.height,0) )
		#draw on top of the background
		self.screen.blit(self.wallSprites, (0,0), (0, 90, 445, 77))
		self.screen.blit(self.wallSprites, (675,0), (675, 90, 525, 77))
		self.screen.blit( self.wallSprites, (0,0), (55, 170, 50, 700))
		self.screen.blit( self.wallSprites, (1150, 0), (1100, 170, 50, 700))
		self.screen.blit( self.wallSprites, (0,650), (55, 895, 445, 50))
		self.screen.blit( self.wallSprites, (675,650), (635, 895, 525, 50))
		
	def checkroom(self,hero_Rect):
		print "room4"
		if hero_Rect.y < 0:
			return pygame.Rect(hero_Rect.x, self.height-70, 58, 68)
		else:
			return pygame.Rect(hero_Rect.x, 2, 58, 68)
			
	def judge(self, hero_Rect):
		if hero_Rect.y < 0:
			return 3
		else:
			return 5
			
class bossland5:		   
	def __init__ (self, screen, width, height, sprites):
		self.themayor = agent.Mayor((581,320))
		self.identity = 5
		self.screen= screen
		
		self.music= "sounds/BKGmusic/ForestCreepy/Clovewood.wav"
		
		self.width = width
		self.height = height
		self.background = sprites[0]
		self.wallSprites = sprites[1]
		self.enemySprites = sprites[2]
		self.walls = [pygame.Rect(0, 0, 445, 50), pygame.Rect(675, 0, 525, 50), pygame.Rect(0, 650, 50, 50), pygame.Rect(1150, 650, 50, 50)]
		self.rock = None
		self.rockx= []
		self.rocky= []
		self.final = False
		self.finalInit = False
		self.finalCounter = 120
		self.shieldCounter = 0
		rockBro = agent.HelpRock(590,330)
		rockBro.setMessage(["[Stone Guardian]: 3 paths... 3 guardians..."])
		
		self.NPCs = [rockBro]

		#Add DA enemies HERE
		self.frameCounter = -1
		#hitbox note: subtract double of |dev| from respective x, y -- width and height of rect
		self.enemies = [agent.Squirrel((self.width*ra.uniform(0.1, 0.9), self.height*ra.uniform(0.2, 0.8)))]
		
	def activateFinal(self):
		self.final = True
	def initFight(self):
		self.finalInit = True
	def bossDead(self):
		return self.enemies[0].isDead()
			
		
	def reset(self):
		self.screen.fill((90,0,0))
		self.screen.blit( self.background, (0,0) )
		self.screen.blit( self.background, (self.height,0) )
		#final battlearu
		if self.final:
			self.walls.append(pygame.Rect(0, 0, 20, 700))
			self.walls.append(pygame.Rect(1199, 0, 1, 700))
			self.walls.append(pygame.Rect(0,0,1200,30))
			self.walls.append(pygame.Rect(0,699,1200,1))
			self.music= "sounds/BKGmusic/BeachBoss/IWillNotDie.wav"
			drag1=agent.TreeBeard((450,100))
			drag2=agent.TreeBeard((636,100))
			drag3=agent.Dragon((600,150))
			drag1.setAggro(False)
			drag2.setAggro(False)
			drag3.setAggro(False)
			self.enemies = [self.themayor, agent.Shield(self.themayor.Rect), drag1, drag2, drag3]
			self.NPCs = []
			self.final = False
		if self.finalInit:
			for enem in self.enemies:
				enem.setAggro(True)
			if not self.enemies[0].isDead():
				self.finalCounter += 1
				if self.finalCounter > 60:
					self.finalCounter = 0
					color = ["brown", "green", "pink"]
					self.enemies.append(agent.Slime((self.width*ra.uniform(0.1, 0.9), self.height*ra.uniform(0.2, 0.8)),True, 5, color[ra.randrange(0,3,1)]))
				if self.enemies[1].isDead():
					self.shieldCounter += 1
					if self.shieldCounter > 120:
						self.enemies[1].ressurect(True,self.themayor.Rect)
						self.shieldCounter = 0
			
		#draw on top of the background
		self.screen.blit(self.wallSprites, (0,0), (0, 90, 445, 77))
		self.screen.blit(self.wallSprites, (675,0), (675, 90, 525, 77))
		self.screen.blit( self.wallSprites, (0, 650), (200, 170, 50, 50)  )
		self.screen.blit( self.wallSprites, (1150,650), (160, 170, 50, 50))
		
	def checkroom(self,hero_Rect):
		print "room5"
		if hero_Rect.x > self.width:
			return pygame.Rect(2, hero_Rect.y, 58, 68)
		elif hero_Rect.x < 0:
			return pygame.Rect(self.width-60, hero_Rect.y, 58, 68)
		elif hero_Rect.y < 0:
			return pygame.Rect(hero_Rect.x, self.height-70, 58, 68)
		else:
			return pygame.Rect(hero_Rect.x, 2, 58, 68)
			
	def judge(self, hero_Rect):
		if hero_Rect.x > self.width:
			return 7
		elif hero_Rect.x < 0:
			return 6
		elif hero_Rect.y < 0:
			return 4
		else:
			return 8
			
class bossland6:		   
	def __init__ (self, screen, width, height, sprites):
		self.identity = 6
		self.screen= screen
		
		self.music= "sounds/BKGmusic/ForestCreepy/Clovewood.wav"
		
		self.width = width
		self.height = height
		self.background = sprites[0]
		self.wallSprites = sprites[1]
		self.enemySprites = sprites[2]
		self.cave = sprites[3]
		self.walls = [pygame.Rect(0, 0, 1200, 50), pygame.Rect(0, 50, 50, 600), pygame.Rect(0, 650, 1200, 50)]
		self.rock = None
		self.rockx= []
		self.rocky= []
		
		self.NPCs = []

		
		#Add DA enemies HERE
		self.frameCounter = -1
		#hitbox note: subtract double of |dev| from respective x, y -- width and height of rect

		self.enemies = [agent.Squirrel((self.width*ra.uniform(0.1, 0.9), self.height*ra.uniform(0.2, 0.8))),
						agent.Squirrel((self.width*ra.uniform(0.1, 0.9), self.height*ra.uniform(0.2, 0.8))),
						agent.Squirrel((self.width*ra.uniform(0.1, 0.9), self.height*ra.uniform(0.2, 0.8))),
						agent.Squirrel((self.width*ra.uniform(0.1, 0.9), self.height*ra.uniform(0.2, 0.8))),
						agent.TreeBeard((50, 250))]
						
	def bossDead(self):
		return self.enemies[-1].isDead()
		
	def reset(self):
		self.screen.fill((90,0,0))
		self.screen.blit( self.background, (0,0) )
		self.screen.blit( self.background, (self.height,0) )
		#draw on top of the background
		self.screen.blit( self.wallSprites, (0,0), (0, 0, 1200, 85) )
		self.screen.blit( self.wallSprites, (0,0), (55, 170, 50, 700))
		self.screen.blit( self.wallSprites, (0, 650), (0, 892, 1200, 50)  )
		
	def checkroom(self,hero_Rect):
		print "room6"
		return pygame.Rect(self.width - 60, hero_Rect.y, 58, 68)

	def judge(self, hero_Rect):
		if hero_Rect.x > 0:
			return 5
			
class bossland7:		   
	def __init__ (self, screen, width, height, sprites):
		self.identity = 7
		self.screen= screen
		
		self.music= "sounds/BKGmusic/ForestCreepy/Clovewood.wav"
		
		self.width = width
		self.height = height
		self.background = sprites[0]
		self.wallSprites = sprites[1]
		self.enemySprites = sprites[2]
		self.walls = [pygame.Rect(0, 0, 1200, 50), pygame.Rect(1150, 50, 50, 600), pygame.Rect(0, 650, 1200, 50)]
		self.rock = None
		self.rockx= []
		self.rocky= []
		
		self.NPCs = []

		#Add DA enemies HERE
		self.frameCounter = -1

		self.enemies = [agent.Deer((self.width*ra.uniform(0.1, 0.9), self.height*ra.uniform(0.2, 0.8))),
						agent.Deer((self.width*ra.uniform(0.1, 0.9), self.height*ra.uniform(0.2, 0.8))),
						agent.Deer((self.width*ra.uniform(0.1, 0.9), self.height*ra.uniform(0.2, 0.8))),
						agent.TreeBeard((950, 250))]
	def bossDead(self):
		return self.enemies[-1].isDead()
		
	def reset(self):
		self.screen.fill((90,0,0))
		self.screen.blit( self.background, (0,0) )
		self.screen.blit( self.background, (self.height,0) )
		#draw on top of the background
		self.screen.blit( self.wallSprites, (0,0), (0, 0, 1200, 85) )
		self.screen.blit( self.wallSprites, (1150, 0), (1100, 170, 50, 700))
		self.screen.blit( self.wallSprites, (0, 650), (0, 892, 1200, 50)  )
			
			
		
	def checkroom(self,hero_Rect):
		print "room7"
		return pygame.Rect(2, hero_Rect.y, 58, 68)

	def judge(self, hero_Rect):
		return 5
			
class bossland8:		   
	def __init__ (self, screen, width, height, sprites):
		self.identity = 8
		self.screen= screen
		
		self.music= "sounds/BKGmusic/ForestCreepy/Clovewood.wav"
		
		self.width = width
		self.height = height
		self.background = sprites[0]
		self.wallSprites = sprites[1]
		self.enemySprites = sprites[2]
		self.walls = [pygame.Rect(0, 0, 50, 700), pygame.Rect(1150, 0, 50, 700),  pygame.Rect(0, 650, 1200, 50)]
		self.rock = None
		self.rockx= []
		self.rocky= []
		self.NPCs =[]

		#Add DA enemies HERE
		self.frameCounter = -1
		
		self.enemies = [agent.Squirrel((self.width*ra.uniform(0.1, 0.9), self.height*ra.uniform(0.2, 0.8))),
						agent.Squirrel((self.width*ra.uniform(0.1, 0.9), self.height*ra.uniform(0.2, 0.8))),
						agent.Squirrel((self.width*ra.uniform(0.1, 0.9), self.height*ra.uniform(0.2, 0.8))),
						agent.Squirrel((self.width*ra.uniform(0.1, 0.9), self.height*ra.uniform(0.2, 0.8))),
						agent.Squirrel((self.width*ra.uniform(0.1, 0.9), self.height*ra.uniform(0.2, 0.8))),
						agent.Squirrel((self.width*ra.uniform(0.1, 0.9), self.height*ra.uniform(0.2, 0.8))),
						agent.Voodoo((self.width*ra.uniform(0.1, 0.9), self.height*ra.uniform(0.2, 0.8))),
						agent.TreeBeard((450, 250))]
	#special method
	def bossDead(self):
		return self.enemies[-1].isDead()
		
	def reset(self):
		self.screen.fill((90,0,0))
		self.screen.blit( self.background, (0,0) )
		self.screen.blit( self.background, (self.height,0) )
		#draw on top of the background
		self.screen.blit( self.wallSprites, (0,0), (55, 170, 50, 700))
		self.screen.blit( self.wallSprites, (1150, 0), (1100, 170, 50, 700))
		self.screen.blit( self.wallSprites, (0, 650), (0, 892, 1200, 50))
		
	def checkroom(self,hero_Rect):
		print "room8"
		return pygame.Rect(hero_Rect.x, 2, 58, 68)
			

	def judge(self, hero_Rect):
		return 5
