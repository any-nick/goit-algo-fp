import turtle
import math

def draw_branch(t, branch_length, angle, depth):
    if depth == 0:  # Базовий випадок
        return

    # Малюємо основну гілку
    t.forward(branch_length)

    # Малюємо ліву гілку
    t.left(angle)
    draw_branch(t, branch_length * 0.8, angle, depth - 1)

    # Повертаємося до попередньої точки
    t.right(2 * angle)
    draw_branch(t, branch_length * 0.8, angle, depth - 1)

    # Повертаємо черепаху у вихідне положення
    t.left(angle)
    t.backward(branch_length)

def draw_pythagoras_tree(order, branch_length=80, angle=45):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.left(90)
    t.penup()
    t.goto(0, -window.window_height() / 2 + 30)
    t.pendown()

    draw_branch(t, branch_length, angle, order)

    window.mainloop()

draw_pythagoras_tree(order=8)
