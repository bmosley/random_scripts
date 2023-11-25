import curses
from multiprocessing import Process


EXAMPLE_STR = "bryan is cool with a capital k"

p = None
def display(stdscr):
    stdscr.clear()
    stdscr.timeout(500)

    maxy, maxx = stdscr.getmaxyx()
    #curses.newwin(2,maxx,3,1)

    # lines, columns, start line, start column
    num_lines = 1
    num_cols = maxx
    start_line = 0
    start_col = 0

    title_bar = curses.newwin(num_lines, num_cols, start_line, start_col)

    stdscr.refresh()

    # invisible cursor
    curses.curs_set(0)

    if (curses.has_colors()):
        # Start colors in curses
        #curses.start_color()
        curses.use_default_colors()
        # Create a custom color set
        # Assign it a number (1-255), a foreground, and background color.
        curses.init_pair(1, curses.COLOR_RED, -1)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_WHITE)

    title_bar.bkgd(curses.color_pair(2))
    title_bar.addstr(0, 2, EXAMPLE_STR)

    title_bar.refresh()

    curses.curs_set(0)
    curses.napms(2000)
    
    # curses.init_pair(1, 0, -1)
    # curses.init_pair(2, 1, -1)
    # curses.init_pair(3, 2, -1)
    # curses.init_pair(4, 3, -1)
    pad = curses.newpad(100, 100)
    pad.addstr("This text is thirty characters")
    pad.refresh(0, 2, 5, 5, 15, 20)

    bottomBox = curses.newwin(16,maxx-2,maxy-16,1)
    bottomBox.box()
    bottomBox.addstr("Bottom Box")
    bottomBox.refresh()

    bottomwindow = curses.newwin(6,maxx-4,maxy-7,2)
    #bottomwindow.addstr("This is my bottom view :P", curses.A_UNDERLINE)
    bottomwindow.refresh()

    while True:
        event = stdscr.getch()
        if event == ord("q"):
            break


if __name__ == '__main__':
    curses.wrapper(display)

