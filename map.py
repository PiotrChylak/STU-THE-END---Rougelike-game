import curses
import actor as a
import item
import random


class Map:

    def __init__(self, x, y, layout, hero):
        self.x = x
        self.y = y
        self.mapLayout = layout
        self.occupied = [[None for _ in range(y)] for _ in range(x)]
        self.hero = hero
        self.explored_area = set()
        self.view_distance = 4

    def check(self, x1, y1):
        print(self.mapLayout[x1][y1].description)

    def update_explored_area(self):
        hero_x, hero_y = self.get_actor_position(self.hero)
        for x in range(hero_x - self.view_distance, hero_x + self.view_distance + 1):
            for y in range(hero_y - self.view_distance, hero_y + self.view_distance + 1):
                if 0 <= x < self.x and 0 <= y < self.y:
                    self.explored_area.add((x, y))

    def print_map(self, stdscr):
        for x in range(self.x):
            for y in range(self.y):
                if not (0 <= x < self.x and 0 <= y < self.y):
                    continue

                field = self.mapLayout[x][y]
                if (x, y) not in self.explored_area:
                    stdscr.addch(x, y * 2, " ")
                else:
                    if field.actorPointer:
                        if isinstance(field.actorPointer, a.Enemy):
                            stdscr.addstr(x, y * 2, field.actorPointer.character, curses.color_pair(1))
                        else:
                            stdscr.addstr(x, y * 2, field.actorPointer.character, curses.color_pair(3))
                    elif field.itemPointer:
                        stdscr.addstr(x, y * 2, field.itemPointer.character, curses.color_pair(2))
                    else:
                        stdscr.addch(x, y * 2, field.character, curses.color_pair(4))

    def place_player(self):
        for x in range(self.x):
            for y in range(self.y):
                if self.mapLayout[x][y].canStand and not self.occupied[y][x]:
                    self.hero.x = x + 2
                    self.hero.y = y + 2
                    self.mapLayout[x + 2][y + 2].actorPointer = self.hero
                    self.occupied[x + 2][y + 2] = self.hero
                    return

    def place_enemy(self, enemy):
        available_positions = [(x, y) for x in range(self.x) for y in range(self.y) if
                               self.mapLayout[x][y].canStand and not self.occupied[x][y]]

        available_positions = [(x, y) for x, y in available_positions
                               if abs(x - self.hero.x) > 1 or abs(y - self.hero.y) > 1]

        if available_positions:
            x, y = random.choice(available_positions)
            enemy.x = x
            enemy.y = y
            self.mapLayout[x][y].actorPointer = enemy
            self.occupied[x][y] = enemy

    def place_item(self, item):
        available_positions = [(x, y) for x in range(self.x) for y in range(self.y) if
                               self.mapLayout[x][y].canStand and not self.occupied[x][y]]

        available_positions = [(x, y) for x, y in available_positions
                               if abs(x - self.hero.x) > 1 or abs(y - self.hero.y) > 1]

        if available_positions:
            x, y = random.choice(available_positions)
            item.x = x
            item.y = y
            self.mapLayout[x][y].itemPointer = item

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

    def is_level_cleared(self):
        for row in self.mapLayout:
            for field in row:
                if field.actorPointer and field.actorPointer != self.hero:
                    return False
        return True

    @staticmethod
    def check_defeated_enemies(enemies):
        defeated_enemies = [enemy for enemy in enemies if enemy.hp <= 0]
        for enemy in defeated_enemies:
            enemies.remove(enemy)

    def move_actor(self, new_x, new_y, stdscr):
        if self.mapLayout[new_x][new_y].canStand and not self.occupied[new_x][new_y]:

            old_x, old_y = self.hero.x, self.hero.y
            self.mapLayout[old_x][old_y].actorPointer = None
            self.occupied[old_x][old_y] = None

            self.hero.x = new_x
            self.hero.y = new_y

            self.mapLayout[new_x][new_y].actorPointer = self.hero
            self.occupied[new_x][new_y] = self.hero

            self.explored_area.add((new_x, new_y))

        else:
            if not self.mapLayout[new_x][new_y].canStand:
                stdscr.addstr(self.y + 6, 0, f"Cannot move to position ({new_x}, {new_y}). It's a wall.", curses.color_pair(1))
            # elif not self.occupied[new_x][new_y]:
            #     stdscr.addstr(0, self.x + self.y, f"Fighting with {self.mapLayout[new_x][new_y].actorPointer.name} at position ({new_x}, {new_y}).", curses.color_pair(1))

    def get_actor_position(self, actor):
        for x in range(self.x):
            for y in range(self.y):
                if self.mapLayout[x][y].actorPointer == actor:
                    return x, y
        return None

    def is_item_on_field(self, stdscr):
        item_position = self.mapLayout[self.hero.x][self.hero.y].itemPointer
        if item_position:
            stdscr.addstr(0, self.x + self.y,
                          f"You found an {item_position.description} ({item_position.item_type})", curses.A_BOLD)
            stdscr.addstr(1, self.x + self.y, f"(+ {item_position.hp_bonus} HP, + {item_position.dmg_bonus} DMG, + {item_position.initiative_bonus} INITIATIVE)", curses.color_pair(2))
            stdscr.addstr(3, self.x + self.y, "If you don't want this item move 2 times.")
            return True
        return False

    def is_enemy_on_field(self, stdscr, x, y):
        if self.mapLayout[x][y].actorPointer and self.mapLayout[x][y].actorPointer != self.hero:
            stdscr.addstr(0, self.x + self.y, f"You fighting with {self.mapLayout[x][y].actorPointer.name}!", curses.A_BOLD | curses.color_pair(1))
            return True
        return False

    def are_enemies_and_items_nearby(self):
        hero_x, hero_y = self.get_actor_position(self.hero)

        nearby_entities = []

        for x in range(max(0, hero_x - 3), min(self.x, hero_x + 4)):
            for y in range(max(0, hero_y - 3), min(self.y, hero_y + 4)):
                if 0 <= x < self.x - 1 and 0 <= y < self.y - 1:
                    entity = self.mapLayout[x][y].actorPointer or self.mapLayout[x][y].itemPointer
                    if entity:
                        nearby_entities.append((x, y, entity))

        return nearby_entities
