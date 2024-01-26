import curses
import random


class Actor:
    def __init__(self, hp, dmg, initiative, x, y):
        self.hp = hp
        self.dmg = dmg
        self.initiative = initiative
        self.inventory = {item_type: None for item_type in ["Helmet", "Armor", "Gloves", "Boots", "Weapon"]}
        self.backpack = []
        self.is_alive = True
        self.x = x
        self.y = y

    def equip_item(self, item, stdscr, x, y):
        if self.inventory[item.item_type] is None:
            self.inventory[item.item_type] = item
            self.update_stats_up(item)
            self.backpack.remove(item)
            stdscr.addstr(0, x + y, f"You equipped {item.name}.")
        else:
            stdscr.addstr(0, x + y, f"You already have {self.inventory[item.item_type].name} equipped in the {item.item_type} slot.")

    def unequip_item(self, item_type, stdscr, x, y):
        if self.inventory[item_type] is not None:
            item = self.inventory[item_type]
            self.inventory[item_type] = None
            self.update_stats_down(item)
            self.backpack.append(item)
            stdscr.addstr(0, x + y, f"You unequipped {item.name}.")
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
                              f"{item_type.capitalize()}: {item.name} "
                              f" + {item.hp_bonus} HP, "
                              f" + {item.dmg_bonus} DMG, "
                              f" + {item.initiative_bonus} INITIATIVE")
                iterator += 1
            else:
                stdscr.addstr(game_map.y + iterator, max_x - eq_window_width, f"{item_type.capitalize()}: Empty")
                iterator += 1

    def pick_an_item(self, stdscr, game_map):
        stdscr.addstr(2, game_map.x + game_map.y,
                      f"You picked up {game_map.mapLayout[self.x][self.y].itemPointer.description}.")
        stdscr.addstr(3, game_map.x + game_map.y,
                      "Now this item is in your backpack.")
        self.add_item(game_map.mapLayout[self.x][self.y].itemPointer)
        game_map.remove_object(self.x, self.y)

    def open_backpack(self, stdscr, game_map):
        stdscr.addstr(0, game_map.x + game_map.y, "Backpack content:")
        for i, item_in_backpack in enumerate(self.backpack, start=1):
            stdscr.addstr(i, game_map.x + game_map.y, f"{i}. {item_in_backpack.description} "
                                                      f" + {[item_in_backpack.hp_bonus]} HP, "
                                                      f" + {[item_in_backpack.dmg_bonus]} DMG, "
                                                      f" + {[item_in_backpack.initiative_bonus]} INITIATIVE")

        selected_item_number = stdscr.getch() - ord('0')
        if 1 <= selected_item_number <= len(self.backpack):
            selected_item = self.backpack[selected_item_number - 1]
            self.equip_item(selected_item, stdscr, game_map.x, game_map.y)
        else:
            stdscr.addstr(0, game_map.x + game_map.y, "Invalid item number.")

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
            stdsrc.addstr(combat_iterator, x + y, f"{current_attacker.name} dealing {damage_roll} dmg to {current_defender.name}.")
            stdsrc.addstr(combat_iterator + 1, x + y, f"{current_defender.name} died!")
            combat_iterator += 2
        else:
            stdsrc.addstr(combat_iterator, x + y, f"{current_attacker.name} dealing {damage_roll} dmg to {current_defender.name}. "
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


# def simulate_combat(player, enemy, stdscr, x, y):
#     while player.hp > 0 and enemy.hp > 0:
#         single_attack(player, enemy, stdscr, x, y)
#         if enemy.hp <= 0:
#             return player
#         elif player.hp <= 0:
#             return enemy
#     #    player, enemy = enemy, player
#     # linia sprawiajaca ze w kazdej kolejce najpierw atakuje gracz a nastepnie przeciwnik
