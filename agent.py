#Edward Zhou
#1/9/15
#basic unit template

import pygame
pygame.init()
class Agent:

	#Constructor
	def __init__ (self,hp,mp,exp, level, attack):
		self.maxHP=hp
		self.HP=hp
		self.maxMP=mp
		self.MP=mp
		self.exp=exp
		self.level = level
		self.upgrade_Points = 1
		self.maxEXP = 10
		self.attack = attack
		self.attackSpeed = 30
		self.hacked = False
		self.tempMaxHP = 0
		self.tempMaxMP = 0
		self.tempattSpeed = 0
		
	#accessors   
	def hack(self):
		if self.hacked == False:
			print ( "bug testing hack activated" )
			self.tempMaxHP = self.maxHP
			self.tempMaxMP = self.maxMP
			self.tempattaSpeed = self.attackSpeed
			self.hacked = True
			self.maxHP=1000000
			self.HP=1000000
			self.maxMP=1000000
			self.MP=1000000
			self.attackSpeed = 3
			print self.maxHP, self.HP, self.maxMP, self.MP, self.attackSpeed
		else:
			print ( "bug testing hack deactivated" )
			self.hacked = False
			self.maxHP = self.tempMaxHP
			self.HP = self.tempMaxHP
			self.maxMP = self.tempMaxMP
			self.MP = self.tempMaxMP
			self.attackSpeed = self.tempattSpeed
			print self.maxHP, self.HP, self.maxMP, self.MP, self.attackSpeed
			
		
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
		if self.exp >= ((self.level ** 2) * 10):
			self.exp = self.exp - ((self.level ** 2)*10)
			self.level += 1
			self.maxEXP = ((self.level ** 2) * 10)
			self.upgrade_Points += 1
			print( "upgrade points", self.upgrade_Points )
	
	def getEXP(self):
		return self.exp
	
	def getMaxEXP(self):
		return self.maxEXP
	
	def getLevel(self):
		return self.level
	
	def getUP(self):
		return self.upgrade_Points
	
	def changeUP(self, change):
		self.upgrade_Points += change
	
	def getAttack(self):
		return self.attack
		
	def setAttack(self, newAttack):
		self.attack = newAttack
	
	def getSpeed(self):
		return self.attackSpeed
	
	def setSpeed(self, newSpeed):
		self.attackSpeed = newSpeed

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
		
class Dialogue(NPC):
	def __init__(self, message):
		super(Dialogue, self).__init__([(152, 0, 38, 60),(152, 0, 38, 60),(152, 0, 38, 60),(152, 0, 38, 60)], -500,-500)
		self.setMessage(message)
		
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
    def __init__ (self, hp, spriteMap, rect, animSpeed, attack=1, EXP=1, directionSprites=False, coward= False):
        self.coward = coward
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
        self.EXP = EXP
	self.treeClock = 0
	self.treeIdle = 0
        
        self.xDev = 0
        self.yDev = 0
        self.directional = directionSprites
        self.internalDClock = 60
        self.internalMClock = -1
        self.idleCounter = 0
        self.directionalCache = self.spriteMap[0]
        self.aggro = False
        self.deadcount= 0
    
    def setDirectional(self, bool):
        self.directional = bool
    def isDirectional(self):
        return self.directional
    def getSprites(self):
        return self.spriteMap
    def setSpriteMap(self, map):
        self.spriteMap = map
    def setCoward(self,bool):
        self.coward= bool
        
    #if spriteMap has directional movements -> automatically grabs the right sprite
    def getCurrentSprite(self):
        if self.directional:
            if self.dead:
				if isinstance(self,TreeBeard):
					self.treeClock += 1
					if self.treeClock > 5:
						self.treeClock = 0
						self.treeIdle = (self.treeIdle + 1)%2
					return self.spriteMap[self.treeIdle - 2]
				else:
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
    def getEXP(self):
        return self.EXP
    def getHP(self):
        return self.HP
    def getAttack(self):
        return self.attack
    def setAttack(self,new):
        self.attack = new
    def setDead(self, boo):
        if boo == True:
            self.dead = True
        elif boo == False:
            self.dead = False
    def isDead(self):
        return self.dead
    def ressurect(self, reco = False, rect= 0):
        if reco == True:
        	self.Rect = rect
        self.dead = False
        self.HP = self.maxHP
        self.hoSpeed = 0
        self.vertSpeed = 0
        self.setAggro(False)
        self.deadcount= 0
        

class Slime(Enemy):
	def __init__ (self, rect, aggress = True, animSpeed = 5, color = "blue"):
		color1 = None
		if color == "blue":
			color1 = [(0, 154, 50, 50), (50, 154, 50, 50), (0, 154, 50, 50), (100, 154, 50, 50), (150, 154, 50, 50)]
		elif color == "pink":
			color1 = [(200, 154, 50, 50), (250, 154, 50, 50), (200, 154, 50, 50), (300, 154, 50, 50), (350, 154, 50, 50)]
		elif color == "green":
			color1 = [(400, 154, 50, 50), (450, 154, 50, 50), (400, 154, 50, 50), (500, 154, 50, 50), (550, 154, 50, 50)]
		else:
			color1 = [(600, 154, 50, 50), (650, 154, 50, 50), (600, 154, 50, 50), (700, 154, 50, 50), (750, 154, 50, 50)]
		super(Slime,self).__init__(3, color1, pygame.Rect(rect[0],rect[1], 10, 10), animSpeed, 2, 7, False)
		self.setDev(-20,-20)
		self.setAggress(aggress)
		self.deathsound = pygame.mixer.Sound("sounds/slimedeath.wav")
		self.deathsound.set_volume(1)
		self.movesound = pygame.mixer.Sound("sounds/slimemove.wav")
		self.movesound.set_volume(.2)
		self.attacksound = pygame.mixer.Sound("sounds/slimemove.wav")
		self.setSpeed(3)

class Dragon(Enemy):
    def __init__ (self, rect, aggress = True, animSpeed = 10, mapS = [(0, 0, 114, 154), (114, 0, 114, 154), (228, 0, 114, 154)]):
        super(Dragon,self).__init__(25, mapS, pygame.Rect(rect[0], rect[1],34, 74), animSpeed,5,100, False)
        self.setAggro(True)    
        self.setDev(-40,-40)
        self.setAggress(aggress)
        self.deathsound = pygame.mixer.Sound("sounds/dragondeath.wav")
        self.deathsound.set_volume(1)
        self.movesound = pygame.mixer.Sound("sounds/slimemove.wav")
        self.movesound.set_volume(.2)
        self.attacksound = pygame.mixer.Sound("sounds/dragonattack.wav")
        self.setSpeed(2)
                
class TreeBeard(Dragon):
    def __init__ (self, rect):
        super(TreeBeard, self).__init__(rect, True, 10, [(0, 331, 201 ,227), (0, 331, 201 ,227), (201, 331, 201 ,227), (201, 331, 201 ,227), (402, 331, 201 ,227), (402, 331, 201 ,227), (0, 331, 201 ,227), (0, 331, 201 ,227),(603, 331, 201 ,227), (603, 331, 201 ,227), (804, 321, 201, 237), (1005, 321, 201, 237)])
        self.setAggro(False)
        self.changeRect(pygame.Rect(rect[0], rect[1], 121, 147))
        self.deathsound.set_volume(0)
        self.setDirectional(True)
        self.deathsound = pygame.mixer.Sound("sounds/treedeath.wav")
        self.deathsound.set_volume(1)
        self.attacksound = pygame.mixer.Sound("sounds/dragonattack.wav")
        self.setSpeed(0)
        
		
class Voodoo(Enemy):
	def __init__ (self, rect, aggress = True, animSpeed = 6):
		super(Voodoo,self).__init__(8, [(0, 229, 55, 66), (0, 229, 55, 66), (56, 229, 55, 66), (112, 229, 55, 66), (168, 229, 55, 66), (224, 229, 55, 66), (280, 229, 55, 66),
							(336, 229, 55, 66), (392, 229, 55, 66), (448, 229, 55, 66), (504, 229, 55, 66)], pygame.Rect(rect[0],rect[1],36,46), animSpeed,3, 20, True)
		self.setDev(-10,-10)
		self.setAggress(aggress)
		self.deathsound = pygame.mixer.Sound("sounds/voodoodeath.wav")
		self.deathsound.set_volume(1)
		self.movesound = pygame.mixer.Sound("sounds/slimemove.wav")
		self.movesound.set_volume(.2)
		self.attacksound = pygame.mixer.Sound("sounds/slimemove.wav")
		self.setSpeed(3)
	
class Squirrel(Enemy):
	def __init__ (self, rect, aggress = True, animSpeed = 5):
		super(Squirrel,self).__init__(2, [(0, 295, 33, 36), (33, 295, 33, 36), (66, 295, 33, 36), (99, 295, 33, 36), (66, 295, 33, 36),(0, 295, 33, 36), (66, 295, 33, 36),
								(99, 295, 33, 36), (99, 295, 33, 36), (33, 295, 33, 36), (132,295,35, 36)], pygame.Rect(rect[0],rect[1],10,12), animSpeed,1, 5, True)
		self.setDev(-12,-12)
		self.setAggress(aggress)
		self.deathsound = pygame.mixer.Sound("sounds/squirreldeath.wav")
		self.deathsound.set_volume(1)
		self.movesound = pygame.mixer.Sound("sounds/slimemove.wav")
		self.movesound.set_volume(.2)
		self.attacksound = pygame.mixer.Sound("sounds/slimemove.wav")
		self.setSpeed(5)
	
class Deer(Enemy):
	def __init__ (self, rect, aggress = True, animSpeed = 5):
		super(Deer,self).__init__(4, [(0, 559, 149, 122), (149, 559, 149, 122), (298, 559, 149, 122), (447, 559, 149, 122), (596, 559, 149, 122),(745, 559, 149, 122), (745, 559, 149, 122),
								(447, 559, 149, 122), (447, 559, 149, 122), (298, 559, 149, 122), (899,559,149, 122)], pygame.Rect(rect[0],rect[1],89,62), animSpeed,1, 5, True)
		self.setDev(-30,-30)
		self.setAggress(aggress)
		self.deathsound = pygame.mixer.Sound("sounds/deerdeath.wav")
		self.deathsound.set_volume(1)
		self.movesound = pygame.mixer.Sound("sounds/slimemove.wav")
		self.movesound.set_volume(.2)
		self.attacksound = pygame.mixer.Sound("sounds/slimemove.wav")
		self.setSpeed(5)
			
class Mayor(Enemy):
	def __init__ (self, rect, aggress = True, animSpeed = 5):
		super(Mayor,self).__init__(40, [(342, 0, 38, 60),(342, 0, 38, 60),(342, 0, 38, 60),(342, 0, 38, 60),(380, 0, 38, 60),(380, 0, 38, 60),(456, 0, 38, 60),(456, 0, 38, 60),
										(418, 0, 38, 60),(418, 0, 38, 60),(494, 0, 38 ,60)], pygame.Rect(rect[0],rect[1],28,50), animSpeed,5, 5, True)
		self.setDev(-5,-5)
		self.setAggress(aggress)
		self.deathsound = pygame.mixer.Sound("sounds/mayordeath.wav")
		self.deathsound.set_volume(1)
		self.movesound = pygame.mixer.Sound("sounds/slimemove.wav")
		self.movesound.set_volume(.2)
		self.attacksound = pygame.mixer.Sound("sounds/dragonattack.wav")
		self.setSpeed(1)

class Shield(Enemy):
	def __init__ (self, rect, aggress = True, animSpeed = 5):
		super(Shield,self).__init__(5, [(342, 60, 77, 80),(342, 60, 77, 80),(342, 60, 77, 80),(342, 60, 77, 80),(342, 60, 77, 80),(342, 60, 77, 80),(342, 60, 77, 80),(342, 60, 77, 80),
										(342, 60, 77, 80),(342, 60, 77, 80),(342, 60, 77, 80),(419, 60, 77, 80) ], pygame.Rect(rect[0],rect[1],57,60), animSpeed,5, 0, True)
		self.setDev(-10,-10)
		self.setAggress(aggress)
		self.deathsound = pygame.mixer.Sound("sounds/shielddeath.wav")
		self.deathsound.set_volume(.1)
		self.movesound = pygame.mixer.Sound("sounds/slimemove.wav")
		self.movesound.set_volume(.2)
		self.attacksound = pygame.mixer.Sound("sounds/slimemove.wav")
		self.setSpeed(1)
