import mapElement as mE
import map as m
import actor as a
import item as i

map_layout = [
    [mE.Wall(), mE.Wall(), mE.Wall(), mE.Wall(), mE.Wall()],
    [mE.Wall(), mE.Floor(), mE.Floor(), mE.Floor(), mE.Wall()],
    [mE.Wall(), mE.Floor(), mE.Floor(), mE.Floor(), mE.Wall()],
    [mE.Wall(), mE.Floor(), mE.Floor(), mE.Floor(), mE.Wall()],
    [mE.Wall(), mE.Wall(), mE.Wall(), mE.Wall(), mE.Wall()],
]

game_map = m.Map(5, 5, map_layout)

player = a.Player(hp=100, dmg=10, initiative=2)
game_map.add_object(player, 1, 1)

# przeciwnik rowny z bohaterem
enemy1 = a.Enemy(hp=100, dmg=10, name="Ghost", initiative=2)
game_map.add_object(enemy1, 3, 3)
# przeciwnik z którym bohater nie ma praktycznie żadnych szans na początku
enemy2 = a.Enemy(hp=120, dmg=20, name="Vampire", initiative=5)
game_map.add_object(enemy2, 6, 6)
# przecinik który raczej przegrywa z bohaterem
enemy3 = a.Enemy(hp=15, dmg=6, name="monke", initiative=10)
game_map.add_object(enemy3, 1, 1)
# przeciwnik ktory w pojedynke nie stanowi zadnego zagrozenia dla gracza
enemy4 = a.Enemy(hp=35, dmg=6, name="small wolf", initiative=2)
# przeciwnik ktory jest duzym wyzwaniem dla bohatera
enemy5 = a.Enemy(hp=100, dmg=15, name="Dark Knight", initiative=3)

item1 = i.Item("Sword", 0, 2, 0)
game_map.add_object(item1, 2, 2)

item4 = i.Item("Big Sword", 0, 7, -2)
game_map.add_object(item4, 1, 3)

item_0 = i.Item("no item", 0, 0, 0)
item2 = i.Item("Shield", 20, 0, 0)
item3 = i.Item("Helmet", 10, 5, 0)
game_map.add_object(item2, 5, 5)
game_map.add_object(item3, 3, 3)

def print_map():
    for r in game_map.mapLayout:
        for f in r:
            if f.actorPointer:
                print(f.actorPointer.character, end=' ')
            elif f.itemPointer:
                print(f.itemPointer.character, end=' ')
            else:
                print(f.character, end=' ')
        print()


print_map()


def print_position_info(x, y, obj_type):
    print(f"{obj_type} is on a {game_map.mapLayout[x][y].description} field at position ({x}, {y}).")


for x_idx, row in enumerate(game_map.mapLayout):
    for y_idx, field in enumerate(row):
        if field.actorPointer == player:
            print_position_info(x_idx, y_idx, "player")
        if field.actorPointer == enemy1:
            print_position_info(x_idx, y_idx, enemy1.name)
        if field.itemPointer == item1:
            print_position_info(x_idx, y_idx, item1.description)
        if field.itemPointer == item4:
            print_position_info(x_idx, y_idx, item4.description)

game_map.remove_object(1, 3)

print_map()


def test_combat(hero, enemy, item, iterations=1000):
    player_wins = 0
    enemy_wins = 0

    for _ in range(iterations):
        player_copy = a.Player(hero.hp, hero.dmg, hero.initiative)
        player_copy.equip_item(item)
        player_copy.update_stats()
        enemy_copy = a.Enemy(enemy.hp, enemy.dmg, enemy.name, enemy.initiative)

        result = a.simulate_combat(player_copy, enemy_copy)
        if result == player_copy:
            player_wins += 1
        else:
            enemy_wins += 1
    if player_wins < 40:
        print("Almost Impossible to win")
    if 40 <= player_wins < 200:
        print("Heroic")
    if 200 <= player_wins < 400:
        print("Hard")
    if 400 <= player_wins < 600:
        print("50/50")
    if 600 <= player_wins < 900:
        print("Easy")
    if 900 <= player_wins <= 1000:
        print("Almost Impossible to lose")

    print(f"Hero with {item.name} wins {player_wins} times with {enemy.name}")
    print(f"{enemy.name} wins {enemy_wins} times with Hero with {item.name}\n")


test_combat(player, enemy1, item_0, 1000)
# test_combat(player, enemy1, item4, 1000)
# test_combat(player, enemy1, item1, 1000)

test_combat(player, enemy2, item_0, 1000)
# test_combat(player, enemy2, item1, 1000)
# test_combat(player, enemy2, item4, 1000)

test_combat(player, enemy3, item_0, 1000)
# test_combat(player, enemy3, item1, 1000)
# test_combat(player, enemy3, item4, 1000)

test_combat(player, enemy4, item_0, 1000)
# (player, enemy4, item1, 1000)
# test_combat(player, enemy4, item4, 1000)

test_combat(player, enemy5, item_0, 1000)
# test_combat(player, enemy5, item1, 1000)
# test_combat(player, enemy5, item4, 1000)
