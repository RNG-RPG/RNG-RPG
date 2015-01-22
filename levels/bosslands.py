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
		
		var =ra.random.uniform(.2, 1.0)
		
		rockBro = agent.HelpRock(150, 50)
		rockBro1 = agent.HelpRock(200, 50)
		rockBro.setMessage(["[Rock Twat]: Congratulation! You've slain that infernal winged beast! (Not that I couldn't have done it)","[Rock Twat]: Now go complete your quest ya scrub."])
		rockBro1.setMessage(["[Rocky Balboa]: You like what you see? These rock hard abs didn't come to be from sitting around all day", ".... Oh wait...."])
		self.NPCs = [rockBro, rockBro1]

		
		#Add DA enemies HERE
		self.frameCounter = -1
		#hitbox note: subtract double of |dev| from respective x, y -- width and height of rect

		self.enemies = [agent.Squirrel((1000,200)),agent.Squirrel((850,200))]
		
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