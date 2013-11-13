#-------------------------------------------------------------------------------
# Name: Chunin Exam (Final Project)
# Purpose: A Text based game based on the naruto tv series.
# we opted to use the command line interface rather than implement a gui
# this allowed us to spend more time on a more complicated battle system
#
#
# Author:   Cplew (Caleb Plew) and Aaron stall
#
# Created:     27/10/2013
#-------------------------------------------------------------------------------
#------------------------ classes and charecters -----------#
import random
import math



class player(object):
    def __init__(self, local = "home", points = 1000, score = 0, baseA = 5, speed = 10, baseS = 10, baseC = 100 , baseST = 50, stamina = 50, baseH = 100, health = 100, chakra = 100, inventory = [], jutsu  = [], style = "none", gekkei = "none"):
        object.__init__(self)
        self.points = 100
        self.score = 0
        self.baseH = 100
        self.baseC = 100
        self.health = 100
        self.chakra = 100
        self.baseA = 5
        self.baseST = 50
        self.stamina = 50
        self.baseS= 10
        self.speed = 10
        self.inventory = []
        self.jutsu = []
        self.local = ""
        self.style = "none" #ninja type, eg. ninjutsu, genjutsu, taijutsu#
        self.gekkei = "none" #sharingan, byakugan, etc#

    def getstats(self):
        # for debugging #
        print "where im from: " + self.local
        print "points: " + str(self.points)
        print "score: " + str(self.score)
        print "Base health and health: " + str(self.baseH) +" / "+ str(self.health)
        print "base chakra: " + str(self.baseC) + " / " + str(self.chakra)
        print "base attack: " + str(self.baseA)
        print "base Stamina: " + str(self.baseST) + "/" + str(self.stamina)
        print "speed: " + str(self.baseS) + " / " + str(self.speed)
        print "inv: "
        print self.inventory
        print "jutsus i know: "
        print self.jutsu
        print "what type of ninja i am: " + self.style
        print "any kekei genkai i have: " + self.gekkei


    def reset(self):
        #makes stats back to base for healing and battles
        self.health = self.baseH
        self.chakra = self.baseC
        self.speed = self.baseS
        self.stamina = self.baseST

#------------- standard opponent, random style---#
class opponent (object):
    def __init__(self, local = "home", baseA = 5, speed = 10, baseS = 10, baseC = 100 , baseST = 50, baseH = 100, health = 100, chakra = 100, inventory = [], jutsu  = [], style = "none", gekkei = "none"):
        object.__init__(self)
        self.baseH = 100
        self.baseC = 100
        self.health = 100
        self.chakra = 100
        self.baseA = 5
        self.baseST = 50
        self.baseS= 10
        self.speed = 10
        self.inventory = []
        self.jutsu = []
        self.local = ""
        self.style = "none" #ninja type, eg. ninjutsu, genjutsu, taijutsu#
        self.gekkei = "none" #sharingan, byakugan, etc#

#---------- bosses-Creator: Aaron stall--------------#
class gaara(object):
    pass
class sasuke(object):
    pass

class naruto (object):
    pass

class neji(object):
    pass

class lee (object):
    pass

#------------------------creator: Caleb Plew---------------------------------#

def battle():
    o = opponent()
    j = Jutsu()
    if p.score < 3:
        # pass opponent through generation to create a unique opponent #
        pass
        print "Your Opponent will be a %s ninja." % o.local
        print "Your opponent is a %s" % o.style
        print "BEGIN BEST OF THREE"
        incombat = True
        while incombat:
            if p.speed >= o.speed:
                turn = 1
            else:
                turn = 2
            #the range variables, determines what moves can be used
            Range = 0
            Dist = ""
            if Range == 0:
                Dist = "Melee Range"
            if Range == 1:
                Dist = "Near"
            if Range == 2:
                Dist = "Middle"
            if Range == 3:
                Dist = "Far"
            #is the player or oppoenent defending?#  
            odef = False
            pdef = False
            
            #are you or the opponent charging mp?
            pcharge = False
            ocharge = False
            
            while turn == 1:
                print "You watch your opponent" 
                print "the enemy is %s" % Dist
                if odef == True:
                    print "the enemy is in a defensive stance"
                if pdef == True:
                    print "You are in a defensive stance, you still have %s Stamina" % str(p.stamina)
                fight0 = raw_input("What do you do? ____ Attack: 1, Defend: 2, Build Chakra: 3, use an item: 4, move: 5.")
                fight0 = int(fight0)
                if fight0 == 1:
                    fight1 = raw_input(" Melee: 1, Jutsu: 2")
                    fight1 = int(fight1)
                    if fight1 == 1:
                        if Range >= 1:
                            print "You are too far from the opponent to do that!"
                        else: 
                            
                    if fight1 == 2:
                        fight2 = raw_input("Which jutsu will you use? offensive: 1, defensive 2")
                        fight2 = int(fight2)
                        if fight2 == 1:
                            pass
                        if fight2 == 2:
                            pass
                if fight0 == 2:
                    print "You settle into a defenseive stance"
                    pdef = True
                        #end turn and go to opponent ai












def intro():
    print "Welcome to the Ninja Exams! After years of training you will now fight other ninja students for your rank as master ninja"
    print "First, where are you from?"
    origin = raw_input("Hidden Leaf:1, Hidden Sand: 2, Hidden Cloud: 3, Hidden mist: 4, Hidden stone: 5")
    origin = int(origin)
    if origin == 1:
        p.local = "Hidden Leaf"
        p.baseA += 1
        p.baseS += 2
        p.baseST -= 10
        p.baseH += 25
    if origin == 2:
        p.local = "Hidden Sand"
        p.baseS -= 3
        p.baseST += 20
        p.baseC -= 25
    if origin == 3:
        p.local = "Hidden Cloud"
        p.baseS += 10
        p.baseC += 25
        p.baseST -= 10
    if origin == 4:
        p.local = "Hidden Mist"
        p.baseS += 3
        p.baseA += 1
        p.baseH -= 25
    if origin == 5:
        p.local = "Hidden Stone"
        p.baseS -= 5
        p.baseH += 50
        p.baseA -= 1

    choice = raw_input("What class of ninja are you?  Ninjutsu: 1, Taijutsu: 2, Genjutsu: 3")
    choice = int(choice)
    if choice == 1:
        p.style = "Ninjutsu specialist"
        p.baseC += 25
        p.baseA += 3
    if choice == 2:
        p.style = "Taijustsu specialist"
        p.baseA += 3
        p.baseST += 30
        p.baseS += 5
    if choice == 3:
        p.style = "Genjustu specialist"
        p.baseC += 75
        p.baseS += 8
        p.baseST -= 30
        p.baseA -= 3



#--- list of the jutsus -(skills/powers), we decided to render them as functions
#--- since the skills had wildly varying effects
#--- basic/advanced shield, basic/advanced strike, rasengan, chidori,
#--- basic advanced healing, sharingan(passive, active), byakugan, sand shield,
#--- shinra tensei, jutsu barrier, phantom flute, mangekyo

class Jutsu(object):
    def __init__(self):
        object.__init__(self)


    def bc_strike():
        pass
    def ac_strike():
        pass




gekkei = ["Sharingan", "Byakugan", "", ""]

p = player()

def main():

    intro()
    p.reset()
    p.getstats()
    battle()




if __name__ == '__main__':
    main()
