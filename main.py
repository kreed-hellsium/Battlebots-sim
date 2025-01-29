#dear AP scorers i could not find a way to download my replit as anything but a zip file, it wouldnt let me upload it and i looked online and found nothing, and my teacher isnt answering so the best i can do is copy and paste the code im sorry. 
from battlebotsclass import battlebots
import random
import math

bot1 = battlebots("killrover", "titanium", "bash", "bash", "medium", "blue")
bot2 = battlebots("destroyer", "steel", "electricity", "projectile", "big", "red")
bot3 = battlebots("mace", "steel", "projectile", "bash", "small", "green")
bot4 = ("terminator", "steel", "water", "water",)
bot5 = battlebots("TheAmyTron", "titanium", "projectile", "bash", "medium", "lavander")
bot6 = battlebots("TheAlanTron", "steel", "electricity", "projectile", "big", "blue")
prerobots = [bot1, bot3, bot2, bot6, bot5]
playerrobots = []
Totalrobots = prerobots + playerrobots
#######################################################
############## Variables Parking Lot ##################
b = len(playerrobots)
c = "yes"
q = 1
#have been used: a h i j k l m x n o p q r s t u
#######################################################
############### Main Menu protocols #################
print("Welcome to battle bot simulator. Here you can build robots, or choose from robots pre-built for you, and make them fight. \n Each robot is different and designed to operate differently \n based on its attributes \n The result of each match will depend on which robot looses all of its health first. Robots can have different attack \n strategies, agility, defense mechanisms, and the likely winner of each match will be determined through an many algorithms. \n \n May the best robot win")
while q == 1:
  a = input ("\n \n                        BATTLE BOTS \n \n 1. See robot catalogue \n 2. See my robots \n 3. Build a Bot\n 4. Explain attributes/manual \n 5. Fight-choose fighters \n\n Make a selection\n")

  if a == "1":
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    for x in Totalrobots:
      print (x.__str__(), "\n")
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nreturning to main menu")
    
  if a == "2":
    if b == 0:
      print("\n you haven't made any custom robots yet. returning to main menu")
  
    else:
      print ("your custom robots are")
      for x in playerrobots:
        print( x.__str__())
      print ("\n now returning to main menu")

  if a == "3":
    print("Here you can build custom robots to fight with. You will assign it with a name, a metal type, an attack type, a defense type, a wheel size and a color. If you are unfamiliar with the specific advantages for the different options, please choose the 'explain attributes/manual' option. \n\n\nMetal types: Steel or titanium. \n\nAttack types: projectile, electricity, water, bash, or \nbulldozer. \n\nDefense types(aka defends against): projectile, electricity, water, bash, \nor bulldozer \n\nWheel size: small, medium, or big \n\ncolors: custom input.") 
    h = input("what would you like to name your robot\n")
    i = input("\nwhat metal do you want to build your robot out of? (remember choosing titanium means you have to use medium wheels)\n")
    j = input("\nwhat attack should your robot have?\n")
    k = input("\nwhat should your robot defend against\n")
    l = input("\nsmall wheels, medium wheels, or big wheels\n")
    m = input("\nwhat color for your sexy robot\n")
    if i == "titanium" and l == "small":
      print("hey hey hey...don-...dont do that. Ur done. You lost robot priviledges. Ur bouta Restart. bc..u suck. dont break rules")
      q = 2
      exit
    if i == "titanium" and l == "big":
      print("hey hey hey...don-...dont do that. Ur done. You lost robot priviledges. Ur bouta Restart.")
      q = 2
      exit
    cutiepie = battlebots(h, i, j, k, l, m) 
    playerrobots.append(cutiepie)
    Totalrobots = prerobots + playerrobots
    print (cutiepie.__str__())
    print ("now returning to main menu")
  if a == "4":
    print("                       How It Works \n \nEvery robot is an object, containing the following attributes. \nA name, a kind of metal its built with, an attack method, two \nmethods of defense, a wheel size, and a color.\n\n                       The Game\n\nEvery robot starts with a certain amount of HP, or health \npoints. For every 'turn' or round, each robot has the chance to attack, and the chance to dodge the attack thrown at them.\n \n For every turn, a random number generated 1-10 will determine whether your robot ands its attack on its opponent, or misses \nthe attack. This number is called the APP, aka, attacks per \nperiod. \n\n Another random number 1-10 decides whether your robot will dodge any attack landed on it, or take the full damage. This number is called the DPP, aka, dodges per period.\n\n for example, if the APP number is between 1 and 4, your robot would land the attack, but if its between 3 and 10, your robot misses the attack. This range can vary. The range depends on the size of wheels. Small wheels have a 30% chance of landing the attack, and a 70% chance of missing the attack per period. (APP under 4 and the robot lands the attack, APP over 3 and the robot misses the attack). However, small wheels have a 70% chance of dodging per period, and a 30% chance of taking the hit (DPP over 3 and the robot dodges, DPP under 4 and the robot gets hit).\n\n There will be however many periods per game that it takes for one of the robots to run out of health. Every time that a robot lands an attack on its opponent, that robot loses HP. \nIf a robot is attacking its opponent who's defense strategy is one that defends against that attack, the opponent will lose less HP, with a co-efficient of 2. It a robot is attacking its opponent who's defense strategy does not match with the attack, the opponent will lose more HP, with a co-efficient of 5. The damage done per hit is 2 x the damage co-efficient. \n \nEvery period will run a new DPP and APP for both the offense and the defense. It will tell you what that number was, what happened in the match, how many hp your robot started that period with, and how much it ended with.\n\n                      The build \n \nEverything you build your robot with, every choice you make, will effect your gameplay. Whether it be how much damage you do to other robots, how much health you start with, even how often your robot will attack. Its best to know what kind of game you want to be fighting, or who you'll make your opponent, before creating a robot. this way, you can plan accordingly. Read the following to understand what the attributes mean. Or, play a round blindly and see how it goes if that sounds more fun to you XD! \n\nMetal Type: You can choose between titanium metal, and steel metal. The metal you build your robots with decides how many healthpoints it starts the game with, but it also may limit you from using a certain kind of wheel, which as we read above plays a very significant role in attacking and dodging \n\n Titanium: \n-Strongest most durable metal.\n-100 HP\n-only works with medium wheels \n\n Steel:\n-less durable metal\n-75 HP\n-Works with both big and small wheels\n\nAttack type and defense type: There really is no difference gameplay wise between the attacks and defenses themselves. Theyre just for cosmetics, and are fun to play with. the only thing that they may relate to is how much damage you to your opponent. For example, if you choose an attack type that your opponent has a defense against, youll do less damage than you would if it were undefended against that attack. The following options are the types of attacks you can choose from, as well as corrasponding defenses. \n\nA: Projectile\nA: Electricity\nA: Water\nA: Bash\nA: bulldozer\n\nWheels, DDP, and APP: \n\nSmall wheels have a 70% chance of dodging per period, and a 30% chance of not dodging the attack (DPP). They have a 40% of landing thier attack, and a 60% chance of missing it(APP)\n\nMedium wheels have a 40% chance of dodging an attack, and a 60% chance of not dodging (DPP). They have a 40% chance of making thier attack, and a 60% chance of missing it(APP)\n\nBig wheels have a 30% chance of dodging an attack, and a 70% chance of not dodging. They have a 30% of missing an attack, and a 70% chance of landing it.\n\nChoose your wheels wisely! Color has no change on the robot or any effect at all. If you wanted, you could even put in random funny words for color and it would still work all the same XD!")
    
  if a == "5":
    o = input("Fightclub starts now! Enter the name of the robot you would like to choose as your fighter! please enter the name exactly as its written, or else the code wont work :( press 1 to see your options again")
    if o == "1":
      for x in Totalrobots:
        print ("\n", x.__str__(), "\n")
    if o != "1":
      o = o
      for s in Totalrobots:
        p = s.get_name()
        if o == p:
          o = s
    d = input ("Please enter the name of the robot you would like to fight against")
    for t in Totalrobots:
      u = t.get_name()
      if d == u:
        d = t
    print ("let the fight begin!")
    
    def evaluateoffense(o):
      o1 = o.get_metaltype()
      if o1 == "steel":
        o.health = 75
      if o1 == "titanium":
        o.health = 100
      o2 = o.get_defensetype()
      do2 = d.get_attacktype()
      if o2 == do2:
        o.damagecoefficient = 2
      if o2 != do2:
        o.damagecoefficient = 4
    def DPP(o):
      o3 = o.get_wheeltype()
      DPPo = (random.randint(0,10))
      print ("DPPo is", DPPo)
      if o3 == "small":
        if DPPo < 4:
          o.attacked_or_defended = "attacked"
        if DPPo > 3:
          o.attacked_or_defended = "defended"
      if o3 == "big":
        if DPPo < 4: 
          o.attacked_or_defended = "defended"
        if DPPo > 3:
          o.attacked_or_defended = "attacked"
      if o3 == "medium":
        if DPPo < 4:
          o.attacked_or_defended = "defended"
        if DPPo > 3:
          o.attacked_or_defended = "attacked"
    def APP(o):
      o4 = o.get_wheeltype()
      APPo = (random.randint(0,10))
      print ("APPo is", APPo)
      if o4 == "small":
        if APPo < 5:
          o.attack_landed_or_missed = "landed"
        if APPo > 4:
          o.attack_landed_or_missed = "missed"
      if o4 == "medium":
        if APPo < 5:
          o.attack_landed_or_missed = "landed"
        if APPo > 4:
          o.attack_landed_or_missed = "missed"
      if o4 == "big": 
        if APPo > 3:
          o.attack_landed_or_missed = "landed"
        if APPo < 4:
          o.attack_landed_or_missed = "missed"
     ############## defense protocols ################# 
    def evaluatedefense(d):
      d1 = d.get_metaltype()
      if d1 == "steel":
        d.health = 75
      if d1 == "titanium":
        d.health = 100
      d2 = d.get_defensetype()
      od2 = o.get_attacktype()
      if d2 == od2:
        d.damagecoefficient = 2
      if d2 != od2:
        d.damagecoefficient = 4
    def DPPd(d):
      d3 = d.get_wheeltype()
      DPPd = (random.randint(0,10))
      print ("DPPd is", DPPd)
      if d3 == "small":
        if DPPd < 4:
          d.attacked_or_defended = "attacked"
        if DPPd > 3:
          d.attacked_or_defended = "defended"
      if d3 == "big":
        if DPPd < 4: 
          d.attacked_or_defended = "defended"
        if DPPd > 3:
          d.attacked_or_defended = "attacked"
      if d3 == "medium":
        if DPPd < 4:
          d.attacked_or_defended = "defended"
        if DPPd > 3:
          d.attacked_or_defended = "attacked"
    def APPd(d):
      d4 = d.get_wheeltype()
      APPd = (random.randint(0,10))
      print ("APPd is", APPd)
      if d4 == "small":
        if APPd < 5:
          d.attack_landed_or_missed = "landed"
        if APPd > 4:
          d.attack_landed_or_missed = "missed"
      if d4 == "medium":
        if APPd < 5:
          d.attack_landed_or_missed = "landed"
        if APPd > 4:
          d.attack_landed_or_missed = "missed"
      if d4 == "big": 
        if APPd > 3:
          d.attack_landed_or_missed = "landed"
        if APPd < 4:
          d.attack_landed_or_missed = "missed"
      
    def fightsimulator():
      evaluatedefense(d)
      print("defense health is", d.health)
      evaluateoffense(o)
      print("offense health is", o.health)
      while o.health > 0 and d.health > 0:
        DPP(o)
        print ("offense dodge or not dodge: ")
        print (o.attacked_or_defended)
        APP(o)
        print("offense attack or missed:")
        print (o.attack_landed_or_missed)
        DPPd(d)
        print("defense dodge or not dodge: ")
        print(d.attacked_or_defended)
        APPd(d)
        print ("defense attack lnaded or missed: ")
        print (d.attack_landed_or_missed)
        if d.attack_landed_or_missed == "landed" and o.attacked_or_defended == "attacked":
          print("offense health before period")
          print (o.health)
          o.health = o.health - 2 * o.damagecoefficient
          print ("offense looses 8 points. defense attacked, offense could not dodge")
          print (o.health)
          ############################################
        if d.attack_landed_or_missed == "landed" and o.attacked_or_defended == "defended":
          print("offense health before period")
          print (o.health)
          o.health = o.health - 2
          print("attack on your fighter was landed, but your fighter dodged most of the attack")
          print("offense health after period")
          print (o.health)
          ######################################
        if o.attack_landed_or_missed == "landed" and d.attacked_or_defended == "attacked":
          print ("defense health before period")
          print (d.health)
          d.health = d.health - 2 * d.damagecoefficient
          print ("your attack on your opponent was landed, and they were unable to defend")
          print (d.health)
          #######################################
        if o.attack_landed_or_missed == "landed" and d.attacked_or_defended == "defended":
          print ("defense health before period")
          print (d.health)
          print("your attack on your oponent was landed but they defended the shot")
          d.health = d.health - 2
          print ("defense health after period")
          print (d.health)
        print ("\n------------period end-------------\n")
      if o.health > d.health:
        print("your fighter wins!")
        print("\n ending stats\n", "defense health:", d.health, "\noffense health:", o.health)
      if d.health > o.health:
        print ("your fighter loses, defending fighter wins!")
        print("\nending stats\n", "defense health:", d.health, "\noffense health:", o.health)
    fightsimulator()
