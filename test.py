import item
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

# tworzenie oraz dodawanie gracza i przeciwnika
player = a.Player(hp=100, dmg=10)
game_map.add_object(player, 1, 1)

enemy1 = a.Enemy(hp=50, dmg=5, name = "Ghost")
game_map.add_object(enemy1, 3, 3)

# tworzenie przedmiotu
item1 = i.Item("Sword", 0, 5)
game_map.add_object(item1, 2, 2)

item4 = i.Item("Big Sword", 0, 10)
game_map.add_object(item4, 1, 3)

# tworzenie obiektow ktore nie moga zostac dodane
item2 = i.Item("Shield", 20, 0)
item3 = i.Item("Helmet", 10, 5)
game_map.add_object(item2, 5, 5)
game_map.add_object(item3, 3, 3)

enemy2 = a.Enemy(hp=100, dmg=30, name="Vampire")
game_map.add_object(enemy2, 6, 6)
enemy3 = a.Enemy(hp=10, dmg=10, name="monke")
game_map.add_object(enemy3, 1, 1)

# game_map.mapLayout[1][1].actorPointer = player
# game_map.mapLayout[3][3].actorPointer = enemy
# game_map.mapLayout[2][2].itemPointer = item1
# game_map.mapLayout[1][3].itemPointer = item4


# wyswietlanie mapy
for row in game_map.mapLayout:
    for field in row:
        if field.actorPointer:
            print(field.actorPointer.character, end=' ')
        elif field.itemPointer:
            print(field.itemPointer.character, end=' ')
        else:
            print(field.character, end=' ')
    print()


# Wyswietlanie informacji o polozeniu gracza, przeciwnika i przedmiotu
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