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