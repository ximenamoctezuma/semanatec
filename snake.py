from turtle import *
from random import randrange
from freegames import square, vector
from random import randrange, choice



food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190


# Función modificada para incluir movimiento de la comida
def move_food():
    directions = [vector(10, 0), vector(-10, 0), vector(0, 10), vector(0, -10)]
    move = choice(directions)
    new_food = food + move

    if inside(new_food):
        food.x = new_food.x
        food.y = new_food.y


# Función modificada para incluir movimiento de la comida
def move():
    "Move snake forward one segment and randomly move the food."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        # La comida se mueve a una posición aleatoria
        while True:
            food_move = choice([vector(-10, 0), vector(10, 0), vector(0, -10), vector(0, 10)])
            new_food = food + food_move
            if inside(new_food):
                food.move(food_move)
                break
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, snake_color)  # Uso de snake_color

    square(food.x, food.y, 9, food_color)  # Uso de food_color
    update()
    ontimer(move, 100)


colors = ['green', 'blue', 'yellow', 'purple', 'orange']  # Lista de colores permitidos
snake_color = choice(colors)  # Color aleatorio para la serpiente
food_color = choice([color for color in colors if color != snake_color])  # Color diferente para la comida


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()