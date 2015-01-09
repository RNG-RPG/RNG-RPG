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