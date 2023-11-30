import random


class Actor:
    def __init__(self, hp, dmg, initiative):
        self.hp = hp
        self.dmg = dmg
        self.initiative = initiative
        self.inventory = []
        self.is_alive = True

    def equip_item(self, item):
        self.inventory.append(item)
        self.update_stats()

    def unequip_item(self, item):
        self.inventory.remove(item)
        self.update_stats()

    def update_stats(self):
        self.hp = sum(item.hp_bonus for item in self.inventory) + self.hp
        self.dmg = sum(item.dmg_bonus for item in self.inventory) + self.dmg
        self.initiative = sum(item.initiative_bonus for item in self.inventory) + self.initiative


class Player(Actor):
    def __init__(self, hp, dmg, initiative):
        super().__init__(hp, dmg, initiative)
        self.dmg = dmg
        self.hp = hp
        self.name = "HERO"
        self.character = "@"
        self.initiative = initiative


class Enemy(Actor):
    def __init__(self, hp, dmg, name, initiative):
        super().__init__(hp, dmg, initiative)
        self.dmg = dmg
        self.hp = hp
        self.name = name
        self.character = "!"
        self.initiative = initiative


def update_status(self):
    if self.hp <= 0:
        self.is_alive = False


def single_attack(player, enemy):
    hero_initiative = random.randint(1, 20) + player.initiative
    enemy_initiative = random.randint(1, 20) + enemy.initiative

    if hero_initiative >= enemy_initiative:
        current_attacker = player
        current_defender = enemy
    else:
        current_attacker = enemy
        current_defender = player

    attack_roll = random.randint(1, 20) + current_attacker.dmg
    if attack_roll >= 16:
        damage_roll = random.randint(1, 6) + current_attacker.dmg
        current_defender.hp -= damage_roll

    #     if current_defender.hp <= 0:
    #         print(f"{current_attacker.name} dealing {damage_roll} dmg to {current_defender.name}.")
    #         print(f"{current_defender.name} died!")
    #     else:
    #         print(f"{current_attacker.name} dealing {damage_roll} dmg to {current_defender.name}.")
    # else:
    #     print(f"{current_attacker.name} missed.")


def simulate_combat(player, enemy):
    while player.hp > 0 and enemy.hp > 0:
        single_attack(player, enemy)
        if enemy.hp <= 0:
            return player
        elif player.hp <= 0:
            return enemy
        # player, enemy = enemy, player
