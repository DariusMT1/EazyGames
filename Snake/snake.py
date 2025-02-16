import curses
import time
import random

# Initialize the screen
stdscr = curses.initscr()
curses.curs_set(0)
sh, sw = stdscr.getmaxyx()
w = curses.newwin(sh, sw, 0, 0)
w.keypad(1)
w.timeout(100)

# Initial position of the snake
snk_x = sw//4
snk_y = sh//2
snake = [
    [snk_y, snk_x],
    [snk_y, snk_x-1],
    [snk_y, snk_x-2]
]

# Initial position of the food
food = [sh//2, sw//2]
w.addch(food[0], food[1], curses.ACS_PI)

# Initial direction of the snake
key = curses.KEY_RIGHT

# Main game loop
while True:
    next_key = w.getch()
    key = key if next_key == -1 else next_key

    # Calculate the new head of the snake
    if key == curses.KEY_DOWN:
        new_head = [snake[0][0] + 1, snake[0][1]]
    if key == curses.KEY_UP:
        new_head = [snake[0][0] - 1, snake[0][1]]
    if key == curses.KEY_LEFT:
        new_head = [snake[0][0], snake[0][1] - 1]
    if key == curses.KEY_RIGHT:
        new_head = [snake[0][0], snake[0][1] + 1]

    # Insert the new head of the snake
    snake.insert(0, new_head)

    # Check if the snake has hit the border or itself
    if (snake[0][0] in [0, sh] or
        snake[0][1] in [0, sw] or
        snake[0] in snake[1:]):
        curses.endwin()
        quit()

    # Check if the snake has eaten the food
    if snake[0] == food:
        food = None
        while food is None:
            nf = [
                random.randint(1, sh-1),
                random.randint(1, sw-1)
            ]
            food = nf if nf not in snake else None
        w.addch(food[0], food[1], curses.ACS_PI)
    else:
        # Remove the last part of the snake
        tail = snake.pop()
        w.addch(tail[0], tail[1], ' ')

    # Draw the snake
    w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)

    # Refresh the screen
    w.refresh()
    time.sleep(0.1)
