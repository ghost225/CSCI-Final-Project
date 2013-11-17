#-------------------------------------------------------------------------------
# Name: Chunin Exam (Final Project)
# Purpose: A Text based arena combat game based on the naruto tv series.
# we opted to use the command line interface rather than implement a gui
# this allowed us to spend more time on a more complicated battle system
# that and the command line interface has a certain minimilistic appeal.
#
# Author:   Cplew (Caleb Plew) and Aaron stall
#
# Created:     27/10/2013
#-------------------------------------------------------------------------------


#------------------------ classes and charecters (mostly aarons work) -----------#
import random
from random import *
import math
import time
import cPickle



class player(object):
    def __init__(self, local = "home", points = 1000, score = 0, baseA = 5,bandages = 5, foodpills = 10, kunai = 10, shruiken = 5,speed = 10, baseS = 10, baseC = 100 , baseST = 50, stamina = 50, baseH = 100, health = 100, chakra = 100, jutsu1 = 0, jutsu2 = 0, jutsu3 = 0, jutsu4 = 0, style = "none", gekkei = "none"):
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
        self.foodpills = 10
        self.kunai = 5
        self.bandages = 5
        self.shruiken = 5
        self.jutsu1 =""
        self.jutsu2 =""
        self.jutsu3 =""
        self.jutsu4 =""
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
        print "i have %s foodpills" % self.foodpills
        print "i have %s kunai knives" % self.kunai
        print "i have %s shruiken" % self.shruiken
        print "what type of ninja i am: " + self.style
        #print "any kekei genkai i have: " + self.gekkei


    def reset(self):
        #makes stats back to base for healing and battles
        self.health = self.baseH
        self.chakra = self.baseC
        self.speed = self.baseS
        self.stamina = self.baseST
#create the player instance
p = player()

def wait(x):
    time.sleep(x)
#------------- standard opponent, random style---#
class opponent (object):
    def __init__(self, local = "home",ai = 0, baseA = 5, speed = 10, baseS = 10, baseC = 100 , baseST = 50, stamina = 50, baseH = 100, health = 100, chakra = 100, inventory = [], jutsu  = [], style = "none", gekkei = "none"):
        object.__init__(self)
        self.baseH = 100
        self.baseC = 100
        self.health = 100
        self.chakra = 100
        self.baseA = 5
        self.baseST = 50
        self.stamina = 50
        self.baseS= 10
        self.speed = 10
        self.local = ""
        self.style = "none" #ninja type, eg. ninjutsu, genjutsu, taijutsu#
        self.gekkei = "none" #sharingan, byakugan, etc#
        self.ai = 0
    def reset(self):
        #makes stats reset to base values for healing and battles
        self.health = self.baseH
        self.chakra = self.baseC
        self.speed = self.baseS
        self.stamina = self.baseST

    def randomize(self):
        #makes unique opponents to fight
        ran = randint(1, 5)
        if ran == 1:
            self.local = "Hidden Leaf"
            self.baseA += 1
            self.baseS += 2
            self.baseST -= 10
            self.baseH += 25
        if ran == 2:
            self.local = "Hidden Sand"
            self.baseS -= 3
            self.baseST += 20
            self.baseC -= 25
        if ran == 3:
            self.local = "Hidden Cloud"
            self.baseS += 10
            self.baseC += 25
            self.baseST -= 10
        if ran == 4:
            self.local = "Hidden Mist"
            self.baseS += 3
            self.baseA += 1
            self.baseH -= 25
        if ran == 5:
            self.local = "Hidden Stone"
            self.baseS -= 5
            self.baseH += 50
            self.baseA -= 1

        stylez = randint(1,3)
        if stylez == 1:
            self.style = "Ninjutsu specialist"
            self.baseC += 25
            self.baseA += 3
        if stylez == 2:
            self.style = "Taijustsu specialist"
            self.baseA += 3
            self.baseST += 30
            self.baseS += 5
        if stylez == 3:
            self.style = "Genjustu specialist"
            self.baseC += 75
            self.baseS += 8
            self.baseST -= 30
            self.baseA -= 3







#---------- bosses-------------------------Creator: Aaron stall--------------#
class gaara(object):
     def __init__(self, local = "Hidden Sand", baseA = 6, speed = 5, baseS = 5, baseC = 200, baseST = 150, baseH = 200, health = 200, chakra = 200, invertory = [], jutsu = [], style = "ninjutsu", gekkei = "none"):
        object.__init__(self)
        self.baseH = 200
        self.baseC = 200
        self.health = 200
        self.chakra = 200
        self.baseA = 6
        self.baseST = 150
        self.baseS = 5
        self.speed = 5
        self.inventory = []
        self.jutsu = []
        self.local = "Hidden Sand"
        self.style = "ninjutsu"
        self.gekkei = "none"
        
class sasuke(object):
     def __init__(self, local = "Hidden Leaf", baseA = 10, speed = 20, baseS = 20, baseC = 125, baseST = 50, baseH = 150, health = 150, chakra = 125, inventory = [], jutsu = [], style = "ninjutsu", gekkei = "sharingan"):
        object.__init__(self)
        self.baseH = 150
        self.baseC = 125
        self.health = 150
        self.chakra = 125
        self.baseA = 10
        self.baseST = 50
        self.baseS = 20
        self.speed = 20
        self.inventory = []
        self.justu = []
        self.local = "Hidden Leaf"
        self.style = "ninjutsu"
        self.gekkei = "sharingan"

class naruto (object):
    def __init__(self, local = "Hidden Leaf", baseA = 7, speed = 15, baseS = 15, baseC = 200, baseST = 100, baseH = 100, health = 100, chakra = 200, inventory = [], jutsu = [], style = "taijutsu", gekkai = "none"):
        object.__init__(self)
        self.baseH = 100
        self.baseC = 200
        self.health = 100
        self.chakra = 200
        self.baseA = 7
        self.baseST = 100
        self.baseS = 15
        self.speed = 15
        self.inventory = []
        self.jutsu = []
        self.local = "Hidden Leaf"
        self.style = "taijutsu"
        self.gekkei = "none"

class neji(object):
    def __init__(self, local = "Hidden Leaf", baseA = 8, speed = 15, baseS = 15, baseC = 150, baseST = 75, baseH = 125, health = 125, chakra = 150, inventory = [], jutsu = [], style = "taijutsu", gekkei = "byakugan"):
        object.__init__(self)
        self.baseH = 125
        self.baseC = 150
        self.health = 125
        self.chakra = 150
        self.baseA = 8
        self.baseST = 75
        self.baseS = 15
        self.speed = 15
        self.inventory = []
        self.justu = []
        self.local = "Hidden Leaf"
        self.style = "taijutsu"
        self.gekkei = "byakugan"

class lee (object):
    def __init__(self, local = "Hidden Leaf", baseA = 9, speed = 20, baseS = 20, baseC = 50, baseST = 100, baseH = 100, health = 100, chakra = 50, inventory = [], jutsu = [], style = "taijutsu", gekkei = "none"):
        object.__init__(self)
        self.baseH = 100
        self.baseC = 50
        self.health = 100
        self.chakra = 50
        self.baseA = 9
        self.baseST = 100
        self.baseS = 20
        self.speed = 20
        self.inventory = []
        self.jutsu = []
        self.local = "Hidden Leaf"
        self.style = "taijutsu"
        self.gekkei = "none"
        
class kiba (object):
    def __init__(self, local = "Hidden Leaf", baseA = 6, speed = 15, baseS = 15, baseC = 75, baseST = 75, baseH = 100, health = 100, chakra = 75, inventory = [], jutsu = [], style = "taijutsu", gekkei = "none"):
        object.__init__(self)
        self.baseH = 100
        self.baseC = 75
        self.health = 100
        self.chakra = 75
        self.baseA = 6
        self.baseST = 75
        self.baseS = 15
        self.speed = 15
        self.inventory = []
        self.jutsu = []
        self.local = "Hidden Leaf"
        self.style = "taijutsu"
        self.gekkei = "none"

#-------------------battle mechanic-----creator: Caleb Plew--------------------#





def battle():
    def enemy_attack():
        if p.stamina > 0:
            p.stamina -= o.baseA - Range
            print "you block the enemy's attack"
            print "you feel %s" % stamina
            print ""
            wait(1)
            turn = 1

        else:
            p.health -= o.baseA - Range
            print "you try to block, but the opponents attack breaks through and does %s damage" % str(o.baseA)
            print ""
            wait(1)
            turn = 1

    def player_attack():
        print "you attack with taijutsu"
        print ""
        last = "attacking"
        if odef == True:
            if o.stamina > 0:
                o.stamina -= p.baseA
                if o.stamina >= 0:
                    o.stamina = 0
                wait(1)
                print "the opponent blocks your attack"
                print ""
                turn = 2
            else:
                o.health -= p.baseA
                print "the opponent tries to block, but your attack breaks through and does %s damage" % str(p.baseA)
                print ""
                turn = 2
        else:
            o.health -= p.baseA
            print "your attack slips through an opening and does %s damage" % str(p.baseA)
            wait(1)
            turn = 2







    if p.score < 3:
        o = opponent()
        o.randomize()
        enemy_foodpill = 10
        enemy_kunai = 5
        enemy_shruiken = 5


        print "Your Opponent will be a %s ninja." % o.local
        print ""
        print "Your opponent is a %s" % o.style
        print ""
        wait(1)
        print "BEGIN BEST OF THREE"
        incombat = True
        while incombat:
            if p.speed >= o.speed:
                turn = 1
            else:
                turn = 2
            #the range variables, determines what moves can be used
            bleeding = False
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
            if Range > 3:
                Range = 3
            if Range < 0:
                Range = 0

            # these variables are mostly for the ai's benefit,
            # allwoing it to check these to perform its needed behavior calculations

            #is the player or opponent defending?#
            odef = False
            pdef = False


            #are you or the opponent charging mp?
            pcharge = False
            ocharge = False

            #check if any passive skils are active
            peyes = False
            oeyes = False

            # stores the last two moves made by the player, eg if the last move
            # made was charging, and the move before that was another mp charge,
            # the ai will get back as fast as it can and defend itself from the
            # incoming heavy attack.

            last = ""
            previous = ""

            #creates immersive health and stamina variables
            health = ""
            stamina = ""
            if p.health > 75:
                health = "healthy"
            if p.health > 50 and p.health <= 75:
                health = "bruised"
            if p.health < 50 and p.health >= 25:
                health = "badly battered"
            if p.health < 25 and p.health >15:
                health = "heavily injured"
            if p.health < 15:
                health = "bleeding out"
                bleeding = True




            if p.stamina >= 70:
                stamina = "fully alert"
            if p.stamina < 70:
                if p.stamina >=50:
                    stamina = "a little tired"
            if p.stamina <50:
                if p.stamina >= 25:
                    stamina = "very tired"
            if p.stamina <25:
                if p.stamina > 15:
                    stamina = "utterly exhausted"
            if p.stamina <= 15:
                stamina = "like you cant even stand up"
            if p.stamina <= 0:
                p.stamina = 0


            #player turn code#
            while turn == 1:
                pdef = False
                previous = last
                print  "You are %s" % health + " and feel %s" % stamina
                if bleeding == True:
                    print "Your losing blood! use a bandage soon!"
                    p.health - 1
                    p.stamina - 10
                    p.speed - 5
                    if p.health <= 0:
                        print "Your vision fades to black and you lose consciousness"
                        print ""
                        print ""
                        print".................GAME OVER!..................."
                        end = raw_input("New game:1 quit: 2")
                        end = int(end)
                        if end == 1:
                            incombat = False
                        else:
                            playing = False
                print ""
                print "You watch your opponent"
                wait(1)
                print ""
                print "the enemy is %s" % Dist
                print ""
                if odef == True:
                    print "the enemy is in a defensive stance"
                    print ""
                if pdef == True:
                    print "You are in a defensive stance"
                    print ""
                wait(1)
                fight0 = raw_input("What do you do?... Attack: 1, Defend: 2, Build Chakra: 3, use an item: 4, move: 5.")
                fight0 = int(fight0)
                if fight0 == 1:
                    fight1 = raw_input(" Melee: 1, Jutsu: 2")
                    fight1 = int(fight1)
                    if fight1 == 1:
                        if Range >= 1:
                            print "You are too far from the opponent to do that!"
                            print ""
                        else:
                            print "you attack with taijutsu"
                            print ""
                            last = "attacking"
                            if odef == True:
                                if o.stamina > 0:
                                    o.stamina -= p.baseA
                                    if o.stamina >= 0:
                                        o.stamina = 0
                                    wait(1)
                                    print "the opponent blocks your attack"
                                    print ""
                                    turn = 2
                                else:
                                    o.health -= p.baseA
                                    print "the opponent tries to block, but your attack breaks through and does %s damage" % str(p.baseA)
                                    print ""
                                    turn = 2
                            else:
                                o.health -= p.baseA
                                print "your attack slips through an opening and does %s damage" % str(p.baseA)
                                wait(1)
                                turn = 2


                    if fight1 == 2:
                        fight2 = raw_input("Which jutsu will you use? offensive: 1, defensive 2")
                        fight2 = int(fight2)
                        if fight2 == 1:
                            pass
                        if fight2 == 2:
                            pass
                if fight0 == 2:
                    print "You settle into a defensive stance"
                    print ""
                    wait(1)
                    pdef = True
                    last = "defending"
                    turn = 2
                if fight0 == 3:
                    print "you feel renewed as you focus your chi and gather your chakra"
                    wait(1)
                    p.chakra + 20
                    p.stamina + 20
                    print ""
                    print "your chakra level is now %s" % p.chakra
                    wait(1)
                    print "you feel %s" % stamina
                    last = "charging"
                    turn = 2
                        #end turn and go to opponent ai
                if fight0 == 4:
                    item = raw_input("You reach into one of your bags... Consumables: 1, Weapons: 2")
                    item = int(item)
                    if item == 1:
                        if Range <= 0:
                            print "Your too close to the enemy to do that!"
                        else:
                            print "you feel around inside the bag and notice you still have %s foodpills" % p.foodpills + " and %s bandages" % p.bandages
                            item_consume = raw_input("use one foodpill: 1.... use one bandage: 2.... back: 3")
                            item_consume = int(item_consume)
                            if item_consume == 1:
                                if p.foodpills <= 0:
                                    print "Your out of food pills!"
                                else:
                                    p.foodpills -1
                                    wait(.5)
                                    print "you quickly swallow one of the food pills and feel it take effect..."
                                    p.health + 20
                                    wait(1)
                                    turn = 2

                            if item_consume == 2:
                                if p.bandages <= 0:
                                    print "Your out of bandages! You cant do that"
                                else:
                                    print "You take out one of the bandages and wrap it quickly around your wounds."
                                    print "you are no longer bleeding"
                                    turn = 2

#----------------------------------ai turn basic: ----------------------- #
# will later update to have 3 different types of ai, with different behavior
# based on ninja type, one aggresive (this one), one tactical ranged, and
# another a constantly healing and then melee attacking one.

            while turn == 2:
                odef = False
                print "you opponent eyes you as he plots his next move..."
                print ""
                wait(1)
                if o.ai == 0:
                    if pdef == True:
                        if Range > 0:
                            Range - 1
                            print "The enemy moves forward cautiosly"
                            print ""
                            wait(1)
                            turn = 1
                        else:
                            print "The enemy lunges forward and attacks you!"
                            print ""
                            wait(1)
                            if p.stamina > 0:
                                p.stamina -= o.baseA
                                print "you block the enemy's attack"
                                print "you have %s stamina" % p.stamina
                                print ""
                                wait(1)
                                turn = 1

                            else:
                                p.health -= o.baseA
                                print "you try to block, but the opponents attack breaks through and does %s damage" % str(o.baseA)
                                print ""
                                wait(1)
                                turn = 1
                    else:
                        if o.health < 50:
                            if Range > 0:
                                if enemy_foodpill > 0:
                                    print "the enemy uses a foodpill"
                                    o.health + 20
                                    enemy_foodpill - 1
                                    turn = 1
                                    wait(1)
                            else:
                                if Range == 0:
                                    if o.stamina > 15:
                                        odef = True
                                        print "The other ninja takes a defensive stance"
                                        turn = 1
                                    else:
                                        Range + 2
                                        print "The other ninja jumps back!"
                                        o.stamina - 20
                                        turn = 1


                        else:
                            if Range >= 1:
                                if enemy_shruiken > 0:
                                    print "the enemy ninja throws a shruiken!"
                                    enemy_shruiken - 1
                                    wait(1)
                                    if p.stamina > 0:
                                        p.stamina -= o.baseA - Range
                                        print "you block the enemy's attack"
                                        print "you feel %s" % stamina
                                        print ""
                                        wait(1)
                                        turn = 1

                                    else:
                                        p.health -= o.baseA - Range
                                        print "you try to block, but the opponents attack breaks through and does %s damage" % str(o.baseA)
                                        print ""
                                        wait(1)
                                        turn = 1
                                else:
                                    Range = 0
                                    print "the opponent suddenly dashes to fist range!"
                                    o.stamina - 30
                                    turn = 1


                            if Range == 0:
                                if last == "charging":
                                    Range = 2
                                    print "the other ninja sense your chakra increasing and jumps back quickly!"
                                    o.stamina - 30
                                    turn = 1
                                elif last =="attacking":
                                    if p.health > 50:
                                        if p.stamina > 0:
                                            p.stamina -= o.baseA - Range
                                            print "you block the enemy's attack"
                                            print "you feel %s" % stamina
                                            print ""
                                            wait(1)
                                            turn = 1

                                        else:
                                            p.health -= o.baseA - Range
                                            print "you try to block, but the opponents attack breaks through and does %s damage" % str(o.baseA)
                                            print ""
                                            wait(1)
                                            turn = 1























def intro():
    print "Welcome to the Ninja Exams! After years of training you will now fight other ninja students for your rank as master ninja"
    wait(1)
    print "load a saved game(1) or start a new game(2)?"
    wait(1)
    load = raw_input("load(1), new game (2)")
    load == int(load)
    if load == 1:
        cPickle.load(save.dat)
    else:
        print "First, where are you from?"
        origin = raw_input("Hidden Leaf:1, Hidden Sand: 2, Hidden Cloud: 3, Hidden mist: 4, Hidden stone: 5")
        origin = int(origin)
        if origin == 1:
            p.local = "Hidden Leaf"
            p.baseA += 1
            p.baseS += 2
            p.baseST -= 10
            p.baseH += 25
            p.foodpills + 5
        if origin == 2:
            p.local = "Hidden Sand"
            p.baseS -= 3
            p.baseST += 20
            p.baseC -= 25
            p.shruiken + 5
            p.foodpills - 5
        if origin == 3:
            p.local = "Hidden Cloud"
            p.baseS += 10
            p.baseC += 25
            p.baseST -= 10
            p.kunai + 5
            p.shruiken - 2
            p.foodpills - 2
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
            p.kunai + 5
            p.shruiken + 5
        if choice == 3:
            p.style = "Genjustu specialist"
            p.baseC += 75
            p.baseS += 8
            p.baseST -= 30
            p.baseA -= 3
            p.foodpills + 2
            p.shruiken - 1
            p.kunai - 3





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








def main():
    playing = True
    while playing:
        intro()
        p.reset()
        p.getstats()
        battle()




if __name__ == '__main__':
    main()
