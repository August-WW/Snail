import curses

# Define the snail
snail = "🐌"

def main(stdscr):
    # Clear screen
    stdscr.clear()
    
    # Initialize starting position
    y, x = 10, 40
    stdscr.addstr(y, x, snail)
    stdscr.refresh()
    
    while True:
        key = stdscr.getch()
        
        # Clear previous position
        stdscr.clear()
        
        # Update position based on the key pressed
        if key == curses.KEY_UP:
            y = max(0, y - 1)
        elif key == curses.KEY_DOWN:
            y = min(curses.LINES - 1, y + 1)
        elif key == curses.KEY_LEFT:
            x = max(0, x - 1)
        elif key == curses.KEY_RIGHT:
            x = min(curses.COLS - 1, x + 1)
        elif key == ord('q'):  # Quit the program
            break
        
        # Draw the snail at the new position
        stdscr.addstr(y, x, snail)
        stdscr.refresh()

curses.wrapper(main)
