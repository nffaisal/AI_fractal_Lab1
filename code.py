import math
import turtle

# 1. Screen Setup
screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.bgcolor("#0f0f1b")  # Dark background to highlight the gradient
screen.title("Pink to Blue Gradient Fractal")
screen.tracer(0, 0)  # Turn off auto-animation for instant/fast rendering

# 2. Turtle Setup
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
screen.colormode(255)


# 3. Linear Interpolation for Pink -> Blue Gradient
def get_gradient_color(progress):
    """Progress ranges from 0.0 (start) to 1.0 (end).

    Transitions from Magenta/Pink (255, 20, 147) to Cyan/Blue (0, 191, 255).
    """
    # Start: Deep Pink (RGB)
    r1, g1, b1 = 255, 20, 147
    # End: Cyan / Deep Sky Blue (RGB)
    r2, g2, b2 = 0, 191, 255

    r = int(r1 + (r2 - r1) * progress)
    g = int(g1 + (g2 - g1) * progress)
    b = int(b1 + (b2 - b1) * progress)

    return (max(0, min(255, r)), max(0, min(255, g)), max(0, min(255, b)))


# 4. Recursive Fractal Tree Function
def draw_fractal(length, depth, max_depth):
    if depth == 0 or length < 2:
        return

    # Calculate color based on current recursion depth
    progress = 1.0 - (depth / max_depth)
    color = get_gradient_color(progress)

    t.pencolor(color)
    t.pensize(max(1, depth * 0.8))

    # Draw central branch
    t.forward(length)

    # Branch angles & scale factors
    angle = 35
    shrink = 0.68

    # Left Sub-Branch
    t.left(angle)
    draw_fractal(length * shrink, depth - 1, max_depth)

    # Right Sub-Branch
    t.right(angle * 2)
    draw_fractal(length * shrink, depth - 1, max_depth)

    # Center-Right Secondary Branch (adds unique complexity)
    t.left(angle)
    t.backward(length * 0.3)
    t.left(90)
    draw_fractal(length * 0.35, depth - 2, max_depth)

    # Return to original position
    t.right(90)
    t.forward(length * 0.3)
    t.backward(length)


# 5. Render Multi-Symmetrical Mandala Star
MAX_DEPTH = 8
BRANCHES = 5  # 5-fold radial symmetry

t.penup()
t.goto(0, 0)
t.pendown()

for i in range(BRANCHES):
    draw_fractal(length=120, depth=MAX_DEPTH, max_depth=MAX_DEPTH)
    t.left(360 / BRANCHES)

screen.update()  # Render everything to screen at once
screen.mainloop()  # Keep window open