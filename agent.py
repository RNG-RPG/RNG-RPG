#Edward Zhou
#1/9/15
#basic unit template

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
        
class Enemy:

    #Constructor
    '''spritemap is this format (source x, source y, width, height)
    '''
    def __init__ (self, hp, spriteMap, rect, animSpeed):
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
        
    def getSprites(self):
        return self.spriteMap
    def getCurrentSprite(self):
        return self.spriteMap[self.activeSprite]
    #this is a number for active sprite
    def changeSprite(self, newNum):
        self.activeSprite = newNum
    def getSpriteNumber(self):
        return self.activeSprite
        
    def setHSpeed(self, x):
        self.hoSpeed = x
    def setVSpeed(self, y):
        self.vertSpeed = y
    def getHSpeed(self):
        return self.hoSpeed
    def getVSpeed(self):
        return self.vertSpeed
    
   
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