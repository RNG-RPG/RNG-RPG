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
        
class Enemy(object):

    #Constructor
    '''spritemap is this format (source x, source y, width, height)
    directional: down idle, down idle2, down1,down2,righ1,righ2,up1,up2,left1,left2, dead
    '''
    def __init__ (self, hp, spriteMap, rect, animSpeed, directionSprites=False):
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
        
        self.xDev = 0
        self.yDev = 0
        self.directional = directionSprites
        self.internalDClock = 60
        self.internalMClock = -1
        self.idleCounter = 0
        self.directionalCache = self.spriteMap[0]
        self.aggro = False
        
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
                    self.directionalCache = self.spriteMap[(self.idleCounter+1) % 2]
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
    def isDead(self):
        return self.dead
    def ressurect(self):
        self.dead = False
        self.HP = self.maxHP
        self.hoSpeed = 0
        self.vertSpeed = 0
        self.setAggro = False

class Slime(Enemy):
	def __init__ (self, hp, spriteMap, rect, animSpeed, directionSprites=False):
		super(Slime,self).__init__(hp, spriteMap, rect, animSpeed, directionSprites)
		self.deathsound = pygame.mixer.Sound("sounds/slimedeath.wav")
		self.deadcount= 0

class Dragon(Enemy):
	def __init__ (self, hp, spriteMap, rect, animSpeed, directionSprites=False):
		super(Dragon,self).__init__(hp, spriteMap, rect, animSpeed, directionSprites)
		self.deathsound = pygame.mixer.Sound("sounds/slimedeath.wav")
		self.deadcount= 0
	
class Voodoo(Enemy):
	def __init__ (self, hp, spriteMap, rect, animSpeed, directionSprites=False):
		super(Voodoo,self).__init__(hp, spriteMap, rect, animSpeed, directionSprites)
		self.deathsound = pygame.mixer.Sound("sounds/slimedeath.wav")
		self.deadcount= 0
	

class Squirrel(Enemy):
	def __init__ (self, hp, spriteMap, rect, animSpeed, directionSprites=False):
		super(Squirrel,self).__init__(hp, spriteMap, rect, animSpeed, directionSprites)
		self.deathsound = pygame.mixer.Sound("sounds/slimedeath.wav")
		self.deadcount= 0
	
