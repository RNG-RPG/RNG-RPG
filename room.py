# created by Raymond Chung
# file  room.py

# imports
import sys, pygame, math, agent, os
import titlescreen, room
		    
class tutorial:		   
	def __init__ (self, screen, width, height):
		self.identity = 0
		self.screen= screen
		
		self.music= "sounds/BKGmusic/TownBoss/VictoryAtLast.wav"
		
		self.width = width
		self.height = height
		self.background = pygame.image.load( "RockGround2.png" ).convert_alpha()
		self.background = pygame.transform.scale(self.background, (self.width, self.height))
		self.left_side = pygame.image.load( "rock_sides.png" ).convert_alpha()
		self.right_side = pygame.image.load( "rock_sides.png" ).convert_alpha()
		self.top_side = pygame.image.load( "rock_top.png" ).convert_alpha()
		self.bottom_side = pygame.image.load( "rock_top.png" ).convert_alpha()
		self.rock = pygame.image.load( "rock.png" ).convert_alpha()
		self.enemySprites = pygame.image.load( "sprites/enemy_main.png" ).convert_alpha()
		self.rockx= []
		self.rocky= []
		
		self.rockx.append(500)
		self.rocky.append(180)

		#Add DA enemies HERE
		self.frameCounter = -1
		dragond = [(0, 0, 114, 154), (114, 0, 114, 154), (214, 0, 114, 154)]
		#hitbox note: subtract double of |dev| from respective x, y -- width and height of rect
		enemyDragon = agent.Dragon([(0, 0, 114, 154), (114, 0, 114, 154), (228, 0, 114, 154)], pygame.Rect(500, 100, 34, 74), 10)
		enemyDragon.setDev(-40, -40)

		enemySlime = agent.Slime([(0, 154, 50, 50), (50, 154, 50, 50), (0, 154, 50, 50), (100, 154, 50, 50), (150, 154, 50, 50)], pygame.Rect(700, 400, 10, 10), 5)
		enemySlime.setDev(-20, -20)
		enemySlime2 = agent.Slime([(0, 154, 50, 50), (50, 154, 50, 50), (0, 154, 50, 50), (100, 154, 50, 50), (150, 154, 50, 50)], pygame.Rect(800, 350, 10, 10), 5)
		enemySlime2.setDev(-20, -20)
		enemySlime3 = agent.Slime([(0, 154, 50, 50), (50, 154, 50, 50), (0, 154, 50, 50), (100, 154, 50, 50), (150, 154, 50, 50)], pygame.Rect(900, 350, 10, 10), 5)
		enemySlime3.setDev(-20, -20)
		enemySlime4 = agent.Slime([(0, 154, 50, 50), (50, 154, 50, 50), (0, 154, 50, 50), (100, 154, 50, 50), (150, 154, 50, 50)], pygame.Rect(900, 450, 10, 10), 5)
		enemySlime4.setDev(-20, -20)
		enemySlime5 = agent.Slime([(0, 154, 50, 50), (50, 154, 50, 50), (0, 154, 50, 50), (100, 154, 50, 50), (150, 154, 50, 50)], pygame.Rect(700, 300, 10, 10), 5)
		enemySlime5.setDev(-20, -20)
		enemySlime6 = agent.Slime([(0, 154, 50, 50), (50, 154, 50, 50), (0, 154, 50, 50), (100, 154, 50, 50), (150, 154, 50, 50)], pygame.Rect(800, 500, 10, 10), 5)

		enemySlime6.setDev(-20, -20)

		#directional facing sprites require more complexity
		enemyVoodoo = agent.Voodoo([(0, 229, 55, 66), (0, 229, 55, 66), (56, 229, 55, 66), (112, 229, 55, 66), (168, 229, 55, 66), (224, 229, 55, 66), (280, 229, 55, 66),
				             (336, 229, 55, 66), (392, 229, 55, 66), (448, 229, 55, 66)], pygame.Rect(1000, 100, 36, 46), 6, True)
		enemyVoodoo.setDev(-10,-10)        
		enemySquirrel = agent.Squirrel([(0, 295, 33, 36), (33, 295, 33, 36), (66, 295, 33, 36), (99, 295, 33, 36), (66, 295, 33, 36),(66, 295, 33, 36), (66, 295, 33, 36),
				                (99, 295, 34, 36), (99, 295, 34, 36), (99, 295, 34, 36)], pygame.Rect(950, 500, 10, 12), 20, True)
		enemySquirrel.setDev(-12,-12)

		self.enemies = [enemyDragon, enemySlime, enemySlime2, enemySlime3, enemySlime4, enemySlime5, enemySlime6, enemyVoodoo, enemySquirrel]
		
		self.screen.blit( self.rock, (self.rockx[0], self.rocky[0]) )
	
	def reset(self):
		self.screen.fill((90,0,0))
		self.screen.blit( self.background, (0,0) )
		self.screen.blit( self.background, (self.height,0) )
		#draw on top of the background
		self.screen.blit( self.rock, (self.rockx[0], self.rocky[0]) )
		self.screen.blit( self.left_side, (0,0) )
		self.screen.blit( self.right_side, (self.width-50, 0) )
		self.screen.blit( self.top_side, (0,0) )
		self.screen.blit( self.bottom_side, (0, self.height-50) )
		enemlist = self.enemies
		self.enemies= []
		self.enemies= enemlist
	
	def judge(self):
		return 0
			
	def enter(self):		
		return pygame.Rect(50, 100, 87, 102)
		

class firstroom:		   
	def __init__ (self, screen, width, height):
		self.identity = 1
		self.screen= screen
		
		self.music= "sounds/BKGmusic/Cave/MagmaWormHunt.wav"
		
		self.width = width
		self.height = height
		self.background = pygame.image.load( "RockGround2.png" ).convert_alpha()
		self.background = pygame.transform.scale(self.background, (self.width, self.height))
		self.left_side = pygame.image.load( "rock_sides.png" ).convert_alpha()
		self.right_side = None
		self.top_side = pygame.image.load( "rock_top.png" ).convert_alpha()
		self.bottom_side = pygame.image.load( "rock_top.png" ).convert_alpha()
		self.rock = pygame.image.load( "rock.png" ).convert_alpha()
		self.enemySprites = pygame.image.load( "sprites/enemy_main.png" ).convert_alpha()
		self.rockx= []
		self.rocky= []
		
		self.rockx.append(500)
		self.rocky.append(180)

		#Add DA enemies HERE
		self.frameCounter = -1
		dragond = [(0, 0, 114, 154), (114, 0, 114, 154), (214, 0, 114, 154)]
		#hitbox note: subtract double of |dev| from respective x, y -- width and height of rect

		enemySlime = agent.Slime([(0, 154, 50, 50), (50, 154, 50, 50), (0, 154, 50, 50), (100, 154, 50, 50), (150, 154, 50, 50)], pygame.Rect(800, 400, 10, 10), 5)
		enemySlime.setDev(-20, -20)
		enemySlime2 = agent.Slime([(0, 154, 50, 50), (50, 154, 50, 50), (0, 154, 50, 50), (100, 154, 50, 50), (150, 154, 50, 50)], pygame.Rect(700, 350, 10, 10), 5)
		enemySlime2.setDev(-20, -20)
		enemySlime3 = agent.Slime([(0, 154, 50, 50), (50, 154, 50, 50), (0, 154, 50, 50), (100, 154, 50, 50), (150, 154, 50, 50)], pygame.Rect(600, 350, 10, 10), 5)
		enemySlime3.setDev(-20, -20)
		enemySlime4 = agent.Slime([(0, 154, 50, 50), (50, 154, 50, 50), (0, 154, 50, 50), (100, 154, 50, 50), (150, 154, 50, 50)], pygame.Rect(720, 450, 10, 10), 5)
		enemySlime4.setDev(-20, -20)
		enemySlime5 = agent.Slime([(0, 154, 50, 50), (50, 154, 50, 50), (0, 154, 50, 50), (100, 154, 50, 50), (150, 154, 50, 50)], pygame.Rect(740, 300, 10, 10), 5)
		enemySlime5.setDev(-20, -20)
		enemySlime6 = agent.Slime([(0, 154, 50, 50), (50, 154, 50, 50), (0, 154, 50, 50), (100, 154, 50, 50), (150, 154, 50, 50)], pygame.Rect(820, 500, 10, 10), 5)
		enemySlime6.setDev(-20, -20)

		self.enemies = [enemySlime, enemySlime2, enemySlime3, enemySlime4, enemySlime5, enemySlime6]
		
		self.screen.blit( self.rock, (self.rockx[0], self.rocky[0]) )
	
	def reset(self):
		self.screen.fill((90,0,0))
		self.screen.blit( self.background, (0,0) )
		self.screen.blit( self.background, (self.height,0) )
		#draw on top of the background
		self.screen.blit( self.rock, (self.rockx[0], self.rocky[0]) )
		self.screen.blit( self.left_side, (0,0) )
		self.screen.blit( self.top_side, (0,0) )
		self.screen.blit( self.bottom_side, (0, self.height-50) )
		enemlist = self.enemies
		self.enemies= []
		self.enemies= enemlist
	
	def judge(self):
		if hero_Rect.x > self.width:
			return self.identity+1
			
	def enter(self):		
		return pygame.Rect(50, 100, 87, 102)
		

class secondroom:		   
	def __init__ (self, screen, width, height):
		self.identity = 2
		self.screen= screen
		
		self.music= "sounds/BKGmusic/CaveBoss/FiresOfHell.wav"
		
		self.width = width
		self.height = height
		self.background = pygame.image.load( "RockGround2.png" ).convert_alpha()
		self.background = pygame.transform.scale(self.background, (self.width, self.height))
		self.left_side = pygame.image.load( "rock_sides.png" ).convert_alpha()
		self.right_side = pygame.image.load( "rock_sides.png" ).convert_alpha()
		self.top_side = pygame.image.load( "rock_top.png" ).convert_alpha()
		self.bottom_side = pygame.image.load( "rock_top.png" ).convert_alpha()
		self.rock = pygame.image.load( "rock.png" ).convert_alpha()
		self.enemySprites = pygame.image.load( "sprites/enemy_main.png" ).convert_alpha()
		self.rockx= []
		self.rocky= []
		
		self.rockx.append(500)
		self.rocky.append(180)

		#Add DA enemies HERE
		self.frameCounter = -1
		dragond = [(0, 0, 114, 154), (114, 0, 114, 154), (214, 0, 114, 154)]
		#hitbox note: subtract double of |dev| from respective x, y -- width and height of rect
		enemyDragon = agent.Dragon([(0, 0, 114, 154), (114, 0, 114, 154), (228, 0, 114, 154)], pygame.Rect(500, 100, 34, 74), 10)
		enemyDragon.setDev(-40, -40)
		
		enemySlime = agent.Slime([(0, 154, 50, 50), (50, 154, 50, 50), (0, 154, 50, 50), (100, 154, 50, 50), (150, 154, 50, 50)], pygame.Rect(400, 400, 10, 10), 5)
		enemySlime.setDev(-20, -20)
		enemySlime2 = agent.Slime([(0, 154, 50, 50), (50, 154, 50, 50), (0, 154, 50, 50), (100, 154, 50, 50), (150, 154, 50, 50)], pygame.Rect(450, 350, 10, 10), 5)
		enemySlime2.setDev(-20, -20)
		enemySlime3 = agent.Slime([(0, 154, 50, 50), (50, 154, 50, 50), (0, 154, 50, 50), (100, 154, 50, 50), (150, 154, 50, 50)], pygame.Rect(470, 350, 10, 10), 5)
		enemySlime3.setDev(-20, -20)
		enemySlime4 = agent.Slime([(0, 154, 50, 50), (50, 154, 50, 50), (0, 154, 50, 50), (100, 154, 50, 50), (150, 154, 50, 50)], pygame.Rect(480, 450, 10, 10), 5)
		enemySlime4.setDev(-20, -20)
		enemySlime5 = agent.Slime([(0, 154, 50, 50), (50, 154, 50, 50), (0, 154, 50, 50), (100, 154, 50, 50), (150, 154, 50, 50)], pygame.Rect(510, 300, 10, 10), 5)
		enemySlime5.setDev(-20, -20)
		enemySlime6 = agent.Slime([(0, 154, 50, 50), (50, 154, 50, 50), (0, 154, 50, 50), (100, 154, 50, 50), (150, 154, 50, 50)], pygame.Rect(530, 500, 10, 10), 5)
		enemySlime6.setDev(-20, -20)
		enemySlime7 = agent.Slime([(0, 154, 50, 50), (50, 154, 50, 50), (0, 154, 50, 50), (100, 154, 50, 50), (150, 154, 50, 50)], pygame.Rect(700, 400, 10, 10), 5)
		enemySlime7.setDev(-20, -20)
		enemySlime8 = agent.Slime([(0, 154, 50, 50), (50, 154, 50, 50), (0, 154, 50, 50), (100, 154, 50, 50), (150, 154, 50, 50)], pygame.Rect(800, 350, 10, 10), 5)
		enemySlime8.setDev(-20, -20)
		enemySlime9 = agent.Slime([(0, 154, 50, 50), (50, 154, 50, 50), (0, 154, 50, 50), (100, 154, 50, 50), (150, 154, 50, 50)], pygame.Rect(900, 350, 10, 10), 5)
		enemySlime9.setDev(-20, -20)
		enemySlime10 = agent.Slime([(0, 154, 50, 50), (50, 154, 50, 50), (0, 154, 50, 50), (100, 154, 50, 50), (150, 154, 50, 50)], pygame.Rect(900, 450, 10, 10), 5)
		enemySlime10.setDev(-20, -20)
		enemySlime11 = agent.Slime([(0, 154, 50, 50), (50, 154, 50, 50), (0, 154, 50, 50), (100, 154, 50, 50), (150, 154, 50, 50)], pygame.Rect(700, 300, 10, 10), 5)
		enemySlime11.setDev(-20, -20)
		enemySlime12 = agent.Slime([(0, 154, 50, 50), (50, 154, 50, 50), (0, 154, 50, 50), (100, 154, 50, 50), (150, 154, 50, 50)], pygame.Rect(800, 500, 10, 10), 5)
		enemySlime12.setDev(-20, -20)

		enemySquirrel = agent.Squirrel([(0, 295, 33, 36), (33, 295, 33, 36), (66, 295, 33, 36), (99, 295, 33, 36), (66, 295, 33, 36),(66, 295, 33, 36), (66, 295, 33, 36),
				                (99, 295, 34, 36), (99, 295, 34, 36), (99, 295, 34, 36)], pygame.Rect(950, 500, 10, 12), 20, True)
		enemySquirrel.setDev(-12,-12)

		self.enemies = [enemyDragon, enemySlime, enemySlime2, enemySlime3, enemySlime4, enemySlime5, enemySlime6, enemySlime7, enemySlime8, enemySlime9, enemySlime10, enemySlime11, enemySlime12, enemySquirrel]
			
		self.screen.blit( self.rock, (self.rockx[0], self.rocky[0]) )
	
	def reset(self):
		self.screen.fill((90,0,0))
		self.screen.blit( self.background, (0,0) )
		self.screen.blit( self.background, (self.height,0) )
		#draw on top of the background
		self.screen.blit( self.rock, (self.rockx[0], self.rocky[0]) )
		self.screen.blit( self.right_side, (self.width-50, 0) )
		self.screen.blit( self.top_side, (0,0) )
		self.screen.blit( self.bottom_side, (0, self.height-50) )
		enemlist = self.enemies
		self.enemies= []
		self.enemies= enemlist

