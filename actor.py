import curses
import random


class Actor:
    def __init__(self, hp, dmg, initiative, x, y):
        self.hp = hp
        self.dmg = dmg
        self.initiative = initiative
        self.inventory = {item_type: None for item_type in ["Hat", "Hoodie", "Accessory", "Drink", "Weapon"]}
        self.backpack = []
        self.is_alive = True
        self.x = x
        self.y = y

    def equip_item(self, item, stdscr, x, y):
        if self.inventory[item.item_type] is None:
            self.inventory[item.item_type] = item
            self.update_stats_up(item)
            self.backpack.remove(item)
            stdscr.addstr(0, x + y, f"You equipped {item.name}.", curses.A_BOLD)
        else:
            stdscr.addstr(0, x + y,
                          f"You already have {self.inventory[item.item_type].name} equipped in the {item.item_type} slot.")

    def unequip_item(self, item_type, stdscr, x, y):
        if self.inventory[item_type] is not None:
            item = self.inventory[item_type]
            self.inventory[item_type] = None
            self.update_stats_down(item)
            self.backpack.append(item)
            stdscr.addstr(7, x + y, f"You unequipped {item.name}.", curses.A_BOLD)
        else:
            stdscr.addstr(0, x + y, f"You don't have any item equipped in the {item_type} slot.")

    def add_item(self, item):
        self.backpack.append(item)

    def throw_item(self, item):
        self.backpack.remove(item)

    def move_item_to_backpack(self, item):
        self.backpack.append(item)
        self.inventory[item.type] = None

    def update_stats_up(self, item):
        self.hp += item.hp_bonus
        self.dmg += item.dmg_bonus
        self.initiative += item.initiative_bonus

    def update_stats_down(self, item):
        self.hp -= item.hp_bonus
        self.dmg -= item.dmg_bonus
        self.initiative -= item.initiative_bonus

    def current_eq(self, game_map, stdscr):
        iterator = 1
        max_y, max_x = stdscr.getmaxyx()
        eq_window_width = max_x - game_map.x - game_map.y - 2

        stdscr.addstr(game_map.y, max_x - eq_window_width, "Your current equipment: ", curses.A_BOLD)

        for item_type, item in self.inventory.items():
            if item is not None:
                stdscr.addstr(game_map.y + iterator, max_x - eq_window_width,
                              f"{item_type.capitalize()}: {item.name}"
                              f" + {item.hp_bonus} HP, "
                              f" + {item.dmg_bonus} DMG, "
                              f" + {item.initiative_bonus} INITIATIVE")
                iterator += 1
            else:
                stdscr.addstr(game_map.y + iterator, max_x - eq_window_width, f"{item_type.capitalize()}: Empty")
                iterator += 1

    def pick_an_item(self, stdscr, game_map):
        stdscr.addstr(2, game_map.x + game_map.y,
                      f"Now {game_map.mapLayout[self.x][self.y].itemPointer.description} is in your backpack.",
                      curses.A_BOLD)
        self.add_item(game_map.mapLayout[self.x][self.y].itemPointer)
        game_map.remove_object(self.x, self.y)

    def open_backpack(self, stdscr, game_map):
        stdscr.addstr(0, game_map.x + game_map.y, "Backpack content:", curses.A_BOLD)
        for i, item_in_backpack in enumerate(self.backpack, start=1):
            stdscr.addstr(i, game_map.x + game_map.y,
                          f"{i}. {item_in_backpack.description} ({item_in_backpack.item_type})"
                          f" + {[item_in_backpack.hp_bonus]} HP, "
                          f" + {[item_in_backpack.dmg_bonus]} DMG, "
                          f" + {[item_in_backpack.initiative_bonus]} INITIATIVE")

        selected_item_number = stdscr.getch() - ord('0')
        if 1 <= selected_item_number <= len(self.backpack):
            selected_item = self.backpack[selected_item_number - 1]
            self.equip_item(selected_item, stdscr, game_map.x, game_map.y)
            stdscr.refresh()
        else:
            stdscr.addstr(0, game_map.x + game_map.y, "Invalid item number.")

    def open_inventory(self, stdscr, game_map):
        stdscr.addstr(0, game_map.x + game_map.y,
                      "This is your inventory, choose the number of item you want to move to the backpack:",
                      curses.A_BOLD)
        for i, (item_type, item_in_inventory) in enumerate(self.inventory.items(), start=1):
            if item_in_inventory is not None:
                stdscr.addstr(i, game_map.x + game_map.y, f"{i}. {item_in_inventory.item_type}: "
                                                          f" + {[item_in_inventory.hp_bonus]} HP, "
                                                          f" + {[item_in_inventory.dmg_bonus]} DMG, "
                                                          f" + {[item_in_inventory.initiative_bonus]} INITIATIVE")
            else:
                stdscr.addstr(i, game_map.x + game_map.y, f"{i}. {item_type}: Empty")

        selected_item_number = stdscr.getch() - ord('0')
        if 1 <= selected_item_number <= len(self.inventory):
            selected_item = list(self.inventory.values())[selected_item_number - 1]
            if selected_item is not None:
                self.unequip_item(selected_item.item_type, stdscr, game_map.x, game_map.y)
                stdscr.refresh()

    def collect_item(self, stdscr, game_map):
        if game_map.is_item_on_field(stdscr):
            self.current_stats(game_map, stdscr)
            self.current_eq(game_map, stdscr)
            game_map.print_map(stdscr)
            key1 = stdscr.getch()
            if key1 == ord('p'):
                self.pick_an_item(stdscr, game_map)

    def duel(self, stdscr, game_map, x, y):
        if game_map.is_enemy_on_field(stdscr, x, y):
            single_attack(self, game_map.mapLayout[x][y].actorPointer, stdscr, game_map.x, game_map.y)
            if game_map.mapLayout[x][y].actorPointer.hp <= 0:
                game_map.remove_object(x, y)

    def current_stats(self, game_map, stdscr):
        stdscr.addstr(game_map.y, 0, "Your current stats: ", curses.A_BOLD)
        stdscr.addstr(game_map.y + 1, 0, f"HP: {self.hp}")
        stdscr.addstr(game_map.y + 2, 0, f"DMG: {self.dmg}")
        stdscr.addstr(game_map.y + 3, 0, f"INITIATIVE: {self.initiative}")
        stdscr.addstr(game_map.y + 5, 0, f"Your position: ({self.x}, {self.y})", curses.A_BOLD)


class Player(Actor):
    def __init__(self, hp, dmg, initiative, x, y):
        super().__init__(hp, dmg, initiative, x, y)
        self.dmg = dmg
        self.hp = hp
        self.name = "HERO"
        self.character = "@"
        self.initiative = initiative
        self.x = x
        self.y = y


def update_status(self):
    if self.hp <= 0:
        self.is_alive = False


def single_attack(player, enemy, stdsrc, x, y):
    hero_initiative = random.randint(1, 20) + player.initiative
    enemy_initiative = random.randint(1, 20) + enemy.initiative

    combat_iterator = 1

    if hero_initiative >= 12:
        current_attacker = player
        current_defender = enemy
    else:
        current_attacker = enemy
        current_defender = player

    attack_roll = random.randint(1, 20) + current_attacker.dmg
    if attack_roll >= random.randint(1, 10) + enemy_initiative:
        damage_roll = random.randint(1, 6) + current_attacker.dmg
        current_defender.hp -= damage_roll

        if current_defender.hp <= 0:
            stdsrc.addstr(combat_iterator, x + y,
                          f"{current_attacker.name} dealing {damage_roll} dmg to {current_defender.name}.")
            stdsrc.addstr(combat_iterator + 1, x + y, f"{current_defender.name} died!")
            combat_iterator += 2
        else:
            stdsrc.addstr(combat_iterator, x + y,
                          f"{current_attacker.name} dealing {damage_roll} dmg to {current_defender.name}. "
                          f"{current_defender.name} current HP = {current_defender.hp}")
            combat_iterator += 1
    else:
        stdsrc.addstr(combat_iterator, x + y, f"{current_attacker.name} missed.")
        combat_iterator += 1


class Enemy(Actor):
    def __init__(self, hp, dmg, name, initiative, x, y):
        super().__init__(hp, dmg, initiative, x, y)
        self.dmg = dmg
        self.hp = hp
        self.name = name
        self.character = "!"
        self.initiative = initiative
        self.x = x
        self.x = y

    def is_player_in_attack_range(self, player):
        return abs(player.x - self.x) <= 1 and abs(player.y - self.y) <= 1

    def is_player_in_vision_distance(self, player):
        return abs(player.x - self.x) <= 3 and abs(player.y - self.y) <= 3

    def move_enemy(self, player, game_map, stdscr):
        if self.is_player_in_attack_range(player):
            player.duel(stdscr, game_map, self.x, self.y)
        elif self.is_player_in_vision_distance(player):
            self.chase_player(player, game_map)
        else:
            self.move_randomly(game_map)

    def chase_player(self, player, game_map):
        while self.is_player_in_vision_distance(player):
            dx = player.x - self.x
            dy = player.y - self.y

            if abs(dx) <= 3 or abs(dy) <= 3:
                if dx != 0:
                    new_x = self.x + (dx // abs(dx))
                else:
                    new_x = self.x

                if dy != 0:
                    new_y = self.y + (dy // abs(dy))
                else:
                    new_y = self.y

                if game_map.mapLayout[new_x][new_y].canStand and not game_map.occupied[new_x][new_y]:
                    self.move_to_position(game_map, new_x, new_y)
                else:
                    break
            else:
                break

    def move_randomly(self, game_map):
        available_moves = [(self.x + dx, self.y + dy) for dx in [-1, 1] for dy in [-1, 1] if dx != 0 or dy != 0]
        random.shuffle(available_moves)

        for new_x, new_y in available_moves:
            if 0 <= new_x < game_map.x and 0 <= new_y < game_map.y and game_map.mapLayout[new_x][new_y].canStand and not \
                    game_map.occupied[new_x][new_y]:
                self.move_to_position(game_map, new_x, new_y)
                break

    def move_to_position(self, game_map, new_x, new_y):
        old_x, old_y = self.x, self.y
        game_map.mapLayout[old_x][old_y].actorPointer = None
        game_map.occupied[old_x][old_y] = None
        self.x = new_x
        self.y = new_y
        game_map.mapLayout[new_x][new_y].actorPointer = self
        game_map.occupied[new_x][new_y] = self

# def simulate_combat(player, enemy, stdscr, x, y):
#     while player.hp > 0 and enemy.hp > 0:
#         single_attack(player, enemy, stdscr, x, y)
#         if enemy.hp <= 0:
#             return player
#         elif player.hp <= 0:
#             return enemy
#     #    player, enemy = enemy, player
#     # linia sprawiajaca ze w kazdej kolejce najpierw atakuje gracz a nastepnie przeciwnik
