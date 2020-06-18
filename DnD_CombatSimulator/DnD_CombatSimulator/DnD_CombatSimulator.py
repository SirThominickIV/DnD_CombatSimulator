import os           #For clearing the console
import webbrowser   #For opening hyperlinks
import random       #For rolling dice in combat

#Menu output
def menu():
        strs = ("Enter 1 to simulate battle\n"
                "Enter 2 for help\n"
                "Enter 3 for a link to DnD Beyond\"s article on how combat works\n"
                "Enter 4 for a link to my GitHub account\n"
                "Enter 5 for a link to my Linkedin Account\n"
                "Enter 6 to exit\n>")
        choice = input(strs)
        try:
            return int(choice) 
        except:
            pass

#The help, for explaining to the user how this program functions
def help():
        strs = ("The purpose of this program is to simulate a battle between two creatures, using the basic rules \n"
                "of Dungeons and Dragons. To simulate this, select the first option in the main menu. Input the \n"
                "statistics for each creature. Here is the list of the stats, and what each one means: \n\n"
                "HP = Hit points - How much health does the creature have? This number varies drastically.\n"
                "It can be as low as 5 or 10. But at higher levels, it can get into the hundreds.\n\n"
                "AC = Armor class - How hard to hit is this creature? The lowest an AC usually gets is\n"
                "around 10. Higher level creatures usually have around 15-20 AC.\n\n"
                "To Hit Bonus = The bonus a creature gets to hit the other creature. A twenty sided die \n"
                "is rolled. The number it lands on is added to the to hit bonus, and if that number meets or \n"
                "excedes the other creatue\"s AC, then the attack is successful. For lower level creatures, the \n"
                "to hit bonus will be low, arounda 2-3. For higher level creatures it will be a 8-12.\n\n"
                "Average damage = The average damage a creature does per round, assuming all of it\"s attacks \n"
                "hit. This number can range from the single digits to the 50s, to the 80s.\n\n"
                "Initiative Bonus = How quick the creature is. The higher the number, the quicker the creature \n"
                "is. This determines which creature goes first. This number usually ranges from around 0 to 5.\n\n"
                "For more detailed information on how this system works, please check out DnD Beyond\"s explanation, \n"
                "through the link in the main menu of this program.\n\n"
                "Press enter to continue . . . ")
        menucontinue = input(strs)
        return menucontinue

class Creature:
    def __init__(self, name, hp, ac, tohit, avedam, heal, initiative):
        self.name = name                    #The name
        self.hp = hp                        #How much health can it have
        self.curhp = hp                     #How much HP does it currently have
        self.ac = ac                        #How hard to hit is it
        self.tohit = tohit                  #How good at hitting it is
        self.avedam = avedam                #How much damage it does
        self.heal = heal                    #How much it heals itself, if at all
        self.initiative = initiative        #How quick is it
        self.wins = 0                       #How many times it won
        self.winpercent = 0/1               #What percentage of the time it won                 

class CreaturePair:                             #For passing both creatures with a single return
    def __init__(self, creature1, creature2):
        self.creature1 = creature1
        self.creature2 = creature2

def CreatureInput(CreatureNumber):

    if CreatureNumber == 1:
        while True:
            try:
                name1 = input("Please enter the name of the first creature:\n>")
                break
            except:
                print("Invalid input, please try again")
    else:
        while True:
            try:
                name1 = input("Please enter the name of the second creature:\n>")
                break
            except:
                print("Invalid input, please try again")
    while True:
        try:
            hp1 = int(input("Please enter the HP of " + name1 + ":\n>"))
            break
        except:
            print("Invalid input, please try again")
    while True:
        try:
            ac1 = int(input("Please enter the AC of " + name1 + ":\n>"))
            break
        except:
            print("Invalid input, please try again")
    while True:
        try:
            tohit1 = int(input("Please enter the To Hit Bonus of " + name1 + ":\n>"))
            break
        except:
            print("Invalid input, please try again")
    while True:
        try:
            avedam1 = int(input("Please enter the average damage per round of " + name1 + ":\n>"))
            break
        except:
            print("Invalid input, please try again")
    while True:
        try:
            heal1 = int(input("Please enter the average self healing per round of " + name1 + ":\n>"))
            break
        except:
            print("Invalid input, please try again")
    while True:
        try:
            int1 = int(input("Please enter the initiative of " + name1 + ":\n>"))
            break
        except:
            print("Invalid input, please try again")

    print("============================================")
    print("The first creature is " + name1)
    print("HP = " + str(hp1))
    print("AC = " + str(ac1))
    print("To Hit = " + str(tohit1))
    print("Average Damage = " + str(avedam1))
    print("Average Healing = " + str(heal1))
    print("Initiative = " + str(int1))
    print("============================================")
    print("")

    creatureR = Creature(name1, hp1, ac1, tohit1, avedam1, heal1, int1)
    return creatureR

def Main():
    os.system("cls")

    creature1 = CreatureInput(1)
    creature2 = CreatureInput(2)

    #Asking how many rounds to simulate
    while True:
        try:
            numRounds = int(input("How many rounds would you like to simulate? (Warning, excessive simulation can take a while)\n>"))
            break
        except:
            print("Invalid input, please try again")

    #Round tracking
    simmedRounds = 0
    roundresult = 0

    #Win %
    creature1winpercent = 0.00
    creature2winpercent = 0.00

    #Simulating all the rounds
    while simmedRounds != numRounds:
        roundresult = oneRound(creature1, creature2)
        if roundresult == 1:
            print("Round #" + str(simmedRounds) + " - " + str(creature1.name) + " won.")
        else:
            print("Round #" + str(simmedRounds) + " - " + str(creature2.name) + " won.")
        simmedRounds = simmedRounds + 1;

    #Final calculation
    creature1.winpercent = creature1.wins/numRounds
    creature2.winpercent = creature2.wins/numRounds

    #Final Output
    print("\n\n============================================")
    print("The first creature is " + creature1.name)
    print("HP = " + str(creature1.hp))
    print("AC = " + str(creature1.ac))
    print("To Hit = " + str(creature1.tohit))
    print("Average Damage = " + str(creature1.avedam))
    print("Average Healing = " + str(creature1.heal))
    print("Initiative = " + str(creature1.initiative))
    print("============================================")
    print("The second creature is " + creature2.name)
    print("HP = " + str(creature2.hp))
    print("AC = " + str(creature2.ac))
    print("To Hit = " + str(creature2.tohit))
    print("Average Damage = " + str(creature2.avedam))
    print("Average Healing = " + str(creature2.heal))
    print("Initiative = " + str(creature2.initiative))
    print("============================================")
    
    print("\n\n" + creature1.name + " won " + "{:.2%}".format(creature1.winpercent) + " of the time, totalling " + str(creature1.wins) + " wins.\n")
    print(creature2.name + " won " + "{:.2%}".format(creature2.winpercent) + " of the time, totalling " + str(creature2.wins) + " wins.\n")

    #Output pause
    menucontinue = input("Press enter to continue . . . ")
    return menucontinue    

#Simulate one round
def OneRound(creature1, creature2):
    #Rolling for initiative
    intRoll1 = random.randint(1,20) + creature1.initiative
    intRoll2 = random.randint(1,20) + creature2.initiative

    #Dealing with a tie
    if intRoll1 == intRoll2:
        tiebreaker = random.randint(1,2)
        if tiebreaker == 1:
            intRoll1 = intRoll2 + 1
        if tiebreaker == 2:
            intRoll2 = intRoll1 + 1

    #Resetting current HP
    creature1.curhp = creature1.hp
    creature2.curhp = creature2.hp

    if intRoll1 > intRoll2: #Depending on the initiative roll, it will change which creature goes first
        #Creature 1 goes first
        while True:
            #Creature 1's turn
            creature1.curhp = creature1.curhp + creature1.heal                              #Doing self healing
            if creature1.curhp > creature1.hp:                                              #Making sure healing won't go over a creature's max hp
                creature1.curhp = creature1.hp
            rolltohit = random.randint(1,20) + creature1.tohit                              #Rolling to hit the other creature
            if rolltohit == 1:                                                              #Checking for a miss - Rolls always miss if the roll is a 1
                pass
            elif ((rolltohit >= creature2.ac) or (rolltohit - creature1.tohit == 20)):      #Checking to see if the roll hits the other creature's AC
                creature2.curhp = creature2.curhp - creature1.avedam                        #Dealing damage to the other creature
                if rolltohit == 20:                                                         #Checking to see if the hit was a critical hit. If it was, extra damage is done
                    creature2.curhp = creature2.curhp - creature1.avedam                    #Extra damage
                if creature2.curhp <= 0:                                                    #Checking to see if the other creature died. If it did, the function ends, returning a 1
                    creature1.wins = creature1.wins + 1
                    return 1
            #Creature 2's turn
            creature2.curhp = creature2.curhp + creature2.heal
            if creature2.curhp > creature2.hp:                                                       
                creature2.curhp = creature2.hp
            rolltohit = random.randint(1,20) + creature2.tohit
            if rolltohit == 1:
                pass
            elif ((rolltohit >= creature1.ac) or (rolltohit - creature2.tohit == 20)):
                creature1.curhp = creature1.curhp - creature1.avedam
                if rolltohit == 20:
                    creature1.curhp = creature1.curhp - creature1.avedam
                if creature1.curhp <= 0:
                    creature2.wins = creature2.wins + 1
                    return 2
    else:
        #Creature 2 goes first
        while True:
            #Creature 2's turn
            creature2.curhp = creature2.curhp + creature2.heal
            if creature2.curhp > creature2.hp:                                                       
                creature2.curhp = creature2.hp
            rolltohit = random.randint(1,20) + creature2.tohit
            if rolltohit == 1:
                pass
            elif ((rolltohit >= creature1.ac) or (rolltohit - creature2.tohit == 20)):
                creature1.curhp = creature1.curhp - creature1.avedam
                if rolltohit == 20:
                    creature1.curhp = creature1.curhp - creature1.avedam
                if creature1.curhp <= 0:
                    creature2.wins = creature2.wins + 1
                    return 2
            #Creature 1's turn
            creature1.curhp = creature1.curhp + creature1.heal   
            if creature1.curhp > creature1.hp:                                                       
                creature1.curhp = creature1.hp
            rolltohit = random.randint(1,20) + creature1.tohit            
            if rolltohit == 1:                                                     
                pass
            elif ((rolltohit >= creature2.ac) or (rolltohit - creature1.tohit == 20)):     
                creature2.curhp = creature2.curhp - creature1.avedam
                if rolltohit == 20:                                      
                    creature2.curhp = creature2.curhp - creature1.avedam                
                if creature2.curhp <= 0:                      
                    creature1.wins = creature1.wins + 1
                    return 1        

#Website links
git_website = "https://github.com/SirThominickIV"
lkd_website = "https://www.linkedin.com/in/thomas-snyder-9212b7187/"
ddb_website = "https://www.dndbeyond.com/sources/basic-rules/combat"

#Main menu loop
while True:   
    os.system("cls")
    choice = menu()
    if choice == 1:
        Main()
    elif choice == 2:
        menucontinue = help()
    elif choice == 3:
        webbrowser.open_new_tab(ddb_website)
    elif choice == 4:
        webbrowser.open_new_tab(git_website)
    elif choice == 5:
        webbrowser.open_new_tab(lkd_website)
    elif choice == 6:
        break
    