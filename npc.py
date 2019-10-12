import dice


class NPC:
    def __init__(self, name, ac, hp, strength, dexterity, constitution, intelligence,
                 wisdom, charisma, toHitMelee, damageMelee, toHitRanged, damageRanged):
        self.name = name
        self.ac = ac
        self.hp = hp
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.toHitMelee = toHitMelee
        self.damageMelee = damageMelee
        self.toHitRanged = toHitRanged
        self.damageRanged = damageRanged

    def to_hit_melee(self):
        return int(dice.roll('1d20')) + self.toHitMelee

    def to_hit_ranged(self):
        return int(dice.roll('1d20')) + self.toHitRanged

    def damage_d4_melee(self):
        return int(dice.roll('1d4')) + self.damageMelee

    def damage_d6_melee(self):
        return int(dice.roll('1d6')) + self.damageMelee

    def damage_d8_melee(self):
        return int(dice.roll('1d8')) + self.damageMelee

    def damage_d4_ranged(self):
        return int(dice.roll('1d4')) + self.damageRanged

    def damage_d6_ranged(self):
        return int(dice.roll('1d6')) + self.damageRanged

    def damage_d8_ranged(self):
        return int(dice.roll('1d8')) + self.damageRanged

    def perception_check(self):
        wis_mod = int((self.wisdom - 10) / 2 + 3)
        return int(dice.roll('1d20')) + wis_mod

    def stealth_check(self):
        dex_mod = int((self.dexterity - 10) / 2 + 3)
        return int(dice.roll('1d20')) + dex_mod


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