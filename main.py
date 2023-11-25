import turtle

def draw_rectangle(width, height, color):
    turtle.begin_fill()
    turtle.fillcolor(color)
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

# Flag dimensions
flag_width = 300
flag_height = 500

# Screen dimensions
screen_width = 600
screen_height = 400

# Calculate starting positions to center the flag
start_x = -(flag_width / 2)
start_y = flag_height / 6

# Calculate center of the screen
center_x = -240
center_y = -120

# Set up the screen
screen = turtle.Screen()
screen.setup(width=screen_width, height=screen_height)
turtle.speed(2)
turtle.hideturtle()

# Calculate adjusted start position to center the flag
start_x = center_x - (flag_width / 2)
start_y = center_y + (flag_height / 2)

# Draw vertical red rectangle
turtle.penup()
turtle.goto(start_x, start_y - 335)
turtle.pendown()
draw_rectangle(120, flag_height, "#EF3340")  # Adjusted width of the red rectangle

# Draw horizontal rectangles
turtle.penup()
turtle.goto(start_x + 120, start_y)
turtle.pendown()
draw_rectangle(flag_width + 360, flag_height / 3, "#009739")  # Upper rectangle in red

turtle.penup()
turtle.goto(start_x + 120, start_y - flag_height / 3)
turtle.pendown()
draw_rectangle(flag_width + 360, flag_height / 3, "#FFFFFF")  # Middle rectangle in white

turtle.penup()
turtle.goto(start_x + 120, start_y - 2 * flag_height / 3)
turtle.pendown()
draw_rectangle(flag_width + 360, flag_height / 3, "#000000")  # Lower rectangle in green

turtle.hideturtle()
turtle.done()
