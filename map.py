import curses
import actor as a
import item


class Map:
    def __init__(self, x, y, layout, hero):
        self.x = x
        self.y = y
        self.mapLayout = layout
        self.occupied = [[None for _ in range(y)] for _ in range(x)]
        self.hero = hero

    def check(self, x1, y1):
        print(self.mapLayout[x1][y1].description)

    def print_map(self, stdscr):
        for y, row in enumerate(self.mapLayout):
            for x, field in enumerate(row):
                if field.actorPointer:
                    stdscr.addstr(y, x * 2, field.actorPointer.character)
                elif field.itemPointer:
                    stdscr.addstr(y, x * 2, field.itemPointer.character)
                else:
                    stdscr.addstr(y, x * 2, field.character)

    def add_object(self, obj, x, y):
        if 0 <= x < self.x and 0 <= y < self.y:
            if not self.mapLayout[x][y].canStand:
                print(f"Cannot place an object on a wall at position ({x}, {y}).")
            elif self.occupied[x][y] is None:
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

    def move_actor(self, new_x, new_y, stdscr):
        if self.mapLayout[new_x][new_y].canStand and not self.occupied[new_x][new_y]:

            old_x, old_y = self.hero.x, self.hero.y
            self.mapLayout[old_x][old_y].actorPointer = None
            self.occupied[old_x][old_y] = None

            self.hero.x = new_x
            self.hero.y = new_y

            self.mapLayout[new_x][new_y].actorPointer = self.hero
            self.occupied[new_x][new_y] = self.hero

        else:
            if not self.mapLayout[new_x][new_y].canStand:
                stdscr.addstr(0, self.x + self.y, f"Cannot move to position ({new_x}, {new_y}). It's a wall.")
            elif not self.occupied[new_x][new_y]:
                stdscr.addstr(0, self.x + self.y,
                              f"Fighting with {self.mapLayout[new_x][new_y].actorPointer.name} at position ({new_x}, {new_y}).",
                              curses.COLOR_RED)

    def get_actor_position(self, actor):
        for x in range(self.x):
            for y in range(self.y):
                if self.mapLayout[x][y].actorPointer == actor:
                    return x, y
        return None

    def is_item_on_field(self, stdscr):
        if self.mapLayout[self.hero.x][self.hero.y].itemPointer:
            stdscr.addstr(0, self.x + self.y,
                          f"You found an {self.mapLayout[self.hero.x][self.hero.y].itemPointer.description}")
            stdscr.addstr(1, self.x + self.y,
                          "If you don't want this item move 2 times.")
            return True
        return False

    def is_enemy_on_field(self, stdscr, x, y):
        if self.mapLayout[x][y].actorPointer and self.mapLayout[x][y].actorPointer != self.hero:
            stdscr.addstr(0, self.x + self.y, f"You fighting with {self.mapLayout[x][y].actorPointer.name}")
            return True
        return False

    def are_enemies_nearby(self, stdscr):
        hero_x, hero_y = self.get_actor_position(self.hero)

        for x in range(max(0, hero_x - 3), min(self.x, hero_x + 4)):
            for y in range(max(0, hero_y - 3), min(self.y, hero_y + 4)):
                if 0 <= x < self.x - 1 and 0 <= y < self.y - 1:
                    if self.mapLayout[x][y].actorPointer and self.mapLayout[x][y].actorPointer != self.hero:
                        return True
        return False
