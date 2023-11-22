class Actor:
    def __init__(self, hp, dmg):
        self.hp = hp
        self.dmg = dmg


class Player(Actor):
    def __init__(self, hp, dmg):
        super().__init__(hp, dmg)
        self.character = "@"


class Enemy(Actor):
    def __init__(self, hp, dmg):
        super().__init__(hp, dmg)
        self.character = "!"

