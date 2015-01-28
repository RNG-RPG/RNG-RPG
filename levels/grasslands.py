#Edo frikin KUN
#1/19/2015
#

import agent, room, pygame, random as ra
def gatherRooms(screen, width, height, sprites):
	return [grassland0(screen, width, height, sprites), grassland1(screen, width, height, sprites), grassland2(screen, width, height, sprites), grassland3(screen, width, height, sprites),
			grassland4(screen, width, height, sprites), grassland5(screen, width, height, sprites), grassland6(screen, width, height, sprites), grassland7(screen, width, height, sprites), 
			grassland8(screen, width, height, sprites), grassland9(screen, width, height, sprites), grassland10(screen, width, height, sprites), grassland11(screen, width, height, sprites), 
			grassland12(screen, width, height, sprites)]
'''sprites are in this format: background, walls, enemies, anything extra'''
class grassland0:		   
	def __init__ (self, screen, width, height, sprites):
		self.identity = 0
		self.screen= screen
		
		self.music= "sounds/BKGmusic/Forest/FollowTheLeaf.wav"
		
		self.width = width
		self.height = height
		self.background = sprites[0]
		self.wallSprites = sprites[1]
		self.enemySprites = sprites[2]
		self.walls = [pygame.Rect(0, 0, 1200, 50), pygame.Rect(0, 50, 50, 600), pygame.Rect(0, 650, 1200, 50)]
		self.rock = None
		self.rockx= []
		self.rocky= []
		
		rockBro = agent.HelpRock(150, 50)
		rockBro1 = agent.HelpRock(500, 600)
		rockBro.setMessage(["[Rock]: I'm a talking rock~ ","[Rock]: You should bump into my friends to see what they have to say!", "You can also hit escape to quit the game whenever you want! (But who would want to do that?)",
				"O! I almost forgot! You better not go west... Nothing interesting is over there!"])
		rockBro1.setMessage(["[Rock Bro]: Cleanse this land of your enemies... or perish... (P.S. Rockbros are not your enemy)"])
		self.NPCs = [rockBro, rockBro1]

		
		#Add DA enemies HERE
		self.frameCounter = -1
		#hitbox note: subtract double of |dev| from respective x, y -- width and height of rect

		self.enemies = [agent.Squirrel((900,200)),agent.Squirrel((850,200)), agent.Deer((555,555))]

	def reset(self):
		self.screen.fill((90,0,0))
		self.screen.blit( self.background, (0,0) )
		self.screen.blit( self.background, (self.height,0) )
		#draw on top of the background
		self.screen.blit( self.wallSprites, (0,0), (0, 0, 1200, 85) )
		self.screen.blit( self.wallSprites, (0, 650), (0, 892, 1200, 50)  )
		
	def checkroom(self,hero_Rect):
		print "room0"
		return pygame.Rect(self.width - 60, hero_Rect.y, 58, 68)

	def judge(self, hero_Rect):
		if hero_Rect.x > 0:
			return 1
			
class grassland1:		   
	def __init__ (self, screen, width, height, sprites):
		self.identity = 1
		self.screen= screen
		
		self.music= "sounds/BKGmusic/Forest/FollowTheLeaf.wav"
		
		self.width = width
		self.height = height
		self.background = sprites[0]
		self.wallSprites = sprites[1]
		self.enemySprites = sprites[2]
		self.walls = [pygame.Rect(0, 0, 50, 50), pygame.Rect(0, 650, 50, 50)]
		self.rock = None
		self.rockx= []
		self.rocky= []
		rockBro = agent.HelpRock(580,270)
		rockBro.setMessage(["I hear strange monsters roam these parts of the woods...", "Best to not get too friendly..."])
		
		self.NPCs = [rockBro]

		#Add DA enemies HERE
		self.frameCounter = -1
		#hitbox note: subtract double of |dev| from respective x, y -- width and height of rect
		self.enemies = [agent.Squirrel((600,300))]
		
	def reset(self):
		self.screen.fill((90,0,0))
		self.screen.blit( self.background, (0,0) )
		self.screen.blit( self.background, (self.height,0) )
		#draw on top of the background
		self.screen.blit( self.wallSprites, (0,0), (215, 285, 100, 85) )
		self.screen.blit( self.wallSprites, (0, 650), (200, 170, 50, 50)  )
		
	def checkroom(self,hero_Rect):
		print "room1"
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
			return 0
		elif hero_Rect.y < 0:
			return 2
		else:
			return 3
			
class grassland2:		   
	def __init__ (self, screen, width, height, sprites):
		self.identity = 2
		self.screen= screen
		
		self.music= "sounds/BKGmusic/Forest/FollowTheLeaf.wav"
		
		self.width = width
		self.height = height
		self.background = sprites[0]
		self.wallSprites = sprites[1]
		self.enemySprites = sprites[2]
		self.walls = [pygame.Rect(0, 0, 1200, 50), pygame.Rect(0, 50, 50, 650)]
		self.rock = None
		self.rockx= []
		self.rocky= []
		self.NPCs = []

		#Add DA enemies HERE
		self.frameCounter = -1
		#hitbox note: subtract double of |dev| from respective x, y -- width and height of rect

		self.enemies = [agent.Squirrel((600,500)),agent.Squirrel((600,300))]
		
	def reset(self):
		self.screen.fill((90,0,0))
		self.screen.blit( self.background, (0,0) )
		self.screen.blit( self.background, (self.height,0) )
		#draw on top of the background
		self.screen.blit( self.wallSprites, (0,0), (0, 0, 1200, 85) )
		self.screen.blit( self.wallSprites, (0, 0), (55, 170, 50, 700)  )
		
	def checkroom(self,hero_Rect):
		print "room2"
		if hero_Rect.x < 0:
			return pygame.Rect(self.width-60, hero_Rect.y, 58, 68)
		else:
			return pygame.Rect(hero_Rect.x, self.height-70, 58, 68)    
			
	def judge(self, hero_Rect):
		if hero_Rect.x > self.width:
			return 8
		else:
			return 1

class grassland3:		   
	def __init__ (self, screen, width, height, sprites):
		self.identity = 3
		self.screen= screen
		
		self.music= "sounds/BKGmusic/Forest/FollowTheLeaf.wav"
		
		self.width = width
		self.height = height
		self.background = sprites[0]
		self.wallSprites = sprites[1]
		self.enemySprites = sprites[2]
		self.walls = [pygame.Rect(0,0, 50, 700), pygame.Rect(1150,650, 50, 50)]
		self.rock = None
		self.rockx= []
		self.rocky= []
		self.NPCs = []

		#Add DA enemies HERE
		self.frameCounter = -1

		self.enemies = [agent.Squirrel((50,500)),agent.Squirrel((800,400))]
		
	def reset(self):
		self.screen.fill((90,0,0))
		self.screen.blit( self.background, (0,0) )
		self.screen.blit( self.background, (self.height,0) )
		#draw on top of the background
		self.screen.blit( self.wallSprites, (0,0), (55, 170, 50, 700))
		self.screen.blit( self.wallSprites, (1150,650), (163, 170, 50, 50))
		
	def checkroom(self,hero_Rect):
		print "room3"
		if hero_Rect.x < 0:
			return pygame.Rect(self.width-60, hero_Rect.y, 58, 68)
		elif hero_Rect.y < 0:
			return pygame.Rect(hero_Rect.x, self.height-70, 58, 68)
		else:
			return pygame.Rect(hero_Rect.x, 2, 58, 68)
			
	def judge(self, hero_Rect):
		print "room3"
		if hero_Rect.x > self.width:
			return 6
		elif hero_Rect.y < 0:
			return 1
		else:
			return 4

class grassland4:		   
	def __init__ (self, screen, width, height, sprites):
		self.identity = 4
		self.screen= screen
		
		self.music= "sounds/BKGmusic/Forest/FollowTheLeaf.wav"
		
		self.width = width
		self.height = height
		self.background = sprites[0]
		self.wallSprites = sprites[1]
		self.enemySprites = sprites[2]
		self.walls = [pygame.Rect(0, 0, 50, 700), pygame.Rect(1150, 0, 50, 700)]
		self.rock = None
		self.rockx= []
		self.rocky= []
		self.NPCs = []

		#Add DA enemies HERE
		self.frameCounter = -1
		
		self.enemies = [agent.Squirrel((600,325)),agent.Squirrel((400,650))]
		
	def reset(self):
		self.screen.fill((90,0,0))
		self.screen.blit( self.background, (0,0) )
		self.screen.blit( self.background, (self.height,0) )
		#draw on top of the background
		self.screen.blit( self.wallSprites, (0,0), (55, 170, 50, 700))
		self.screen.blit( self.wallSprites, (1150, 0), (1100, 170, 50, 700)  )
		
	def checkroom(self,hero_Rect):
		print "room4"
		if hero_Rect.y < 0:
			return pygame.Rect(hero_Rect.x, self.height-70, 58, 68)
		else:
			return pygame.Rect(hero_Rect.x, 2, 58, 68)
			

	def judge(self, hero_Rect):
		if hero_Rect.y > 0:
			return 5
		else:
			return 3

class grassland5:		   
	def __init__ (self, screen, width, height, sprites):
		self.identity = 5
		self.screen= screen
		
		self.music= "sounds/BKGmusic/Forest/FollowTheLeaf.wav"
		
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
		
		self.enemies = [agent.Squirrel((300,600)),agent.Squirrel((400,610)),agent.Squirrel((500,620)),agent.Squirrel((700,620)),
						agent.Squirrel((800,610)),agent.Squirrel((900,600)),agent.Slime((self.width*ra.uniform(0.1, 0.9), self.height*ra.uniform(0.2, 0.8)), True, 5, "green"),
						agent.Voodoo(((600,640)))]
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
		print "room5"
		return pygame.Rect(hero_Rect.x, 2, 58, 68)
			

	def judge(self, hero_Rect):
		return 4

class grassland6:		   
	def __init__ (self, screen, width, height, sprites):
		self.identity = 6
		self.screen= screen
		
		self.music= "sounds/BKGmusic/Forest/FollowTheLeaf.wav"
		
		self.width = width
		self.height = height
		self.background = sprites[0]
		self.wallSprites = sprites[1]
		self.enemySprites = sprites[2]
		self.walls = [pygame.Rect(0, 650, 1200, 50), pygame.Rect(1150, 0, 50, 700)]
		self.rock = None
		self.rockx= []
		self.rocky= []
		self.NPCs = []
		
		#Add DA enemies HERE
		self.frameCounter = -1    

		self.enemies = [agent.Squirrel((800,400))]
		
	def reset(self):
		self.screen.fill((90,0,0))
		self.screen.blit( self.background, (0,0) )
		self.screen.blit( self.background, (self.height,0) )
		#draw on top of the background
		self.screen.blit( self.wallSprites, (1150, 0), (1100, 170, 50, 700)  )
		self.screen.blit( self.wallSprites, (0, 650), (0, 892, 1200, 50)  )
		
	def checkroom(self,hero_Rect):
		print "room6"
		if hero_Rect.y > self.height:
			return pygame.Rect(hero_Rect.x, 2, 58, 68)
		else:
			return pygame.Rect(2, hero_Rect.y, 58, 68)
			

	def judge(self, hero_Rect):
		if hero_Rect.y < 0:
			return 7
		else:
			return 3

class grassland7:		   
	def __init__ (self, screen, width, height, sprites):
		self.identity = 7
		self.screen= screen
		
		self.music= "sounds/BKGmusic/Forest/FollowTheLeaf.wav"
		
		self.width = width
		self.height = height
		self.background = sprites[0]
		self.wallSprites = sprites[1]
		self.enemySprites = sprites[2]
		self.walls = [pygame.Rect(1150,650, 50, 50)]
		self.rock = None
		self.rockx= []
		self.rocky= []
		girl = agent.LostGirl(581, 320)
		girl.setMessage(["[???]: All of the squirrels are flying!", "[???]: I wonder if there is a reason."])
		self.NPCs = [girl]

		#Add DA enemies HERE
		self.frameCounter = -1

		self.enemies = []
		
	# special event method
	def setNPC(self, message):
		self.NPCs[0].setMessage(message)
	def reset(self):
		self.screen.fill((90,0,0))
		self.screen.blit( self.background, (0,0) )
		self.screen.blit( self.background, (self.height,0) )
		#draw on top of the background
		self.screen.blit( self.wallSprites, (1150,650), (163, 170, 50, 50))
		
	def checkroom(self,hero_Rect):
		print "room7"
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
			return 11
		elif hero_Rect.x < 0:
			return 1
		elif hero_Rect.y < 0:
			return 8
		else:
			return 6
			
class grassland8:		   
	def __init__ (self, screen, width, height, sprites):
		self.identity = 8
		self.screen= screen
		
		self.music= "sounds/BKGmusic/Forest/FollowTheLeaf.wav"
		
		self.width = width
		self.height = height
		self.background = sprites[0]
		self.wallSprites = sprites[1]
		self.enemySprites = sprites[2]
		self.walls = [pygame.Rect(0, 0, 445, 50), pygame.Rect(675, 0, 525, 50)]
		self.rock = None
		self.rockx= []
		self.rocky= []
		self.NPCs = []

		#Add DA enemies HERE
		self.frameCounter = -1

		self.enemies = [agent.Deer((self.width*ra.uniform(0.1, 0.9), self.height*ra.uniform(0.2, 0.8))), agent.Voodoo((580,50)), agent.Squirrel((650, 75)), agent.Squirrel((540,75))]
		
	def reset(self):
		self.screen.fill((90,0,0))
		self.screen.blit( self.background, (0,0) )
		self.screen.blit( self.background, (self.height,0) )
		#draw on top of the background
		self.screen.blit(self.wallSprites, (0,0), (0, 90, 445, 77))
		self.screen.blit(self.wallSprites, (675,0), (675, 90, 525, 77))
		
	def checkroom(self,hero_Rect):
		print "room8"
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
			return 10
		elif hero_Rect.x < 0:
			return 2
		elif hero_Rect.y < 0:
			return 9
		else:
			return 7
			
class grassland9:		   
	def __init__ (self, screen, width, height, sprites):
		self.identity = 9
		self.screen= screen
		
		self.music= "sounds/BKGmusic/Forest/FollowTheLeaf.wav"
		
		self.width = width
		self.height = height
		self.background = sprites[0]
		self.wallSprites = sprites[1]
		self.enemySprites = sprites[2]
		self.walls = [pygame.Rect(0, 0, 1200, 50), pygame.Rect(0, 50, 50, 600),  pygame.Rect(1150, 50, 50, 600),  pygame.Rect(0, 50, 50, 600), pygame.Rect(0, 650, 445, 50), pygame.Rect(675, 650, 525, 50)]
		self.rock = None
		self.rockx= []
		self.rocky= []
		self.NPCs = []

		#Add DA enemies HERE
		self.frameCounter = -1

		self.enemies = [agent.Squirrel((555,222)),agent.Squirrel((333,200)),agent.Squirrel((111,111)),agent.Squirrel((666,232)),agent.Squirrel((432,80)),agent.Squirrel((999,76)),agent.Squirrel((1000,400)),
						agent.Voodoo((580,55))]
	
	#special method
	def bossDead(self):
		return self.enemies[-1].isDead()
	
	def reset(self):
		self.screen.fill((90,0,0))
		self.screen.blit( self.background, (0,0) )
		self.screen.blit( self.background, (self.height,0) )
		#draw on top of the background
		self.screen.blit( self.wallSprites, (0,0), (0, 0, 1200, 85) )
		self.screen.blit( self.wallSprites, (0,0), (55, 170, 50, 700))
		self.screen.blit( self.wallSprites, (1150, 0), (1100, 170, 50, 700)  )
		self.screen.blit( self.wallSprites, (0,650), (55, 895, 445, 50))
		self.screen.blit( self.wallSprites, (675,650), (635, 895, 525, 50))
		
	def checkroom(self,hero_Rect):
		print "room9"
		return pygame.Rect(hero_Rect.x, self.height-70, 58, 68)

			
	def judge(self, hero_Rect):
		return 8
		
class grassland10:		   
	def __init__ (self, screen, width, height, sprites):
		self.identity = 10
		self.screen= screen
		
		self.music= "sounds/BKGmusic/Forest/FollowTheLeaf.wav"
		
		self.width = width
		self.height = height
		self.background = sprites[0]
		self.wallSprites = sprites[1]
		self.enemySprites = sprites[2]
		self.walls = [pygame.Rect(0, 0, 1200, 50), pygame.Rect(1150,650, 50, 50)]
		self.rock = None
		self.rockx= []
		self.rocky= []
		self.NPCs = []

		#Add DA enemies HERE
		self.frameCounter = -1

		self.enemies = [agent.Squirrel((555,333)),agent.Squirrel((999,222)),agent.Squirrel((300,300))]
		
	def reset(self):
		self.screen.fill((90,0,0))
		self.screen.blit( self.background, (0,0) )
		self.screen.blit( self.background, (self.height,0) )
		#draw on top of the background
		self.screen.blit( self.wallSprites, (0,0), (0, 0, 1200, 85) )
		self.screen.blit( self.wallSprites, (1150,650), (163, 170, 50, 50))
		
	def checkroom(self,hero_Rect):
		print "room10"
		if hero_Rect.x > self.width:
			return pygame.Rect(2, hero_Rect.y, 58, 68)
		elif hero_Rect.x < 0:
			return pygame.Rect(self.width-60, hero_Rect.y, 58, 68)
		else:
			return pygame.Rect(hero_Rect.x, self.height-70, 58, 68)
			
	def judge(self, hero_Rect):
		if hero_Rect.x > self.width:
			return 12
		elif hero_Rect.x < 0:
			return 8
		else:
			return 11
			
class grassland11:		   
	def __init__ (self, screen, width, height, sprites):
		self.identity = 11
		self.screen= screen
		
		self.music= "sounds/BKGmusic/Forest/FollowTheLeaf.wav"
		
		self.width = width
		self.height = height
		self.background = sprites[0]
		self.wallSprites = sprites[1]
		self.enemySprites = sprites[2]
		self.walls = [pygame.Rect(0, 650, 1200, 50), pygame.Rect(1150, 0, 50, 650)]
		self.rock = None
		self.rockx= []
		self.rocky= []
		self.NPCs = []

		#Add DA enemies HERE
		self.frameCounter = -1
		
		self.enemies = [agent.Squirrel((666,666))]
		
	def reset(self):
		self.screen.fill((90,0,0))
		self.screen.blit( self.background, (0,0) )
		self.screen.blit( self.background, (self.height,0) )
		#draw on top of the background
		self.screen.blit( self.wallSprites, (0, 650), (0, 892, 1200, 50)  )
		self.screen.blit( self.wallSprites, (1150, 0), (1100, 170, 50, 700)  )
		
	def checkroom(self,hero_Rect):
		print "room11"
		if hero_Rect.x > self.width:
			return pygame.Rect(2, hero_Rect.y, 58, 68)
		else:
			return pygame.Rect(hero_Rect.x, 2, 58, 68)
			
	def judge(self, hero_Rect):
		if hero_Rect.x < 0:
			return 7
		else:
			return 10
			
class grassland12:		   
	def __init__ (self, screen, width, height, sprites):
		self.identity = 12
		self.screen= screen
		
		self.music= "sounds/BKGmusic/Forest/FollowTheLeaf.wav"
		
		self.width = width
		self.height = height
		self.background = sprites[0]
		self.wallSprites = sprites[1]
		self.enemySprites = sprites[2]
		self.cave = sprites[3]
		self.walls = [pygame.Rect(0, 0, 1200, 50), pygame.Rect(1150, 50, 50, 600), pygame.Rect(0, 650, 1200, 50)]
		self.rock = None
		self.rockx= []
		self.rocky= []
		
		rockBro = agent.HelpRock(1100,570)
		rockBro.setMessage(["[Rocky The Rock]: YOU SHALL NOT PASS!", "Of course unless you do... but that requires more work from your end."])
		self.NPCs = [rockBro]

		#Add DA enemies HERE
		self.frameCounter = -1
		enem = agent.TreeBeard(((700,250)))
		enem.setAggro(False)
		self.enemies = [enem]
		
	# special event methods and field
		self.passable = False
	def setNPC(self, message):
		self.NPCs[0].setMessage(message)
	def setPass(self, bool):
		self.passable = bool
		
	def reset(self):
		self.screen.fill((90,0,0))
		self.screen.blit( self.background, (0,0) )
		self.screen.blit( self.background, (self.height,0) )
		#draw on top of the background
		self.screen.blit( self.wallSprites, (0,0), (0, 0, 1200, 85) )
		
		if self.passable:
			self.walls = [pygame.Rect(0, 0, 1200, 50), pygame.Rect(0, 650, 1200, 50), pygame.Rect(1150, 50, 50, 285), pygame.Rect(1150, 425, 50, 250)]
			self.screen.blit( self.cave, (1150,85), (0, 0,50,250))
			self.screen.blit( self.cave, (1150,425), (0, 0,50,250))
		else:
			self.screen.blit( self.cave, (1150,85), (0, 0,50, 600) )
		
		self.screen.blit( self.wallSprites, (0, 650), (0, 892, 1200, 50)  )
			
			
		
	def checkroom(self,hero_Rect):
		print "room12"
		return pygame.Rect(2, hero_Rect.y, 58, 68)

	def judge(self, hero_Rect):
		if hero_Rect.x < 0:
			return 10
		if hero_Rect.x > self.width:
			return 99
			