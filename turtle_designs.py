import turtle
import math

def gradient_color(level, max_level):
    """
    Generate a color that smoothly transitions from one color to another based on the level.
    This function returns a tuple (r, g, b).
    """
    r = int(255 * (1 - level / max_level))  # Gradual change from red
    g = int(255 * (level / max_level))      # Gradual change from green
    b = int(255 * (0.5 * (1 + math.cos(level / max_level * math.pi))))  # Blue transition
    return f'#{r:02x}{g:02x}{b:02x}'

def draw_fractal_circle(t, x, y, radius, level, max_level):
    """
    Draw a recursive circle with fractal branches and gradient color.
    """
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    
    color = gradient_color(level, max_level)
    t.color(color)
    t.circle(radius)

    if level < max_level:
        draw_fractal_circle(t, x, y, radius * 0.67, level + 1, max_level)

def draw_fractal_branches(t, length, depth, angle, max_depth):
    """
    Draw fractal branches emanating from a point, with varying angles.
    """
    if depth == 0:
        return

    t.forward(length)
    t.left(angle)
    draw_fractal_branches(t, length * 0.67, depth - 1, angle, max_depth)
    t.right(2 * angle)
    draw_fractal_branches(t, length * 0.67, depth - 1, angle, max_depth)
    t.left(angle)
    t.backward(length)

def draw_rotational_fractal(t, radius, layers):
    """
    Draws multiple fractal circles arranged in a rotational pattern.
    """
    angle_step = 360 / layers
    for i in range(layers):
        t.setheading(i * angle_step)
        draw_fractal_circle(t, 0, 0, radius, 0, 5)

def draw_complex_design(t):
    """
    Combine fractal branches and rotational symmetry to create a complex, layered design.
    """
    # Draw fractal circles in multiple layers
    draw_rotational_fractal(t, 200, 8)

    # Add fractal branches at each circle intersection
    for i in range(8):
        t.setheading(i * 45)
        draw_fractal_branches(t, 150, 6, 30, 6)
