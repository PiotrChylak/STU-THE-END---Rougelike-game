import mapElement as mE


class Map:
    def __init__(self, x, y, layout):
        self.x = x
        self.y = y
        self.mapLayout = layout
        self.occupied = [[None for _ in range(y)] for _ in range(x)]

    def check(self, x1, y1):
        print(self.mapLayout[x1][y1].description)

    def add_object(self, obj, x, y):
        if 0 <= x < self.x and 0 <= y < self.y:
            if self.occupied[x][y] is None:
                self.mapLayout[x][y].actorPointer = obj
                self.occupied[x][y] = obj
            else:
                print(f"cannot place an object on the field ({x}, {y}). the field is already occupied.")
        else:
            print("invalid coordinate provided")
