"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to arrow keys.

"""

from turtle import update, clear, ontimer, setup
from turtle import hideturtle, tracer, listen, onkey, done
from random import randrange
from freegames import square, vector

wall= vector(50, 20)
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)


def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

"controlador que rtermina el juego si la serpiente sale del mapa"
def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    "Move snake forward one segment."
    head = snake[-1].copy()

    "sitio a dónde apunta la cabeza."
    head.move(aim)

    "controlador de cuando la serpiente muere"
    if not inside(head) or head in snake or head == wall:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    "controlador de cuando la serpiente come"
    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
        wall.x = randrange(-15, 15) * 10
        wall.y = randrange(-15, 15) * 10
        
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    "Comida"
    square(food.x, food.y, 9, 'green')
    update()
    "Move snake forward one segment."
    ontimer(move, 100)
    square(wall.x, wall.y, 9, 'blue')


"especificaciones del mapa"
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
"controles"
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
