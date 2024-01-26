import curses
import actor as a
import item
import mapElement as mE
import map as m
import MapGenerator
import Info


def main(stdscr):
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)

    def print_position_info(x, y, label, info_iterator, word, enemy_info, hp, dmg, initiative, color_pair):
        stdscr.addstr(info_iterator, game_map.x + game_map.y, f"{label}", curses.color_pair(color_pair) | curses.A_BOLD)
        stdscr.addstr(f" is {word} at field ({x}, {y}).")
        if enemy_info:
            stdscr.addstr(f" [HP = {hp}][DMG = {dmg}][INITIATIVE = {initiative}]", curses.color_pair(1))

    def display_info():
        stdscr.addstr(0, game_map.x + game_map.y, "Items and Enemies on the map:", curses.A_BOLD)
        info_iterator = 1
        for x_idx, row in enumerate(game_map.mapLayout):
            for y_idx, field in enumerate(row):
                if field.actorPointer and field.actorPointer != player:
                    label = field.actorPointer.name

                    if game_map.are_enemies_nearby(stdscr):
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
                    print_position_info(x_idx, y_idx, field.itemPointer.description, info_iterator, "placed", False,
                                        None, None, None, color_pair=2)
                    stdscr.addstr("\n")
                    info_iterator += 1

        stdscr.refresh()

    mG = MapGenerator.MapGenerator(30, 30, 7)
    map_layout = mG.generate_map()

    player = a.Player(hp=100, dmg=10, initiative=2, x=5, y=5)
    game_map = m.Map(30, 30, map_layout, player)

    while True:

        player.current_stats(game_map, stdscr)
        player.current_eq(game_map, stdscr)
        stdscr.addstr(game_map.y + 7, 0, "If you want to see Game Controls press 'c'")

        key = stdscr.getch()

        stdscr.clear()

        if key == ord('q'):
            break

        elif key == curses.KEY_UP:
            player.duel(stdscr, game_map, player.x - 1, player.y)
            game_map.move_actor(player.x - 1, player.y, stdscr)
            player.collect_item(stdscr, game_map)

        elif key == curses.KEY_DOWN:
            player.duel(stdscr, game_map, player.x + 1, player.y)
            game_map.move_actor(player.x + 1, player.y, stdscr)
            player.collect_item(stdscr, game_map)

        elif key == curses.KEY_LEFT:
            player.duel(stdscr, game_map, player.x, player.y - 1)
            game_map.move_actor(player.x, player.y - 1, stdscr)
            player.collect_item(stdscr, game_map)

        elif key == curses.KEY_RIGHT:
            player.duel(stdscr, game_map, player.x, player.y + 1)
            game_map.move_actor(player.x, player.y + 1, stdscr)
            player.collect_item(stdscr, game_map)

        elif key == ord('b'):
            game_map.print_map(stdscr)
            player.current_stats(game_map, stdscr)
            player.current_eq(game_map, stdscr)
            player.open_backpack(stdscr, game_map)

        elif key == ord('e'):
            game_map.print_map(stdscr)
            player.current_stats(game_map, stdscr)

        elif key == ord('i'):
            display_info()

        elif key == ord('c'):
            Info.display_controls_info(stdscr)
            stdscr.clear()

        game_map.print_map(stdscr)
        stdscr.refresh()


curses.wrapper(main)
