# name: Nicolai Hejlesen Jørgensen
# date: 28-09-2019
# description: Text-based role-playing adventure game (CYOA game)

import random
from time import sleep
import os
import dice
from npc import (giantCentipede, cultist)

# quick commands

def clear():
    #os.system('cls')    # clears screen on Windows
    os.system('clear')  # clears screen on Linux / OS X

def pressToContinue():
    try:
        input("Press Enter to continue...")
    except SyntaxError:
        pass

# character configuration

def character():
    print("Use your favorite point-buy website, or roll 4d6 (keep the three highest values)")
    sleep(3)
    character.name = input("What is the name of your character?: ").title()
    try:
        character.strength = int(input("Input your Strength score: ").strip())
        character.dexterity = int(input("Input your Dexterity score: ").strip())
        character.constitution = int(input("Input your Constitution score: ").strip())
        character.intelligence = int(input("Input your Intelligence score: ").strip())
        character.wisdom = int(input("Input your Wisdom score: ").strip())
        character.charisma = int(input("Input your Charisma score: ").strip())
        character.health = int(8 + ((character.constitution - 10) / 2))
        print("\nWell met, " + character.name + "!")
        print("Your max HP is " + str(character.health) + "\n")
    except ValueError:
        clear()
        print("Error:")
        print("That's not a number!")
        sleep(3)
        clear()
        character()

def randomCharacter():
    character.name = input("What is the name of your character?: ").title()
    character.strength = int(dice.roll('3d6'))
    character.dexterity = int(dice.roll('3d6'))
    character.constitution = int(dice.roll('3d6'))
    character.intelligence = int(dice.roll('3d6'))
    character.wisdom = int(dice.roll('3d6'))
    character.charisma = int(dice.roll('3d6'))
    character.health = int(8 + ((character.constitution - 10) / 2))
    print("Strength: " + str(character.strength))
    print("Dexterity: " + str(character.dexterity))
    print("Constitution: " + str(character.constitution))
    print("Intelligence: " + str(character.intelligence))
    print("Wisdom: " + str(character.charisma))
    print("Charisma: " + str(character.charisma))
    print("\nWell met, " + character.name + "!")
    print("Your max HP is " + str(character.health) + "\n")

def characterAttack():
    character.strMod = int((character.strength - 10) / 2)
    character.dexMod = int((character.dexterity - 10) / 2)
    character.meleeAttackToHit = int(dice.roll('1d20')) + 2 + character.strMod
    character.rangedAttackToHit = int(dice.roll('1d20')) + 2 + character.dexMod



# game start

def gameStart():
    clear()
    ranChar = input("Would you like roll up a character with random stats? (yes or y to skip): ").lower().strip()
    if ranChar == "yes" or ranChar == "y":
        clear()
        randomCharacter()
    else:
        clear()
        character()
    skipStart = input("Would you like to skip the adventure intro? (yes or y to skip): ").lower().strip()
    if skipStart == "yes" or skipStart == "y":
        adventureBegins()
    else:
        displayIntro()

def displayIntro():
    clear()
    print("BACKSTORY")
    print("- Arrival in Orlbar- \n")
    print("It is the year 1349 DR, in the month of Deepwinter.\nYou have been on the road for nearly two months now,\nand snow hangs thick on the trees as you make your way\ntowards the town of Orlbar, at the foot of the Greypeak Mountains.\nThe Greypeaks are known throughout Faerun for their silver and iron mines,\nbut it is a different type of metal that brought you here: gold.\nWhile you were in Neverwinter you overheard rumours of a large\nhorde of treasure within an abandoned goblin keep.\nEven tavern rumours prove to be fruitful sometimes,\nand having been without a purpose for some months,\nyou departed immediately for the Grey Vale.\nWhen you reach Orlbar, the air is brisk and town is busy.\nCarts carry all manner of goods: timber, wool bales, grain,\nand animals from the surrounding country.\nSome of these goods would be bound for Waterdeep or Neverwinter,\nothers for the nearby city of Loudwater.\n\n")
    pressToContinue()
    clear()
    print("BACKSTORY")
    print("- Arrival in Orlbar -\n")
    print("Hungry and thirsty after many days on the road,\nyou enter the first tavern you see, The Woodsman’s Retreat,\nand satisfy your cravings.\nBread, cheese and a hot mulled wine do the trick nicely.\nYou then enquire from the barkeep about accomodation.\nYour bones ache and rest is essential.\nThe mountains can wait one or two days\nwhile you rest and replenish your supplies in town.\nThe barkeep tells you that a very respectable inn,\nthe Silver Flask, is just nearby.\nToting your backpack, you walk down the street\nto the Silver Flask and pay for a room. The inkeep is\na jolly woman who is glad to have your business,\nand she lights a cosy fire in your room. You bathe,\nthen lie down to rest and soon fall into a deep sleep;\nit’s been a while since your travel-hardened self has had\nclean sheets and a roof overhead!\n\n")
    pressToContinue()
    clear()
    print("BACKSTORY")
    print("- Arrival in Orlbar -\n")
    print("You are woken later that night by noise from the next room.\nYou can hear a woman openly sobbing on the other side of the wall.\nThe sound is gut-wrenching.\nEvery now and then a male voice says something, as if trying to comfort her.\nYou tolerate this for a while, but eventually it becomes evident that sleep\nis going to be impossible, and you walk out into the hallway and knock\non the door to the room next to yours. An elderly man answers.\nHe is dressed finely, like a member of the aristocracy, but sports a nasty\nblack eye and a gash across his cheek.\nIn the background a woman, also richly dressed, sits on a chair by the fire,\nher face buried in her hands.\n\n")
    pressToContinue()
    clear()
    print("BACKSTORY")
    print("- Arrival in Orlbar -\n")
    print("“Yes? What is it?” the elderly gentleman asks directly.\nYou straighten yourself up, peering into the room.\n\n“I was wondering what all the noise was about,” you say, although now you\ndon’t feel quite so annoyed.\n\n“I could hear the crying from next door. I was wondering,” you say gruffly,\nnot used to dealing with aristocrats,“If it’s anything I can help you with?\nPerhaps then we can all get some rest?”\n\nAt this the woman looks up and sees you. You probably look a fright,\nafter all those weeks on the road – ungroomed, hair dishevelled, travel-worn clothes -\nbut you’ve had a bath so you at least you don’t smell bad.\nHowever, your type has an... air about them.\nYou’ve seen a fight or two and knowhow to handle yourself in most situations.\nYou’re what’s known in these parts as ‘the adventuring type.’\nSuch types generally know how to get things done, things that others might shy away from.\n\n“Show our guest in, Elric,” the woman says weakly,\ndrying her tears with a silk handkerchief.\n\n")
    pressToContinue()
    clear()
    print("BACKSTORY")
    print("- The Mysterious Knight -\n")
    sleep(2)
    print("You are shown to a chair. For some reason, this old couple,\nwho introduce themselves as Lord and Lady Brewmont, welcome your presence,\nif only as a distraction from the grief they seem consumed by.\n\n“We arrived here last night,” Lady Brewmont begins.\n“Elric is so busy these days, so we thought we would bring\nourselves out to Orlbar for a little holiday.\nOur son, he’s so fond of the mountains.\nLoves all the stories. Well, he’s our grandson really.\nThe son of our daughter who died some years ago.\nHe is all we have left of her. We call him our son.“\n\nLady Brewmont begins sobbing once more. Elric Brewmont picks up the thread.\n\n“Long story short, my friend, we were accosted on the highway.\nWe were passing along a lonely stretch of read when he appeared, from nowhere.\nA knight, a towering brute of a man, all clad in armour.”\n\nLord Elric points to his face.\n\n“Did this to me, knocked me out cold. Then he grabbed our boy,\nthrew him on a horse and bolted! Without a word!”\n\n")
    pressToContinue()
    clear()
    print("BACKSTORY")
    print("- The Mysterious Knight -\n")
    print("“Hmm,” you say, mulling over this information. “Did he seem familiar, this knight?”\n\nElric shakes his head.\n\n“I know what you’re thinking. Wealthy aristocrat, on holiday from Loudwater,\nsomeone must have known we were coming out here, and siezed the opportunity.\nIt’s true, I am what you would call... a public figure.\nIt is well known, in Loudwater at least, that I am a wealthy man.\nBut no.... this knight was something else.\nWe didn’t see his face, it was hidden by a great metal visor.\nA towering warrior he was, a hulk of a man.”\n\nLady Brewmont speaks again.\n\n“And he has kidnapped our poor little Darek! Abducted him, just ripped him out of our grasp!”\n\n")
    pressToContinue()
    clear()
    print("BACKSTORY")
    print("- Incompetent Fools -\n")
    sleep(2)
    print("“What did you do then?” you ask.\n\n“We came straight to Orlbar,” Lady Brewmont says.\n“We went to the Captain of the Guard, but he, he...”\n\n“A thoroughly incompetent fool,” Lord Brewmont growls.\n“Said this Knight was a ghost, that he’d chosen Darek as his squire,\nand that there was nothing we could do about it! Said Darek wasn’t the first.\nCalled him The Death Knight!\nYou can imagine what a comfort that was to us.”\n\n“They say the Knight lives in the wood nearby,” Lady Brewmont says airily,\nas if in a waking dream.\n“Weathercote Wood, isn’t it dear?”\n\nThe old man grits his teeth, staring into the fire, and punches his palm.\n\n")
    pressToContinue()
    clear()
    print("BACKSTORY")
    print("- Incompetent Fools -\n")
    print("“Ghost my arse!” he snarls through gritted teeth.\n“That knight looked real enough to me. He’s a lunatic, nothing more,\na lunatic who kidnaps young boys! And when I find the blaggard,\nby the Gods will he pay!”\n\nYou can’t help thinking that Lord Brewmont is a bit out of his depth here.\nYou don’t doubt his resolve, but he looks as though his days of conquest are well behind him.\nYou feel for this poor old couple.\nWhile not usually associating with the wealthy, you do know that you have\nsomething to offer them, and you’re never one to shy away from a good adventure...\nEspecially when the chance of a reward is on the table.\n\n")
    pressToContinue()
    clear()
    print("BACKSTORY")
    print("- Incompetent Fools -\n")
    print("“I can find your boy,” you hear yourself saying.\n\nThe woman looks up, and new hope begins to shine from her eyes.\n\n“Oh Gods,” she says, her voice quavering.\n“We’ll give you anything, anything...”\n\nThe old man is a little more practical.\n\n“If I was a few decades younger, I’d be out there myself.\nI saw action in the Battle of Tanglefork, when we freed the Vale from Rensha rule.”\n\nYou nod appreciatively – that battle happened about 30 years ago,\nand was said to be fierce. You are not surprised – Elric Brewmont definitely\ncarries himself like an old veteran.\n\n“I can’t put my sword forward any more, but I can offer you gold, my friend...\n2000 pieces of it, to be exact...”\n\n")
    pressToContinue()

# adventure start

def adventureBegins():
    clear()
    sleep(2)
    print("The Adventure Begins...\n")
    sleep(2)
    print("At dawn the next day, following the few scraps of information you have,\nyou saddle your horse and ride to the outskirts of town.\nThe townsfolk pay you little mind as you go, casting you the occasional glance.\n\nThe journey to Weathercote Wood lies due east, but is no short ride.\nThe Captain of the Guard tells you that the Death Knight\nhas always been seen in a small patch of wood that juts out\nfrom the western side of Weathercote, “like a wart on a giant’s nose.”\n\nBy midday you reach a sign which tells you you have another 15 miles to go.\nYou should make it there by nightfall.\nNot far past the sign is a small inn and tavern. An old man sits\non a chair in the afternoon sun, and raises a tankard of ale as you pass.\n\n“Last drink for many miles!” the old man calls to you.\n“Come, sit! I’ll buy you an ale!”\n\n\n")
    print("\x1B[3mDo you accept the old man’s invitation? If so, type BREWSKI.\nIf you are mindful of the time and choose to ride on, type KEEPGOING.\x1B[23m\n")

    choice = input("Which path will you choose? (BREWSKI or KEEPGOING): ").lower().strip()
    while True:
        if choice == "brewski":
            brewski()
            break
        elif choice == "keepgoing":
            keepGoing()
            break
        else:
            choice = input("That is not a valid path. Choose either BREWSKI or KEEPGOING: ").lower().strip()



# Adventure entries below:

def brewski():
    clear()
    print("- BREWSKI -\n")
    sleep(2)
    print("You tie your horse up to the tavern’s porch and join the old man,\nwho directs a young boy to bring you a frothing tankard of ale.\nThe boy also brings a bowl of stew for you to eat.\n\n")
    sleep(5)
    print("“What brings you out this way?” the old man asks eventually.\n\n\n")
    print("\x1B[3mDo you tell him of your quest? If so, type QUESTCONVO.\nIf you choose to simply replenish yourself and be on your way, type REPLENISH.\x1B[23m\n")

    choice = input("Which path will you choose? (QUESTCONVO or REPLENISH): ").lower().strip()
    while True:
        if choice == "questconvo":
            questConvo()
            break
        elif choice == "replenish":
            replenish()
            break
        else:
            choice = input("That is not a valid path. Choose either QUESTCONVO or REPLENISH: ").lower().strip()

def questConvo():
    clear()
    print("- QUESTCONVO -\n")
    sleep(2)
    print("You find yourself telling the old man all about your quest to find the mysterious\nknight and return Darek Brewmont to his grandparents.\n\nThe old man nods solemnly.\n\n“The Death Knight,” he says quietly, and leans forward in his chair.\n“Local legend, they say, but ah....”\n\n“What?” you ask.\n\nHe straightens up, looking you straight in the eye.\n\n“It’s no legend,” he says firmly.\n“I was a boy when they hung him, from the Red Tree in Weathercote Wood.”\n\nThe old man goes on to tell you the story.\nThe man who would become the Death Knight was once a good man,\nwho came from a village in the far south. After his wife died from the pox,\nhe left his village taking his only son with him as his squire,\neager to teach him the ways of the righteous warrior.\nBut a large band of brigands ambushed them on the road,\nshot the knight with a poison dart, and kidnapped his son.\nThey left a note pinned in the ground with a dagger, demanding the knight plunder\nthe treasury in Orlbar and deliver the gold to them.\n\n")
    pressToContinue()
    clear()
    print("- QUESTCONVO -\n")
    print("The Knight did so, almost dying in the process,\nbut the town guard pursued him from town. When the kidnapperss saw the Knight\ncoming with the authorities close behind, they killed the poor boy and fled.\nUpon finding his son’s body, the Knight swore vengeance\non the bandits and vowed to pursue them unto the ends of the world.\n\nUnwilling to be taken by the town guard, the Knight drew his weapon to resist the arrest.\nThe ensuing fight was bloody, but the knight slew all who came against him.\nWhen the fight was over, the Knight pursued the bandits deeper into the wood\nbut lost their tracks in the undergrowth. His rage deepened until\nthe bloodlust and madness possessed him entirely, driven insane at the\nthought of his son’s killers escaping unpunished.\nNone would cross his path and live until the bandits\nhad been brought to justice at the tip of his blade.\n\nEventually more soldiers had to come from Loudwater to capture the insane knight.\n\n“When they finally did,” the old man concludes,\n“they hung him in Weathercote Wood, from a Red Tree.”\n\n")
    pressToContinue()
    clear()
    print("- QUESTCONVO -\n")
    print("The old man looks down.\n\n“But his unfulfilled quest to find his son’s killers brought him back. As undead.\nThe Death Knight, they call him now. And since then, every few years or so,\na boy will go missing... He’s looking for a squire, someone to help him on his quest.”\n\nYou take a moment to digest all this information and drink from your tankard.\n\nAfter a while, you thank the old man for the company and\nthe information and are on your way.\n\n")
    pressToContinue()
    keepGoing()

def replenish():
    clear()
    print("- REPLENISH -\n")
    sleep(2)
    print("In response to the old man’s question, you say that you are\nlooking for a lost horse, a prize stallion. He shrugs.\nYou proceed to drink the ale with relish – it has been a hard ride –\nand eat the bowlful of stew, thinking that a midday meal was probably a very\nwise idea, as you do not know what time you will arrive at Weathercote Wood.\n\nYou thank the old man for his hospitality and are on your way.\n\n")
    pressToContinue()
    keepGoing()

def keepGoing():
    clear()
    print("- KEEPGOING -\n")
    sleep(2)
    print("It is late when you finally reach Weathercote Wood, some 55 miles east of Orlbar.\nThere, on the wood’s edge, you camp and let your horse run free.\nYou won’t be needing him for a while.\n\nWeathercote Wood is thick, the foliage dense, towering walls of green.\nAnd in there somewhere, if the information you have is to be trusted,\nis the boy Darek Brewmont. You settle down in your bedroll,\nthe embers of your fire keeping you warm well into the night.\nAfter a full day’s riding it doesn’t take long for you to fall into a deep slumber,\nthe sound of a nearby river lulling you to sleep.\n\nYou wake just before dawn, fully rested. But a noise instantly puts you on guard;\nfrom somewhere nearby comes a wet, slavering sound. Quietly you pick up your weapon and\nmove forward stealthily. When you are some hundred or so feet away,\nwhatever is lurking catches your scent, and you hear it running quickly away.\nOnly dim starlight shows any detail, and all you can see is a darkened shape moving\nthrough the night, towards the wood.\n\n\n")
    print("\x1B[3mIf you use a ranged weapon, and you wish to attack using it, type SHOOTAFTER.\nIf not, type DEADNELLY.\x1B[23m\n")

    choice = input("Which path will you choose? (SHOOTAFTER or DEADNELLY): ").lower().strip()
    while True:
        if choice == "shootafter":
            shootAfter()
            break
        elif choice == "deadnelly":
            # deadNelly() FIX THIS ENTRY
            break
        else:
            choice = input("That is not a valid path. Choose either SHOOTAFTER or DEADNELLY: ").lower().strip()

def shootAfter():
    clear()
    print("- SHOOTAFTER -\n")
    sleep(2)
    print("Your target is about 100ft away. You lift your weapon,\ntaking a quick assessment of the conditions, and fire.\n\n\n")
    print("\x1B[3mMake a ranged attack at whatever is fleeing from you.\x1B[3m\n")
    try:
        input("Press Enter to SHOOT!")
    except SyntaxError:
        pass
    clear()
    sleep(1)
    print(".")
    sleep(1)
    clear()
    print("..")
    sleep(1)
    clear()
    print("...\n\n")

    shootAfterShot = random.randint(0, 5)
    if shootAfterShot == 5:
        print("Miss!")
        sleep(2)
        miss()
    else:
        print("Hit!")
        sleep(2)
        goodShot()


playAgain = "yes"
while playAgain == "yes" or playAgain == "y":
    gameStart()
    playAgain = input("You you want to play again? (yes or y to continue playing): ")