class Field:
    def __init__(self):
        self.actorPointer = None
        self.itemList = None


class Floor(Field):
    def __init__(self):
        super().__init__()
        self.character = "-"
        self.canStand = True


class Wall(Field):
    def __init__(self):
        super().__init__()
        self.character = "#"
        self.canStand = False
