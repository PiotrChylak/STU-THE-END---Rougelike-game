import mapElement as mE
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
                    obj.itemPointer = obj  # Ustawienie wskaźnika
                else:
                    print("Invalid object type.")
            else:
                print(f"Cannot place an object on the field ({x}, {y}). The field is already occupied.")
        else:
            print("Invalid coordinate provided.")

#    def delete_object(self, obj, x, y):
