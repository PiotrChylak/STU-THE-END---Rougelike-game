class Field:
    def __init__(self):
        self.actorPointer = None
        self.itemList = None
        self.name = None


class Floor(Field):
    def __init__(self):
        super().__init__()
        self.character = "-"
        self.canStand = True
        self.name = "podloga"


class Wall(Field):
    def __init__(self):
        super().__init__()
        self.character = "#"
        self.canStand = False
        self.name = "sciana"