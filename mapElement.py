class Field:
    def __init__(self):
        self.actorPointer = None
        self.itemList = None
        self.description = None
        self.itemPointer = None


class Floor(Field):
    def __init__(self):
        super().__init__()
        self.character = "-"
        self.canStand = True
        self.description = "floor"


class Wall(Field):
    def __init__(self):
        super().__init__()
        self.character = "#"
        self.canStand = False
        self.description = "wall"
