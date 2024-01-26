import curses


def display_controls_info(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "GAME CONTROLS:", curses.A_BOLD)
    stdscr.addstr(2, 0, "Movement:", curses.A_BOLD)
    stdscr.addstr(3, 2, "Arrow Up: Move Up")
    stdscr.addstr(4, 2, "Arrow Down: Move Down")
    stdscr.addstr(5, 2, "Arrow Left: Move Left")
    stdscr.addstr(6, 2, "Arrow Right: Move Right")

    stdscr.addstr(8, 0, "Actions:", curses.A_BOLD)
    stdscr.addstr(9, 2, "B: Open Backpack")
    stdscr.addstr(10, 2, "E: Open Equipment")
    stdscr.addstr(11, 2, "I: Display Map Info")

    stdscr.addstr(13, 0, "Combat:", curses.A_BOLD)
    stdscr.addstr(14, 2, "Arrow keys: Fight with Enemy")
    stdscr.addstr(15, 2, "P: Pick Up Item")

    stdscr.addstr(17, 0, "Control: ", curses.A_BOLD)
    stdscr.addstr(18, 2, "C: Display Controls Info")
    stdscr.addstr(19, 2, "Q: Quit Game")

    stdscr.refresh()
    stdscr.getch()



