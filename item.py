class Item:
    def __init__(self, name, hp_bonus, dmg_bonus, initiative_bonus, item_type):
        self.character = "$"
        self.name = name
        self.description = f"{name}"
        self.hp_bonus = hp_bonus
        self.dmg_bonus = dmg_bonus
        self.initiative_bonus = initiative_bonus
        self.item_type = item_type
