import curses

from face import curses_main


def main():
    curses.wrapper(curses_main)


if __name__ == '__main__':
    main()
