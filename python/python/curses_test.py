import curses

EXAMPLE_STR = "Example String"

screen = curses.initscr()
num_rows, num_cols = screen.getmaxyx()

# lines, columns, start line, start column
num_lines = 1
num_cols = num_cols
start_line = 0
start_col = 0

title_bar = curses.newwin(num_lines, num_cols, start_line, start_col)

# Create a custom color set
# Assign it a number (1-255), a foreground, and background color.
curses.start_color()
curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)

title_bar.bkgd(curses.color_pair(1))

title_bar.addstr(0, 2, EXAMPLE_STR)
curses.curs_set(0)

title_bar.refresh()

# play
# screen.addstr(5, 0, "Current mode: Typing mode", curses.A_REVERSE)
# screen.refresh()
# /play

curses.napms(2000)

screen.refresh()
curses.endwin()