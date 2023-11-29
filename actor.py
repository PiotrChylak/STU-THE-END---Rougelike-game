class Actor:
    def __init__(self, hp, dmg):
        self.base_hp = hp
        self.base_dmg = dmg
        self.inventory = []

    def equip_item(self, item):
        self.inventory.append(item)
        self.update_stats()

    def unequip_item(self, item):
        self.inventory.remove(item)
        self.update_stats()

    def update_stats(self):
        self.hp = sum(item.hp_bonus for item in self.inventory) + self.base_hp
        self.dmg = sum(item.dmg_bonus for item in self.inventory) + self.base_dmg


class Player(Actor):
    def __init__(self, hp, dmg, initiative):
        super().__init__(hp, dmg)
        self.dmg = dmg
        self.hp = hp
        self.name = "HERO"
        self.character = "@"
        self.initiative = initiative


class Enemy(Actor):
    def __init__(self, hp, dmg, name, initiative):
        super().__init__(hp, dmg)
        self.dmg = dmg
        self.hp = hp
        self.name = name
        self.character = "!"
        self.initiative = initiative

