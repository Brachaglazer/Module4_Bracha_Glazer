'''
Pseudocode:
Import systems necessary to run the program:
1. turtle as T - inorder to easily refer to it
2. random - to draw trees at random side each time the program is run.

Define the default screen size and margins:
    CANVAS_W, CANVAS_H = 800, 600
    TOP_MARGIN, BOTTOM_MARGIN = 40, 40

Create a list of the house size options and their measurements:
    SIZES = {
        "s": (120, 80),
        "m": (150, 100),
        "l": (180, 120),
    }

Create a list of the theme options and a dictionary for the colors of each item:
    THEMES = {
        "pastel": dict(body="#ffd1dc", roof="#c1e1c1", door="#b5d3e7", window="#fff7ae"),
        "primary": dict(body="red", roof="blue", door="gold", window="#aee3ff"),
    }

Create helper functions to keep the main functions short, clean, and simple:
1. move_to(x,y)
    x - number on x axis
    y - number on y axis
    T.penup(), T.goto(x,y), and T.pendown() - move to coordinate in args

2. draw_line(x1, y1, x2, y2)
    x1, y1 - point 1
    x2, y2 - point 2
    move_to(x1,y1) - move to first point
    T.goto(x2, y2) - draw line to second point

3. fill_rect_center(cx, cy, w, h, color)
    cx - center of rectangle x axis
    cy - center of rectangle y axis
    w - width of rectangle
    h - height of rectangle
    color - color of rectangle (taken from color themes)

    T.fillcolor(), T.pencolor()
    call move_to(cx - w/2, cy + h/2)
    cx - w/2, cy + h/2 - top left corner of rectangle

    T.begin_fill()
    Rectangle border - for _ in range(2)
        T.forward(w), T.right(90), T.forward(h), T.right(90) - One line across and one down.
    T.end_fill()

4. fill_triangle(p1, p2, p3, color)
    p1 — coordinate 1 (x1, y1)
    p2 — coordinate 2 (x2, y2)
    p3 — coordinate 3 (x3, y3)
    color — fill color for the triangle (taken from color themes)

    T.fillcolor(), T.pencolor()
    call move_to(*p1), T.begin_fill()
    T.goto(*p2), T.goto(*p3), T.goto(*p1) - draw to each point.
    T.end_fill()

5. fill_circle_center(cx, cy, r, color)
    definition of circle:
    cx - center of circle on x axis
    cy - center of circle on y axis
    r - radius
    color - color of circle (not in color themes)

    T.fillcolor(), T.pencolor()
    call move_to(cx, cy - r)
    cx, cy - r - point on left border of circle
    T.begin_fill(), T.circle(r), T.end_fill()

Create input helper functions:
1. ask_choice_int(prompt, allowed)
    prompt - ask user for an integer
        houses per row, how many houses
    allowed - only int in allowed set is accepted

    allowed_set = set(allowed)
    while loop - continue until true
        Try - validate input
            houses = int(input(prompt))
        Except error
            print message and continue

        if input is not allowed, print message.
        else return houses.

2. ask_choice_str(prompt, allowed)
    prompt - ask user for an integer
        house size, color theme, roof type, sun
    allowed - only str in allowed list is accepted

    allowed_lower = .lower() for index in allowed
    while loop - continues until true
        user_options = input(prompt})
        if input is not allowed, print message.
        else return user_options.

Create functions to draw village:
1. draw_house_centered(cx, cy, size_key, theme_key, roof_style)
    Draw house centered at cx, cy.

    Sizes and colors dependent on user input.
    w, h = SIZES[size_key]
    colors = THEMES[theme_key]
    body_c = color for body
    roof_c = color for roof
    door_c = color for door
    win_c = color for window

    draw house - Call fill_rect_center(cx, cy, w, h, body_c)
    draw roof - dependent on user input
                if roof_style is "triangle" call fill_triangle((cx - 0.5 * w, cy + .5 * h), (cx, yT + 0.5 * h), (cx + 0.5 * w, cy + .5 * h), roof_c)
                    cx - 0.5 * w, cy + .5 * h - bottom left corner of triangle roof
                    cx, yT + 0.5 * h - apex of triangle roof
                    cx + 0.5 * w, cy + .5 * h - bottom right corner of triangle roof
                else call fill_rect_center(cx, cy + 0.5 * h, 1.03 * w, 0.25 * h, roof_c)
                    cx - x coordinate
                    cy + 0.5 * h - y coordinate
                    1.03 * w - width of rectangle roof slighly larger than width of house
                    0.25 * h - height of flat rectangle for roof
    draw door - call fill_rect_center(cx, cy - 0.23 * h, 0.2 * w, 0.5 * h, door_c)
        cx - x coordinate
        cy - 0.23 * h - y coordinate
        0.2 * w - w of door smaller than w of house
        0.5 * h - h of door is half h of house
    draw window - fill_rect_center(cx - 0.22 * w, cy + 0.08 * h, 0.17 * w, 0.15 * h, win_c)
        cx - 0.22 * w - x coordinate
        cy + 0.08 * h - y coordinate
        0.17 * w - w of door smaller than w of house
        0.15 * h - h of window smaller than h of house

2. draw_tree_near(cx, cy, size_key)
    Draw tree on random side of house.

    draw trunk - fill_rect_center(tx, ty, tw, th, "#8f777d")
        side = random.choice -1 or 1
        tx = cx + side * 0.45w - x coordinate can change with random
        ty = cy - 0.5h + th/2 - y coordinate always the same
        Size depends on user input.
        w, h = SIZES[size_key]
        tw, th = w*0.10, h*0.40
    draw canopy - fill_circle_center(tx, cy, r, "#4f9c70")
        r = 0.18w - will change with size

3. draw_village(cols, rows, size_key, theme_key, sun_flag, roof_style)
    Draw roads to create cells, and draw house.

    Cell sizes are dependent on the user input for the amount of houses and rows.
    cols - user input amount of houses per row
    rows - user input amount of rows
    cell_w = CANVAS_W / cols
    cell_h = (CANVAS_H - TOP_MARGIN - BOTTOM_MARGIN) / rows

    Call draw_roads(cols, rows, cell_w, cell_h)
    Nested loops to draw grid.
    for loop of c in range(cols) nested in for loop r in range(rows)
        define cx - cx = -CANVAS_W / 2 + (c + 0.5) * cell_w
        define cx - cy = CANVAS_H / 2 - TOP_MARGIN - (r + 0.5) * cell_h
        draw house - call draw_house_centered(cx, cy, size_key, theme_key, roof_style)
        draw tree - call draw_tree_near(cx, cy, size_key)
    draw sun - dependent on user input.
        r = 35
        cx = CANVAS_W/2 - r - 20
        cy = CANVAS_H/2 - r - 20
        call fill_circle_center(cx, cy, r, "yellow")

Create main function:
Pull program together in a neat fashion.

main()
    print("Welcome to Turtle Village — Lite!")
    cols = ask_choice_int("How many houses per row?", [2, 3])
    rows = ask_choice_int("How many rows?", [2])  # you may change to [2, 3]
    size_key = ask_choice_str("House size", ["S","M","L"]).lower()
    theme_key = ask_choice_str("Color theme", ["pastel","primary"]).lower()  # Added .lower()
    roof_style = ask_choice_str("Roof type", ["triangle","flat"]).lower()
    sun_flag = ask_choice_str("Draw a sun?", ["y","n"]).lower()

    Set window, property size, and tracer:
    T.setup(CANVAS_W, CANVAS_H), T.speed(), T.tracer(false)
    cell_w = CANVAS_W / cols
    cell_h = (CANVAS_H - TOP_MARGIN - BOTTOM_MARGIN) / rows

    draw village - call draw_village(cols, rows, size_key, theme_key, sun_flag, roof_style)

    finalize - T.tracer(True), T.hideturtle(), T.done()

Call main() to run all parts of the program:
if __name__ == "__main__":
    main()


Short Reflection (6–8 sentences):

1. Where did you use while vs for, and why?
    I used while loops to prompt the user for input so that the loop will run until the user gives valid input.
    A while loop does not require you to give it an amount of times to run and I don't know how many times I'll want
    the loop to run, so I used it.
    I used for loops to draw the lines because once the user inputs the amount of houses and rows I have a definite
    number of times I want the loop to run.
    A for loop requires you to give it an amount of times to run and I had a specific amount of times I wanted it to run.
2. Where did you use try/except, and what errors did you guard against?
    I used try and except to validate that the user entered an integer in the ask_choice_int() function. I guarded
    against a ValueError, if the input was not an int, the program would not be able to transfer it to an int so it
    would raise an error.
'''

import turtle as T
import random

CANVAS_W, CANVAS_H = 800, 600
TOP_MARGIN, BOTTOM_MARGIN = 40, 40

SIZES = {
    "s": (120, 80),
    "m": (150, 100),
    "l": (180, 120),
}

THEMES = {
    "pastel": dict(body="#ffd1dc", roof="#c1e1c1", door="#b5d3e7", window="#fff7ae"),
    "primary": dict(body="red", roof="blue", door="gold", window="#aee3ff"),
}


# ---------- tiny turtle helpers (provided) ----------
def move_to(x, y):
    """Move pen to a point."""
    '''
    x - position on x coordinate axis
    y - position on y coordinate axis
    '''
    T.penup(); T.goto(x, y); T.pendown()


def draw_line(x1, y1, x2, y2):
    """Draw a line from point1 to point2."""
    '''
       we draw a line from x1,y1
       x1 - position on x coordinate axis
       y1 - position on y coordinate axis
       
       to x2, y2
       x2 - position on x coordinate axis
       y2 - position on y coordinate axis
       '''
    move_to(x1, y1); T.goto(x2, y2)


def fill_rect_center(cx, cy, w, h, color):
    """Draw a rectangle.
    for loop runs twice to draw half of shape each time.

    Args:
    cx - center of rectangle x coordinate 
    cy - center of rectangle y coordinate 
    w - width of rectangle 
    h - height of rectangle 
    color - color of rectangle 
    """
    T.fillcolor(color); T.pencolor("black")
    move_to(cx - w / 2, cy + h / 2)
    T.begin_fill()
    for _ in range(2):
        T.forward(w); T.right(90); T.forward(h); T.right(90)
    T.end_fill()


def fill_triangle(p1, p2, p3, color):
    """
    Draw a filled triangle defined by three points.
    
    p1 — point 1 (x1, y1)
    p2 — point 2 (x2, y2)
    p3 — point 3 (x3, y3)
    color — fill color for the triangle
    
    Notes:
    - Each point is an (x, y) tuple.
    - Depending on your triangle, some x’s or y’s may be equal (e.g., flat base).
    
    Example:
    p1 = (x1, y1)
    p2 = (x2, y2)
    p3 = (x3, y3)
    fill_triangle(p1, p2, p3, color)
    """
    T.fillcolor(color); T.pencolor("black")
    move_to(*p1); T.begin_fill()
    T.goto(*p2); T.goto(*p3); T.goto(*p1)
    T.end_fill()


def fill_circle_center(cx, cy, r, color):
    """
    a circle is defined by
    cx - the center of your circle, x coordinate
    cy - center of your circle, y coordinate
    r - radius
    color - color of circle
    """
    T.fillcolor(color); T.pencolor("black")
    move_to(cx, cy - r)  # turtle draws circles from the bottom
    T.begin_fill(); T.circle(r); T.end_fill()


# ---------- input helpers (complete; you may extend) ----------
def ask_choice_int(prompt, allowed):
    """Ask for an integer in the allowed set; reprompt on error.
        in a while loop, ask for a valid number from allowed list, exception is printed if incorrect number given,
        while loop continues until true 
        
        prompt for : 
        1. houses per row
        2. how many houses
    """
    # a set is a list which only allows one unique item to exist, not any duplicates
    # if duplicates are given, set removes all duplicates
    allowed_set = set(allowed)
    while True:
        try:  # Validate input.
            houses = int(input(f"{prompt} {allowed}: "))
        except ValueError:
            print("Please provide a valid integer.")
            continue

        if houses not in allowed_set:
            print(f"Please provide a valid allowed integer {allowed}.")
        else:  # If user input is in allowed set.
            return houses


def ask_choice_str(prompt, allowed):
    """Ask for a string in the allowed list (case-insensitive); reprompt on error.
    in a while loop, ask for a valid string from allowed list, exception is printed if incorrect number given,
        while loop continues until true
        
        prompt for : 
        1. house size 
        2. color theme
        3. roof type 
        4. sun

        Return:
        Returns valid user input.
    """
    allowed_lower = [a.lower() for a in allowed] # converting to lower case all in allowed list
    while True:
        user_options = input(f"{prompt} {allowed}: ")
        if user_options not in allowed_lower:
            print(f"Please provide a valid entry {allowed}.")
        else:  # If user input is in allowed list
            return user_options


# ---------- TODO: draw_roads ----------
def draw_roads(cols, rows, cell_w, cell_h):
    """Draw straight separator lines between rows and columns (simple roads).
    In a for loop, draw horizontal lines per number of rows.
    In a for loop , draw vertical lines per number of cols.

    Args:
    cols - user input number of columns chosen
    rows - user input number of rows chosen
    cell_w - width of each cell
    cell_h - height of each cell
    """
    top_y = CANVAS_H / 2 - TOP_MARGIN
    bot_y = -CANVAS_H / 2 + BOTTOM_MARGIN
    left_x = -CANVAS_W / 2
    right_x = CANVAS_W / 2


    T.pencolor("black"); T.width(1)
    # TODO: HORIZONTAL separators for r in 1..rows-1 at y = CANVAS_H/2 - TOP_MARGIN - r*cell_h
    for r in range(1, rows):
    #           here are are we vary y across rows (y = top_y - r*cell_h) and then
        y = top_y - r * cell_h
    #           drawing a line from (left_x, y) to (right_x, y)
        draw_line(left_x, y, right_x, y)

    # TODO: VERTICAL separators for c in 1..cols-1 at x = -CANVAS_W/2 + c*cell_w
    for c in range(1, cols):
    #           here we vary x across columns(x=left_x + c * cell_w) and
        x = left_x + c * cell_w
    #           then draw from (x, top_y) to(x, bot_y).
        draw_line(x, top_y, x, bot_y)


# ---------- TODO: draw_house_centered ----------
def draw_house_centered(cx, cy, size_key, theme_key, roof_style):
    """Draw a simple house centered at (cx, cy).
    Draw a rectangle house, flat rectangle or triangle roof, rectangle door, and a rectangle window.

    Args:
    cx - center of rectangle, x coordinate
    cy - center of rectangle, y coordinate
    size_key - user input size chosen
    theme_key - user input theme chosen
    roof_style - user input roof chosen
    """
    # width/height
    w, h = SIZES[size_key]
    # color for each item
    colors = THEMES[theme_key]  # where theme_key is either "pastel" or "primary"
    body_c = colors["body"]  # we then can access the colors for the body of the house
    roof_c = colors["roof"]  # color of the roof of the house
    door_c = colors["door"]  # color of the door of the house
    win_c = colors["window"]  # window -- feel free to add or change the colors
    # TODO: body as centered rectangle
    fill_rect_center(cx, cy, w, h, body_c)
    # TODO: roof: if roof_style is a 'triangle' draw a triangle; otherwise draw a thin flat rectangle
    # if yT = cy + h/2
    if roof_style == "triangle":
        yT = cy + h / 2
        fill_triangle((cx - 0.5 * w, cy + 0.5 * h), (cx, yT + 0.5 * h), (cx + 0.5 * w, cy + 0.5 * h), roof_c)
    else:  # if user chose flat rectangle.
        fill_rect_center(cx, cy + 0.5 * h, 1.03 * w, 0.25 * h, roof_c)

    # TODO: add a small door centered on x=cx
    fill_rect_center(cx, cy - 0.23 * h, 0.2 * w, 0.5 * h, door_c)
    # (optional) add one window off to the left
    fill_rect_center(cx - 0.22 * w, cy + 0.08 * h, 0.17 * w, 0.15 * h, win_c)


# ---------- TODO: draw_tree_near ----------
def draw_tree_near(cx, cy, size_key):
    """Draw a small tree near the house (left or right).
    Draw a rectangle trunk, and a circle canopy.

    Args:
    cx - center of tree, x coordinate
    cy - center of tree, y coordinate
    size_key - user input size chosen
    """
    # trunk
    w, h = SIZES[size_key]
    # trunk size (ratios)
    tw, th = w * 0.10, h * 0.40
    # place to left or right of the house randomly
    side = random.choice([-1, 1])
    tx = cx + side * (w * 0.45)
    ty = cy - h * 0.5 + th / 2
    # TODO: trunk: use fill_rect_center(tx, ty, tw, th, color)
    fill_rect_center(tx, ty, tw, th, "#8f777d")
    # TODO: canopy: use fill_circle_center(...) above trunk
    r = 0.18 * w
    fill_circle_center(tx, cy, r, "#4f9c70")


# ---------- TODO: draw_village (orchestration) ----------
def draw_village(cols, rows, size_key, theme_key, sun_flag, roof_style):
    """Compute cell sizes, draw roads, and loop over grid to place houses/trees.

    Args:
    cols - user input number of columns chosen
    rows - user input number of rows chosen
    size_key - user input size choice
    theme_key - user input theme choice
    sun_flag - user input sun choice
    roof_style - user input roof choice
    """
    cell_w = CANVAS_W / cols
    cell_h = (CANVAS_H - TOP_MARGIN - BOTTOM_MARGIN) / rows

    # TODO: draw roads first
    draw_roads(cols, rows, cell_w, cell_h)
    # TODO: nested loops over r, c
    for r in range(rows):
        for c in range(cols):
    #   compute cx, cy (center per formulas)
            cx = -CANVAS_W / 2 + (c + 0.5) * cell_w
            cy = CANVAS_H / 2 - TOP_MARGIN - (r + 0.5) * cell_h
    #   draw_house_centered(...) and draw_tree_near(...)
            draw_house_centered(cx, cy, size_key, theme_key, roof_style)
            draw_tree_near(cx, cy, size_key)

    # sun (optional)
    if sun_flag == 'y':
        r = 35
        cx = CANVAS_W/2 - r - 20
        cy = CANVAS_H/2 - r - 20
        fill_circle_center(cx, cy, r, "yellow")


# ---------- main ----------
def main():
    """Prompt user and draw village."""
    print("Welcome to Turtle Village — Lite!")
    cols = ask_choice_int("How many houses per row?", [2, 3])  # Unpack how many houses/columns user chose.
    rows = ask_choice_int("How many rows?", [2])  # Unpack how many rows user chose.
    size_key = ask_choice_str("House size", ["S","M","L"]).lower()  # Unpack size user chose.
    theme_key = ask_choice_str("Color theme", ["pastel","primary"]).lower()  # Added .lower()
    roof_style = ask_choice_str("Roof type", ["triangle","flat"]).lower()
    sun_flag = ask_choice_str("Draw a sun?", ["y","n"]).lower()

    # window
    T.setup(CANVAS_W, CANVAS_H); T.speed(0); T.tracer(False)

    # the size of the property
    cell_w = CANVAS_W / cols
    cell_h = (CANVAS_H - TOP_MARGIN - BOTTOM_MARGIN) / rows

    # TODO: call draw_village with inputs
    draw_village(cols, rows, size_key, theme_key, sun_flag, roof_style)
    # TODO: finalize
    T.tracer(True); T.hideturtle(); T.done()


if __name__ == "__main__":
    main()
