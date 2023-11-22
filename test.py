import mapElement as mE
import map as m
import actor as a

# Creating a simple map
map_layout = [
    [mE.Wall(), mE.Wall(), mE.Wall(), mE.Wall(), mE.Wall()],
    [mE.Wall(), mE.Floor(), mE.Floor(), mE.Floor(), mE.Wall()],
    [mE.Wall(), mE.Floor(), mE.Floor(), mE.Floor(), mE.Wall()],
    [mE.Wall(), mE.Floor(), mE.Floor(), mE.Floor(), mE.Wall()],
    [mE.Wall(), mE.Wall(), mE.Wall(), mE.Wall(), mE.Wall()],
]

# Creating a map instance
game_map = m.Map(5, 5, map_layout)

# Creating a player and enemy
player = a.Player(hp=100, dmg=10)
enemy = a.Enemy(hp=50, dmg=5)

# Placing the player and enemy on the map
game_map.mapLayout[1][1].actorPointer = player
game_map.mapLayout[3][3].actorPointer = enemy

# Displaying the map with the characters
for row in game_map.mapLayout:
    for field in row:
        if field.actorPointer:
            print(field.actorPointer.character, end=' ')
        else:
            print(field.character, end=' ')
    print()

# Finding the player's location and displaying the description
for x_idx, row in enumerate(game_map.mapLayout):
    for y_idx, field in enumerate(row):
        if field.actorPointer == player:
            print(f"You are on a {field.description} field at position ({x_idx}, {y_idx}).")

# Finding the enemy's location and displaying the description
for x_idx, row in enumerate(game_map.mapLayout):
    for y_idx, field in enumerate(row):
        if field.actorPointer == enemy:
            print(f"The enemy is on a {field.description} field at position ({x_idx}, {y_idx}).")



