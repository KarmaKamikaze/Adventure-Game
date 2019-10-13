# author: Nicolai Hejlesen Jørgensen
# date: 28-09-2019
# description: Text-based role-playing adventure game (CYOA game)

import random
from time import sleep
import os
import dice
import pickle
from player_character import PC
from npc import NPC

# character ability tracking
character = pickle.load(open("character.dat", "rb"))
stealth_points = 0
checked_traps = pickle.load(open("checks.dat", "rb"))
damage_taken = 0
pickle.dump(damage_taken, open("damage_taken.dat", "wb"))
stealth_check = pickle.load(open("checks.dat", "rb"))
perception_check = pickle.load(open("checks.dat", "rb"))
has_blood_knight_sword = False
has_potion_of_healing = 0
stealth_quotes = ['You feel rather sneaky.', 'You are one with the shadows.', 'Non shall see you pass.']

# npc stats
# Darek Brewmont uses a d4 to roll damage with his weapon.
darekBrewmont = NPC("Darek Brewmont", 10, 4, 10, 10, 10, 10, 10, 10, 2, 2, 0, 0)

# The Giant Centipede uses a d4 to roll damage with its bite.
giantCentipede = NPC("Giant Centipede", 13, 4, 5, 14, 12, 1, 7, 3, 4, 2, 0, 0)

# The Cultists use a d6 to roll damage with its scimitar (melee) and its hand-crossbow (ranged).
cultist = NPC("Cultist", 12, 9, 11, 12, 10, 10, 11, 10, 2, 0, 3, 0)

# The Death Knight uses a d8 to roll damage with its Hellreaver.
deathKnight = NPC("Death Knight", 15, 28, 15, 11, 13, 12, 10, 5, 5, 3, 0, 0)

# The Goblins uses a d6 to roll damage with the spear and the battleaxe but a d4 for the bonestaff.
goblin = NPC("Goblin", 15, 7, 8, 14, 10, 10, 8, 8, 1, 1, 2, 2)

# The Kobold uses a d4 to roll damage with the dagger and a d6 for the fireball.
kobold = NPC("Kobold", 12, 5, 7, 15, 9, 8, 7, 8, 4, 2, 2, 0)

# The Forest Bat uses a d4 to roll damage with its bite.
forestBat = NPC("Forest Bat", 12, 5, 7, 15, 8, 2, 12, 4, 0, 0, 0, 0)

# The Skeleton uses a d6 to roll damage with its shortsword.
skeleton = NPC("Skeleton", 13, 13, 10, 14, 15, 6, 8, 5, 4, 2, 0, 0, )

# The Giant Wolf Spider uses a d6 to roll damage with its bite.
# IMPORTANT: Set up poison damage in main code when a check is needed.
giantWolfSpider = NPC("Giant Wolf Spider", 13, 11, 12, 16, 13, 3, 12, 4, 3, 1, 0, 0)

# The Zombie uses a d6 to roll damage with its slam.
# IMPORTANT: Set up the Undead Fortitude feature in main code when a check is needed.
zombie = NPC("Zombie", 8, 22, 13, 6, 16, 3, 6, 5, 3, 1, 0, 0)


# quick commands
def clear():
    # os.system('cls')    # clears screen on Windows
    os.system('clear')  # clears screen on Linux / OS X


def press_to_continue():
    try:
        input("\x1B[3mPress Enter to continue...\x1B[23m")
    except SyntaxError:
        pass


# character configuration
def manuel_character_initiation():
    print("Use your favorite point-buy website, or roll 4d6 (keep the three highest values)")
    sleep(3)

    global character
    try:
        character = PC(input("What is the name of your character?: ").title(),
                       int(input("Input your Strength score: ").strip()),
                       int(input("Input your Dexterity score: ").strip()),
                       int(input("Input your Constitution score: ").strip()),
                       int(input("Input your Intelligence score: ").strip()),
                       int(input("Input your Wisdom score: ").strip()),
                       int(input("Input your Charisma score: ").strip()))
        pickle.dump(character, open("character.dat", "wb"))
        print("\nWell met, " + character.name + "!")
        print("Your max HP is " + str(PC.hp(character)) + "\n")
    except ValueError:
        clear()
        print("Error:")
        print("That's not a number!")
        sleep(3)
        clear()
        manuel_character_initiation()


def random_character_initiation():
    global character
    character = PC(input("What is the name of your character?: ").title(),
                   int(dice.roll('3d6')),  # Strength
                   int(dice.roll('3d6')),  # Dexterity
                   int(dice.roll('3d6')),  # Constitution
                   int(dice.roll('3d6')),  # Intelligence
                   int(dice.roll('3d6')),  # Wisdom
                   int(dice.roll('3d6')))  # Charisma
    pickle.dump(character, open("character.dat", "wb"))
    print("Strength: " + str(character.strength))
    print("Dexterity: " + str(character.dexterity))
    print("Constitution: " + str(character.constitution))
    print("Intelligence: " + str(character.intelligence))
    print("Wisdom: " + str(character.charisma))
    print("Charisma: " + str(character.charisma))
    print("\nWell met, " + character.name + "!")
    print("Your max HP is " + str(PC.hp(character)) + "\n")


# game start
def start_game():
    clear()
    random_character = input(
        "Would you like roll up a character with random stats? (yes or y to skip): ").lower().strip()
    if random_character == "yes" or random_character == "y":
        clear()
        random_character_initiation()
    else:
        clear()
        manuel_character_initiation()
    skip_start = input("Would you like to skip the adventure intro? (yes or y to skip): ").lower().strip()
    if skip_start == "yes" or skip_start == "y":
        adventure_begins()
    else:
        display_intro()
        adventure_begins()


def display_intro():
    clear()
    print("BACKSTORY")
    print("- Arrival in Orlbar- \n")
    print("It is the year 1349 DR, in the month of Deepwinter.\nYou have been on the road for nearly two months now,"
          "\nand snow hangs thick on the trees as you make your way\ntowards the town of Orlbar, at the foot of the "
          "Greypeak Mountains.\nThe Greypeaks are known throughout Faerun for their silver and iron mines,\nbut it is "
          "a different type of metal that brought you here: gold.\nWhile you were in Neverwinter you overheard "
          "rumours of a large\nhorde of treasure within an abandoned goblin keep.\nEven tavern rumours prove to be "
          "fruitful sometimes,\nand having been without a purpose for some months,\nyou departed immediately for the "
          "Grey Vale.\nWhen you reach Orlbar, the air is brisk and town is busy.\nCarts carry all manner of goods: "
          "timber, wool bales, grain,\nand animals from the surrounding country.\nSome of these goods would be bound "
          "for Waterdeep or Neverwinter,\nothers for the nearby city of Loudwater.\n\n")
    press_to_continue()
    clear()
    print("BACKSTORY")
    print("- Arrival in Orlbar -\n")
    print("Hungry and thirsty after many days on the road,\nyou enter the first tavern you see, The Woodsman’s "
          "Retreat,\nand satisfy your cravings.\nBread, cheese and a hot mulled wine do the trick nicely.\nYou then "
          "enquire from the barkeep about accomodation.\nYour bones ache and rest is essential.\nThe mountains can "
          "wait one or two days\nwhile you rest and replenish your supplies in town.\nThe barkeep tells you that a "
          "very respectable inn,\nthe Silver Flask, is just nearby.\nToting your backpack, you walk down the "
          "street\nto the Silver Flask and pay for a room. The inkeep is\na jolly woman who is glad to have your "
          "business,\nand she lights a cosy fire in your room. You bathe,\nthen lie down to rest and soon fall into a "
          "deep sleep;\nit’s been a while since your travel-hardened self has had\nclean sheets and a roof "
          "overhead!\n\n")
    press_to_continue()
    clear()
    print("BACKSTORY")
    print("- Arrival in Orlbar -\n")
    print("You are woken later that night by noise from the next room.\nYou can hear a woman openly sobbing on the "
          "other side of the wall.\nThe sound is gut-wrenching.\nEvery now and then a male voice says something, "
          "as if trying to comfort her.\nYou tolerate this for a while, but eventually it becomes evident that "
          "sleep\nis going to be impossible, and you walk out into the hallway and knock\non the door to the room "
          "next to yours. An elderly man answers.\nHe is dressed finely, like a member of the aristocracy, "
          "but sports a nasty\nblack eye and a gash across his cheek.\nIn the background a woman, also richly "
          "dressed, sits on a chair by the fire,\nher face buried in her hands.\n\n")
    press_to_continue()
    clear()
    print("BACKSTORY")
    print("- Arrival in Orlbar -\n")
    print("“Yes? What is it?” the elderly gentleman asks directly.\nYou straighten yourself up, peering into the "
          "room.\n\n“I was wondering what all the noise was about,” you say, although now you\ndon’t feel quite so "
          "annoyed.\n\n“I could hear the crying from next door. I was wondering,” you say gruffly,\nnot used to "
          "dealing with aristocrats,“If it’s anything I can help you with?\nPerhaps then we can all get some "
          "rest?”\n\nAt this the woman looks up and sees you. You probably look a fright,\nafter all those weeks on "
          "the road – ungroomed, hair dishevelled, travel-worn clothes -\nbut you’ve had a bath so you at least you "
          "don’t smell bad.\nHowever, your type has an... air about them.\nYou’ve seen a fight or two and know how to "
          "handle yourself in most situations.\nYou’re what’s known in these parts as ‘the adventuring type.’\nSuch "
          "types generally know how to get things done, things that others might shy away from.\n\n“Show our guest "
          "in, Elric,” the woman says weakly,\ndrying her tears with a silk handkerchief.\n\n")
    press_to_continue()
    clear()
    print("BACKSTORY")
    print("- The Mysterious Knight -\n")
    sleep(2)
    print("You are shown to a chair. For some reason, this old couple,\nwho introduce themselves as Lord and Lady "
          "Brewmont, welcome your presence,\nif only as a distraction from the grief they seem consumed by.\n\n“We "
          "arrived here last night,” Lady Brewmont begins.\n“Elric is so busy these days, so we thought we would "
          "bring\nourselves out to Orlbar for a little holiday.\nOur son, he’s so fond of the mountains.\nLoves all "
          "the stories. Well, he’s our grandson really.\nThe son of our daughter who died some years ago.\nHe is all "
          "we have left of her. We call him our son.“\n\nLady Brewmont begins sobbing once more. Elric Brewmont picks "
          "up the thread.\n\n“Long story short, my friend, we were accosted on the highway.\nWe were passing along a "
          "lonely stretch of read when he appeared, from nowhere.\nA knight, a towering brute of a man, all clad in "
          "armour.”\n\nLord Elric points to his face.\n\n“Did this to me, knocked me out cold. Then he grabbed our "
          "boy,\nthrew him on a horse and bolted! Without a word!”\n\n")
    press_to_continue()
    clear()
    print("BACKSTORY")
    print("- The Mysterious Knight -\n")
    print("“Hmm,” you say, mulling over this information. “Did he seem familiar, this knight?”\n\nElric shakes his "
          "head.\n\n“I know what you’re thinking. Wealthy aristocrat, on holiday from Loudwater,\nsomeone must have "
          "known we were coming out here, and seized the opportunity.\nIt’s true, I am what you would call... a "
          "public figure.\nIt is well known, in Loudwater at least, that I am a wealthy man.\nBut no.... this knight "
          "was something else.\nWe didn’t see his face, it was hidden by a great metal visor.\nA towering warrior he "
          "was, a hulk of a man.”\n\nLady Brewmont speaks again.\n\n“And he has kidnapped our poor little Darek! "
          "Abducted him, just ripped him out of our grasp!”\n\n")
    press_to_continue()
    clear()
    print("BACKSTORY")
    print("- Incompetent Fools -\n")
    sleep(2)
    print("“What did you do then?” you ask.\n\n“We came straight to Orlbar,” Lady Brewmont says.\n“We went to the "
          "Captain of the Guard, but he, he...”\n\n“A thoroughly incompetent fool,” Lord Brewmont growls.\n“Said this "
          "Knight was a ghost, that he’d chosen Darek as his squire,\nand that there was nothing we could do about "
          "it! Said Darek wasn’t the first.\nCalled him The Death Knight!\nYou can imagine what a comfort that was to "
          "us.”\n\n“They say the Knight lives in the wood nearby,” Lady Brewmont says airily,\nas if in a waking "
          "dream.\n“Weathercote Wood, isn’t it dear?”\n\nThe old man grits his teeth, staring into the fire, "
          "and punches his palm.\n\n")
    press_to_continue()
    clear()
    print("BACKSTORY")
    print("- Incompetent Fools -\n")
    print("“Ghost my arse!” he snarls through gritted teeth.\n“That knight looked real enough to me. He’s a lunatic, "
          "nothing more,\na lunatic who kidnaps young boys! And when I find the blaggard,\nby the Gods will he "
          "pay!”\n\nYou can’t help thinking that Lord Brewmont is a bit out of his depth here.\nYou don’t doubt his "
          "resolve, but he looks as though his days of conquest are well behind him.\nYou feel for this poor old "
          "couple.\nWhile not usually associating with the wealthy, you do know that you have\nsomething to offer "
          "them, and you’re never one to shy away from a good adventure...\nEspecially when the chance of a reward is "
          "on the table.\n\n")
    press_to_continue()
    clear()
    print("BACKSTORY")
    print("- Incompetent Fools -\n")
    print("“I can find your boy,” you hear yourself saying.\n\nThe woman looks up, and new hope begins to shine from "
          "her eyes.\n\n“Oh Gods,” she says, her voice quavering.\n“We’ll give you anything, anything...”\n\nThe old "
          "man is a little more practical.\n\n“If I was a few decades younger, I’d be out there myself.\nI saw action "
          "in the Battle of Tanglefork, when we freed the Vale from Rensha rule.”\n\nYou nod appreciatively – that "
          "battle happened about 30 years ago,\nand was said to be fierce. You are not surprised – Elric Brewmont "
          "definitely\ncarries himself like an old veteran.\n\n“I can’t put my sword forward any more, "
          "but I can offer you gold, my friend...\n2000 pieces of it, to be exact...”\n\n")
    press_to_continue()


# adventure start
def adventure_begins():
    clear()
    sleep(2)
    print("The Adventure Begins...\n")
    sleep(2)
    print("At dawn the next day, following the few scraps of information you have,\nyou saddle your horse and ride to "
          "the outskirts of town.\nThe townsfolk pay you little mind as you go, casting you the occasional "
          "glance.\n\nThe journey to Weathercote Wood lies due east, but is no short ride.\nThe Captain of the Guard "
          "tells you that the Death Knight\nhas always been seen in a small patch of wood that juts out\nfrom the "
          "western side of Weathercote, “like a wart on a giant’s nose.”\n\nBy midday you reach a sign which tells "
          "you you have another 15 miles to go.\nYou should make it there by nightfall.\nNot far past the sign is a "
          "small inn and tavern. An old man sits\non a chair in the afternoon sun, and raises a tankard of ale as you "
          "pass.\n\n“Last drink for many miles!” the old man calls to you.\n“Come, sit! I’ll buy you an ale!”\n\n\n")
    print("\x1B[3mDo you accept the old man’s invitation? If so, type BREWSKI.\nIf you are mindful of the time and "
          "choose to ride on, type KEEPGOING.\x1B[23m\n")

    choice = input("Which path will you choose? (BREWSKI or KEEPGOING): ").lower().strip()
    while True:
        if choice == "brewski":
            brewski()
            break
        elif choice == "keepgoing":
            keep_going()
            break
        else:
            choice = input("That is not a valid path. Choose either BREWSKI or KEEPGOING: ").lower().strip()


# pre weathercote wood entries:
def brewski():
    clear()
    print("- BREWSKI -\n")
    sleep(2)
    print("You tie your horse up to the tavern’s porch and join the old man,\nwho directs a young boy to bring you a "
          "frothing tankard of ale.\nThe boy also brings a bowl of stew for you to eat.\n\n")
    sleep(5)
    print("“What brings you out this way?” the old man asks eventually.\n\n\n")
    print("\x1B[3mDo you tell him of your quest? If so, type QUESTCONVO.\nIf you choose to simply replenish yourself "
          "and be on your way, type REPLENISH.\x1B[23m\n")

    choice = input("Which path will you choose? (QUESTCONVO or REPLENISH): ").lower().strip()
    while True:
        if choice == "questconvo":
            quest_convo()
            break
        elif choice == "replenish":
            replenish()
            break
        else:
            choice = input("That is not a valid path. Choose either QUESTCONVO or REPLENISH: ").lower().strip()


def quest_convo():
    clear()
    print("- QUESTCONVO -\n")
    sleep(2)
    print("You find yourself telling the old man all about your quest to find the mysterious\nknight and return Darek "
          "Brewmont to his grandparents.\n\nThe old man nods solemnly.\n\n“The Death Knight,” he says quietly, "
          "and leans forward in his chair.\n“Local legend, they say, but ah....”\n\n“What?” you ask.\n\nHe "
          "straightens up, looking you straight in the eye.\n\n“It’s no legend,” he says firmly.\n“I was a boy when "
          "they hung him, from the Red Tree in Weathercote Wood.”\n\nThe old man goes on to tell you the story.\nThe "
          "man who would become the Death Knight was once a good man,\nwho came from a village in the far south. "
          "After his wife died from the pox,\nhe left his village taking his only son with him as his squire,"
          "\neager to teach him the ways of the righteous warrior.\nBut a large band of brigands ambushed them on the "
          "road,\nshot the knight with a poison dart, and kidnapped his son.\nThey left a note pinned in the ground "
          "with a dagger, demanding the knight plunder\nthe treasury in Orlbar and deliver the gold to them.\n\n")
    press_to_continue()
    clear()
    print("- QUESTCONVO -\n")
    print("The Knight did so, almost dying in the process,\nbut the town guard pursued him from town. When the "
          "kidnapperss saw the Knight\ncoming with the authorities close behind, they killed the poor boy and "
          "fled.\nUpon finding his son’s body, the Knight swore vengeance\non the bandits and vowed to pursue them "
          "unto the ends of the world.\n\nUnwilling to be taken by the town guard, the Knight drew his weapon to "
          "resist the arrest.\nThe ensuing fight was bloody, but the knight slew all who came against him.\nWhen the "
          "fight was over, the Knight pursued the bandits deeper into the wood\nbut lost their tracks in the "
          "undergrowth. His rage deepened until\nthe bloodlust and madness possessed him entirely, driven insane at "
          "the\nthought of his son’s killers escaping unpunished.\nNone would cross his path and live until the "
          "bandits\nhad been brought to justice at the tip of his blade.\n\nEventually more soldiers had to come from "
          "Loudwater to capture the insane knight.\n\n“When they finally did,” the old man concludes,\n“they hung him "
          "in Weathercote Wood, from a Red Tree.”\n\n")
    press_to_continue()
    clear()
    print("- QUESTCONVO -\n")
    print("The old man looks down.\n\n“But his unfulfilled quest to find his son’s killers brought him back. As "
          "undead.\nThe Death Knight, they call him now. And since then, every few years or so,\na boy will go "
          "missing... He’s looking for a squire, someone to help him on his quest.”\n\nYou take a moment to digest "
          "all this information and drink from your tankard.\n\nAfter a while, you thank the old man for the company "
          "and\nthe information and are on your way.\n\n")
    press_to_continue()
    keep_going()


def replenish():
    clear()
    print("- REPLENISH -\n")
    sleep(2)
    print("In response to the old man’s question, you say that you are\nlooking for a lost horse, a prize stallion. "
          "He shrugs.\nYou proceed to drink the ale with relish – it has been a hard ride –\nand eat the bowlful of "
          "stew, thinking that a midday meal was probably a very\nwise idea, as you do not know what time you will "
          "arrive at Weathercote Wood.\n\nYou thank the old man for his hospitality and are on your way.\n\n")
    press_to_continue()
    keep_going()


def keep_going():
    clear()
    print("- KEEPGOING -\n")
    sleep(2)
    print("It is late when you finally reach Weathercote Wood, some 55 miles east of Orlbar.\nThere, on the wood’s "
          "edge, you camp and let your horse run free.\nYou won’t be needing him for a while.\n\nWeathercote Wood is "
          "thick, the foliage dense, towering walls of green.\nAnd in there somewhere, if the information you have is "
          "to be trusted,\nis the boy Darek Brewmont. You settle down in your bedroll,\nthe embers of your fire "
          "keeping you warm well into the night.\nAfter a full day’s riding it doesn’t take long for you to fall into "
          "a deep slumber,\nthe sound of a nearby river lulling you to sleep.\n\nYou wake just before dawn, "
          "fully rested. But a noise instantly puts you on guard;\nfrom somewhere nearby comes a wet, "
          "slavering sound. Quietly you pick up your weapon and\nmove forward stealthily. When you are some hundred "
          "or so feet away,\nwhatever is lurking catches your scent, and you hear it running quickly away.\nOnly dim "
          "starlight shows any detail, and all you can see is a darkened shape moving\nthrough the night, towards the "
          "wood.\n\n\n")
    print("\x1B[3mIf you use a ranged weapon, and you wish to attack using it, type SHOOTAFTER.\nIf not, "
          "type DEADNELLY.\x1B[23m\n")

    choice = input("Which path will you choose? (SHOOTAFTER or DEADNELLY): ").lower().strip()
    while True:
        if choice == "shootafter":
            shoot_after()
            break
        elif choice == "deadnelly":
            dead_nelly()
            break
        else:
            choice = input("That is not a valid path. Choose either SHOOTAFTER or DEADNELLY: ").lower().strip()


def shoot_after():
    clear()
    print("- SHOOTAFTER -\n")
    sleep(2)
    print("Your target is about 100ft away. You lift your weapon,\ntaking a quick assessment of the conditions, "
          "and fire.\n\n\n")
    print("\x1B[3mMake a ranged attack at whatever is fleeing from you.\x1B[23m\n")
    try:
        input("\x1B[3mPress Enter to SHOOT!\x1B[23m")
    except SyntaxError:
        pass
    clear()
    sleep(1)
    print("Rolling.")
    sleep(1)
    clear()
    print("Rolling..")
    sleep(1)
    clear()
    print("Rolling...\n\n")

    nelly_ac = int(17)
    if PC.to_hit_ranged(character) >= nelly_ac:
        print("\x1B[3mHit!\x1B[23m")
        sleep(2)
        good_shot()
    else:
        print("\x1B[3mMiss!\x1B[23m")
        sleep(2)
        miss()


def good_shot():
    clear()
    print("- GOODSHOT -\n")
    sleep(2)
    print("You hear your arrow make its mark, and hear a cry of pain –\ndefinitely not human, you know that "
          "much.\n\nHowever, the creature hardly slows, and soon it is out of sight,\ndisappeared within the dark "
          "green of Weathercote Wood.\n\n\n")
    press_to_continue()
    dead_nelly()


def miss():
    clear()
    print("- MISS -\n")
    sleep(2)
    print("You watch the black shape scurry away, back into the cover of\nWeathercote Wood, and curse your poor "
          "aim.\n\nThen you walk forward to where the creature had been before\nyou startled it and sent it running "
          "for the trees.\n\n\n")
    press_to_continue()
    dead_nelly()


def dead_nelly():
    clear()
    print("- DEADNELLY -\n")
    sleep(2)
    print("You walk forward to where the beast had been before, making all\nthat noise that woke you. There, "
          "twitching in its death throes,\nis the horse you rode from Orlbar. Gritting your teeth in anger,"
          "\nyou take out your weapon and quickly put the poor beast out of its misery.\n\nThe first rays of dawn "
          "begin to creep into the sky.\nWith a sigh of resignation, you wipe the horse’s blood from your weapon\nand "
          "begin the trek towards the wood’s edge. The morning is peaceful,\nin contrast to the savagery you have "
          "just witnessed, and a chorus\nof birds greet the dawn with calls that echo off the low hills\nof the "
          "surrounding landscape. As you near Weathercote Wood and can see down\nthe single path that leads into its "
          "depths, you see that little light\nseems to penetrate in through the canopy. Night still hides "
          "beneath\nthe mossy boughs and dark green vines that thread the ancient trees together.\n\nYou step onto "
          "the path and enter Weathercote Wood...\nwho knows what fate awaits you within these shadowed "
          "depths...\n\n\n")
    try:
        input("\x1B[3mPress Enter to enter Weathercote Wood!\x1B[23m")
    except SyntaxError:
        pass
    location_one()


# weathercote wood locations
def location_one():
    clear()
    print("WEATHERCOTE WOOD")
    print("- Location One -\n")
    sleep(2)
    print("You move ahead, deeper into the wood, and it almost seems\nas if the trees themselves are watching your "
          "progress.\nIndeed, as you go on, you really do get the feeling you are being watched.\n\n\n")

    print("OPTIONS:")
    print("\x1B[3mYou can move with stealth. Make a stealth check, if you wish by typing STEALTH.\nYou can check for "
          "traps: Roll perception by typing TRAP.\nIf you just wish to continue type CONTINUE.\x1B[23m\n")
    # If you succeed the stealth check, you may add 10 points to any d100 chance rolls you make while on this Location.

    global stealth_check
    global perception_check
    stealth_check = False
    perception_check = False

    choice = input("What do you wish to do? (STEALTH, TRAP or CONTINUE): ").lower().strip()
    while stealth_check is False and perception_check is False:
        if choice == "stealth":
            stealth_check = True
            pickle.dump(stealth_check, open("checks.dat", "wb"))
            location_one_stealth()
            break
        elif choice == "trap":
            perception_check = True
            pickle.dump(perception_check, open("checks.dat", "wb"))
            location_one_trap()
            break
        elif choice == "continue":
            break
        else:
            choice = input("Choose either STEALTH, TRAP or CONTINUE: ").lower().strip()

    while stealth_check is True and perception_check is False:
        clear()
        print("OPTIONS:")
        print("\x1B[3mYou can check for traps: Roll perception by typing TRAP.\nIf you just wish to continue type "
              "CONTINUE.\x1B[23m\n")
        if choice == "trap":
            perception_check = True
            pickle.dump(perception_check, open("checks.dat", "wb"))
            location_one_trap()
            break
        elif choice == "continue":
            break
        else:
            choice = input("Choose either TRAP or CONTINUE: ").lower().strip()

    while stealth_check is False and perception_check is True:
        clear()
        print("OPTIONS:")
        print("\x1B[3mYou can move with stealth. Make a stealth check, if you wish by typing STEALTH.\nIf you just "
              "wish to continue type CONTINUE.\x1B[23m\n")
        if choice == "stealth":
            stealth_check = True
            pickle.dump(stealth_check, open("checks.dat", "wb"))
            location_one_stealth()
            break
        elif choice == "continue":
            break
        else:
            choice = input("Choose either STEALTH or CONTINUE: ").lower().strip()
    quiet_entry()


def location_one_stealth():
    stealth_dc = int(12)
    if PC.stealth_check(character) >= stealth_dc:
        stealth_reward = int(stealth_points + 10)
        print("\n" + random.choice(stealth_quotes) + "\n\n\n")
        press_to_continue()
    else:
        print("\n" + random.choice(stealth_quotes) + "\n\n\n")
        press_to_continue()


def location_one_trap():
    trap_dc = int(12)
    if PC.perception_check(character) >= trap_dc:
        check_success()
    else:
        trap_fail()


def check_success():
    clear()
    print("- CHECKSUCCESS -\n")
    sleep(2)
    print("You search carefully around, but see nothing to indicate any traps are set here.\n\n\n")
    press_to_continue()


def trap_fail():
    clear()
    print("- TRAPFAIL -\n")
    sleep(2)
    print("You search around but are unable to locate anything resembling a trap.\n\n\n")
    press_to_continue()


def quiet_entry():
    clear()
    print("- QUIETENTRY -\n")
    sleep(2)
    print("You pause for a second, thinking you heard something.\n\nBut no, it was just some bird flapping off out of "
          "cover.\nYou watch it rise into the canopy and then look around at the three paths that lead off from "
          "here.\n\n\n")
    print("\x1B[3mYou are ready to move in the direction you desire.\x1B[23m\n")
    choice = input("Which path will you choose? (LEFT, RIGHT or AHEAD): ").lower().strip()
    while True:
        if choice == "left":
            locationThree()
            break
        elif choice == "right":
            location_two()
            break
        elif choice == "ahead":
            locationFive()
            break
        else:
            choice = input("That is not a valid path. Choose either LEFT, RIGHT or AHEAD: ").lower().strip()


def location_two():
    clear()
    print("WEATHERCOTE WOOD")
    print("- Location Two -\n")
    sleep(2)
    print("The track bends to the southeast, and you follow it,\nall light from the forest entrance now "
          "disappearing.\nIt is like night still hides in here.\nOnly the faintest light seeps in through the "
          "canopy.\n\nAhead, you see something white and whispy spanning the path. COBWEBS!\nSlowly, "
          "you edge forward...")

    print("OPTIONS:")
    print("\x1B[3mMoving with stealth? Make a stealth check, by typing STEALTH.\nChecking for traps? Roll perception "
          "by typing TRAP.\nWant to go back to the previous location? Type RETURN.\nIf you just wish to continue "
          "forward, type CONTINUE.\x1B[23m\n")
    # If you succeed the stealth check, you may add 10 points to any d100 chance rolls you make while on this Location.

    global stealth_check
    global perception_check
    stealth_check = False
    perception_check = False

    choice = input("What do you wish to do? (STEALTH, TRAP, RETURN or CONTINUE): ").lower().strip()
    while stealth_check is False and perception_check is False:
        if choice == "stealth":
            stealth_check = True
            pickle.dump(stealth_check, open("checks.dat", "wb"))
            print("\n" + random.choice(stealth_quotes) + "\n\n\n")
            press_to_continue()
            forward()
            break
        elif choice == "trap":
            perception_check = True
            pickle.dump(perception_check, open("checks.dat", "wb"))
            print("\nYou can only search thoroughly once the webs are removed.\n\n\n")
            press_to_continue()
            forward()
        elif choice == "return":
            quiet_entry()
            break
        elif choice == "continue":
            forward()
            break
        else:
            choice = input("Choose either STEALTH, TRAP, RETURN or CONTINUE: ").lower().strip()


def forward():
    clear()
    print("- FORWARD -\n")
    sleep(2)
    print("You edge forward, drawing your weapon and keeping watch on all sides.\nAfter all, where there’s "
          "webs...\n\nYou stop before the first web, a thick mass of silken threads.\nIt looks tough; an ordinary "
          "weapon is going to struggle to cut through this.\n\n\n")

    print("OPTIONS:")
    print("\x1B[3mIf you want to try and use an ordinary torch to burn them away, type FLAMEWEB.\nIf you’d prefer to "
          "try and move them with your weapon, type SLASHWEB\nOr, you could just throw something at the web and see "
          "what happens? Type TESTWEB\x1B[23m\n")

    choice = input("What do you wish to do? (FLAMEWEB, SLASHWEB or TESTWEB): ").lower().strip()
    while True:
        if choice == "flameweb":
            flameweb()
            break
        elif choice == "slashweb":
            slashweb()
            break
        elif choice == "testweb":
            testweb()
            break
        else:
            choice = input("That is not a valid option. Choose either FLAMEWEB, SLASHWEB or TESTWEB: ").lower().strip()


def obvious():
    clear()
    print("- OBVIOUS -\n")
    sleep(2)
    print("Apart from the webs, you see no evidence of any traps.\n\n\n")
    press_to_continue()


def trapless():
    clear()
    print("- TRAPLESS -\n")
    sleep(2)
    print("Apart from the webs, you see no evidence of any traps.\n\n\n")
    press_to_continue()


def flameweb():
    clear()
    print("- FLAMEWEB -\n")
    sleep(2)
    print("You produce your flint and tinder and start trying to light some tinder to create fire...\n\nYou crouch "
          "down, working the stone, trying to produce a fire that\ncan burn the webs away.\n\n\n")
    press_to_continue()
    while stealth_check:
        stealth_dc = int(15)
        if PC.stealth_check(character) >= stealth_dc:
            here_we_go()
            break
        else:
            oh_no()
            break
    oh_no()


def slashweb():
    clear()
    print("- SLASHWEB -\n")
    sleep(2)
    print("You produce your weapon and start hacking away at the webs, but they\nare not giving way easily! This is "
          "going to take some time.\n\n\n")
    press_to_continue()
    while stealth_check:
        stealth_dc = int(15)
        if PC.stealth_check(character) >= stealth_dc:
            here_we_go()
            break
        else:
            oh_no()
            break
    oh_no()


def testweb():
    clear()
    print("- TESTWEB -\n")
    sleep(2)
    print("You pick up a stick and toss it into the web, then draw your weapon,\nawaiting what might come...\n\n\n")
    press_to_continue()
    here_we_go()


def here_we_go():
    clear()
    print("- HEREWEGO -\n")
    sleep(2)
    print("Suddenly you hear a rustling, movement off to the right side of the path.\nSuddenly, from the undergrowth, "
          "two GIANT WOLF SPIDERS appear!\nSeeing you in their territory, the rear up, hissing horribly,\nand launch "
          "themselves at you!\n\n\n")
    press_to_continue()
    spider_battle()


def oh_no():
    clear()
    print("- OHNO -\n")
    sleep(2)
    print("Suddenly, you feel something pounce on you from behind!\n\nYour noisy progress through the forest must "
          "have alerted it to your presence.\nYou turn frantically, trying to get the thing off, whatever it "
          "is.\n\n\n")
    press_to_continue()

    spider_attack = NPC.to_hit_melee(giantWolfSpider)
    if spider_attack >= PC.ac(character):
        surprise_crawly()
    else:
        clear()
        print("- OHNO -\n")
        print("You manage to get the thing off your shoulder, and can now have a good look at it.\n\nA GIANT WOLF "
              "SPIDER is before you, hissing horribly.\nIt is quickly joined by a mate, and they both attack "
              "you!\n\n\n")
        press_to_continue()
        spider_battle()


def surprise_crawly():
    clear()
    print("- SURPRISECRAWLY -\n")
    sleep(2)
    print("You feel something biting into your neck, and a burning sensation in your skin.\nSomething poisonous has "
          "bitten you!\n\n\n")
    sleep(2)

    global damage_taken
    surprise_bite = int(NPC.damage_d6_melee(giantWolfSpider))
    surprise_poison = int(dice.roll('2d6'))

    if PC.constitution_save(character) >= 11:
        damage_taken += surprise_bite + int((surprise_poison / 2))
        pickle.dump(damage_taken, open("damage_taken.dat", "wb"))
        print("You steady yourself against the spiders poisonous bite.")
        print("You take " + str(surprise_bite + int((surprise_poison / 2)))
              + " points of damage from the poison-infested bite!\n\nYou have "
              + str(PC.hp(character) - damage_taken) + " HP left!\n\n\n")
        press_to_continue()
        death_check()
    else:
        damage_taken += surprise_bite + surprise_poison
        pickle.dump(damage_taken, open("damage_taken.dat", "wb"))
        print("You succumb to the poison in the spiders fangs.")
        print("You take " + str(surprise_bite + surprise_poison)
              + " points of damage from the poison-infested bite!\n\nYou have "
              + str(PC.hp(character) - damage_taken) + " HP left!\n\n\n")
        press_to_continue()
        death_check()

    clear()
    print("- SURPRISECRAWLY -\n")
    print("Quickly you bat the thing off and turn, drawing your weapon.\nTwo GIANT WOLF SPIDERS are before you, "
          "moving their pincers menacingly.\nStill smarting from the surprise attack, you move in,\nintent on "
          "destroying the horrible creatures.\n\n\n")
    press_to_continue()
    spider_battle()


def spider_battle():
    clear()
    print("- SPIDERBATTLE -\n")
    sleep(2)

    global has_blood_knight_sword
    global damage_taken
    bite_damage = int(NPC.damage_d6_melee(giantWolfSpider))
    poison_damage = int(dice.roll('2d6'))

    spider_npc_1_max_hp = giantWolfSpider.hp
    spider_npc_2_max_hp = giantWolfSpider.hp
    spider_npc_1_damage_taken = 0
    spider_npc_2_damage_taken = 0

    npc_initiative = NPC.initiative(giantWolfSpider)
    pc_initiative = PC.initiative(character)

    while damage_taken <= PC.hp(character) and spider_npc_1_damage_taken <= spider_npc_1_max_hp:
        if pc_initiative >= npc_initiative:
            clear()
            print("- SPIDERBATTLE -\n")
            print("You prepare yourself to attack the spider!\n\n")
            print("Two GIANT WOLF SPIDERS are still alive!\n\n")
            try:
                input("\x1B[3mPress Enter to ATTACK...\x1B[23m")
            except SyntaxError:
                pass
            character_attack = PC.to_hit_melee(character)
            clear()
            sleep(1)
            print("Rolling.")
            sleep(1)
            clear()
            print("Rolling..")
            sleep(1)
            clear()
            print("Rolling...\n\n")
            if character_attack >= giantWolfSpider.ac:
                if has_blood_knight_sword:
                    print(str(character_attack) + "\x1B[3m HITS!\x1B[23m")
                    sleep(1)
                    print("\nThe spider takes " + str(PC.blood_damage_melee(character)) + " points of damage!\n\n\n")
                    spider_npc_1_damage_taken += PC.blood_damage_melee(character)
                    press_to_continue()
                    if spider_npc_1_damage_taken >= spider_npc_1_max_hp:
                        break
                    else:
                        pass
                    clear()
                    print("- SPIDERBATTLE -\n")
                    print("The spider tries to attack you!\n\n")
                    if NPC.to_hit_melee(giantWolfSpider) >= PC.ac(character):
                        print("It thrusts its fangs deep into your soft skin.\n")
                        sleep(1)
                        if PC.constitution_save(character) >= 11:
                            damage_taken += bite_damage + int((poison_damage / 2))
                            pickle.dump(damage_taken, open("damage_taken.dat", "wb"))
                            print("You manage to steady yourself against the spiders poisonous bite.")
                            print("You take " + str(bite_damage + int((poison_damage / 2)))
                                  + " points of damage from the poison-infested bite!\n\nYou have "
                                  + str(PC.hp(character) - damage_taken) + " HP left!\n\n\n")
                            press_to_continue()
                            death_check()
                        else:
                            damage_taken += bite_damage + poison_damage
                            pickle.dump(damage_taken, open("damage_taken.dat", "wb"))
                            print("You succumb to the poison in the spiders fangs.")
                            print("You take " + str(bite_damage + poison_damage)
                                  + " points of damage from the poison-infested bite!\n\nYou have "
                                  + str(PC.hp(character) - damage_taken) + " HP left!\n\n\n")
                            press_to_continue()
                            death_check()
                else:
                    print(str(character_attack) + "\x1B[3m HITS!\x1B[23m")
                    sleep(1)
                    print("\nThe spider takes " + str(PC.damage_melee(character)) + " points of damage!\n\n\n")
                    spider_npc_1_damage_taken += PC.damage_melee(character)
                    press_to_continue()
                    if spider_npc_1_damage_taken >= spider_npc_1_max_hp:
                        break
                    else:
                        pass
                    clear()
                    print("- SPIDERBATTLE -\n")
                    print("The spider tries to attack you!\n\n")
                    if NPC.to_hit_melee(giantWolfSpider) >= PC.ac(character):
                        print("It thrusts its fangs deep into your soft skin.\n")
                        sleep(1)
                        if PC.constitution_save(character) >= 11:
                            damage_taken += bite_damage + int((poison_damage / 2))
                            pickle.dump(damage_taken, open("damage_taken.dat", "wb"))
                            print("You manage to steady yourself against the spiders poisonous bite.")
                            print("You take " + str(bite_damage + int((poison_damage / 2)))
                                  + " points of damage from the poison-infested bite!\n\nYou have "
                                  + str(PC.hp(character) - damage_taken) + " HP left!\n\n\n")
                            press_to_continue()
                            death_check()
                        else:
                            damage_taken += bite_damage + poison_damage
                            pickle.dump(damage_taken, open("damage_taken.dat", "wb"))
                            print("You succumb to the poison in the spiders fangs.")
                            print("You take " + str(bite_damage + poison_damage)
                                  + " points of damage from the poison-infested bite!\n\nYou have "
                                  + str(PC.hp(character) - damage_taken) + " HP left!\n\n\n")
                            press_to_continue()
                            death_check()
                    else:
                        sleep(1)
                        print("It misses!\n\n\n")
                        press_to_continue()
            else:
                print(str(character_attack) + "\x1B[3m MISSES!\x1B[23m")
                press_to_continue()
                clear()
                print("- SPIDERBATTLE -\n")
                print("The spider tries to attack you!\n\n")
                if NPC.to_hit_melee(giantWolfSpider) >= PC.ac(character):
                    print("It thrusts its fangs deep into your soft skin.\n")
                    sleep(1)
                    if PC.constitution_save(character) >= 11:
                        damage_taken += bite_damage + int((poison_damage / 2))
                        pickle.dump(damage_taken, open("damage_taken.dat", "wb"))
                        print("You manage to steady yourself against the spiders poisonous bite.")
                        print("You take " + str(bite_damage + int((poison_damage / 2)))
                              + " points of damage from the poison-infested bite!\n\nYou have "
                              + str(PC.hp(character) - damage_taken) + " HP left!\n\n\n")
                        press_to_continue()
                        death_check()
                    else:
                        damage_taken += bite_damage + poison_damage
                        pickle.dump(damage_taken, open("damage_taken.dat", "wb"))
                        print("You succumb to the poison in the spiders fangs.")
                        print("You take " + str(bite_damage + poison_damage)
                              + " points of damage from the poison-infested bite!\n\nYou have "
                              + str(PC.hp(character) - damage_taken) + " HP left!\n\n\n")
                        press_to_continue()
                        death_check()
        else:
            clear()
            print("- SPIDERBATTLE -\n")
            print("The spider tries to attack you!\n\n")
            print("Two GIANT WOLF SPIDERS are still alive!\n\n")
            if NPC.to_hit_melee(giantWolfSpider) >= PC.ac(character):
                print("It thrusts its fangs deep into your soft skin.\n")
                sleep(1)
                if PC.constitution_save(character) >= 11:
                    damage_taken += bite_damage + int((poison_damage / 2))
                    pickle.dump(damage_taken, open("damage_taken.dat", "wb"))
                    print("You manage to steady yourself against the spiders poisonous bite.")
                    print("You take " + str(bite_damage + int((poison_damage / 2)))
                          + " points of damage from the poison-infested bite!\n\nYou have "
                          + str(PC.hp(character) - damage_taken) + " HP left!\n\n\n")
                    press_to_continue()
                    death_check()
                    clear()
                    print("- SPIDERBATTLE -\n")
                    print("You prepare yourself to attack the spider!\n\n")
                    try:
                        input("\x1B[3mPress Enter to ATTACK...\x1B[23m")
                    except SyntaxError:
                        pass
                    character_attack = PC.to_hit_melee(character)
                    clear()
                    sleep(1)
                    print("Rolling.")
                    sleep(1)
                    clear()
                    print("Rolling..")
                    sleep(1)
                    clear()
                    print("Rolling...\n\n")
                    if character_attack >= giantWolfSpider.ac:
                        if has_blood_knight_sword:
                            print(str(character_attack) + "\x1B[3m HITS!\x1B[23m")
                            sleep(1)
                            print("\nThe spider takes " + str(PC.blood_damage_melee(character)) + " points of damage!\n\n\n")
                            spider_npc_1_damage_taken += PC.blood_damage_melee(character)
                            press_to_continue()
                            if spider_npc_1_damage_taken >= spider_npc_1_max_hp:
                                break
                            else:
                                pass
                        else:
                            print(str(character_attack) + "\x1B[3m HITS!\x1B[23m")
                            sleep(1)
                            print("\nThe spider takes " + str(PC.damage_melee(character)) + " points of damage!\n\n\n")
                            spider_npc_1_damage_taken += PC.damage_melee(character)
                            press_to_continue()
                            if spider_npc_1_damage_taken >= spider_npc_1_max_hp:
                                break
                            else:
                                pass
                    else:
                        print(str(character_attack) + "\x1B[3m MISSES!\x1B[23m")
                        press_to_continue()
                else:
                    damage_taken += bite_damage + poison_damage
                    pickle.dump(damage_taken, open("damage_taken.dat", "wb"))
                    print("You succumb to the poison in the spiders fangs.")
                    print("You take " + str(bite_damage + poison_damage)
                          + " points of damage from the poison-infested bite!\n\nYou have "
                          + str(PC.hp(character) - damage_taken) + " HP left!\n\n\n")
                    press_to_continue()
                    death_check()
                    clear()
                    print("- SPIDERBATTLE -\n")
                    print("You prepare yourself to attack the spider!\n\n")
                    try:
                        input("\x1B[3mPress Enter to ATTACK...\x1B[23m")
                    except SyntaxError:
                        pass
                    character_attack = PC.to_hit_melee(character)
                    clear()
                    sleep(1)
                    print("Rolling.")
                    sleep(1)
                    clear()
                    print("Rolling..")
                    sleep(1)
                    clear()
                    print("Rolling...\n\n")
                    if character_attack >= giantWolfSpider.ac:
                        if has_blood_knight_sword:
                            print(str(character_attack) + "\x1B[3m HITS!\x1B[23m")
                            sleep(1)
                            print("\nThe spider takes " + str(PC.blood_damage_melee(character)) + " points of damage!\n\n\n")
                            spider_npc_1_damage_taken += PC.blood_damage_melee(character)
                            press_to_continue()
                            if spider_npc_1_damage_taken >= spider_npc_1_max_hp:
                                break
                            else:
                                pass
                        else:
                            print(str(character_attack) + "\x1B[3m HITS!\x1B[23m")
                            sleep(1)
                            print("\nThe spider takes " + str(PC.damage_melee(character)) + " points of damage!\n\n\n")
                            spider_npc_1_damage_taken += PC.damage_melee(character)
                            press_to_continue()
                            if spider_npc_1_damage_taken >= spider_npc_1_max_hp:
                                break
                            else:
                                pass
                    else:
                        print(str(character_attack) + "\x1B[3m MISSES!\x1B[23m")
                        press_to_continue()
            else:
                sleep(1)
                print("It misses!\n\n\n")
                press_to_continue()
                clear()
                print("- SPIDERBATTLE -\n")
                print("You prepare yourself to attack the spider!\n\n")
                try:
                    input("\x1B[3mPress Enter to ATTACK...\x1B[23m")
                except SyntaxError:
                    pass
                character_attack = PC.to_hit_melee(character)
                clear()
                sleep(1)
                print("Rolling.")
                sleep(1)
                clear()
                print("Rolling..")
                sleep(1)
                clear()
                print("Rolling...\n\n")
                if character_attack >= giantWolfSpider.ac:
                    if has_blood_knight_sword:
                        print(str(character_attack) + "\x1B[3m HITS!\x1B[23m")
                        sleep(1)
                        print("\nThe spider takes " + str(PC.blood_damage_melee(character)) + " points of damage!\n\n\n")
                        spider_npc_1_damage_taken += PC.blood_damage_melee(character)
                        press_to_continue()
                        if spider_npc_1_damage_taken >= spider_npc_1_max_hp:
                            break
                        else:
                            pass
                    else:
                        print(str(character_attack) + "\x1B[3m HITS!\x1B[23m")
                        sleep(1)
                        print("\nThe spider takes " + str(PC.damage_melee(character)) + " points of damage!\n\n\n")
                        spider_npc_1_damage_taken += PC.damage_melee(character)
                        press_to_continue()
                        if spider_npc_1_damage_taken >= spider_npc_1_max_hp:
                            break
                        else:
                            pass
                else:
                    print(str(character_attack) + "\x1B[3m MISSES!\x1B[23m")
                    press_to_continue()

    while damage_taken <= PC.hp(character) and spider_npc_2_damage_taken <= spider_npc_2_max_hp:
        if pc_initiative >= npc_initiative:
            clear()
            print("- SPIDERBATTLE -\n")
            print("You prepare yourself to attack the spider!\n\n")
            print("One GIANT WOLF SPIDER still remain!\n\n")
            try:
                input("\x1B[3mPress Enter to ATTACK...\x1B[23m")
            except SyntaxError:
                pass
            character_attack = PC.to_hit_melee(character)
            clear()
            sleep(1)
            print("Rolling.")
            sleep(1)
            clear()
            print("Rolling..")
            sleep(1)
            clear()
            print("Rolling...\n\n")
            if character_attack >= giantWolfSpider.ac:
                if has_blood_knight_sword:
                    print(str(character_attack) + "\x1B[3m HITS!\x1B[23m")
                    sleep(1)
                    print("\nThe spider takes " + str(PC.blood_damage_melee(character)) + " points of damage!\n\n\n")
                    spider_npc_2_damage_taken += PC.blood_damage_melee(character)
                    press_to_continue()
                    if spider_npc_2_damage_taken >= spider_npc_2_max_hp:
                        break
                    else:
                        pass
                else:
                    print(str(character_attack) + "\x1B[3m HITS!\x1B[23m")
                    sleep(1)
                    print("\nThe spider takes " + str(PC.damage_melee(character)) + " points of damage!\n\n\n")
                    spider_npc_2_damage_taken += PC.damage_melee(character)
                    press_to_continue()
                    if spider_npc_2_damage_taken >= spider_npc_2_max_hp:
                        break
                    else:
                        pass
                    clear()
                    print("- SPIDERBATTLE -\n")
                    print("The spider tries to attack you!\n\n")
                    if NPC.to_hit_melee(giantWolfSpider) >= PC.ac(character):
                        print("It thrusts its fangs deep into your soft skin.\n")
                        sleep(1)
                        if PC.constitution_save(character) >= 11:
                            damage_taken += bite_damage + int((poison_damage / 2))
                            pickle.dump(damage_taken, open("damage_taken.dat", "wb"))
                            print("You manage to steady yourself against the spiders poisonous bite.")
                            print("You take " + str(bite_damage + int((poison_damage / 2)))
                                  + " points of damage from the poison-infested bite!\n\nYou have "
                                  + str(PC.hp(character) - damage_taken) + " HP left!\n\n\n")
                            press_to_continue()
                            death_check()
                        else:
                            damage_taken += bite_damage + poison_damage
                            pickle.dump(damage_taken, open("damage_taken.dat", "wb"))
                            print("You succumb to the poison in the spiders fangs.")
                            print("You take " + str(bite_damage + poison_damage)
                                  + " points of damage from the poison-infested bite!\n\nYou have "
                                  + str(PC.hp(character) - damage_taken) + " HP left!\n\n\n")
                            press_to_continue()
                            death_check()
                    else:
                        sleep(1)
                        print("It misses!\n\n\n")
                        press_to_continue()
            else:
                print(str(character_attack) + "\x1B[3m MISSES!\x1B[23m")
                press_to_continue()
                clear()
                print("- SPIDERBATTLE -\n")
                print("The spider tries to attack you!\n\n")
                if NPC.to_hit_melee(giantWolfSpider) >= PC.ac(character):
                    print("It thrusts its fangs deep into your soft skin.\n")
                    sleep(1)
                    if PC.constitution_save(character) >= 11:
                        damage_taken += bite_damage + int((poison_damage / 2))
                        pickle.dump(damage_taken, open("damage_taken.dat", "wb"))
                        print("You manage to steady yourself against the spiders poisonous bite.")
                        print("You take " + str(bite_damage + int((poison_damage / 2)))
                              + " points of damage from the poison-infested bite!\n\nYou have "
                              + str(PC.hp(character) - damage_taken) + " HP left!\n\n\n")
                        press_to_continue()
                        death_check()
                    else:
                        damage_taken += bite_damage + poison_damage
                        pickle.dump(damage_taken, open("damage_taken.dat", "wb"))
                        print("You succumb to the poison in the spiders fangs.")
                        print("You take " + str(bite_damage + poison_damage)
                              + " points of damage from the poison-infested bite!\n\nYou have "
                              + str(PC.hp(character) - damage_taken) + " HP left!\n\n\n")
                        press_to_continue()
                        death_check()
        else:
            clear()
            print("- SPIDERBATTLE -\n")
            print("The spider tries to attack you!\n\n")
            print("One GIANT WOLF SPIDER still remain!\n\n")
            if NPC.to_hit_melee(giantWolfSpider) >= PC.ac(character):
                print("It thrusts its fangs deep into your soft skin.\n")
                sleep(1)
                if PC.constitution_save(character) >= 11:
                    damage_taken += bite_damage + int((poison_damage / 2))
                    pickle.dump(damage_taken, open("damage_taken.dat", "wb"))
                    print("You manage to steady yourself against the spiders poisonous bite.")
                    print("You take " + str(bite_damage + int((poison_damage / 2)))
                          + " points of damage from the poison-infested bite!\n\nYou have "
                          + str(PC.hp(character) - damage_taken) + " HP left!\n\n\n")
                    press_to_continue()
                    death_check()
                    clear()
                    print("- SPIDERBATTLE -\n")
                    print("You prepare yourself to attack the spider!\n\n")
                    try:
                        input("\x1B[3mPress Enter to ATTACK...\x1B[23m")
                    except SyntaxError:
                        pass
                    character_attack = PC.to_hit_melee(character)
                    clear()
                    sleep(1)
                    print("Rolling.")
                    sleep(1)
                    clear()
                    print("Rolling..")
                    sleep(1)
                    clear()
                    print("Rolling...\n\n")
                    if character_attack >= giantWolfSpider.ac:
                        if has_blood_knight_sword:
                            print(str(character_attack) + "\x1B[3m HITS!\x1B[23m")
                            sleep(1)
                            print("\nThe spider takes " + str(PC.blood_damage_melee(character)) + " points of damage!\n\n\n")
                            spider_npc_2_damage_taken += PC.blood_damage_melee(character)
                            press_to_continue()
                            if spider_npc_2_damage_taken >= spider_npc_2_max_hp:
                                break
                            else:
                                pass
                        else:
                            print(str(character_attack) + "\x1B[3m HITS!\x1B[23m")
                            sleep(1)
                            print("\nThe spider takes " + str(PC.damage_melee(character)) + " points of damage!\n\n\n")
                            spider_npc_2_damage_taken += PC.damage_melee(character)
                            press_to_continue()
                            if spider_npc_2_damage_taken >= spider_npc_2_max_hp:
                                break
                            else:
                                pass
                    else:
                        print(str(character_attack) + "\x1B[3m MISSES!\x1B[23m")
                        press_to_continue()
                else:
                    damage_taken += bite_damage + poison_damage
                    pickle.dump(damage_taken, open("damage_taken.dat", "wb"))
                    print("You succumb to the poison in the spiders fangs.")
                    print("You take " + str(bite_damage + poison_damage)
                          + " points of damage from the poison-infested bite!\n\nYou have "
                          + str(PC.hp(character) - damage_taken) + " HP left!\n\n\n")
                    press_to_continue()
                    death_check()
                    clear()
                    print("- SPIDERBATTLE -\n")
                    print("You prepare yourself to attack the spider!\n\n")
                    try:
                        input("\x1B[3mPress Enter to ATTACK...\x1B[23m")
                    except SyntaxError:
                        pass
                    character_attack = PC.to_hit_melee(character)
                    clear()
                    sleep(1)
                    print("Rolling.")
                    sleep(1)
                    clear()
                    print("Rolling..")
                    sleep(1)
                    clear()
                    print("Rolling...\n\n")
                    if character_attack >= giantWolfSpider.ac:
                        if has_blood_knight_sword:
                            print(str(character_attack) + "\x1B[3m HITS!\x1B[23m")
                            sleep(1)
                            print("\nThe spider takes " + str(PC.blood_damage_melee(character)) + " points of damage!\n\n\n")
                            spider_npc_2_damage_taken += PC.blood_damage_melee(character)
                            press_to_continue()
                            if spider_npc_2_damage_taken >= spider_npc_2_max_hp:
                                break
                            else:
                                pass
                        else:
                            print(str(character_attack) + "\x1B[3m HITS!\x1B[23m")
                            sleep(1)
                            print("\nThe spider takes " + str(PC.damage_melee(character)) + " points of damage!\n\n\n")
                            spider_npc_2_damage_taken += PC.damage_melee(character)
                            press_to_continue()
                            if spider_npc_2_damage_taken >= spider_npc_2_max_hp:
                                break
                            else:
                                pass
                    else:
                        print(str(character_attack) + "\x1B[3m MISSES!\x1B[23m")
                        press_to_continue()
            else:
                sleep(1)
                print("It misses!\n\n\n")
                press_to_continue()
                clear()
                print("- SPIDERBATTLE -\n")
                print("You prepare yourself to attack the spider!\n\n")
                try:
                    input("\x1B[3mPress Enter to ATTACK...\x1B[23m")
                except SyntaxError:
                    pass
                character_attack = PC.to_hit_melee(character)
                clear()
                sleep(1)
                print("Rolling.")
                sleep(1)
                clear()
                print("Rolling..")
                sleep(1)
                clear()
                print("Rolling...\n\n")
                if character_attack >= giantWolfSpider.ac:
                    if has_blood_knight_sword:
                        print(str(character_attack) + "\x1B[3m HITS!\x1B[23m")
                        sleep(1)
                        print("\nThe spider takes " + str(PC.blood_damage_melee(character)) + " points of damage!\n\n\n")
                        spider_npc_2_damage_taken += PC.blood_damage_melee(character)
                        press_to_continue()
                        if spider_npc_2_damage_taken >= spider_npc_2_max_hp:
                            break
                        else:
                            pass
                    else:
                        print(str(character_attack) + "\x1B[3m HITS!\x1B[23m")
                        sleep(1)
                        print("\nThe spider takes " + str(PC.damage_melee(character)) + " points of damage!\n\n\n")
                        spider_npc_2_damage_taken += PC.damage_melee(character)
                        press_to_continue()
                        if spider_npc_2_damage_taken >= spider_npc_2_max_hp:
                            break
                        else:
                            pass
                else:
                    print(str(character_attack) + "\x1B[3m MISSES!\x1B[23m")
                    press_to_continue()

    if spider_npc_1_damage_taken >= spider_npc_1_max_hp and spider_npc_2_damage_taken >= spider_npc_2_max_hp:
        dead_spiders()
    else:
        pass


def dead_spiders():
    clear()
    print("- DEADSPIDERS -\n")
    sleep(2)
    print("\x1B[3mYou gain 100 xp!\x1B[23m\n\n")
    sleep(2)
    print("You take a moment to catch your breath, recovering from the battle with the spiders.\nTheir dismembered "
          "corpses litter the ground. You destroy the rest of the webs,\nand then assess the situation.\n\n\n")

    print("OPTIONS:")
    print("\x1B[3mTo have a look around near the spiders corpses, type INVESTIGATESPIDERS.\nOtherwise, if you just "
          "want to continue, type CONTINUE.\x1B[23m\n")

    choice = input("What do you wish to do? (INVESTIGATESPIDERS or CONTINUE): ").lower().strip()
    while True:
        if choice == "investigatespiders":
            investigate_spiders()
            break
        elif choice == "continue":
            location_two_cleared()
            break
        else:
            choice = input("That is not a valid option. Choose either INVESTIGATESPIDERS or CONTINUE: ").lower().strip()


def investigate_spiders():
    clear()
    print("- INVESTIGATESPIDERS -\n")
    sleep(2)
    print("You start to look around, searching the bush by the track and seeingif you can\nfind anything – or anyone "
          "– the spiders may have stashed nearby.\n\nJust off the path, you find several dried up corpses, "
          "wrapped in old webs –\nthe remains of a few hapless travellers. A quick look through the pockets\nof a "
          "dead orc turns up 21 copper pieces and a dagger.\nA further search of two human corpses produces a heavy "
          "crossbow and... jackpot!\nA bottle labelled “Potion of Healing”!\n\nYou even recognize the script: it’s "
          "from a reputable dealer in Neverwinter\nwho you have bought potions from before. You drop the items "
          "into\nyour backpack and move back onto the path.\n\n\n")
    press_to_continue()
    location_two_cleared()


def location_two_cleared():
    clear()
    print("WEATHERCOTE WOOD")
    print("- Location Two -\n")
    sleep(2)
    print("\x1B[3mChecking for traps? Roll perceptionby typing TRAP.\nYou can move deeper into the forest by typing "
          "LEFT.\nOr you can choose to head back to location one by typing BACK.\x1B[23m\n")

    global perception_check
    perception_check = False

    choice = input("What do you wish to do? (TRAP, LEFT or BACK): ").lower().strip()
    while perception_check is False:
        if choice == "trap":
            perception_check = True
            pickle.dump(perception_check, open("checks.dat", "wb"))
            trap_dc = int(15)
            if PC.perception_check(character) >= trap_dc:
                obvious()
                break
            else:
                trapless()
                break
        elif choice == "left":
            location_six()
            break
        elif choice == "back":
            quiet_entry()
            break
        else:
            choice = input("Choose either TRAP, LEFT or BACK: ").lower().strip()

    while perception_check is True:
        if choice == "left":
            location_six()
            break
        elif choice == "back":
            quiet_entry()
            break
        else:
            choice = input("Choose either LEFT or BACK: ").lower().strip()


def location_six():
    clear()
    print("WEATHERCOTE WOOD")
    print("- Location Six -\n")
    sleep(2)
    print("You round the corner and see a house on the western side of the path.\nIt appears to be inhabited: smoke "
          "is drifting from the chimney.\nWho knows who waits inside here? An kindly old wizard hermit,\nor a warlock "
          "quietly plotting the domination of the world?\n\nCome to think of if, this could even be where the death "
          "knight is hiding!\nThe cabin doesn’t look like much though... it could just be a\ncommoner family. And "
          "they might have food...\n\nYour belly begins to rumble at the thought of a hot meal.\n\n\n")

    print("OPTIONS:")
    print("\x1B[3mYou can move with stealth. Make a stealth check, if you wish by typing STEALTH.\nYou can check for "
          "traps: Roll perception by typing TRAP.\nTo approach and investigate the house, type LITTLEHUT.\nIf you "
          "just wish to continue type CONTINUE.\nIf you wish to turn back to location two, type BACK.\x1B[23m\n")
    # If you succeed the stealth check, you may add 10 points to any d100 chance rolls you make while on this Location.

    global stealth_check
    global perception_check
    global checked_traps
    stealth_check = False
    perception_check = False
    checked_traps = False

    choice = input("What do you wish to do? (STEALTH, TRAP, LITTLEHUT, CONTINUE or BACK): ").lower().strip()
    while stealth_check is False and perception_check is False:
        if choice == "stealth":
            stealth_check = True
            pickle.dump(stealth_check, open("checks.dat", "wb"))
            # take note of stealth check success of failure for later.
            print("\n" + random.choice(stealth_quotes) + "\n\n\n")
            press_to_continue()
            break
        elif choice == "trap":
            perception_check = True
            checked_traps = True
            pickle.dump(perception_check, open("checks.dat", "wb"))
            pickle.dump(checked_traps, open("checks.dat", "wb"))
            more_traps()
            break
        elif choice == "littlehut":
            little_hut()
            break
        elif choice == "continue":
            what_awaits()
            break
        elif choice == "back":
            location_two_cleared()
            break
        else:
            choice = input("Choose either STEALTH, TRAP, LITTLEHUT, CONTINUE or BACK: ").lower().strip()

    while stealth_check is True and perception_check is False:
        clear()
        print("OPTIONS:")
        print("\x1B[3mYou can check for traps: Roll perception by typing TRAP.\nTo approach and investigate the "
              "house, type LITTLEHUT.\nIf you just wish to continue type CONTINUE.\nIf you wish to turn back to "
              "location two, type BACK.\x1B[23m\n")
        if choice == "trap":
            perception_check = True
            checked_traps = True
            pickle.dump(perception_check, open("checks.dat", "wb"))
            pickle.dump(checked_traps, open("checks.dat", "wb"))
            more_traps()
            break
        elif choice == "littlehut":
            little_hut()
            break
        elif choice == "continue":
            what_awaits()
            break
        elif choice == "back":
            location_two_cleared()
            break
        else:
            choice = input("Choose either TRAP, LITTLEHUT, CONTINUE or BACK: ").lower().strip()

    while stealth_check is False and perception_check is True:
        clear()
        print("OPTIONS:")
        print("\x1B[3mYou can move with stealth. Make a stealth check, if you wish by typing STEALTH.\nTo approach "
              "and investigate the house, type LITTLEHUT.\nIf you just wish to continue type CONTINUE.\nIf you wish "
              "to turn back to location two, type BACK.\x1B[23m\n")
        if choice == "stealth":
            stealth_check = True
            pickle.dump(stealth_check, open("checks.dat", "wb"))
            # take note of stealth check success of failure for later.
            print("\n" + random.choice(stealth_quotes) + "\n\n\n")
            press_to_continue()
            break
        elif choice == "littlehut":
            little_hut()
            break
        elif choice == "continue":
            what_awaits()
            break
        elif choice == "back":
            location_two_cleared()
            break
        else:
            choice = input("Choose either STEALTH, LITTLEHUT, CONTINUE or BACK: ").lower().strip()

    while stealth_check is True and perception_check is True:
        clear()
        print("OPTIONS:")
        print("\x1B[3mTo approach and investigate the house, type LITTLEHUT.\nIf you just wish to continue type "
              "CONTINUE.\nIf you wish to turn back to location two, type BACK.\x1B[23m\n")
        if choice == "littlehut":
            little_hut()
            break
        elif choice == "continue":
            what_awaits()
            break
        elif choice == "back":
            location_two_cleared()
            break
        else:
            choice = input("Choose either LITTLEHUT, CONTINUE or BACK: ").lower().strip()


def more_traps():
    trap_dc = int(18)
    if PC.perception_check(character) >= trap_dc:
        path_danger()
    else:
        seems_not()


def seems_not():
    clear()
    print("- SEEMSNOT -\n")
    sleep(2)
    print("You do a pretty thorough search for traps, but find nothing.\n\n\n")
    press_to_continue()


def path_danger():
    clear()
    print("- PATHDANGER -\n")
    sleep(2)
    print("You have a good look around this part of the path, visually searching the ground and the trees,\nlooking "
          "for any sign of a trap. And that’s exactly what you find.\nEtched into the trunk of one tree on the east "
          "side of the path, so well hidden\nthat it could be easily missed, you see a rune of some sort.\nYou’re not "
          "entirely unfamiliar with this sort of thing. A sorcerer friend\nof yours gave you a long lecture on these "
          "once. They are known as glyphs,\nand they trigger magical effects when someone comes near them.\nYou duck "
          "behind a tree and peer out, examining it from a distance.\nHow are you going to get past this?\n\n\n")

    print("OPTIONS:")
    print("\x1B[3mIf you want to go off the path and pass the tree on the right hand side, type GOAROUND.\nIf you "
          "want to drop to the ground and go under the level of the glyph, type DUCKUNDER.\nYou could also backtrack. "
          "To backtrack, type LOCATIONTWO.\nIf you want to ignore the glyph and continue north, type WHATAWAITS.\nThe "
          "entrance to the house is closer on the path than the glyph.\nTo visit the house without walking past the "
          "glyph, type LITTLEHUT.\x1B[23m\n")

    choice = input("What do you wish to do? "
                   "(GOAROUND, DUCKUNDER, LOCATIONTWO, WHATAWAITS or LITTLEHUT): ").lower().strip()
    while True:
        if choice == "goaround":
            go_around()
            break
        elif choice == "duckunder":
            duck_under()
            break
        elif choice == "locationtwo":
            location_two_cleared()
            break
        elif choice == "whatawaits":
            what_awaits()
            break
        elif choice == "littlehut":
            little_hut()
            break
        else:
            choice = input("Choose either GOAROUND, DUCKUNDER, LOCATIONTWO, WHATAWAITS or LITTLEHUT: ").lower().strip()


def go_around():
    clear()
    print("- GOAROUND -\n")
    sleep(2)
    print("You go around the eastern side of the tree, taking care to crouch as well, just to be safe.\nIf there is "
          "some sort of effect inherent in this glyph, you have managed to avoid it.\nGood work!\n\nHowever, "
          "could you go to the hut, visit there, while avoiding any effects the glyph had?\nPerhaps the glyph itself "
          "is redundant? There is no way of telling!\n\n\n")

    print("OPTIONS:")
    print("\x1B[3mTo investigate the little house, type LITTLEHUT.\nTo ignore the little house and continue down the "
          "path, type CONTINUE.\x1B[23m\n")

    choice = input("What do you wish to do? (LITTLEHUT or CONTINUE): ").lower().strip()
    while True:
        if choice == "littlehut":
            little_hut()
            break
        elif choice == "continue":
            what_awaits()
            break
        else:
            choice = input("Choose either LITTLEHUT or CONTINUE: ").lower().strip()


def duck_under():
    clear()
    print("- DUCKUNDER -\n")
    sleep(2)
    print("You crouch as you make your way forward along the path,\ntaking care to stay below the level of the "
          "glyph.\n\nIf there is any sort of effect that it is supposed to emanate,\nyou seem to be avoiding "
          "it.\n\n\n")

    print("OPTIONS:")
    print("\x1B[3mDo you want to investigate the hut? If so, type LITTLEHUT.\nTo ignore the little house and continue "
          "down the path, type CONTINUE.\x1B[23m\n")

    choice = input("What do you wish to do? (LITTLEHUT or CONTINUE): ").lower().strip()
    while True:
        if choice == "littlehut":
            little_hut()
            break
        elif choice == "continue":
            what_awaits()
            break
        else:
            choice = input("Choose either LITTLEHUT or CONTINUE: ").lower().strip()


def little_hut():
    clear()
    print("- LITTLEHUT -\n")
    sleep(2)
    print("You approach the little hut that sits to the side of the forest path.\nIt is well made, if a little "
          "dilapidated, and covered in vines and creepers.\n\nCautiously you approach the door, and slowly reach for "
          "the handle...\n\n\n")

    print("OPTIONS:")
    print("\x1B[3mDo you want to check for traps? Roll perception, by typing TRAP.\nTo press on, type "
          "CONTINUE.\x1B[23m\n")

    choice = input("What do you wish to do? (TRAP or CONTINUE): ").lower().strip()
    while True:
        if choice == "trap":
            little_hut_trap_checker()
            break
        elif choice == "continue":
            well_damn()
            break
        else:
            choice = input("Choose either TRAP or CONTINUE: ").lower().strip()


def little_hut_trap_checker():
    trap_dc = int(15)
    if PC.perception_check(character) >= trap_dc:
        print("\nYou rolled " + str(PC.perception_check(character)) + " for your perception check!")
        press_to_continue()
        hut_traps()
    else:
        print("\nYou rolled " + str(PC.perception_check(character)) + " for your perception check!"
                                                                      "\nWhat could go wrong?")
        well_damn()


def hut_traps():
    clear()
    print("- HUTTRAPS -\n")
    sleep(2)
    print("You search all around the door frame, and the ground, but cannot find \nanything that looks like a trap "
          "here. Cautiously you put your hand on\nthe door handle and quietly push down...\n\n\n")
    press_to_continue()
    cabin_entry()


def well_damn():
    clear()
    print("- WELLDAMN -\n")
    sleep(2)
    print("Try as you might, you cannot detect anything that looks like a trap around this door.\nShrugging, "
          "you reach for the door handle, turn it, and gently push the door inwards.\n\n\n")
    press_to_continue()
    cabin_entry()


def cabin_entry():
    clear()
    print("- CABINENTRY -\n")
    sleep(2)
    print("You cautiously edge inside the cabin, looking around. It appears empty, even though\na crackling fire "
          "burns in the hearth. There is a strange smell in here...\n\nSuddenly you feel something press against your "
          "skull, as if a giant\ninvisible hand were crushing it! You resist as best you can,\nbut the force is "
          "overwhelming. Within moments, you have blacked out.\n\nYou wake at what seems like many hours later.\nIt "
          "is dark inside the room, probably night-time, and the room is empty.\n\n\n")
    press_to_continue()
    inducted()


def inducted():
    clear()
    print("- INDUCTED -\n")
    sleep(2)
    print("Within the cabin there is a kind of burnt smell, like smouldering embers,\nand the room has only the most "
          "basic furniture. A table, a couple of chairs, a fireplace...\n\nSuddenly your heart stops. In the "
          "darkness, you see a figure, standing against\none of the walls, completely silent, watching you. A tall "
          "figure, and dressed\nall in armour. As you watch, this figure begins to glow, red in the darkness,"
          "\nand you see that it is in fact a knight! A sinister-looking tower of a Knight,\nholding a huge "
          "greatsword that shimmers with an unearthly radiance.\n\nThe Death Knight?\n\n\n")
    press_to_continue()
    clear()
    print("- INDUCTED -\n")
    print("Feeling a cold sweat break out on your brow, you feel for your weapon...\nNo, that’s gone, as are all your "
          "supplies.\n\n“Do not bother searching for your equipment, mortal,” a voice booms... it must be\nthe "
          "Knight’s although it seems to come from all around you rather than from his direction.\n\n“Listen mortal, "
          "and listen carefully!” the voice booms again.\n“I have a task for you. There is a knight who claims "
          "ownership over this forest,\na warrior who, like myself, is not of this realmmmm.....” A chill travels up "
          "your spine.\n\nThe voice is deep, booming, but hollow and devoid of life.\nAt least now you know you’re "
          "not speaking to the Death Knight. Who could this be then?\n\n\n")
    press_to_continue()
    clear()
    print("- INDUCTED -\n")
    print("“My followers call me the Blood Night of Kiaransalee. I am a loyal follower of Kiaransalee,\nthe Dark "
          "Goddess, Enemy of Lolth and Orcus, The Vengeful Banshee!”\n\nThese names make your blood run cold. You had "
          "thought that the Cult of Kiaransalee\nwas long dead. Their deeds are detailed in ancient histories, "
          "and they are\nresponsible for numerous atrocities throughout the ages.\n\n“My followers and I will see the "
          "Mother return to her former power...\nand we have chosen this Wood of Weathercote as the point of her "
          "arrival.\nIt is aligned with the unseen stars and the nodes of power that exist in this land...\nit is a "
          "small but potent place. “But this one who they call the Death Knight...\nHe must die, mortal. And you have "
          "been chosen by the Goddess as the bringer of his demise!”\n\n\n")
    press_to_continue()
    clear()
    print("- INDUCTED -\n")
    print("Your spirits lift a little. Isn’t this your quest anyway?\nYou are about to voice agreement when the Blood "
          "Knight adds,\n\n“And as reward, you will become my most exalted follower! My general, who shall\nstand "
          "beside me in glory as we return the Goddess Kiaransalee to her\nrightful place as ruler of this "
          "land!”\n\nThis part, you are not so much in agreeance with. You are stunned into silence.\nThe Blood "
          "Knight continues.\n\n“You must leave this place now.” He walks forward, taking a couple of massive\nsteps "
          "towards you, and red sparks skitter out from his feet as he walks.\n“Do not be afraid mortal. I am "
          "Myrkbrood, made from the embers of the cremated dead.\nAnd this weapon is of the Myrk as well!”\n\nFrom "
          "some unseen place the Blood Knight produces a long sword, glowing\nwith a red light, as if embers burn "
          "inside it.\n\n“This is known as a Sword of the Goddess’s Wrath. You will use it to slay the\none known as "
          "the Death Knight! And then, return it to me before the dawn.\nIf you refuse any part of this task, "
          "my followers will pursue you to the\nends of the world! You shall live a cursed life, always\nlooking over "
          "your shoulder. Are we in agreeance, mortal?”\n")
    press_to_continue()
    clear()
    print("- INDUCTED -\n")
    print("You take the sword in your hand. It pulsates with a volatile potency,\nand almost hurts to hold. The dark "
          "energy runs up your arm and\nyou feel a little of it creep into your very soul.\n\n\n")
    sleep(5)

    print("What is your response to the Blood Knight?")
    print("\x1B[3m“Hell yeah, sign me up!” Type DARKQUEST.\n“Aaahhh yeah, the first part of what you say, "
          "I can do that.\nBut the whole becoming your general thing... Not so sure.” Type NEGOTIATE.\n“Do you know "
          "what Blood Knight? Take your Sword of Whatever and stick it where the sun don’t shine!” Type "
          "BALLSYMOVE\x1B[23m\n")

    choice = input("What do you wish to answer? (DARKQUEST, NEGOTIATE or BALLSYMOVE): ").lower().strip()
    while True:
        if choice == "darkquest":
            dark_quest()
            break
        elif choice == "negotiate":
            negotiate()
            break
        elif choice == "ballsymove":
            ballsy_move()
        else:
            choice = input("Choose either DARKQUEST, NEGOTIATE or BALLSYMOVE: ").lower().strip()


def dark_quest():
    clear()
    print("- DARKQUEST -\n")
    sleep(2)

    global has_blood_knight_sword
    has_blood_knight_sword = True

    print("At these words, you hear a crackling sound, like logs moving in a fire,\nand through the Blood Knight’s "
          "visor, you see the twisted shape of a hideous smile\nmade out in embers, like a thin line of fire. You "
          "stare in horror.\n\n“Excellent, mortal! You have pleased me well. I would complete this task myself, "
          "but until\nthe Goddess’s arrival I cannot risk standing in sunlight. As soon as Kiaransalee comes,"
          "\nshe will grant me physical form. Then, for a time, I may roam free. Now go, fulfill your "
          "destiny!!!”\n\n\n")
    press_to_continue()
    clear()
    print("- DARKQUEST -\n")
    print("You stand, and, as if in trance, walk from the cabin. There, in a small pile outside\nthe door, "
          "are your belongings. You quickly check them: yes everything is there,\nincluding your provisions. You "
          "shoulder your backpack, regaining some small\nmeasure of comfort, and look around, getting your bearings. "
          "You wonder for a\nsecond if this was all a dream, but then you feel for your newly acquired sword...\nand "
          "yes, it is still there. Quickly you turn, open the door, and peer inside again...\nbut the hut is now "
          "empty. The Blood Knight is gone, and the table and chairs\nare overturned and covered in cobwebs and "
          "dust.\n\nWhat?! What just happened?\n\n\n")
    print("\x1B[3mYou now wield the Sword of the Goddess's Wrath!\n\x1B[23m\n")
    press_to_continue()
    what_awaits()


def negotiate():
    clear()
    print("- NEGOTIATE -\n")
    sleep(2)
    print("The Blood Knight’s roar fills the room.\n\n“You will accept this quest, or you will die as all mortal "
          "flesh dies,\non the end of my sword!”\n\nHe brings his greatsword underneath your chin. You try to move, "
          "but you are frozen\non the spot,as if by magic. You don’t doubt his words,\nand you are unarmed. It seems "
          "you have little choice.\n\n\n")

    print("OPTIONS:")
    print("\x1B[3mIf you still voice your disapproval, type NOFEAR.\n“If you bow to this intimidating warrior and "
          "accept his quest, type DARKQUEST\x1B[23m\n")

    choice = input("What do you wish to do? (NOFEAR or DARKQUEST): ").lower().strip()
    while True:
        if choice == "nofear":
            no_fear()
            break
        elif choice == "darkquest":
            dark_quest()
            break
        else:
            choice = input("Choose either NOFEAR or DARKQUEST: ").lower().strip()


def no_fear():
    clear()
    print("- NOFEAR -\n")
    sleep(2)
    print("The Blood Knight keeps his blade levelled at your chin, malice seeping\nfrom every inch of his ruined, "
          "infernal body. You try to move again, but\nare completely unable to. It seems you are held there with some "
          "sort of spell.\nYou have heard of the Myrkbrood before, but to actually be faced\nwith one – that "
          "isanother thing entirely.\n\n“You seem devoid of fear, traveller,” the Blood Knight growls.\n“Do I not "
          "intimidate you? I am impressed. Such a soul as you will\nmake a perfect general. Now BOW, or DIE LIKE A "
          "DOG!”\n\n\n")

    print("OPTIONS:")
    print("\x1B[3mDo you bow, and accept the quest? If so, type DARKQUEST.\nOr do you still resist? "
          "Type RESIST\x1B[23m\n")

    choice = input("What do you wish to do? (DARKQUEST or RESIST): ").lower().strip()
    while True:
        if choice == "darkquest":
            dark_quest()
            break
        elif choice == "resist":
            resist()
            break
        else:
            choice = input("Choose either DARKQUEST or RESIST: ").lower().strip()


def resist():
    clear()
    print("- RESIST -\n")
    sleep(2)
    print("At your final words of defiance, the Blood Knight of Kiaransalee thrusts his blade forward.\n\n\n")
    press_to_continue()

    blood_knight_attack = int(dice.roll('1d20')) + 8

    if blood_knight_attack >= PC.ac(character):
        oh_well()
    else:
        run()


def run():
    clear()
    print("- RUN -\n")
    sleep(2)
    print("It is all a blur, but somehow you avoid the killing blow!\nQuickly you get to your feet, now able to move, "
          "and bolt for the door.\nYou hear loud cursing in Infernal as you pull the door shut behind you,"
          "\nremembering that the Blood Knight said he couldn't walk in daylight. Yet.\nYour belongings are outside "
          "the door, but in the confusion,\nyou left the magic sword behind!\n\n\n")
    press_to_continue()
    what_awaits()


def ballsy_move():
    clear()
    print("- BALLSYMOVE -\n")
    sleep(2)
    print("There is a long, awkward silence, and you fear the worst.\nThen the Blood Knight throws his head back and "
          "laughs uproariously,\nthe sound filling the room and nearly deafening you. You wince, covering your "
          "ears.\nFinally he stops, and addresses you, leveling his greatsword under your chin.\nSuddenly you feel "
          "paralyzed, as if by a spell.\n\n“You are very brave, traveller.You will make a perfect general for the "
          "Goddess. Now BOW, or DIE LIKE A DOG!”\n\n\n")

    print("OPTIONS:")
    print("\x1B[3mDo you bow to the Blood Knight’s will? If so, type DARKQUEST.\nIf you still resist, "
          "type RESIST\x1B[23m\n")

    choice = input("What do you wish to do? (DARKQUEST or RESIST): ").lower().strip()
    while True:
        if choice == "darkquest":
            dark_quest()
            break
        elif choice == "resist":
            resist()
            break
        else:
            choice = input("Choose either DARKQUEST or RESIST: ").lower().strip()


def what_awaits():

    global perception_check

    if perception_check:
        chance_roll()
    else:
        hold_that_thought()


def chance_roll():

    global stealth_check

    if stealth_check:
        good_chance = int(dice.roll('1d100')) + 10
        if good_chance <= 33:
            dry_bones()
        elif 34 <= good_chance <= 65:
            phantasm()
        elif good_chance >= 66:
            quiet_path()
    else:
        bad_chance = int(dice.roll('1d100'))
        if bad_chance <= 33:
            dry_bones()
        elif 34 <= bad_chance <= 65:
            phantasm()
        elif bad_chance >= 66:
            quiet_path()


def death_check():
    if PC.hp(character) - damage_taken <= 0:
        oh_well()
    else:
        pass


def oh_well():
    clear()
    print("- OHWELL -\n")
    sleep(2)
    print("\x1B[3mHere endeth your adventure.\x1B[23m\n\n\n")
    sleep(2)
    print("\x1B[3mBut this doesn’t have to be the end. Why not take another stab at this?\nGo and roll up a fresh PC, "
          "and try again!\nThere might be other things unexplored in this adventure,\nand surely Darek Brewmont "
          "deserves a second chance?\x1B[23m\n\nThank you for playing The Death Knight’s Squire!\n\n\n")
    raise SystemExit(0)


playAgain = "yes"
while playAgain == "yes" or playAgain == "y":
    start_game()
    playAgain = input("Do you want to play again? (yes or y to continue playing): ")
