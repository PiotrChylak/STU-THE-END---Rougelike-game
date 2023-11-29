import actor as a
import item


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
                if isinstance(obj, a.Enemy) or isinstance(obj, a.Player):
                    self.mapLayout[x][y].actorPointer = obj
                    self.occupied[x][y] = obj
                elif isinstance(obj, item.Item):
                    self.mapLayout[x][y].itemPointer = obj
                    obj.itemPointer = obj
                else:
                    print("Invalid object type.")
            else:
                print(f"Cannot place an object on the field ({x}, {y}). The field is already occupied.")
        else:
            print("Invalid coordinate provided.")

    def remove_object(self, x, y):
        if 0 <= x < self.x and 0 <= y < self.y:
            if self.mapLayout[x][y].actorPointer and isinstance(self.mapLayout[x][y].actorPointer, a.Enemy):
                print(f"Enemy {self.mapLayout[x][y].actorPointer.name} removed from position ({x}, {y}).")
                self.mapLayout[x][y].actorPointer = None
                self.occupied[x][y] = None
            elif self.mapLayout[x][y].itemPointer and isinstance(self.mapLayout[x][y].itemPointer, item.Item):
                print(f"Item {self.mapLayout[x][y].itemPointer.description} removed from position ({x}, {y}).")
                self.mapLayout[x][y].itemPointer = None
            else:
                print("No object to remove at this position.")
        else:
            print("Invalid coordinate provided.")
