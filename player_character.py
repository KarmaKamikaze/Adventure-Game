import dice
import pickle


class PC:
    def __init__(self, name, strength, dexterity, constitution, intelligence, wisdom, charisma):
        self.name = name
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma

    def hp(self):
        current_hp = int(8 + (self.constitution - 10) / 2) - damage_taken
        return current_hp

    def ac(self):
        return int(13 + (self.dexterity - 10) / 2)

    def to_hit_melee(self):
        strength_modifier = int((self.strength - 10) / 2 + 2)
        return int(dice.roll('1d20')) + strength_modifier

    def to_hit_ranged(self):
        dexterity_modifier = int((self.dexterity - 10) / 2 + 2)
        return int(dice.roll('1d20')) + dexterity_modifier

    def stealth_check(self):
        dexterity_modifier = int((self.dexterity - 10) / 2 + 2)
        return int(dice.roll('1d20')) + 3 + dexterity_modifier

    def perception_check(self):
        wisdom_modifier = int((self.wisdom - 10) / 2 + 2)
        return int(dice.roll('1d20')) + 3 + wisdom_modifier


# might not be needed once ported to main.py
damage_taken = 0

character = pickle.load(open("character.dat", "rb"))