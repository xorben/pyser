import curses

def main(stdscr):
    """
    Main entry point for the curses application.

    Args:
        stdscr: The standard screen object provided by curses.
    """
    # Clear the screen
    stdscr.clear()

    # Disable cursor and enable keypad input
    curses.curs_set(0)
    stdscr.keypad(True)

    # Display some text
    stdscr.addstr(0, 0, "Hello, Curses!")
    stdscr.addstr(1, 0, "Press 'q' to quit.")
    stdscr.refresh()

    # Main loop
    while True:
        key = stdscr.getch()  # Wait for user input
        if key == ord('q'):   # Exit on 'q'
            break
        elif key == curses.KEY_UP:
            stdscr.addstr(3, 0, "You pressed UP  ")
        elif key == curses.KEY_DOWN:
            stdscr.addstr(3, 0, "You pressed DOWN")
        stdscr.refresh()

if __name__ == "__main__":
    try:
        curses.wrapper(main)  # Initializes curses and handles cleanup
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting...")
