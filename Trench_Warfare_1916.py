ver=print("version 0.1.0")
#ver0.0.1
#4 sectors working in parallel

#ver0.0.2
#bugfix on line 617
#added quits
#added manual
#[some] redundant variables removed
#added flanking effects! Game cannot be completed in fewer than 9 moves

#ver0.1.0
#added a dynamic battle map!
#fixed Tanks: bonus no longer applies to overall combat power
#fixed defenders not taking damage to def on a failed assault; counter attacks are less likely to succeed
#fixed card selection when hand is empty
#balance adjusted
#play order changed
#added weather! Currently only rain works; Tank bonus is reduced when rain is rolled by the weather function
#fixed Skirmish! Skirmish now prevents counterattacks
#card descriptions improved

#ver0.1.1
#minor script edits
#player can now choose not to select a card

from random import choices, randint
defensive_line_1=0
defensive_line_2=0
defensive_line_3=0
defensive_line_4=0

combat_power_1=80
combat_power_2=80
combat_power_3=80
combat_power_4=80

defensive_potential_1=100+randint(-20, 40)
defensive_potential_2=100+randint(-20, 40)
defensive_potential_3=100+randint(-20, 40)
defensive_potential_4=100+randint(-20, 40)

front_1_defeat=None
front_2_defeat=None
front_3_defeat=None
front_4_defeat=None

victory_state=None
forecast=None
difficulty=None
tank_attack=None
tank_bonus=0
skirmishers=False
battle_sector=None

flanked_1=None
flanked_2=None
flanked_3=None
flanked_4=None
double_flanked_2=None
double_flanked_3=None
outflanked=False

ver
##### DIFFICULTY #####
def diff_setting():
    global combat_power_1
    global combat_power_2
    global combat_power_3
    global combat_power_4
    global difficulty
    diff=input("\nChoose difficulty:\n1: Don't hurt me\n2: Capable Commander\n3: There Is Only War!\nChoose: ")
    if diff=="1":
        difficulty="easy"
        combat_power_1+=20
        combat_power_2+=20
        combat_power_3+=20
        combat_power_4+=20
    elif diff=="3":
        difficulty="hard"
        combat_power_1-=20
        combat_power_2-=20
        combat_power_3-=20
        combat_power_4-=20
    elif diff=="2":
        difficulty="normal"
        combat_power_1
        combat_power_2
        combat_power_3
        combat_power_4
    else: print("try again"); diff_setting()
##### INTRO/MANUAL #####
def manual():
    print("\n\nThe objective of this game is to defeat all four of the enemy defensive lines.\nDo this by attacking when your Attacking Strength is greater than the Defensive Might of the enemy.\n\nThe Attacking Strength and Defensive Might for each Sector is shown after starting the game. Initially, your Attacking Strength will be determined by the chosen difficulty level.\n\n")
    input("****press enter****\n\n")
    print("Attacking Strength and Defensive Might are affected by many factors, but can be affected most by the tactical use of Resource Cards.\nA number of Resource Cards are selected according to the chosen difficulty, and are listed after viewing the Battle Map.\nYou must type to select a card to view its description, and accept it.\nOnly ONE card may be played per turn. \nIf you play it, the card is discarded and you may select a new one at the start of a new turn. Otherwise, you may either retain it to use on your next turn, or discard it to select a new one.\n\nResource Cards are both essential for success, and a limited resource.\nUse them wisely.\n\n")
    input("****press enter****\n\n")
    print("The battlefield is split into four Sectors.\nEach Sector must be fought seperately.\nIn order not to leave your troops exposed on their flanks, it is best not to push too far ahead in one sector.\nAllow your men either side of the spearhead to catch up, at least one defensive line behind.\nFailure to do so might invite a flanking counterattack, sometimes from both flanks.\n\nEach turn of the game is an offensive from, or defense of, one sector.\n\n")
    input("****press enter****\n\n")
    print("Success in battle is determined by ensuring your Attacking Strength is greater then the opponent's Defensive Might at the moment of advancing.\nAttacking Strength and Defensive Might are only shown before and after choosing a Resource Card, and will change if you play a card, usually in your favour.\nOr, should you decide to defend rather than advance, defending will give a moderate bonus to your Attacking Strength.\nThis will help to repel any potential counterattack by the enemy.\nCounter attacks may also trigger in the event of a failed advance.\nA successful counterattack by the enemy will push your force in that sector back to the previous defensive line.\nConversely, a successful advance will rout the enemy from their defensive line, for you to occupy.\nHowever, a fresh enemy contingent awaits in the next layer of defenses.\n\n")
    input("****press enter****\n\n")
    print("Total victory is achieved by successfully pushing the enemy out of 3 layers of defense in a single sector, achieving a breakthrough.\n\nTotal defeat occurs in the event that a sector's Attacking Strength is reduced to zero, or a sector's attacking force is pushed back beyond our starting position.\nYour war will continue until either Victory or Defeat is ours.\n\nHigh Command expects much from you. Do not make them regret placing their trust in your ability.\n\n")
    input("press enter to continue playing")
def intro():
    print("\nIt is 1916.\nYou are the commander of a handful of sectors along the Western front.\n\nYour objective:\n\nTo break the stalemate of trench warfare, and lead your men to victory.\n\nTo do this, you must push through the layers of defensive trenches the enemy is dug into — with a decisive offensive.\nBe careful not to throw away your men's lives by sending them into a fight they cannot win, or by leaving them outflanked.\nHigh command has resources available for you. Make best use of them to bring an end to this terrible conflict.\n \nGood luck, commander.\n")
    help=input("\nTo read the manual, press 'M', otherwise press enter to continue: ")
    if help=="m" or help=="M":
        manual()
###### RESOURCE CARDS #####
Cards=["Barrage", "Tanks", "Gas", "Reinforcements", "Skirmish", "Mine"]
card_lookup={"Barrage": "\nThe King of Battle.\nA battery of artillery will smash the enemy defenses, lowering their defensive potential.\n", "Tanks" : "\nThese lumbering steel land ships multiply your combat power, but are only of use in attack.\n", "Gas" : "\nA silent killer. At least, until the screams of the dying fill the toxic air.\nBe warned, a change in wind could see your own men caught.\n", "Reinforcements" : "\nA war cannot be fought without riflemen.\nFresh reserves improve our chances in both offense and defense.\n", "Skirmish" : "\nSkilled trench fighters will throw enemy defenses into disarray, lowering their defensive potential and preventing counterattack\n", "Mine" : "\nEngineers will undermine the enemy trench line and destroy it from below, drastically lowing their defensive potential.\nThe few enemy left must still be fought, however.\n"}
def diff_hand():
    global hand
    global select
    if difficulty=="easy":
        hand=choices(Cards,[8,2,1,7,3,1], k=10)
    elif difficulty=="normal":
        hand=choices(Cards,[8,2,1,7,3,1], k=8)
    elif difficulty=="hard":
        hand=choices(Cards,[8,2,1,7,3,1], k=10)
    select=""   
def select_card():
    global select
    global hand
    if select=="":
        print(f"\nYou have the following resources: \n")
        for x in hand:
            print(x)
        select=input("\nChoose, or type 'None': ")
        if select.capitalize() in hand:
            print("\nDescription:")
            print(card_lookup[select.capitalize()])
            keep=input("Keep this card?\n1: Yes\n2: No\nChoose: ")
            if keep=="1":
                hand.remove(select.capitalize())
            else:
                select=""
                select_card()
        elif select=="none" or select=="None":
            select=""
            sure=input("Continue without a resource?\n1: Yes\n2: No\nChoose: ")
            if sure!="1":
                select_card()
            else:
                input("\nIs that wise, commander?\n\n")
        else: 
            print("\nType the name of a resource to continue\n")
            select=""
            select_card()
    else:
        discard=input(f"\nYou have {select.capitalize()} available.\nDiscard?\n1: Yes\n2: No\nChoose: ")
        if discard=="1":
            select=""
        if discard=="2":
            exit
        else: select_card()
def play_card():
    global select
    global tank_attack
    if select!="":
        play=input("\nPlay your card now?\n1: Yes\n2: No\nChoose: ")
        if play=="1":
            print(f"\nPlaying: {select.capitalize()}\n")
            if select.capitalize()=="Barrage":
                Barrage()
                select=""
            elif select.capitalize()=="Tanks":
                tank_attack=True
                print("\nYour infantry will be supported by the latest in mobile armour technology\n")
                select=""
            elif select.capitalize()=="Gas":
                Gas()
                select=""
            elif select.capitalize()=="Reinforcements":
                Reinforcements()
                select=""
            elif select.capitalize()=="Skirmish":
                Skirmish()
                select=""
            elif select.capitalize()=="Mine":
                Mine()
                select=""
            else: print("Play card???")
        elif play=="2":
            exit
        else: print("Try again"); play_card()
def hand_check():
    hand.sort()
    print(f"\nYou have the following resources: \n")
    for x in hand:
        print(x)
    input("\npress enter\n")
def Gas():
    global combat_power_1
    global combat_power_2
    global combat_power_3
    global combat_power_4
    global defensive_potential_1
    global defensive_potential_2
    global defensive_potential_3
    global defensive_potential_4
    wind_chance=randint(1,20)
    print("Gas attack!")
    if wind_chance>=5:
        gas_success=True
    else: gas_success=False
    if battle_sector==1:
        if gas_success==False:
            print("Horror! The wind has changed, and your men suffer.")
            combat_power_1-=combat_power_1*(randint(2, 5)/10)
        else: 
            print("The enemy is choking and blinded")
            defensive_potential_1-=defensive_potential_1*(randint(2, 9)/10)
    if battle_sector==2:
        if gas_success==False:
            print("Horror! The wind has changed, and your men suffer.")
            combat_power_2-=combat_power_2*(randint(2, 5)/10)
        else: 
            print("The enemy is choking and blinded")
            defensive_potential_2-=defensive_potential_2*(randint(2, 9)/10)
    if battle_sector==3:
        if gas_success==False:
            print("Horror! The wind has changed, and your men suffer.")
            combat_power_3-=combat_power_3*(randint(2, 5)/10)
        else: 
            print("The enemy is choking and blinded")
            defensive_potential_3-=defensive_potential_3*(randint(2, 9)/10)
    if battle_sector==4:
        if gas_success==False:
            print("Horror! The wind has changed, and your men suffer.")
            combat_power_4-=combat_power_4*(randint(2, 5)/10)
        else: 
            print("The enemy is choking and blinded")
            defensive_potential_4-=defensive_potential_4*(randint(2, 9)/10)
    ##phosgene? chlorine? mustard? lacrimosal?
def Barrage():
    global combat_power_1
    global combat_power_2
    global combat_power_3
    global combat_power_4
    global defensive_potential_1
    global defensive_potential_2
    global defensive_potential_3
    global defensive_potential_4
    print("An artillery barrage rains death on the enemy")
    if battle_sector==1:
        defensive_potential_1-=50+randint(-20, 10)
    elif battle_sector==2:
        defensive_potential_2-=50+randint(-20, 10)
    elif battle_sector==3:
        defensive_potential_3-=50+randint(-20, 10)
    elif battle_sector==4:
        defensive_potential_4-=50+randint(-20, 10)
def Tanks():
    global combat_power_1
    global combat_power_2
    global combat_power_3
    global combat_power_4
    global tank_bonus
    if tank_attack==True and battle_sector==1:
        tank_bonus=combat_power_1*(randint(50,75)/100)
    elif  tank_attack==True and battle_sector==2:
        tank_bonus=combat_power_2*(randint(50,75)/100)
    elif  tank_attack==True and battle_sector==3:
        tank_bonus=combat_power_3*(randint(50,75)/100)
    elif  tank_attack==True and battle_sector==4:
        tank_bonus=combat_power_4*(randint(50,75)/100)
    elif tank_attack==None or tank_attack==False:
        tank_bonus=0
    else: print("TANK ERROR!!")
def Reinforcements():
    global combat_power_1
    global combat_power_2
    global combat_power_3
    global combat_power_4
    print("Fresh troops to the front")  
    if battle_sector==1:
        combat_power_1+=45+(50/(randint(3,10)))
        print(f"Attacking Strength: {combat_power_1}\n")
    elif battle_sector==2:
        combat_power_2+=45+(50/(randint(3,10)))
        print(f"Attacking Strength: {combat_power_2}\n")
    elif battle_sector==3:
        combat_power_3+=45+(50/(randint(3,10)))
        print(f"Attacking Strength: {combat_power_3}\n")
    elif battle_sector==4:
        combat_power_4+=45+(50/(randint(3,10)))
        print(f"Attacking Strength: {combat_power_4}\n")
def Skirmish():
    global defensive_potential_1
    global defensive_potential_2
    global defensive_potential_3
    global defensive_potential_4
    global skirmishers
    skirmishers=True
    print("Elite skirmishers have infiltrated the enemy line, throwing their defenses into dissarray")
    if battle_sector==1:
        defensive_potential_1*=0.5
    elif battle_sector==2:
        defensive_potential_2*=0.5
    elif battle_sector==3:
        defensive_potential_3*=0.5
    elif battle_sector==4:
        defensive_potential_4*=0.5   
def Mine():
    global defensive_potential_1
    global defensive_potential_2
    global defensive_potential_3
    global defensive_potential_4
    print("Our intrepid engineers have undermined the enemy trench with TNT. The detonation will be spectacular.")
    if battle_sector==1:
        defensive_potential_1*=(randint(10, 50)/100)
    elif battle_sector==2:
        defensive_potential_2*=(randint(10, 50)/100)
    elif battle_sector==3:
        defensive_potential_3*=(randint(10, 50)/100)
    elif battle_sector==4:
        defensive_potential_4*=(randint(10, 50)/100)
# def Pillboxes():
    # print("The defenders have prepared fortified positions!")
    # global defensive_potential_1
    # defensive_potential_1*=1.5
###### COMBAT #####
def sector_select():
    global battle_sector
    sector=input("\nSelect a sector to command:\n1: Sector 1\n2: Sector 2\n3: Sector 3\n4: Sector 4\n\nQ: Quit\nChoose: ")
    if sector=="1":
        battle_sector=1
    elif sector=="2":
        battle_sector=2
    elif sector=="3":
        battle_sector=3
    elif sector=="4":
        battle_sector=4
    elif sector=="q" or sector=="Q":
        exit()
    else: print("Try again"); sector_select()
def sector_1_combat():
    global defensive_line_1
    surprised_attackers=False
    global combat_power_1
    global defensive_potential_1
    global victory_state
    print(f"\nAttacker's strength={combat_power_1}")
    print(f"Defender's might={defensive_potential_1}")
    if select:
        print(f"\nYour card is: {select.capitalize()}")
    def advance_defend():
        global combat_power_1
        global defensive_potential_1
        global defensive_line_1
        global tank_bonus
        global skirmishers
        attack=input("\nShould this sector advance?\n1: Advance\n2: Defend\nChoose: ")
        if attack=="1":
            Tanks()
            if combat_power_1+tank_bonus>=defensive_potential_1:
                defensive_line_1+=1
                print("\n\nAttack successful!")
                combat_power_1-=(defensive_potential_1*(randint(10,25)/100))
                defensive_potential_1=0
                tank_bonus=0
            else:
                defensive_potential_1-=combat_power_1*(randint(1,5)/10)
                combat_power_1-=(defensive_potential_1*(randint(15,50)/100))
                tank_bonus=0
                print("\n\nAssault has failed!")
                if skirmishers==False:
                    counter_attack()
        elif attack=="2":
            combat_power_1+=(combat_power_1*(randint(5,15)/100))
            print("\n\nYour men brace for enemy action...")
            if skirmishers==False:
                counter_attack()
        else: print("Try again"); advance_defend()
    def counter_attack():
        global combat_power_1
        global defensive_potential_1
        global front_1_defeat
        global defensive_line_1
        print("\ncounterattacked!")
        input("\npress enter")
        if combat_power_1<=defensive_potential_1*(randint(5,9)/10):
            print("defeat!")
            defensive_line_1-=1
            if defensive_line_1<0:
                front_1_defeat=True
        else: 
            print("The enemy is repelled.\n") 
            defensive_potential_1-=combat_power_1*(randint(1,5)/10)
            combat_power_1-=defensive_potential_1*(randint(1,5)/10)
    if select:
        play_card()
    advance_defend()
    def obliteration_check():
        global defensive_potential_1
        global defensive_line_1
        if defensive_potential_1<0:
            defensive_potential_1=0
            move_up=input("\nThe enemy has abandoned their position! Quickly, move your men up to reverse their defensive line!\n\n1: Yes\n2: No\nChoose: ")
            if move_up=="1":
                defensive_line_1+=1
                flank_check()
                if flanked_1==True:
                    print("\nCommander! You forgot to check your flanks!\n")
            if move_up=="2":
                print("\nThe enemy is sure to re-occupy the trench line if you will not.\n")
            else: obliteration_check()
    obliteration_check()
    print(f"\nAttacker's remaining strength = {round(combat_power_1)}")
    print(f"Defender's remaining might    = {round(defensive_potential_1)}")
    print(f"\nTrench line reached: {defensive_line_1}\n")
def sector_2_combat():
    global defensive_line_2
    surprised_attackers=False
    global combat_power_2
    global defensive_potential_2
    global victory_state
    print(f"\nAttacker's strength={combat_power_2}")
    print(f"Defender's might={defensive_potential_2}")
    if select:
        print(f"\nYour card is: {select.capitalize()}")
    def advance_defend():
        global combat_power_2
        global defensive_potential_2
        global defensive_line_2
        global tank_bonus
        global skirmishers
        attack=input("\nShould this sector advance?\n1: Advance\n2: Defend\nChoose: ")
        if attack=="1":
            Tanks()
            if combat_power_2+tank_bonus>=defensive_potential_2:
                defensive_line_2+=1
                print("\n\nAttack successful!")
                combat_power_2-=(defensive_potential_2*(randint(10,25)/100))
                defensive_potential_2=0
                tank_bonus=0
            else:
                defensive_potential_2-=combat_power_1*(randint(1,5)/10)
                combat_power_2-=(defensive_potential_2*(randint(15,50)/100))
                print("\n\nAssault has failed!")
                tank_bonus=0
                if skirmishers==False:
                    counter_attack()
        elif attack=="2":
            combat_power_2+=(combat_power_2*(randint(5,15)/100))
            print("\n\nYour men brace for enemy action...")
            if skirmishers==False:
                counter_attack()
        else: print("Try again"); advance_defend()
        skirmishers=False
    def counter_attack():
        global combat_power_2
        global defensive_potential_2
        global front_2_defeat
        global defensive_line_2
        print("\ncounterattacked!")
        input("\npress enter")
        if combat_power_2<=defensive_potential_2*(randint(5,9)/10):
            print("defeat!")
            defensive_line_2-=1
            if defensive_line_2<0:
                front_2_defeat=True
        else: 
            print("The enemy is repelled\n") 
            defensive_potential_2-=combat_power_1*(randint(1,5)/10)
            combat_power_2-=defensive_potential_2*(randint(1,5)/10)
    if select:
        play_card()
    advance_defend()
    def obliteration_check():
        global defensive_potential_2
        global defensive_line_2
        if defensive_potential_2<0:
            defensive_potential_2=0
            move_up=input("\nThe enemy has abandoned their position! Quickly, move your men up to reverse their defensive line!\n\n1: Yes\n2: No\nChoose: ")
            if move_up=="1":
                defensive_line_2+=1
                flank_check()
                if flanked_2==True:
                    print("\nCommander! You forgot to check your flanks!\n")
            if move_up=="2":
                print("\nThe enemy is sure to re-occupy the trench line if you will not.\n")
            else: obliteration_check()
    obliteration_check()
    print(f"\nAttacker's remaining strength = {round(combat_power_2)}") ############## replace
    print(f"Defender's remaining might    = {round(defensive_potential_2)}")######## with
    print(f"\nTrench line reached: {defensive_line_2}\n")## grafix
def sector_3_combat():
    global defensive_line_3
    surprised_attackers=False
    global combat_power_3
    global defensive_potential_3
    global victory_state
    print(f"\nAttacker's strength={combat_power_3}")
    print(f"Defender's might={defensive_potential_3}")
    if select:
        print(f"\nYour card is: {select.capitalize()}")
    def advance_defend():
        global combat_power_3
        global defensive_potential_3
        global defensive_line_3
        global tank_bonus
        global skirmishers
        attack=input("\nShould this sector advance?\n1: Advance\n2: Defend\nChoose: ")
        if attack=="1":
            Tanks()
            if combat_power_3+tank_bonus>=defensive_potential_3:
                defensive_line_3+=1
                print("\n\nAttack successful!")
                combat_power_3-=(defensive_potential_3*(randint(10,25)/100))
                defensive_potential_3=0
                tank_bonus=0
            else:
                defensive_potential_3-=combat_power_3*(randint(1,5)/10)
                combat_power_3-=(defensive_potential_3*(randint(15,50)/100))
                print("\n\nAssault has failed!")
                tank_bonus=0
                if skirmishers==False:
                    counter_attack()
        elif attack=="2":
            combat_power_3+=(combat_power_3*(randint(5,15)/100))
            print("\n\nYour men brace for enemy action...")
            if skirmishers==False:
                counter_attack()
        else: print("Try again"); advance_defend()
        skirmishers=False
    def counter_attack():
        global combat_power_3
        global defensive_potential_3
        global front_3_defeat
        global defensive_line_3
        print("\ncounterattacked!")
        input("\npress enter")
        if combat_power_3<=defensive_potential_3*(randint(5,9)/10):
            print("defeat!")
            defensive_line_3-=1
            if defensive_line_3<0:
                front_3_defeat=True
        else: 
            print("The enemy is repelled\n") 
            defensive_potential_3-=combat_power_3*(randint(1,5)/10)
            combat_power_3-=defensive_potential_3*(randint(1,5)/10)
    if select:
        play_card()
    advance_defend()
    def obliteration_check():
        global defensive_line_3
        global defensive_potential_3
        if defensive_potential_3<0:
            defensive_potential_3=0
            move_up=input("\nThe enemy has abandoned their position! Quickly, move your men up to reverse their defensive line!\n\n1: Yes\n2: No\nChoose: ")
            if move_up=="1":
                defensive_line_3+=1
                flank_check()
                if flanked_3==True:
                    print("\nCommander! You forgot to check your flanks!\n")
            if move_up=="2":
                print("\nThe enemy is sure to re-occupy the trench line if you will not.\n")
            else: obliteration_check()
    obliteration_check()
    print(f"\nAttacker's remaining strength = {round(combat_power_3)}") ############## replace
    print(f"Defender's remaining might    = {round(defensive_potential_3)}")######## with
    print(f"\nTrench line reached: {defensive_line_3}\n")## grafix
def sector_4_combat():
    global defensive_line_4
    surprised_attackers=False
    global combat_power_4
    global defensive_potential_4
    global victory_state
    print(f"\nAttacker's strength={combat_power_4}")
    print(f"Defender's might={defensive_potential_4}")
    if select:
        print(f"\nYour card is: {select.capitalize()}")
    def advance_defend():
        global combat_power_4
        global defensive_potential_4
        global defensive_line_4
        global tank_bonus
        global skirmishers
        attack=input("\nShould this sector advance?\n1: Advance\n2: Defend\nChoose: ")  
        if attack=="1":
            Tanks()
            if combat_power_4+tank_bonus>=defensive_potential_4:
                defensive_line_4+=1
                print("\n\nAttack successful!")
                combat_power_4-=(defensive_potential_4*(randint(10,25)/100))
                defensive_potential_4=0
                tank_bonus=0
            else:
                defensive_potential_4-=combat_power_4*(randint(1,5)/10)
                combat_power_4-=(defensive_potential_4*(randint(15,50)/100))
                print("\n\nAssault has failed!")
                tank_bonus=0
                if skirmishers==False:
                    counter_attack()
        elif attack=="2":
            combat_power_4+=(combat_power_4*(randint(5,15)/100))
            print("\n\nYour men brace for enemy action...")
            if skirmishers==False:
                counter_attack()
        else: print("Try again"); advance_defend()
        skirmishers=False
    def counter_attack():
        global combat_power_4
        global defensive_potential_4
        global front_4_defeat
        global defensive_line_4
        print("\ncounterattacked!\n")
        input("\npress enter")
        if combat_power_4<=defensive_potential_4*(randint(5,9)/10):
            print("defeat!")
            defensive_line_4-=1
            if defensive_line_4<0:
                front_4_defeat=True
        else: 
            print("The enemy is repelled\n") 
            defensive_potential_4-=combat_power_4*(randint(1,5)/10)
            combat_power_4-=defensive_potential_4*(randint(1,5)/10)   
    if select:
        play_card()
    advance_defend()
    def obliteration_check():
        global defensive_potential_4
        global defensive_line_4
        if defensive_potential_4<0:
            defensive_potential_4=0
            move_up=input("\nThe enemy has abandoned their position! Quickly, move your men up to reverse their defensive line!\n\n1: Yes\n2: No\nChoose: ")
            if move_up=="1":
                defensive_line_4+=1
                flank_check()
                if flanked_4==True:
                    print("\nCommander! You forgot to check your flanks!\n")
            if move_up=="2":
                print("\nThe enemy is sure to re-occupy the trench line if you will not.\n")
            else: obliteration_check()
    obliteration_check()
    print(f"\nAttacker's remaining strength = {round(combat_power_4)}") ############## replace
    print(f"Defender's remaining might    = {round(defensive_potential_4)}")######## with
    print(f"\nTrench line reached: {defensive_line_4}\n")## grafix
###### OUTCOME #####
def sector_1_combat_outcome():
    global battle_sector
    global victory_state
    global front_1_defeat
    if front_1_defeat==True or defensive_line_1<0 or combat_power_1<0:
        print("\nReport immediately to High Command. Your war is over.\n")
        victory_state=False
        battle_sector=None
    else: 
        front_1_defeat=False
        if defensive_line_1==4:
            print("\nBreakthrough! \n\nAd Victoriam!")
            victory_state=True
            battle_sector=None
            
        else: 
            victory_state=None
            battle_sector=None
            quit=input("\nTo quit, press 'Q, or press enter to continue: ")
            if quit=="q" or quit=="Q":
                exit()
            print("\nThe war continues.\n")
def sector_2_combat_outcome():
    global battle_sector
    global victory_state
    global front_2_defeat
    if front_2_defeat==True or defensive_line_2<0 or combat_power_2<0:
        print("\nReport immediately to High Command. Your war is over.\n")
        victory_state=False
        battle_sector=None
    else: 
        front_2_defeat=False
        if defensive_line_2==4:
            print("\nBreakthrough! \n\nAd Victoriam!")
            victory_state=True
            battle_sector=None
            
        else: 
            victory_state=None
            battle_sector=None
            quit=input("\nTo quit, press 'Q, or press enter to continue: ")
            if quit=="q" or quit=="Q":
                exit()
            print("\nThe war continues.\n")
def sector_3_combat_outcome():
    global battle_sector
    global victory_state
    global front_3_defeat
    if front_3_defeat==True or defensive_line_3<0 or combat_power_3<0:
        print("\nReport immediately to High Command. Your war is over.\n")
        victory_state=False
        battle_sector=None
    else: 
        front_3_defeat=False
        if defensive_line_3==4:
            print("\nBreakthrough! \n\nAd Victoriam!")
            victory_state=True
            battle_sector=None
            
        else: 
            victory_state=None
            battle_sector=None
            quit=input("\nTo quit, press 'Q, or press enter to continue: ")
            if quit=="q" or quit=="Q":
                exit()
            print("\nThe war continues.\n")
def sector_4_combat_outcome():
    global battle_sector
    global victory_state
    global front_4_defeat
    if front_4_defeat==True or defensive_line_4<0 or combat_power_4<0:
        print("\nReport immediately to High Command. Your war is over")
        victory_state=False
        battle_sector=None
    else: 
        front_4_defeat=False
        if defensive_line_4==4:
            print("\nBreakthrough! \n\nAd Victoriam!")
            victory_state=True
            battle_sector=None
        else: 
            victory_state=None
            battle_sector=None
            quit=input("\nTo quit, press 'Q, or press enter to continue: ")
            if quit=="q" or quit=="Q":
                exit()
            print("\nYour war continues.\n")
def flank_check():
    global defensive_line_1
    global defensive_line_2
    global defensive_line_3
    global defensive_line_4
    global flanked_1
    global flanked_2
    global flanked_3
    global flanked_4
    global double_flanked_2
    global double_flanked_3
    if defensive_line_1>defensive_line_2+1 and not defensive_line_2<0:
        flanked_1=True
    elif defensive_line_2>defensive_line_1+1 and defensive_line_2>defensive_line_3+1 and not defensive_line_3<0 and not defensive_line_1<0:
        double_flanked_2=True
    elif defensive_line_3>defensive_line_2+1 and defensive_line_3>defensive_line_4+1 and not defensive_line_4<0 and not defensive_line_2<0:
        double_flanked_3=True        
    elif defensive_line_2>defensive_line_1+1 and not defensive_line_1<0:
        flanked_2=True    
    elif defensive_line_2>defensive_line_3+1 and not defensive_line_3<0:
        flanked_2+True
    elif defensive_line_3>defensive_line_2+1 and not defensive_line_2<0:
        flanked_3=True
    elif defensive_line_3>defensive_line_4+1 and not defensive_line_4<0:
        flanked_3=True
    elif defensive_line_4>defensive_line_3+1 and not defensive_line_3<0:
        flanked_4=True
    else: 
        flanked_1=False
        flanked_2=False
        flanked_3=False
        flanked_4=False
        double_flanked_2=False
        double_flanked_3=False
def flank_attack():
    global flanked_1
    global flanked_2
    global flanked_3
    global flanked_4
    global double_flanked_2
    global double_flanked_3
    global front_1_defeat
    global front_2_defeat
    global front_3_defeat
    global front_4_defeat
    global victory_state
    global combat_power_1
    global combat_power_2
    global combat_power_3
    global combat_power_4
    if double_flanked_3==True:
        global outflanked
        print("\n\nPincered!\n")
        input("\npress enter\n\n")
        if randint(1,20)<20:
            print("\nCounterattack!\n")
            if combat_power_3<=200+randint(-20, 50)*(randint(5,9)/10):
                outflanked=True
                print("\nYour incompetence has opened a hole in the front that a better commander must seek to plug.\n")
                front_3_defeat=True
                victory_state=False
            else: 
                print("\nYou have lead your men into a lion's den, and akin to the Book of Daniel, a scant few survive thanks to divine intervention.\n\n")
                combat_power_3-=((combat_power_3*randint(75, 90))/100)
                front_3_defeat=False       
        else:
            print("\nYour incompetent leadership has gone unpunished.\nReinforce the flank at the nearest opportunity.\n\n")
    elif double_flanked_2==True:
        print("\n\nPincered!\n")
        input("\npress enter\n\n")
        if randint(1,20)<20:
            print("\nCounterattack!\n")
            if combat_power_2<=200+randint(-20, 50)*(randint(5,9)/10):
                outflanked=True
                print("\nYour incompetence has opened a hole in the front that a better commander must seek to plug.\n")
                front_2_defeat=True
                victory_state=False
            else: 
                print("\nYou have lead your men into a lion's den, and akin to the Book of Daniel, a scant few survive thanks to divine intervention.\n\n")
                combat_power_2-=((combat_power_2*randint(75, 90))/100)
                front_2_defeat=False             
        else:
            print("\nYour incompetent leadership has gone unpunished.\nReinforce the flank at the nearest opportunity.\n\n") 
    elif flanked_1==True:
        print("\n\nOutflanked!\n")
        input("\npress enter\n\n")
        if randint(1,10)<10:
            print("\nCounterattack!\n")
            if combat_power_1<=100+randint(-20, 50)*(randint(5,9)/10):
                outflanked=True
                print("\nYour troops have no hope of being saved. You have abandoned them to the enemy.\n")
                front_1_defeat=True
                victory_state=False
            else: 
                print("\nYour men have paid for your recklessness with blood and bravery.\n\n")
                combat_power_1-=((combat_power_1*100)/randint(75, 90))
        else:
            print("\nYour recklessness has gone unnoticed — for now.\nReinforce the flank at the nearest opportunity.\n\n")
    elif flanked_2==True:
        print("\n\nOutflanked!\n")
        input("\npress enter\n\n")
        if randint(1,10)<10:
            print("\nCounterattack!\n")
            if combat_power_2<=100+randint(-20, 50)*(randint(5,9)/10):
                outflanked=True
                print("\nYour troops have no hope of being saved. You have abandoned them to the enemy.\n")
                front_2_defeat=True
                victory_state=False
            else: 
                print("\nYour men have paid for your recklessness with blood and bravery.\n\n")
                combat_power_2-=((combat_power_2*100)/randint(75, 90))
        else:
            print("\nYour recklessness has gone unnoticed — for now.\nReinforce the flank at the nearest opportunity.\n\n")
    elif flanked_3==True:
        print("\n\nOutflanked!\n")
        input("\npress enter\n\n")
        if randint(1,10)<10:
            print("\nCounterattack!\n")
            if combat_power_3<=100+randint(-20, 50)*(randint(5,9)/10):
                outflanked=True
                print("\nYour troops have no hope of being saved. You have abandoned them to the enemy.\n")
                front_3_defeat=True
                victory_state=False
            else: 
                print("\nYour men have paid for your recklessness with blood and bravery.\n\n")
                combat_power_3-=((combat_power_3*100)/randint(75, 90))
        else:
            print("\nYour recklessness has gone unnoticed — for now.\nReinforce the flank at the nearest opportunity.\n\n")
    elif flanked_4==True:
        print("\n\nOutflanked!\n")
        input("\npress enter\n\n")
        if randint(1,10)<10:
            print("\nCounterattack!\n")
            if combat_power_4<=100+randint(-20, 50)*(randint(5,9)/10):
                outflanked=True
                print("\nYour troops have no hope of being saved. You have abandoned them to the enemy.\n")
                front_4_defeat=True
                victory_state=False
            else: 
                print("\nYour men have paid for your recklessness with blood and bravery.\n\n")
                combat_power_4-=((combat_power_4*100)/randint(75, 90))
        else:
            print("\nYour recklessness has gone unnoticed — for now.\nReinforce the flank at the nearest opportunity.\n\n") 
def renew_defense():
    global defensive_potential_1
    global defensive_potential_2
    global defensive_potential_3
    global defensive_potential_4
    if defensive_potential_1==0:
        defensive_potential_1+=100+randint(-20, 20)
    elif defensive_potential_2==0:
        defensive_potential_2+=100+randint(-20, 20)
    elif defensive_potential_3==0:
        defensive_potential_3+=100+randint(-20, 20)
    elif defensive_potential_4==0:
        defensive_potential_4+=100+randint(-20, 20) 
###### MAP #####
def state_of_theatre():
    print("\n\n****BATTLEMAP****")
    print(f"\n       Sector 1\nDefender's Might: {round(defensive_potential_1)}\nAttacking Strength: {round(combat_power_1)}\nDefensive Lines Defeated: {round(defensive_line_1)}/4\n\n       Sector 2\nDefender's Might: {round(defensive_potential_2)}\nAttacking Strength: {round(combat_power_2)}\nDefensive Lines Defeated: {defensive_line_2}/4\n \n      Sector 3\nDefender's Might: {round(defensive_potential_3)}\nAttacking Strength: {round(combat_power_3)}\nDefensive Lines Defeated: {round(defensive_line_3)}/4\n\n       Sector 4\nDefender's Might: {round(defensive_potential_4)}\nAttacking Strength: {round(combat_power_4)}\nDefensive Lines Defeated: {defensive_line_4}/4\n")
def battle_map():

    if defensive_line_1==0:
        trench_layer_0_1="^^^^^^^^"
    else:
        trench_layer_0_1="        "
    if defensive_line_2==0:
        trench_layer_0_2="^^^^^^^^"
    else:
        trench_layer_0_2="        "
    if defensive_line_3==0:
        trench_layer_0_3="^^^^^^^^"
    else:
        trench_layer_0_3="        "
    if defensive_line_4==0:
        trench_layer_0_4="^^^^^^^^"
    else:
        trench_layer_0_4="        "
    if defensive_line_1==1:
        trench_layer_1_1="^^^^^^^^"
    elif defensive_line_1==0:
        trench_layer_1_1="________"
    else:
        trench_layer_1_1="        "
    if defensive_line_2==1:
        trench_layer_1_2="^^^^^^^^"
    elif defensive_line_2==0:
        trench_layer_1_2="________"
    else:
        trench_layer_1_2="        "
    if defensive_line_3==1:
        trench_layer_1_3="^^^^^^^^"
    elif defensive_line_3==0:
        trench_layer_1_3="________"
    else:
        trench_layer_1_3="        "
    if defensive_line_4==1:
        trench_layer_1_4="^^^^^^^^"
    elif defensive_line_4==0:
        trench_layer_1_4="________"
    else:
        trench_layer_1_4="        "
    if defensive_line_1==2:
        trench_layer_2_1="^^^^^^^^"
    elif defensive_line_1<2:
        trench_layer_2_1="________"
    else:
        trench_layer_2_1="        "
    if defensive_line_2==2:
        trench_layer_2_2="^^^^^^^^"
    elif defensive_line_2<2:
        trench_layer_2_2="________"
    else:
        trench_layer_2_2="        "
    if defensive_line_3==2:
        trench_layer_2_3="^^^^^^^^"
    elif defensive_line_3<2:
        trench_layer_2_3="________"
    else:
        trench_layer_2_3="        "
    if defensive_line_4==2:
        trench_layer_2_4="^^^^^^^^"
    elif defensive_line_4<2:
        trench_layer_2_4="________"
    else:
        trench_layer_2_4="        "
    if defensive_line_1==3:
        trench_layer_3_1="^^^^^^^^"
    elif defensive_line_1<3:
        trench_layer_3_1="________"
    else:
        trench_layer_3_1="        "
    if defensive_line_2==3:
        trench_layer_3_2="^^^^^^^^"
    elif defensive_line_2<3:
        trench_layer_3_2="________"
    else:
        trench_layer_3_2="        "
    if defensive_line_3==3:
        trench_layer_3_3="^^^^^^^^"
    elif defensive_line_3<3:
        trench_layer_3_3="________"
    else:
        trench_layer_3_3="        "
    if defensive_line_4==3:
        trench_layer_3_4="^^^^^^^^"
    elif defensive_line_4<3:
        trench_layer_3_4="________"
    else:
        trench_layer_3_4="        "
    if defensive_line_1==4:
        trench_layer_4_1="^^^^^^^^"
    elif defensive_line_1<4:
        trench_layer_4_1="________"
    else:
        trench_layer_4_1="        "
    if defensive_line_2==4:
        trench_layer_4_2="^^^^^^^^"
    elif defensive_line_2<4:
        trench_layer_4_2="________"
    else:
        trench_layer_4_2="        "
    if defensive_line_3==4:
        trench_layer_4_3="^^^^^^^^"
    elif defensive_line_3<4:
        trench_layer_4_3="________"
    else:
        trench_layer_4_3="        "
    if defensive_line_4==4:
        trench_layer_4_4="^^^^^^^^"
    elif defensive_line_4<4:
        trench_layer_4_4="________"
    else:
        trench_layer_4_4="        "  
    print("|Sector 1|Sector 2|Sector 3|Sector 4|")
    print(f"|{trench_layer_4_1}|{trench_layer_4_2}|{trench_layer_4_3}|{trench_layer_4_4}|")
    print(f"|{trench_layer_3_1}|{trench_layer_3_2}|{trench_layer_3_3}|{trench_layer_3_4}|")
    print(f"|{trench_layer_2_1}|{trench_layer_2_2}|{trench_layer_2_3}|{trench_layer_2_4}|")
    print(f"|{trench_layer_1_1}|{trench_layer_1_2}|{trench_layer_1_3}|{trench_layer_1_4}|")
    print(f"|{trench_layer_0_1}|{trench_layer_0_2}|{trench_layer_0_3}|{trench_layer_0_4}|")
def weather():
    chance_of_rain=randint(1, 20)
    global forecast
    global tank_bonus
    if chance_of_rain<=10:
        print("\nThe weather forecast is: sunny\nThe ground is firm and visibility is good.\n")
        forecast="sunny"
    elif chance_of_rain>10<15:
        print("\nThe weather forecast is: raining\nThe battlefield will be muddy, and visibility poor.\n")
        forecast="raining"
        tank_bonus-=((tank_bonus*randint(35,75)*100))
    elif chance_of_rain<=15:
        print("\nThe weather forecast is: windy\nThis doesn't affect anything yet.\n")
        forecast="windy"
    else: print("weather???")
##### END STATE #####
def end_state():
        if victory_state==True:
            print("\n\nExcellent work, Commander. Report to High Command for commendation.\n")
            exit()
        elif victory_state==False:
            print("\n\nYou wasted the lives of a great many men braver than yourself.\n")
            exit()
        elif victory_state==None:
            print("\nYour work is not over, yet, Commander.\n")
        else: print("end state broken!!")
##### GAME START #####
diff_setting()
intro()
diff_hand()
while victory_state==None:
    renew_defense()
    if hand:
        hand_check()
    state_of_theatre()
    battle_map()
    sector_select()
    while battle_sector==1:
        input("\npress Enter to select a resource card")
        if hand:
            select_card()
        weather()           
        sector_1_combat()
        flank_check()
        flank_attack()
        sector_1_combat_outcome()
    while battle_sector==2:
        input("\npress Enter to select a resource card")
        if hand:
            select_card()
        weather()
        sector_2_combat()
        flank_check()
        flank_attack()
        sector_2_combat_outcome()
    while battle_sector==3:
        input("\npress Enter to select a resource card")
        if hand:
            select_card()
        weather()
        sector_3_combat()
        flank_check()
        flank_attack()
        sector_3_combat_outcome()
    while battle_sector==4:
        input("\npress Enter to select a resource card")
        if hand:
            select_card()
        weather()
        sector_4_combat()
        flank_check()
        flank_attack()
        sector_4_combat_outcome()
    if outflanked==False:
        battle_map()
    end_state()