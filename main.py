import curses
import actor as a
import item
import mapElement as mE
import map as m
import MapGenerator
import Info
import data


def main(stdscr):
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_BLACK, curses.COLOR_BLACK)

    def print_position_info(x, y, label, info_iterator, word, enemy_info, hp, dmg, initiative, color_pair):
        stdscr.addstr(info_iterator, game_map.x + game_map.y, f"{label}", curses.color_pair(color_pair) | curses.A_BOLD)
        stdscr.addstr(f" is {word} at field ({x}, {y}).")

        if enemy_info:
            stdscr.addstr(f" [HP = {hp}][DMG = {dmg}][INITIATIVE = {initiative}]", curses.color_pair(1))

    def display_info():
        stdscr.addstr(0, game_map.x + game_map.y, "Items and Enemies on the map:", curses.A_BOLD)
        info_iterator = 1

        nearby_entities = game_map.are_enemies_and_items_nearby()

        for x_idx, row in enumerate(game_map.mapLayout):
            for y_idx, field in enumerate(row):
                if field.actorPointer and field.actorPointer != player:
                    label = field.actorPointer.name

                    if nearby_entities and (x_idx, y_idx, field.actorPointer) in nearby_entities:
                        hp = field.actorPointer.hp
                        dmg = field.actorPointer.dmg
                        initiative = field.actorPointer.initiative
                        print_position_info(x_idx, y_idx, label, info_iterator, "currently", True, hp, dmg, initiative,
                                            color_pair=1)
                    else:
                        print_position_info(x_idx, y_idx, label, info_iterator, "currently", False, None, None, None,
                                            color_pair=1)

                    info_iterator += 1

                if field.itemPointer:
                    label = field.itemPointer.description

                    if nearby_entities and (x_idx, y_idx, field.itemPointer) in nearby_entities:
                        print_position_info(x_idx, y_idx, label, info_iterator, "placed", False, None, None, None,
                                            color_pair=2)
                        stdscr.addstr("\n")
                        info_iterator += 1
                    else:
                        print_position_info(x_idx, y_idx, label, info_iterator, "placed", False, None, None, None,
                                            color_pair=2)
                        stdscr.addstr("\n")
                        info_iterator += 1

        stdscr.refresh()

    player = a.Player(hp=100, dmg=10, initiative=2, x=1, y=1)

    enemies, items = data.lvl_items_and_enemies(1)

    mG = MapGenerator.MapGenerator(20, 20, 5)
    map_layout = mG.generate_map()

    game_map = m.Map(20, 20, map_layout, player)
    game_map.place_player()
    current_level = 1

    for enemy in enemies:
        game_map.place_enemy(enemy)

    for item_ in items:
        game_map.place_item(item_)

    while True:

        player.current_stats(game_map, stdscr)
        player.current_eq(game_map, stdscr)
        game_map.check_defeated_enemies(enemies)
        stdscr.addstr(game_map.y + 7, 0, "If you want to see Game Controls press 'c'")
        stdscr.addstr(game_map.y, game_map.x + game_map.y - 20, f"Current LEVEL: {current_level}", curses.A_BOLD)

        if len(enemies) == 0:
            stdscr.addstr(game_map.y + 1, game_map.x + game_map.y - 20, f"Level {current_level} cleared!", curses.A_BOLD)
        else:
            stdscr.addstr(game_map.y + 1, game_map.x + game_map.y - 20, f"Enemies left: {len(enemies)}", curses.A_BOLD)

        key = stdscr.getch()

        stdscr.clear()

        if game_map.is_level_cleared():
            if current_level < 3:
                stdscr.refresh()

                if key == 10:
                    player.hp += player.hp + current_level * 50
                    player.dmg += player.dmg + current_level * 10
                    player.initiative += player.initiative + current_level * 3
                    current_level += 1
                    enemies, items = data.lvl_items_and_enemies(current_level)
                    mG = MapGenerator.MapGenerator(20, 20, 5)
                    map_layout = mG.generate_map()

                    game_map = m.Map(20, 20, map_layout, player)
                    game_map.place_player()

                    for enemy in enemies:
                        game_map.place_enemy(enemy)

                    for item_ in items:
                        game_map.place_item(item_)

            else:
                Info.display_win(stdscr)
                key = stdscr.getch()

                break

        if key == ord('q'):
            break

        elif key == curses.KEY_UP:
            player.duel(stdscr, game_map, player.x - 1, player.y)
            if player.hp <= 0:
                Info.display_game_over(stdscr)
                key = stdscr.getch()
                break
            game_map.move_actor(player.x - 1, player.y, stdscr)
            player.collect_item(stdscr, game_map)
            for enemy in enemies:
                enemy.move_enemy(player, game_map, stdscr)

        elif key == curses.KEY_DOWN:
            player.duel(stdscr, game_map, player.x + 1, player.y)
            if player.hp <= 0:
                Info.display_game_over(stdscr)
                key = stdscr.getch()
                break
            game_map.move_actor(player.x + 1, player.y, stdscr)
            player.collect_item(stdscr, game_map)
            for enemy in enemies:
                enemy.move_enemy(player, game_map, stdscr)

        elif key == curses.KEY_LEFT:
            player.duel(stdscr, game_map, player.x, player.y - 1)
            if player.hp <= 0:
                Info.display_game_over(stdscr)
                key = stdscr.getch()
                break
            game_map.move_actor(player.x, player.y - 1, stdscr)
            player.collect_item(stdscr, game_map)
            for enemy in enemies:
                enemy.move_enemy(player, game_map, stdscr)

        elif key == curses.KEY_RIGHT:
            player.duel(stdscr, game_map, player.x, player.y + 1)
            if player.hp <= 0:
                Info.display_game_over(stdscr)
                key = stdscr.getch()
                break
            game_map.move_actor(player.x, player.y + 1, stdscr)
            player.collect_item(stdscr, game_map)
            for enemy in enemies:
                enemy.move_enemy(player, game_map, stdscr)

        elif key == ord('b'):
            game_map.print_map(stdscr)
            player.current_stats(game_map, stdscr)
            player.current_eq(game_map, stdscr)
            player.open_backpack(stdscr, game_map)

        elif key == ord('e'):
            game_map.print_map(stdscr)
            player.current_stats(game_map, stdscr)
            player.open_inventory(stdscr, game_map)

        elif key == ord('i'):
            display_info()

        elif key == ord('c'):
            Info.display_controls_info(stdscr)
            stdscr.clear()

        game_map.update_explored_area()
        game_map.print_map(stdscr)
        stdscr.refresh()


curses.wrapper(main)
