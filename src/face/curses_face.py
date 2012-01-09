from time import sleep


def main(window):
    height, width = window.getmaxyx()
    panel_width = int(width / 3)
    folders_win = window.subwin(height, int(panel_width / 1.618034), 0, 0)
    messages_win = window.subwin(height, panel_width, 0,
        folders_win.getmaxyx()[1])
    preview_win = window.subwin(
        0, messages_win.getbegyx()[1] + messages_win.getmaxyx()[1])
    [win.border() for win in (folders_win, messages_win, preview_win)]
    window.refresh()
    while True: pass
