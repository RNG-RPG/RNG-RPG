#Edo frikin KUN
#1/19/2015
#

import agent, room, pygame
def gatherRooms(screen, width, height):
	return [grassland0(screen, width, height), grassland1(screen, width, height), grassland2(screen, width, height), grassland3(screen, width, height), grassland4(screen, width, height),
			grassland5(screen, width, height), grassland6(screen, width, height), grassland7(screen, width, height), grassland8(screen, width, height), grassland9(screen, width, height),
			grassland10(screen, width, height), grassland11(screen, width, height), grassland12(screen, width, height)]

class grassland0:		   
	def __init__ (self, screen, width, height):
		self.identity = 0
		self.screen= screen
		
		self.music= "sounds/BKGmusic/Forest/FollowTheLeaf.wav"
		
		self.width = width
		self.height = height
		self.background = pygame.image.load( "GrassGround.png" ).convert_alpha()
		self.background = pygame.transform.scale(self.background, (self.width, self.height))
		self.wallSprites = pygame.image.load('sprites/treewall_main.png').convert_alpha()
		self.walls = [pygame.Rect(0, 0, 1200, 50), pygame.Rect(0, 50, 50, 600), pygame.Rect(0, 650, 1200, 50)]
		self.enemySprites = pygame.image.load( "sprites/enemy_main.png" ).convert_alpha()
		self.rock = None
		self.rockx= []
		self.rocky= []
		
		rockBro = agent.HelpRock(150, 85)
		rockBro1 = agent.HelpRock(500, 600)
		rockBro2 = agent.HelpRock(1100, 100)
		rockBro.setMessage(["I'm a talking rock~ you should bump into my friends to see what they have to say!"])
		rockBro1.setMessage(["Cleanse this land of your enemies... or perish... (P.S. Rockbros are not your enemy)"])
		rockBro2.setMessage(["I hear strange monsters roam these parts of the woods...", "Best to not get too friendly..."])
		self.NPCs = [rockBro, rockBro1, rockBro2]

		#Add DA enemies HERE
		self.frameCounter = -1
		#hitbox note: subtract double of |dev| from respective x, y -- width and height of rect
		enemyVoodoo = agent.Voodoo(pygame.Rect(550, 320, 36, 46))
		enemyVoodoo.setDev(-10,-10)     

		self.enemies = [enemyVoodoo]
		
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
	def __init__ (self, screen, width, height):
		self.identity = 1
		self.screen= screen
		
		self.music= "sounds/BKGmusic/Forest/FollowTheLeaf.wav"
		
		self.width = width
		self.height = height
		self.background = pygame.image.load( "GrassGround.png" ).convert_alpha()
		self.background = pygame.transform.scale(self.background, (self.width, self.height))
		self.wallSprites = pygame.image.load('sprites/treewall_main.png').convert_alpha()
		self.walls = [pygame.Rect(0, 0, 50, 50), pygame.Rect(0, 650, 50, 50)]
		self.enemySprites = pygame.image.load( "sprites/enemy_main.png" ).convert_alpha()
		self.rock = None
		self.rockx= []
		self.rocky= []
		self.NPCs = []

		#Add DA enemies HERE
		self.frameCounter = -1
		#hitbox note: subtract double of |dev| from respective x, y -- width and height of rect
		enemyVoodoo = agent.Voodoo(pygame.Rect(550, 320, 36, 46))
		enemyVoodoo.setDev(-10,-10)     

		self.enemies = [enemyVoodoo]
		
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
	def __init__ (self, screen, width, height):
		self.identity = 2
		self.screen= screen
		
		self.music= "sounds/BKGmusic/Forest/FollowTheLeaf.wav"
		
		self.width = width
		self.height = height
		self.background = pygame.image.load( "GrassGround.png" ).convert_alpha()
		self.background = pygame.transform.scale(self.background, (self.width, self.height))
		self.wallSprites = pygame.image.load('sprites/treewall_main.png').convert_alpha()
		self.walls = [pygame.Rect(0, 0, 1200, 50), pygame.Rect(0, 50, 50, 650)]
		self.enemySprites = pygame.image.load( "sprites/enemy_main.png" ).convert_alpha()
		self.rock = None
		self.rockx= []
		self.rocky= []
		self.NPCs = []

		#Add DA enemies HERE
		self.frameCounter = -1
		#hitbox note: subtract double of |dev| from respective x, y -- width and height of rect
		enemyVoodoo = agent.Voodoo(pygame.Rect(550, 320, 36, 46))
		enemyVoodoo.setDev(-10,-10)     

		self.enemies = [enemyVoodoo]
		
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
	def __init__ (self, screen, width, height):
		self.identity = 3
		self.screen= screen
		
		self.music= "sounds/BKGmusic/Forest/FollowTheLeaf.wav"
		
		self.width = width
		self.height = height
		self.background = pygame.image.load( "GrassGround.png" ).convert_alpha()
		self.background = pygame.transform.scale(self.background, (self.width, self.height))
		self.wallSprites = pygame.image.load('sprites/treewall_main.png').convert_alpha()
		self.walls = [pygame.Rect(0,0, 50, 700)]
		self.enemySprites = pygame.image.load( "sprites/enemy_main.png" ).convert_alpha()
		self.rock = None
		self.rockx= []
		self.rocky= []
		self.NPCs = []

		#Add DA enemies HERE
		self.frameCounter = -1
		#hitbox note: subtract double of |dev| from respective x, y -- width and height of rect
		enemyVoodoo = agent.Voodoo(pygame.Rect(550, 320, 36, 46))
		enemyVoodoo.setDev(-10,-10)     

		self.enemies = [enemyVoodoo]
		
	def reset(self):
		self.screen.fill((90,0,0))
		self.screen.blit( self.background, (0,0) )
		self.screen.blit( self.background, (self.height,0) )
		#draw on top of the background
		self.screen.blit( self.wallSprites, (0,0), (55, 170, 50, 700))
		
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
	def __init__ (self, screen, width, height):
		self.identity = 4
		self.screen= screen
		
		self.music= "sounds/BKGmusic/Forest/FollowTheLeaf.wav"
		
		self.width = width
		self.height = height
		self.background = pygame.image.load( "GrassGround.png" ).convert_alpha()
		self.background = pygame.transform.scale(self.background, (self.width, self.height))
		self.wallSprites = pygame.image.load('sprites/treewall_main.png').convert_alpha()
		self.walls = [pygame.Rect(0, 0, 50, 700), pygame.Rect(1150, 0, 50, 700)]
		self.enemySprites = pygame.image.load( "sprites/enemy_main.png" ).convert_alpha()
		self.rock = None
		self.rockx= []
		self.rocky= []
		self.NPCs = []

		#Add DA enemies HERE
		self.frameCounter = -1
		#hitbox note: subtract double of |dev| from respective x, y -- width and height of rect
		enemyVoodoo = agent.Voodoo(pygame.Rect(550, 320, 36, 46))
		enemyVoodoo.setDev(-10,-10)     

		self.enemies = [enemyVoodoo]
		
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
	def __init__ (self, screen, width, height):
		self.identity = 5
		self.screen= screen
		
		self.music= "sounds/BKGmusic/Forest/FollowTheLeaf.wav"
		
		self.width = width
		self.height = height
		self.background = pygame.image.load( "GrassGround.png" ).convert_alpha()
		self.background = pygame.transform.scale(self.background, (self.width, self.height))
		self.wallSprites = pygame.image.load('sprites/treewall_main.png').convert_alpha()
		self.walls = [pygame.Rect(0, 0, 50, 700), pygame.Rect(1150, 0, 50, 700),  pygame.Rect(0, 650, 1200, 50)]
		self.enemySprites = pygame.image.load( "sprites/enemy_main.png" ).convert_alpha()
		self.rock = None
		self.rockx= []
		self.rocky= []
		self.NPCs =[]

		#Add DA enemies HERE
		self.frameCounter = -1
		#hitbox note: subtract double of |dev| from respective x, y -- width and height of rect
		enemyVoodoo = agent.Voodoo(pygame.Rect(550, 320, 36, 46))
		enemyVoodoo.setDev(-10,-10)     

		self.enemies = [enemyVoodoo]
		
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
	def __init__ (self, screen, width, height):
		self.identity = 6
		self.screen= screen
		
		self.music= "sounds/BKGmusic/Forest/FollowTheLeaf.wav"
		
		self.width = width
		self.height = height
		self.background = pygame.image.load( "GrassGround.png" ).convert_alpha()
		self.background = pygame.transform.scale(self.background, (self.width, self.height))
		self.wallSprites = pygame.image.load('sprites/treewall_main.png').convert_alpha()
		self.walls = [pygame.Rect(0, 650, 1200, 50), pygame.Rect(1150, 0, 50, 700)]
		self.enemySprites = pygame.image.load( "sprites/enemy_main.png" ).convert_alpha()
		self.rock = None
		self.rockx= []
		self.rocky= []
		self.NPCs = []
		
		#Add DA enemies HERE
		self.frameCounter = -1
		#hitbox note: subtract double of |dev| from respective x, y -- width and height of rect
		enemyVoodoo = agent.Voodoo(pygame.Rect(550, 320, 36, 46))
		enemyVoodoo.setDev(-10,-10)     

		self.enemies = [enemyVoodoo]
		
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
	def __init__ (self, screen, width, height):
		self.identity = 7
		self.screen= screen
		
		self.music= "sounds/BKGmusic/Forest/FollowTheLeaf.wav"
		
		self.width = width
		self.height = height
		self.background = pygame.image.load( "GrassGround.png" ).convert_alpha()
		self.background = pygame.transform.scale(self.background, (self.width, self.height))
		self.wallSprites = pygame.image.load('sprites/treewall_main.png').convert_alpha()
		self.walls = []
		self.enemySprites = pygame.image.load( "sprites/enemy_main.png" ).convert_alpha()
		self.rock = None
		self.rockx= []
		self.rocky= []
		self.NPCs = []

		#Add DA enemies HERE
		self.frameCounter = -1
		#hitbox note: subtract double of |dev| from respective x, y -- width and height of rect
		enemyVoodoo = agent.Voodoo(pygame.Rect(550, 320, 36, 46))
		enemyVoodoo.setDev(-10,-10)     

		self.enemies = [enemyVoodoo]
		
	def reset(self):
		self.screen.fill((90,0,0))
		self.screen.blit( self.background, (0,0) )
		self.screen.blit( self.background, (self.height,0) )
		#draw on top of the background
		
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
	def __init__ (self, screen, width, height):
		self.identity = 8
		self.screen= screen
		
		self.music= "sounds/BKGmusic/Forest/FollowTheLeaf.wav"
		
		self.width = width
		self.height = height
		self.background = pygame.image.load( "GrassGround.png" ).convert_alpha()
		self.background = pygame.transform.scale(self.background, (self.width, self.height))
		self.wallSprites = pygame.image.load('sprites/treewall_main.png').convert_alpha()
		self.walls = [pygame.Rect(0, 0, 445, 50), pygame.Rect(675, 0, 525, 50)]
		self.enemySprites = pygame.image.load( "sprites/enemy_main.png" ).convert_alpha()
		self.rock = None
		self.rockx= []
		self.rocky= []
		self.NPCs = []

		#Add DA enemies HERE
		self.frameCounter = -1
		#hitbox note: subtract double of |dev| from respective x, y -- width and height of rect
		enemyVoodoo = agent.Voodoo(pygame.Rect(550, 320, 36, 46))
		enemyVoodoo.setDev(-10,-10)     

		self.enemies = [enemyVoodoo]
		
	def reset(self):
		self.screen.fill((90,0,0))
		self.screen.blit( self.background, (0,0) )
		self.screen.blit( self.background, (self.height,0) )
		#draw on top of the background
		self.screen.blit(self.wallSprites, (0,0), (0, 90, 445, 85))
		self.screen.blit(self.wallSprites, (675,0), (675, 90, 525, 85))
		
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
	def __init__ (self, screen, width, height):
		self.identity = 9
		self.screen= screen
		
		self.music= "sounds/BKGmusic/Forest/FollowTheLeaf.wav"
		
		self.width = width
		self.height = height
		self.background = pygame.image.load( "GrassGround.png" ).convert_alpha()
		self.background = pygame.transform.scale(self.background, (self.width, self.height))
		self.wallSprites = pygame.image.load('sprites/treewall_main.png').convert_alpha()
		self.walls = [pygame.Rect(0, 0, 1200, 50), pygame.Rect(0, 50, 50, 600),  pygame.Rect(1150, 50, 50, 600),  pygame.Rect(0, 50, 50, 600), pygame.Rect(0, 650, 445, 50), pygame.Rect(675, 650, 525, 50)]
		self.enemySprites = pygame.image.load( "sprites/enemy_main.png" ).convert_alpha()
		self.rock = None
		self.rockx= []
		self.rocky= []
		self.NPCs = []

		#Add DA enemies HERE
		self.frameCounter = -1
		#hitbox note: subtract double of |dev| from respective x, y -- width and height of rect
		enemyVoodoo = agent.Voodoo(pygame.Rect(550, 320, 36, 46))
		enemyVoodoo.setDev(-10,-10)     

		self.enemies = [enemyVoodoo]
		
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
	def __init__ (self, screen, width, height):
		self.identity = 10
		self.screen= screen
		
		self.music= "sounds/BKGmusic/Forest/FollowTheLeaf.wav"
		
		self.width = width
		self.height = height
		self.background = pygame.image.load( "GrassGround.png" ).convert_alpha()
		self.background = pygame.transform.scale(self.background, (self.width, self.height))
		self.wallSprites = pygame.image.load('sprites/treewall_main.png').convert_alpha()
		self.walls = [pygame.Rect(0, 0, 1200, 50)]
		self.enemySprites = pygame.image.load( "sprites/enemy_main.png" ).convert_alpha()
		self.rock = None
		self.rockx= []
		self.rocky= []
		self.NPCs = []

		#Add DA enemies HERE
		self.frameCounter = -1
		#hitbox note: subtract double of |dev| from respective x, y -- width and height of rect
		enemyVoodoo = agent.Voodoo(pygame.Rect(550, 320, 36, 46))
		enemyVoodoo.setDev(-10,-10)     

		self.enemies = [enemyVoodoo]
		
	def reset(self):
		self.screen.fill((90,0,0))
		self.screen.blit( self.background, (0,0) )
		self.screen.blit( self.background, (self.height,0) )
		#draw on top of the background
		self.screen.blit( self.wallSprites, (0,0), (0, 0, 1200, 85) )
		
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
	def __init__ (self, screen, width, height):
		self.identity = 11
		self.screen= screen
		
		self.music= "sounds/BKGmusic/Forest/FollowTheLeaf.wav"
		
		self.width = width
		self.height = height
		self.background = pygame.image.load( "GrassGround.png" ).convert_alpha()
		self.background = pygame.transform.scale(self.background, (self.width, self.height))
		self.wallSprites = pygame.image.load('sprites/treewall_main.png').convert_alpha()
		self.walls = [pygame.Rect(0, 650, 1200, 50), pygame.Rect(1150, 0, 50, 650)]
		self.enemySprites = pygame.image.load( "sprites/enemy_main.png" ).convert_alpha()
		self.rock = None
		self.rockx= []
		self.rocky= []
		self.NPCs = []

		#Add DA enemies HERE
		self.frameCounter = -1
		#hitbox note: subtract double of |dev| from respective x, y -- width and height of rect
		enemyVoodoo = agent.Voodoo(pygame.Rect(550, 320, 36, 46))
		enemyVoodoo.setDev(-10,-10)     

		self.enemies = [enemyVoodoo]
		
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
	def __init__ (self, screen, width, height):
		self.identity = 12
		self.screen= screen
		
		self.music= "sounds/BKGmusic/Forest/FollowTheLeaf.wav"
		
		self.width = width
		self.height = height
		self.background = pygame.image.load( "GrassGround.png" ).convert_alpha()
		self.background = pygame.transform.scale(self.background, (self.width, self.height))
		self.wallSprites = pygame.image.load('sprites/treewall_main.png').convert_alpha()
		self.cave = pygame.image.load('sprites/rockwall_main.png').convert_alpha()
		self.walls = [pygame.Rect(0, 0, 1200, 50), pygame.Rect(1150, 50, 50, 600), pygame.Rect(0, 650, 1200, 50)]
		self.enemySprites = pygame.image.load( "sprites/enemy_main.png" ).convert_alpha()
		self.rock = None
		self.rockx= []
		self.rocky= []
		self.NPCs = []

		#Add DA enemies HERE
		self.frameCounter = -1
		#hitbox note: subtract double of |dev| from respective x, y -- width and height of rect
		enemyVoodoo = agent.Voodoo(pygame.Rect(550, 320, 36, 46))
		enemyVoodoo.setDev(-10,-10)     

		self.enemies = [enemyVoodoo]
		
	def reset(self):
		self.screen.fill((90,0,0))
		self.screen.blit( self.background, (0,0) )
		self.screen.blit( self.background, (self.height,0) )
		#draw on top of the background
		self.screen.blit( self.wallSprites, (0,0), (0, 0, 1200, 85) )
		self.screen.blit( self.wallSprites, (0, 650), (0, 892, 1200, 50)  )
		
	def checkroom(self,hero_Rect):
		print "room12"
		return pygame.Rect(2, hero_Rect.y, 58, 68)

	def judge(self, hero_Rect):
		if hero_Rect.x < 0:
			return 10
			