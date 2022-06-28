import turtle
from turtle import *
from random import randrange
from freegames import square, vector

wn = turtle.Screen()
wn.title("Snake game")
wn.bgcolor("white")
wn.setup(width=800, height=600)
wn.tracer(0)

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)


def change(x, y):
    aim.x = x
    aim.y = y


def inside(head):
    return -400 < head.x < 390 and -295 < head.y < 295


def move():
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print("snake", len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10

    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, "green")

    square(food.x, food.y, 9, "red")
    update()
    ontimer(move, 50)


hideturtle()
tracer(False)
listen()
onkeypress(lambda: change(10, 0), "Right")
onkeypress(lambda: change(-10, 0), "Left")
onkeypress(lambda: change(0, 10), "Up")
onkeypress(lambda: change(0, -10), "Down")
move()
done()
