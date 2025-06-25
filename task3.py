
import turtle

# Set up the screen
win = turtle.Screen()
win.bgcolor("white")



import turtle

# Set up the screen
win = turtle.Screen()
win.bgcolor("white")

# Create a new turtle object
board = turtle.Turtle()
board.speed(0)
board.hideturtle()

# Function to draw a square
def draw_square(x, y, color):
    board.penup()
    board.goto(x, y)
    board.pendown()
    board.fillcolor(color)
    board.begin_fill()
    for _ in range(4):
        board.forward(50)
        board.right(90)
    board.end_fill()

# Draw the chess board
for row in range(8):
    for col in range(8):
        color = "gray" if (row + col) % 2 == 0 else "white"
        draw_square(col * 50 - 200, row * 50 - 200, color)


# Function to draw a square
def draw_square(x, y, color):
    board.penup()
    board.goto(x, y)
    board.pendown()
    board.fillcolor(color)
    board.begin_fill()
    for _ in range(4):
        board.forward(50)
        board.right(90)
    board.end_fill()

# Draw the chess board
for row in range(8):
    for col in range(8):
        color = "gray" if (row + col) % 2 == 0 else "white"
        draw_square(col * 50 - 200, row * 50 - 200, color)

turtle.done()


