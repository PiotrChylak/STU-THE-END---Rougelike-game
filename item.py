class Item:
    def __init__(self, name, hp_bonus, dmg_bonus):
        self.character = "$"
        self.name = name
        self.description = f"item: {name}"
        self.hp_bonus = hp_bonus
        self.dmg_bonus = dmg_bonus
