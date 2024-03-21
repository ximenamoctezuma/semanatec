import turtle
import random

# Definir constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BG_COLOR = "white"
PLAYER_COLOR = "black"
OBSTACLE_COLOR = "red"
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
OBSTACLE_WIDTH = 50
OBSTACLE_HEIGHT = 50
OBSTACLE_SPEED = 10  # Aumento de velocidad
PLAYER_SPEED = 10  # Aumento de velocidad

# Inicializar Turtle
screen = turtle.Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor(BG_COLOR)

# Crear al jugador
player = turtle.Turtle()
player.shape("square")
player.color(PLAYER_COLOR)
player.penup()
player.setposition(-350, 0)
player.speed(0)

# Función para mover al jugador hacia arriba
def move_up():
    y = player.ycor()
    y += PLAYER_SPEED
    player.sety(y)

# Función para mover al jugador hacia abajo
def move_down():
    y = player.ycor()
    y -= PLAYER_SPEED
    player.sety(y)

# Enlazar teclas
screen.listen()
screen.onkeypress(move_up, "Up")
screen.onkeypress(move_down, "Down")

# Bucle principal del juego
running = True
while running:
    # Crear obstáculos
    if random.randint(0, 100) < 5:
        obstacle = turtle.Turtle()
        obstacle.shape("square")
        obstacle.color(OBSTACLE_COLOR)
        obstacle.penup()
        obstacle.setposition(400, random.randint(-275, 275))

    # Mover obstáculos
    for obstacle in screen.turtles():
        if obstacle.color()[0] == OBSTACLE_COLOR:
            x = obstacle.xcor()
            x -= OBSTACLE_SPEED
            obstacle.setx(x)

            # Comprobar colisiones
            if obstacle.distance(player) < 20:
                running = False

    # Actualizar pantalla
    screen.update()

# Mostrar "Juego terminado"
end_text = turtle.Turtle()
end_text.hideturtle()
end_text.penup()
end_text.goto(0, 0)
end_text.write("Juego terminado", align="center", font=("Arial", 24, "normal"))

# Salir del juego
screen.mainloop()
