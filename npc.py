import dice

def giantCentipede():
    giantCentipede.Name = "Giant Centipede"
    giantCentipede.Size = "Small"
    giantCentipede.Type = "beast"
    giantCentipede.Alignment = "Unaligned"
    giantCentipede.AC = int(13)
    giantCentipede.HP = int(4)
    giantCentipede.Speed = "30 ft. / Climb 30 ft."
    giantCentipede.Strength = int(5)
    giantCentipede.Dexterity = int(14)
    giantCentipede.Constitution = int(12)
    giantCentipede.Intelligence = int(1)
    giantCentipede.Wisdom = int(7)
    giantCentipede.Charisma = int(3)
    giantCentipede.Senses = "Blindsight 30 ft., passive Perception 8"
    giantCentipede.PerceptionSkill = int(((giantCentipede.Wisdom - 10) / 2) + 5)
    giantCentipede.StealthSkill = int(((giantCentipede.Dexterity - 10) / 2) + 5)
    giantCentipede.CR = "1/4 (50 xp)"
    giantCentipede.BiteToHit = int(dice.roll('1d20')) + 4
    giantCentipede.BiteDamage = int(dice.roll('1d4')) + 2

def cultist():
    cultist.Name = "Cultist"
    cultist.Size = "Medium"
    cultist.Type = "human"
    cultist.Alignment = "Lawful Evil"
    cultist.AC = int(12)
    cultist.HP = int(9)
    cultist.Speed = "30 ft. / Climb 30 ft."
    cultist.Strength = int(11)
    cultist.Dexterity = int(12)
    cultist.Constitution = int(10)
    cultist.Intelligence = int(10)
    cultist.Wisdom = int(11)
    cultist.Charisma = int(10)
    cultist.Senses = "passive Perception 10"
    cultist.ReligionSkill = int(((cultist.Intelligence - 10) / 2) + 2)
    cultist.DeceptionSkill = int(((cultist.Charisma - 10) / 2) + 2)
    cultist.CR = "1/8 (25 xp)"
    cultist.HandCrossbowToHit = int(dice.roll('1d20')) + 3
    cultist.HandCrossbowDamage = int(dice.roll('1d6'))
    cultist.ScimitarToHit = int(dice.roll('1d20')) + 2
    cultist.ScimitarDamage = int(dice.roll('1d6'))
