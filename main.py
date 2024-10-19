import turtle
from turtle_designs import draw_complex_design

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")  # Set background to black

# Initialize the turtle
pen = turtle.Turtle()
pen.speed(0)  # Maximum speed
pen.width(2)  # Pen width

# Draw the complex fractal design
draw_complex_design(pen)

# Hide the turtle and keep the window open
pen.hideturtle()
screen.mainloop()
