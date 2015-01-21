#Edward Zhou
#1/9/15
#basic unit template

import pygame
pygame.init()
class Agent:

	#Constructor
	def __init__ (self,hp,mp,exp):
		self.maxHP=hp
		self.HP=hp
		self.maxMP=mp
		self.MP=mp
		self.exp=exp
		
	#accessors   
	def getMaxHP(self):
		return self.maxHP
		
	def changeMaxHP(self,change):
		self.maxHP+=change
		
	def getHP(self):
		return self.HP
		
	def changeHP(self,change):
		self.HP+=change
		
	def getMaxMP(self):
		return self.maxMP
		
	def changeMaxMP(self,change):
		self.maxMP+=change
		
	def getMP(self):
		return self.MP
		
	def changeMP(self,change):
		self.MP+=change
		
	def changeEXP(self,change):
		self.exp+=change

class NPC(object):
	#Constructor
	'''spriteMap format: down, right, up, left'''
	def __init__(self, sprites, x, y):
		self.spriteMap = sprites
		self.rect = pygame.Rect(x, y, 40, 60 )
		self.message = []
		self.messageCounter = -1
		
	def getRect(self):
		return self.rect
			
	'''depends on hero location'''
	def getCurrentSprite(self, herox, heroy):
		if abs(herox-self.rect.x) > abs(heroy - self.rect.y):
			if herox - self.rect.x > 0:
				return self.spriteMap[1]
			else: 
				return self.spriteMap[3]
		else:
			if heroy - self.rect.y > 0:
				return self.spriteMap[0]
			else:
				return self.spriteMap[2]
	
	def getMessage(self):
		self.messageCounter +=1
		if self.messageCounter > len(self.message)-1:
			self.messageCounter = -1
			return None
		return self.message[self.messageCounter]
	
	def setMessage(self, mes):
		self.message = mes
		self.messageCounter = -1
		
class HelpRock(NPC):
	def __init__(self, x, y):
		super(HelpRock, self).__init__([(152, 0, 38, 60),(152, 0, 38, 60),(152, 0, 38, 60),(152, 0, 38, 60)], x, y)
		
class LostGirl(NPC):
	def __init__(self, x, y):
		super(LostGirl, self).__init__([(0, 0, 38, 60),(38, 0, 38, 60),(76, 0, 38, 60),(114, 0, 38, 60)], x, y)
		
class Enemy(object):

	#Constructor
	'''spritemap is this format (source x, source y, width, height)
	directional: down idle, down idle2, down1,down2,righ1,righ2,up1,up2,left1,left2, dead
	'''
	def __init__ (self, hp, spriteMap, rect, animSpeed, attack, directionSprites=False):
		self.maxHP=hp
		self.HP=hp
		self.spriteMap=spriteMap
		self.activeSprite = 0
		self.Rect = rect
		self.originalRect = rect
		self.animSpeed = animSpeed
		self.dead=False
		self.hoSpeed = 0
		self.vertSpeed = 0
		self.speedBoost = 1
		self.aggressive = True
		self.attack = attack
		
		self.xDev = 0
		self.yDev = 0
		self.directional = directionSprites
		self.internalDClock = 60
		self.internalMClock = -1
		self.idleCounter = 0
		self.directionalCache = self.spriteMap[0]
		self.aggro = False
		self.deadcount= 0
		
	def isDirectional(self):
		return self.directional
	def getSprites(self):
		return self.spriteMap
		
	#if spriteMap has directional movements -> automatically grabs the right sprite
	def getCurrentSprite(self):
		if self.directional:
			if self.dead:
				return self.spriteMap[-1]
			self.internalDClock += 1
			if self.internalDClock > 60:
				self.internalDClock = 0
			if self.hoSpeed == 0 and self.vertSpeed == 0:
				if self.internalDClock >59:
					self.idleCounter = (self.idleCounter+1) % 2
					self.directionalCache = self.spriteMap[self.idleCounter]
			else:
				self.internalMClock += 1
				if self.internalMClock > 29:
					self.internalMClock = 0
				if self.internalMClock % self.animSpeed == 0:
					
					self.idleCounter = (self.idleCounter+1)%2
					if self.hoSpeed > 0:
						self.directionalCache = self.spriteMap[self.idleCounter +4]
					elif self.hoSpeed < 0:
						self.directionalCache =  self.spriteMap[self.idleCounter +8]
					elif self.vertSpeed > 0:
						self.directionalCache = self.spriteMap[self.idleCounter +2]
					else:
						self.directionalCache = self.spriteMap[self.idleCounter +6]
			return self.directionalCache
		else:
			return self.spriteMap[self.activeSprite]
	def setAggress(self, aggressive):
		self.aggressive = aggressive
	#this is a number for active sprite
	def changeSprite(self, newNum):
		self.activeSprite = newNum
	def getSpriteNumber(self):
		return self.activeSprite
	#Deviation for drawn images and hitboxes
	def setDev(self, x, y):
		self.xDev = x
		self.yDev = y
	def getxDev(self):
		return self.xDev
	def getyDev(self):
		return self.yDev
		
	def setHSpeed(self, x):
		self.hoSpeed = x
	def setVSpeed(self, y):
		self.vertSpeed = y
	def getHSpeed(self):
		return self.hoSpeed * self.speedBoost
	def getVSpeed(self):
		return self.vertSpeed * self.speedBoost
	'''in addition to the base speed'''
	def setSpeed(self, change):
		self.speedBoost = change
	
	def setAggro(self, boolean):
		self.aggro = boolean
	
	def isAggro(self):
		return self.aggro

	def getRect(self):
		return self.Rect
	def getOriginalRect(self):
		return self.originalRect
	def changeRect(self, newRect):
		self.Rect=newRect
	
	def getFrameSpeed(self):
		return self.animSpeed
	def getMaxHP(self):
		return self.maxHP
	def changeMaxHP(self,change):
		self.maxHP+=change     
	def changeHP(self,change):
		self.HP+=change       
		if self.HP <= 0:
			self.dead = True
			self.hoSpeed = 0
			self.vertSpeed = 0
	def getHP(self):
		return self.HP
	def getAttack(self):
		return self.attack
	def isDead(self):
		return self.dead
	def ressurect(self):
		self.dead = False
		self.HP = self.maxHP
		self.hoSpeed = 0
		self.vertSpeed = 0
		self.setAggro(False)
		self.deadcount= 0
		

class Slime(Enemy):
	def __init__ (self, rect, aggress = True, animSpeed = 5):
		super(Slime,self).__init__(3, [(0, 154, 50, 50), (50, 154, 50, 50), (0, 154, 50, 50), (100, 154, 50, 50), (150, 154, 50, 50)], rect, animSpeed)
		self.setDev(-20,-20)
		self.setAggress(aggress)
		self.deathsound = pygame.mixer.Sound("sounds/slimedeath.wav")
		self.deathsound.set_volume(1)
		self.movesound = pygame.mixer.Sound("sounds/slimemove.wav")
		self.movesound.set_volume(.2)
		self.attacksound = pygame.mixer.Sound("sounds/slimemove.wav")
		self.setSpeed(3)

class Dragon(Enemy):
	def __init__ (self, rect, aggress = True, animSpeed = 10):
		super(Dragon,self).__init__(20, [(0, 0, 114, 154), (114, 0, 114, 154), (228, 0, 114, 154)], pygame.Rect(rect[0], rect[1],34, 74), animSpeed, False)
		self.setDev(-40,-40)
		self.setAggress(aggress)
		self.deathsound = pygame.mixer.Sound("sounds/dragondeath.wav")
		self.deathsound.set_volume(1)
		self.movesound = pygame.mixer.Sound("sounds/slimemove.wav")
		self.movesound.set_volume(.2)
		self.attacksound = pygame.mixer.Sound("sounds/slimemove.wav")
		self.setSpeed(1)
		
class Voodoo(Enemy):
	def __init__ (self, rect, aggress = True, animSpeed = 6):
		super(Voodoo,self).__init__(5, [(0, 229, 55, 66), (0, 229, 55, 66), (56, 229, 55, 66), (112, 229, 55, 66), (168, 229, 55, 66), (224, 229, 55, 66), (280, 229, 55, 66),
							(336, 229, 55, 66), (392, 229, 55, 66), (448, 229, 55, 66)], pygame.Rect(rect[0],rect[1],36,46), animSpeed, True)
		self.setDev(-10,-10)
		self.setAggress(aggress)
		self.deathsound = pygame.mixer.Sound("sounds/voodoodeath.wav")
		self.deathsound.set_volume(1)
		self.movesound = pygame.mixer.Sound("sounds/slimemove.wav")
		self.movesound.set_volume(.2)
		self.attacksound = pygame.mixer.Sound("sounds/slimemove.wav")
		self.setSpeed(2)
	
class Squirrel(Enemy):
	def __init__ (self, rect, aggress = True, animSpeed = 20):
		super(Squirrel,self).__init__(2, [(0, 295, 33, 36), (33, 295, 33, 36), (66, 295, 33, 36), (99, 295, 33, 36), (66, 295, 33, 36),(66, 295, 33, 36), (66, 295, 33, 36),
								(99, 295, 34, 36), (99, 295, 34, 36), (99, 295, 34, 36)], pygame.Rect(rect[0],rect[1],10,12), animSpeed, True)
		self.setDev(-12,-12)
		self.setAggress(aggress)
		self.deathsound = pygame.mixer.Sound("sounds/squirreldeath.wav")
		self.deathsound.set_volume(1)
		self.movesound = pygame.mixer.Sound("sounds/slimemove.wav")
		self.movesound.set_volume(.2)
		self.attacksound = pygame.mixer.Sound("sounds/slimemove.wav")
		self.setSpeed(5)
	
