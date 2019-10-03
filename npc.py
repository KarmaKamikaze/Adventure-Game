import dice

def darekBrewmont():
    darekBrewmont.name = "Darek Brewmont"
    darekBrewmont.size = "Medium"
    darekBrewmont.type = "humanoid"
    darekBrewmont.alignment = "Lawful Good"
    darekBrewmont.AC = int(10)
    darekBrewmont.HP = int(4)
    darekBrewmont.speed = "30 ft."
    darekBrewmont.strength = int(10)
    darekBrewmont.dexterity = int(10)
    darekBrewmont.constitution = int(10)
    darekBrewmont.intelligence = int(10)
    darekBrewmont.wisdom = int(10)
    darekBrewmont.charisma = int(10)
    darekBrewmont.senses = "passive Perception 10"
    darekBrewmont.weaponToHit = int(dice.roll('1d20') + 2)
    darekBrewmont.weaponDamage = int(dice.roll('1d4') + 2)

def giantCentipede():
    giantCentipede.name = "Giant Centipede"
    giantCentipede.size = "Small"
    giantCentipede.type = "beast"
    giantCentipede.alignment = "Unaligned"
    giantCentipede.AC = int(13)
    giantCentipede.HP = int(4)
    giantCentipede.speed = "30 ft. / Climb 30 ft."
    giantCentipede.strength = int(5)
    giantCentipede.dexterity = int(14)
    giantCentipede.constitution = int(12)
    giantCentipede.intelligence = int(1)
    giantCentipede.wisdom = int(7)
    giantCentipede.charisma = int(3)
    giantCentipede.senses = "Blindsight 30 ft., passive Perception 8"
    giantCentipede.perceptionSkill = int(((giantCentipede.wisdom - 10) / 2) + 5)
    giantCentipede.stealthSkill = int(((giantCentipede.dexterity - 10) / 2) + 5)
    giantCentipede.CR = "1/4 (50 xp)"
    giantCentipede.biteToHit = int(dice.roll('1d20') + 4)
    giantCentipede.biteDamage = int(dice.roll('1d4') + 2)

def cultist():
    cultist.name = "Cultist"
    cultist.size = "Medium"
    cultist.type = "human"
    cultist.alignment = "Lawful Evil"
    cultist.AC = int(12)
    cultist.HP = int(9)
    cultist.speed = "30 ft. / Climb 30 ft."
    cultist.strength = int(11)
    cultist.dexterity = int(12)
    cultist.constitution = int(10)
    cultist.intelligence = int(10)
    cultist.wisdom = int(11)
    cultist.charisma = int(10)
    cultist.senses = "passive Perception 10"
    cultist.religionSkill = int(((cultist.intelligence - 10) / 2) + 2)
    cultist.deceptionSkill = int(((cultist.charisma - 10) / 2) + 2)
    cultist.CR = "1/8 (25 xp)"
    cultist.handCrossbowToHit = int(dice.roll('1d20') + 3)
    cultist.handCrossbowDamage = int(dice.roll('1d6'))
    cultist.scimitarToHit = int(dice.roll('1d20') + 2)
    cultist.scimitarDamage = int(dice.roll('1d6'))

def deathKnight():
    deathKnight.name = "Death Knight"
    deathKnight.size = "Medium"
    deathKnight.type = "undead"
    deathKnight.alignment = "Lawful Evil"
    deathKnight.AC = int(15)
    deathKnight.HP = int(28)
    deathKnight.speed = "30 ft."
    deathKnight.strength = int(15)
    deathKnight.dexterity = int(11)
    deathKnight.constitution = int(13)
    deathKnight.intelligence = int(12)
    deathKnight.wisdom = int(10)
    deathKnight.charisma = int(5)
    deathKnight.strMod = int((deathKnight.strength - 10) / 2)
    deathKnight.strSave = int(deathKnight.strMod + 1)
    deathKnight.senses = "Darkvision 60 ft., passive Perception 8"
    deathKnight.CR = "1 (200 xp)"
    deathKnight.hellreaverToHit = int(dice.roll('1d20') + 5)
    deathKnight.hellreaverDamage = int(dice.roll('1d8') + 3)

def goblin():
    goblin.name = "Goblin"
    goblin.size = "Small"
    goblin.type = "humanoid"
    goblin.alignment = "Neutral Evil"
    goblin.AC = int(15)
    goblin.HP = int(7)
    goblin.speed = "30 ft."
    goblin.strength = int(8)
    goblin.dexterity = int(14)
    goblin.constitution = int(10)
    goblin.intelligence = int(10)
    goblin.wisdom = int(8)
    goblin.charisma = int(8)
    goblin.senses = "Darkvision 60 ft., passive Perception 9"
    goblin.CR = "1/4 (50 xp)"
    goblin.spearToHit = int(dice.roll('1d20') + 4)
    goblin.spearDamage = int(dice.roll('1d6') + 2)
    goblin.bonestaffToHit = int(dice.roll('1d20') + 1)
    goblin.bonestaffDamage = int(dice.roll('1d4') + 1)
    goblin.battleaxeToHit = int(dice.roll('1d20') + 1)
    goblin.battleaxeDamage = int(dice.roll('1d6') + 1)

def kobold():
    kobold.name = "Kobold"
    kobold.size = "Small"
    kobold.type = "humanoid"
    kobold.alignment = "Lawful Evil"
    kobold.AC = int(12)
    kobold.HP = int(5)
    kobold.speed = "30 ft."
    kobold.strength = int(7)
    kobold.dexterity = int(15)
    kobold.constitution = int(9)
    kobold.intelligence = int(8)
    kobold.wisdom = int(7)
    kobold.charisma = int(8)
    kobold.senses = "Darkvision 60 ft., passive Perception 8"
    kobold.CR = "1/8 (25 xp)"
    kobold.daggerToHit = int(dice.roll('1d20') + 4)
    kobold.daggerDamage = int(dice.roll('1d4') + 2)
    kobold.fireballToHit = int(dice.roll('1d20') + 2)
    kobold.fireballDamage = int(dice.roll('1d6'))

def forestBat():
    forestBat.name = "Forest Bat"
    forestBat.size = "Medium"
    forestBat.type = "beast"
    forestBat.alignment = "Unaligned"
    forestBat.AC = int(12)
    forestBat.HP = int(5)
    forestBat.speed = "30 ft."
    forestBat.strength = int(7)
    forestBat.dexterity = int(15)
    forestBat.constitution = int(8)
    forestBat.intelligence = int(2)
    forestBat.wisdom = int(12)
    forestBat.charisma = int(4)
    forestBat.senses = "Blindsight 60 ft., passive Perception 11"
    forestBat.CR = "1/8 (25 xp)"
    forestBat.biteToHit = int(dice.roll('1d20'))
    forestBat.biteDamage = int(dice.roll('1d4'))

def skeleton():
    skeleton.name = "Skeleton"
    skeleton.size = "Medium"
    skeleton.type = "undead"
    skeleton.alignment = "Lawful Evil"
    skeleton.AC = int(13)
    skeleton.HP = int(13)
    skeleton.speed = "30 ft."
    skeleton.strength = int(10)
    skeleton.dexterity = int(14)
    skeleton.constitution = int(15)
    skeleton.intelligence = int(6)
    skeleton.wisdom = int(8)
    skeleton.charisma = int(5)
    skeleton.senses = "Darkvision 60 ft., passive Perception 9"
    skeleton.CR = "1/4 (50 xp)"
    skeleton.shortswordToHit = int(dice.roll('1d20') + 4)
    skeleton.shortswordDamage = int(dice.roll('1d6') + 2)