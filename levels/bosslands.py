#Edo frikin KUN
#1/22/2015
#

import agent, room, pygame, random as ra

class bossland0:		   
	def __init__ (self, screen, width, height, sprites):
		self.identity = 0
		self.screen= screen
		
		self.music= "sounds/BKGmusic/Forest/FollowTheLeaf.wav"
		
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
		rockBro.setMessage(["[Rock Twat]: Congratulation! You've slain that infernal winged beast! (Not that I couldn't have done it)","[Rock Twat]: Now go complete your quest ya scrub."])
		rockBro1.setMessage(["[Rocky Balboa]: You like what you see? These rock hard abs didn't come to be from sitting around all day", ".... Oh wait...."])
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
		
		self.music= "sounds/BKGmusic/Forest/FollowTheLeaf.wav"
		
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
		
		self.music= "sounds/BKGmusic/Forest/FollowTheLeaf.wav"
		
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
		
		self.music= "sounds/BKGmusic/Forest/FollowTheLeaf.wav"
		
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
		self.screen.blit(self.wallSprites, (0,0), (0, 90, 445, 85))
		self.screen.blit(self.wallSprites, (675,0), (675, 90, 525, 85))
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
		
		self.music= "sounds/BKGmusic/Forest/FollowTheLeaf.wav"
		
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
		self.screen.blit(self.wallSprites, (0,0), (0, 90, 445, 85))
		self.screen.blit(self.wallSprites, (675,0), (675, 90, 525, 85))
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
		self.identity = 5
		self.screen= screen
		
		self.music= "sounds/BKGmusic/Forest/FollowTheLeaf.wav"
		
		self.width = width
		self.height = height
		self.background = sprites[0]
		self.wallSprites = sprites[1]
		self.enemySprites = sprites[2]
		self.walls = [pygame.Rect(0, 0, 50, 50), pygame.Rect(0, 650, 50, 50), pygame.Rect(1150, 0, 50, 50), pygame.Rect(1150, 650, 50, 50)]
		self.rock = None
		self.rockx= []
		self.rocky= []
		rockBro = agent.HelpRock(590,330)
		rockBro.setMessage(["[Stone Guardian]: 3 paths... 3 guardians..."])
		
		self.NPCs = [rockBro]

		#Add DA enemies HERE
		self.frameCounter = -1
		#hitbox note: subtract double of |dev| from respective x, y -- width and height of rect
		self.enemies = [agent.Squirrel((self.width*ra.uniform(0.1, 0.9), self.height*ra.uniform(0.2, 0.8)))]
		
	def reset(self):
		self.screen.fill((90,0,0))
		self.screen.blit( self.background, (0,0) )
		self.screen.blit( self.background, (self.height,0) )
		#draw on top of the background
		self.screen.blit( self.wallSprites, (0,0), (215, 285, 100, 85) )
		self.screen.blit( self.wallSprites, (0, 650), (200, 170, 50, 50)  )
        self.screen.blit( self.wallSprites, (1100,650), (110, 285, 100, 85))
        self.screen.blit( self.wallSprites, (1150,0), (215, 285, 100, 85) )
		
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
		
		self.music= "sounds/BKGmusic/Forest/FollowTheLeaf.wav"
		
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
						agent.Squirrel((self.width*ra.uniform(0.1, 0.9), self.height*ra.uniform(0.2, 0.8)))]
		
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
		
		self.music= "sounds/BKGmusic/Forest/FollowTheLeaf.wav"
		
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

		self.enemies = []
		
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
		
		self.enemies = [agent.Squirrel((self.width*ra.uniform(0.1, 0.9), self.height*ra.uniform(0.2, 0.8))),
                        agent.Squirrel((self.width*ra.uniform(0.1, 0.9), self.height*ra.uniform(0.2, 0.8))),
                        agent.Squirrel((self.width*ra.uniform(0.1, 0.9), self.height*ra.uniform(0.2, 0.8))),
                        agent.Squirrel((self.width*ra.uniform(0.1, 0.9), self.height*ra.uniform(0.2, 0.8))),
						agent.Squirrel((self.width*ra.uniform(0.1, 0.9), self.height*ra.uniform(0.2, 0.8))),
                        agent.Squirrel((self.width*ra.uniform(0.1, 0.9), self.height*ra.uniform(0.2, 0.8))),
                        agent.Voodoo((self.width*ra.uniform(0.1, 0.9), self.height*ra.uniform(0.2, 0.8)))]
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