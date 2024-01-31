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
    stdscr.addstr(9, 2, "B: Open Backpack (Choose number of item to put in to your EQ)")
    stdscr.addstr(10, 2, "E: Open Equipment (Chose number of item to remove it from EQ and move it to your BackPack)")
    stdscr.addstr(11, 2, "I: Display Map Info")

    stdscr.addstr(13, 0, "Combat:", curses.A_BOLD)
    stdscr.addstr(14, 2, "Arrow keys: Fight with Enemy")
    stdscr.addstr(15, 2, "P: Pick Up Item")

    stdscr.addstr(17, 0, "Control: ", curses.A_BOLD)
    stdscr.addstr(18, 2, "C: Display Controls Info")
    stdscr.addstr(19, 2, "ENTER: Proceed to next level after killing all enemies")
    stdscr.addstr(20, 2, "Q: Quit Game")

    stdscr.refresh()
    stdscr.getch()


def display_game_over(stdscr):
    stdscr.clear()
    stdscr.addstr(5, 0, "            ███▀▀▀██ ███▀▀▀███ ███▀█▄█▀███ ██▀▀▀", curses.color_pair(1))
    stdscr.addstr(6, 0, "            ██    ██ ██     ██ ██   █   ██ ██", curses.color_pair(1))
    stdscr.addstr(7, 0, "            ██   ▄▄▄ ██▄▄▄▄▄██ ██   ▀   ██ ██▀▀▀", curses.color_pair(1))
    stdscr.addstr(8, 0, "            ██    ██ ██     ██ ██       ██ ██", curses.color_pair(1))
    stdscr.addstr(9, 0, "            ███▄▄▄██ ██     ██ ██       ██ ██▄▄▄", curses.color_pair(1))
    stdscr.addstr(10, 0, "", curses.color_pair(1))
    stdscr.addstr(11, 0, "           ███▀▀▀███  ▀███  ██▀ ██▀▀▀ ██▀▀▀▀██▄", curses.color_pair(1))
    stdscr.addstr(12, 0, "           ██     ██    ██  ██  ██    ██     ██", curses.color_pair(1))
    stdscr.addstr(13, 0, "           ██     ██    ██  ██  ██▀▀▀ ██▄▄▄▄▄▀▀", curses.color_pair(1))
    stdscr.addstr(14, 0, "           ██     ██    ██  █▀  ██    ██    ██", curses.color_pair(1))
    stdscr.addstr(15, 0, "           ███▄▄▄███     ▀█▀    ██▄▄▄ ██    ██▄", curses.color_pair(1))
    stdscr.addstr(16, 0, "", curses.color_pair(1))
    stdscr.addstr(17, 0, "                    ██               ██", curses.color_pair(1))
    stdscr.addstr(18, 0, "                  ████▄   ▄▄▄▄▄▄▄   ▄████", curses.color_pair(1))
    stdscr.addstr(19, 0, "                     ▀▀█▄█████████▄█▀▀", curses.color_pair(1))
    stdscr.addstr(20, 0, "                       █████████████", curses.color_pair(1))
    stdscr.addstr(21, 0, "                       ██▀▀▀███▀▀▀██", curses.color_pair(1))
    stdscr.addstr(22, 0, "                       ██   ███   ██", curses.color_pair(1))
    stdscr.addstr(23, 0, "                       █████▀▄▀█████", curses.color_pair(1))
    stdscr.addstr(24, 0, "                        ███████████", curses.color_pair(1))
    stdscr.addstr(25, 0, "                    ▄▄▄██  █▀█▀█  ██▄▄▄", curses.color_pair(1))
    stdscr.addstr(26, 0, "                    ▀▀██           ██▀▀", curses.color_pair(1))
    stdscr.addstr(27, 0, "                      ▀▀           ▀▀", curses.color_pair(1))
    stdscr.refresh()
    key = stdscr.getch()


def display_win(stdscr):
    stdscr.clear()
    stdscr.addstr(5, 0, " ▄· ▄▌      ▄• ▄▌    ▄▄▌ ▐ ▄▌       ▐ ▄      ▄▄·        ▐ ▄  ▄▄ • ▄▄▄   ▄▄▄· ▄▄▄▄▄.▄▄ · ▄▄ ", curses.color_pair(5))
    stdscr.addstr(6, 0, "▐█▪██▌▪     █▪██▌    ██· █▌▐█▪     •█▌▐█    ▐█ ▌▪▪     •█▌▐█▐█ ▀ ▪▀▄ █·▐█ ▀█ •██  ▐█ ▀. ██▌", curses.color_pair(5))
    stdscr.addstr(7, 0, "▐█▌▐█▪ ▄█▀▄ █▌▐█▌    ██▪▐█▐▐▌ ▄█▀▄ ▐█▐▐▌    ██ ▄▄ ▄█▀▄ ▐█▐▐▌▄█ ▀█▄▐▀▀▄ ▄█▀▀█  ▐█.▪▄▀▀▀█▄▐█·", curses.color_pair(5))
    stdscr.addstr(8, 0, " ▐█▀·.▐█▌.▐▌▐█▄█▌    ▐█▌██▐█▌▐█▌.▐▌██▐█▌    ▐███▌▐█▌.▐▌██▐█▌▐█▄▪▐█▐█•█▌▐█ ▪▐▌ ▐█▌·▐█▄▪▐█.▀ ", curses.color_pair(5))
    stdscr.addstr(9, 0, "  ▀ •  ▀█▄▀▪ ▀▀▀      ▀▀▀▀ ▀▪ ▀█▄▀▪▀▀ █▪    ·▀▀▀  ▀█▄▀▪▀▀ █▪·▀▀▀▀ .▀  ▀ ▀  ▀  ▀▀▀  ▀▀▀▀  ▀ ", curses.color_pair(5))
    stdscr.addstr(10, 0, "")
    stdscr.addstr(11, 0, "            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", curses.color_pair(2))
    stdscr.addstr(12, 0, "            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⢀⣴⠟⠉⠀⠀⠀⠈⠻⣦⡀⠀⠀⠀⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", curses.color_pair(2))
    stdscr.addstr(13, 0, "            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣷⣀⢀⣾⠿⠻⢶⣄⠀⠀⣠⣶⡿⠶⣄⣠⣾⣿⠗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", curses.color_pair(2))
    stdscr.addstr(14, 0, "            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⢻⣿⣿⡿⣿⠿⣿⡿⢼⣿⣿⡿⣿⣎⡟⠉⠀⠀⠀", curses.color_pair(2))
    stdscr.addstr(15, 0, "           ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡟⠉⠛⢛⣛⡉⠀⠀⠙⠛⠻⠛⠑⣷⠀⠀⠀⠀⠀", curses.color_pair(2))
    stdscr.addstr(16, 0, "           ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣧⣤⣴⠿⠿⣷⣤⡤⠴⠖⠳⣄⣀⣹⠀⠀⠀⠀", curses.color_pair(2))
    stdscr.addstr(17, 0, "           ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣀⣟⠻⢦⣀⡀⠀⠀⠀⠀⣀⡈⠻⣿⠀⠀⠀⠀", curses.color_pair(2))
    stdscr.addstr(18, 0, "           ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⡿⠉⡇⠀⠀⠛⠛⠛⠋⠉⠉⠀⠀⠀⠹⢧⡀⠀⠀", curses.color_pair(2))
    stdscr.addstr(19, 0, "              ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⡟⠀⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠃⠀⠈⠑⠪⠷⠤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀", curses.color_pair(2))
    stdscr.addstr(20, 0, "              ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣿⣿⣿⣦⣼⠛⢦⣤⣄⡀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠑⠢⡀⠀⠀⠀⠀⠀", curses.color_pair(2))
    stdscr.addstr(21, 0, "              ⠀⠀⠀⠀⠀⠀⠀⢀⣠⠴⠲⠖⠛⠻⣿⡿⠛⠉⠉⠻⠷⣦⣽⠿⠿⠒⠚⠋⠉⠁⡞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢦⠀⠀⠀", curses.color_pair(2))
    stdscr.addstr(22, 0, "⠀         ⠀⠀⠀⠀⢀⣾⠛⠁⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⠒⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢣⠀⠀⠀", curses.color_pair(2))
    stdscr.addstr(23, 0, "              ⠀⠀⠀⠀⣰⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣑⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡇⠀⠀", curses.color_pair(2))
    stdscr.addstr(24, 0, "              ⠀⠀⠀⣰⣿⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣧⣄⠀⠀⠀⠀⠀⠀⢳⡀⠀", curses.color_pair(2))
    stdscr.addstr(25, 0, "              ⠀⠀⠀⣿⡾⢿⣀⢀⣀⣦⣾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⣫⣿⡿⠟⠻⠶⠀⠀⠀⠀⠀⢳⠀", curses.color_pair(2))
    stdscr.addstr(26, 0, "              ⠀⠀⢀⣿⣧⡾⣿⣿⣿⣿⣿⡷⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⢀⡴⢿⣿⣧⠀⡀⠀⢀⣀⣀⢒⣤⣶⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇", curses.color_pair(2))
    stdscr.addstr(27, 0, "             ⠀⠀⡾⠁⠙⣿⡈⠉⠙⣿⣿⣷⣬⡛⢿⣶⣶⣴⣶⣶⣶⣤⣤⠤⠾⣿⣿⣿⡿⠿⣿⠿⢿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇", curses.color_pair(2))
    stdscr.addstr(28, 0, "             ⠀⣸⠃⠀⠀⢸⠃⠀⠀⢸⣿⣿⣿⣿⣿⣿⣷⣾⣿⣿⠟⡉⠀⠀⠀⠈⠙⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇", curses.color_pair(2))
    stdscr.addstr(29, 0, "             ⠀⣿⠀⠀⢀⡏⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⠿⠿⠛⠛⠉⠁⠀⠀⠀⠀⠀⠉⠠⠿⠟⠻⠟⠋⠉⢿⣿⣦⡀⢰⡀⠀⠀⠀⠀⠀⠀⠁", curses.color_pair(2))
    stdscr.addstr(31, 0, "             ⢀⣿⡆⢀⡾⠀⠀⠀⠀⣾⠏⢿⣿⣿⣿⣯⣙⢷⡄⠀⠀⠀⠀⠀⢸⡄⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣿⣻⢿⣷⣀⣷⣄⠀⠀⠀⠀⢸⠀", curses.color_pair(2))
    stdscr.addstr(32, 0, "             ⢸⠃⠠⣼⠃⠀⠀⣠⣾⡟⠀⠈⢿⣿⡿⠿⣿⣿⡿⠿⠿⠿⠷⣄⠈⠿⠛⠻⠶⢶⣄⣀⣀⡠⠈⢛⡿⠃⠈⢿⣿⣿⡿⠀⠀⠀⠀⠀", curses.color_pair(2))
    stdscr.addstr(33, 0, "             ⠟⠀⠀⢻⣶⣶⣾⣿⡟⠁⠀⠀⢸⣿⢅⠀⠈⣿⡇⠀⠀⠀⠀⠀⣷⠂⠀⠀⠀⠀⠐⠋⠉⠉⠀⢸⠁⠀⠀⠀⢻⣿⠛⠀⠀⠀⠀⢀⠇", curses.color_pair(2))
    stdscr.addstr(34, 0, "             ⠀⠀⠀⠀⠹⣿⣿⠋⠀⠀⠀⠀⢸⣧⠀⠰⡀⢸⣷⣤⣤⡄⠀⠀⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡆⠀⠀⠀⠀⡾⠀⠀⠀⠀⠀⠀⢼⡇", curses.color_pair(2))
    stdscr.addstr(35, 0, "             ⠀⠀⠀⠀⠀⠙⢻⠄⠀⠀⠀⠀⣿⠉⠀⠀⠈⠓⢯⡉⠉⠉⢱⣶⠏⠙⠛⠚⠁⠀⠀⠀⠀⠀⣼⠇⠀⠀⠀⢀⡇⠀⠀⠀⠀⠀⠀⠀⡇", curses.color_pair(2))
    stdscr.addstr(36, 0, "      ⠀⠀⠀⠀⠀⠀⠻⠄⠀⠀⠀⢀⣿⠀⢠⡄⠀⠀⠀⣁⠁⡀⠀⢠⠀⠀⠀⠀⠀⠀⠀⠀⢀⣐⡟⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⢠⡇", curses.color_pair(2))
    stdscr.refresh()
    key = stdscr.getch()
