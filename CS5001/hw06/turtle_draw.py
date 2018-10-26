import turtle as t
import math


def draw_circle():
    """Drawing circle"""
    t.begin_fill()
    t.pencolor('blue')
    t.circle(-250/math.cos(math.radians(18)))
    t.fillcolor('cyan')
    t.end_fill()


def draw_star():
    """Drawing star"""
    t.pencolor('red')
    t.right(72)
    t.begin_fill()
    t.fillcolor('yellow')
    for i in range(5):
        t.forward(500)
        t.right(144)
    t.end_fill()
    t.hideturtle()


def main():
    window = t.Screen()
    t.penup()
    t.setposition(0, 250/math.cos(math.radians(18)))
    t.pendown()
    draw_circle()
    draw_star()
    window.exitonclick()


main()
