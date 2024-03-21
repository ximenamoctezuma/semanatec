import turtle
import random

# Configuración de la pantalla
screen = turtle.Screen()
screen.title("Endless Runner")
screen.bgcolor("white")
screen.setup(width=600, height=400)
screen.tracer(0)

# Creación del jugador
player = turtle.Turtle()
player.shape("turtle")
player.color("blue")
player.penup()
player.speed(0)
player.setposition(-250, 0)
player.setheading(0)  # Cambia la orientación hacia la derecha (0 grados)

# Definir límites de la pantalla
screen_height = screen.window_height()
screen_width = screen.window_width()

# Bandera para controlar el estado del juego
game_over = False

# Bandera para controlar el movimiento del jugador
player_move_allowed = True

# Funciones de movimiento del jugador
def move_up():
    if player_move_allowed:
        y = player.ycor() + 20
        if y < screen_height / 2:
            player.sety(y)

def move_down():
    if player_move_allowed:
        y = player.ycor() - 20
        if y > -screen_height / 2:
            player.sety(y)

# Controles del jugador
screen.listen()
screen.onkeypress(move_up, "Up")
screen.onkeypress(move_down, "Down")

# Función para crear obstáculos
def create_obstacle():
    if not game_over:  # Solo crea obstáculos si el juego está en curso
        gap = random.randint(50, 150)
        top_height = random.randint(-screen_height // 2 + gap // 2, screen_height // 2 - gap // 2)
        bottom_height = top_height - gap - 200  # Aseguramos que haya espacio suficiente entre los obstáculos
        
        top_obstacle = turtle.Turtle()
        top_obstacle.shape("square")
        top_obstacle.color("red")
        top_obstacle.shapesize(stretch_wid=2, stretch_len=2)
        top_obstacle.penup()
        top_obstacle.speed(0)
        top_obstacle.setposition(screen_width / 2, top_height)
        
        bottom_obstacle = turtle.Turtle()
        bottom_obstacle.shape("square")
        bottom_obstacle.color("red")
        bottom_obstacle.shapesize(stretch_wid=2, stretch_len=2)
        bottom_obstacle.penup()
        bottom_obstacle.speed(0)
        bottom_obstacle.setposition(screen_width / 2, bottom_height)
        
        obstacles.append(top_obstacle)
        obstacles.append(bottom_obstacle)

# Función para mover los obstáculos
def move_obstacles():
    if not game_over:  # Solo mueve los obstáculos si el juego está en curso
        for obstacle in obstacles:
            obstacle.setx(obstacle.xcor() - 10)  # Aumentamos la velocidad aquí

# Función para detener el juego y mostrar la opción de reiniciar
def game_over_function():
    global game_over
    global player_move_allowed
    game_over = True  # Establecer el estado del juego como terminado
    player_move_allowed = False  # Desactivar el movimiento del jugador
    screen.onclick(None)  # Desactivar la detección de clics para evitar acciones duplicadas
    
    # Mostrar mensaje de juego terminado
    game_over_text = turtle.Turtle()
    game_over_text.color("black")
    game_over_text.penup()
    game_over_text.hideturtle()
    game_over_text.goto(0, 50)
    game_over_text.write("Juego Terminado", align="center", font=("Arial", 24, "normal"))
    
    # Mostrar botón de reinicio
    restart_button = turtle.Turtle()
    restart_button.shape("square")
    restart_button.color("green")
    restart_button.penup()
    restart_button.goto(0, 0)
    restart_button.write("Reiniciar", align="center", font=("Arial", 16, "normal"))
    
    # Función para reiniciar el juego al hacer clic en el botón de reinicio
    def restart_game(x, y):
        global game_over
        global player_move_allowed
        game_over = False  # Restablecer el estado del juego como en curso
        player_move_allowed = True  # Permitir el movimiento del jugador
        game_over_text.clear()  # Limpiar el mensaje de juego terminado
        game_over_text.hideturtle()  # Ocultar el texto de juego terminado
        restart_button.clear()  # Limpiar el botón de reinicio
        restart_button.hideturtle()  # Ocultar el botón de reinicio
        player.setposition(-250, 0)  # Reposicionar al jugador
        player.color("blue")  # Restaurar el color del jugador
        
        # Limpiar obstáculos
        for obstacle in obstacles:
            obstacle.hideturtle()
        obstacles.clear()  # Limpiar la lista de obstáculos
        
        screen.update()  # Actualizar la pantalla
        screen.onclick(click_restart)  # Reactivar la detección de clics
    
    # Función para detectar clics en el botón de reinicio
    def click_restart(x, y):
        if -50 < x < 50 and -20 < y < 20:
            restart_game(x, y)
    
    screen.update()
    screen.onclick(click_restart)

# Lista para almacenar los obstáculos
obstacles = []

# Bucle principal del juego
while True:
    screen.update()
    
    # Crear nuevos obstáculos con mayor frecuencia
    if random.randint(1, 50) == 1:
        create_obstacle()
    
    # Mover el jugador y los obstáculos
    move_obstacles()
    
    # Comprobar colisiones con obstáculos
    for obstacle in obstacles:
        if player.distance(obstacle) < 20:
            player.color("red")
            game_over_function()
            break
    
    # Eliminar los obstáculos fuera de la pantalla
    for obstacle in obstacles[:]:
        if obstacle.xcor() < -screen_width / 2:
            obstacles.remove(obstacle)
            obstacle.hideturtle()
            del obstacle
    
    # Ajustar la velocidad de la pantalla
    screen.update()
