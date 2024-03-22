import turtle
import random
from PIL import Image


def resize_image(image_path, output_path, width, height):
    with Image.open(image_path) as img:
        # Redimensionar la imagen manteniendo la relación de aspecto y alta calidad
        img = img.resize((width, height), Image.Resampling.LANCZOS)  # Actualizado aquí
        # Guardar la imagen redimensionada como un nuevo archivo GIF
        img.save(output_path, 'GIF')
    return output_path


# Configuración de la pantalla
screen = turtle.Screen()
screen.title("Benvenuto Run")
screen.bgcolor("white")
screen.setup(width=600, height=400)
screen.tracer(0)

player_shape = resize_image("images/foto.jpeg", "images/benve2_resized.gif", 50, 50)
screen.register_shape(player_shape )

# Creación del jugador
player = turtle.Turtle()
player.shape(player_shape )
player.color("blue")
player.penup()
player.speed(0)
player.setposition(-250, 0) 
player.setheading(0)

# Definir límites de la pantalla
screen_height = screen.window_height()
screen_width = screen.window_width()

# Bandera para controlar el estado del juego
game_over = True

# Bandera para controlar el movimiento del jugador
player_move_allowed = False

# Puntuación
score = 0
high_score = 0

# Lista para almacenar los obstáculos
obstacles = []

# Texto de puntuación
score_text = turtle.Turtle()
score_text.penup()
score_text.hideturtle()
score_text.goto(0, screen_height // 2 - 40)

def on_click(x, y):
    global game_over
    if game_over:
        restart_game()
    else:
        pass


def update_score():
    score_text.clear()
    score_text.color("gold")
    score_text.write(f"Score: {score}", align="center", font=("Courier New", 16, "normal"))

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

image_path = "images/lsd.gif"
rezised = "images/lsd_resized.gif"

# Redimensiona la imagen
resize_image(image_path, rezised, 50, 50)
screen.register_shape(rezised)

def create_obstacle():
    if not game_over:
        gap = random.randint(50, 150)
        top_height = random.randint(-screen_height // 2 + gap // 2, screen_height // 2 - gap // 2)
        bottom_height = top_height - gap - 200
        
        top_obstacle = turtle.Turtle()
        top_obstacle.shape(rezised)
        top_obstacle.color("red")
        top_obstacle.shapesize(stretch_wid=2, stretch_len=2)
        top_obstacle.penup()
        top_obstacle.speed(0)
        top_obstacle.setposition(screen_width / 2, top_height)
        
        bottom_obstacle = turtle.Turtle()
        bottom_obstacle.shape(rezised)
        bottom_obstacle.color("red")
        bottom_obstacle.shapesize(stretch_wid=2, stretch_len=2)
        bottom_obstacle.penup()
        bottom_obstacle.speed(0)
        bottom_obstacle.setposition(screen_width / 2, bottom_height)
        
        obstacles.append(top_obstacle)
        obstacles.append(bottom_obstacle)

def move_obstacles():
    global score
    if not game_over:
        for obstacle in obstacles:
            obstacle.setx(obstacle.xcor() - 10)
        score += 1
        update_score()

def show_start_screen():
    screen.bgpic("images/fondojuego.gif")
    start_text = turtle.Turtle()
    start_text.penup()
    start_text.hideturtle()
    start_text.goto(0, 0)
  
    # Mejorar el aspecto del texto
    start_text.color("gold")
    start_text.write("Benvenuto Run", align="center", font=("Courier New", 34, "bold"))

    # Texto secundario para instrucciones
    start_text.goto(0, -30)
    start_text.color("white")
    start_text.write("Click to start", align="center", font=("Courier New", 24, "italic"))

    screen.onclick(lambda x, y: start_game(start_text))

def start_game(start_text):
    global game_over, player_move_allowed, score

    if game_over:
        
        start_text.clear()
        game_over = False
        player_move_allowed = True
        score = 0
        update_score()
        main_game_loop()

def restart_game():
    global game_over, player_move_allowed, score, game_over_text


    game_over = False
    player_move_allowed = True

    # Limpiar obstáculos restantes
    for obstacle in obstacles:
        obstacle.clear()
    obstacles.clear()

    # Reiniciar variables
    
    score = 0
    update_score()

    # Borrar texto de Game Over
    if 'game_over_text' in globals():
        game_over_text.clear()

    # Comenzar el bucle del juego
    main_game_loop()


def show_game_over_screen():
    global game_over_text
    game_over_text = turtle.Turtle()
    game_over_text.penup()
    game_over_text.hideturtle()
    game_over_text.goto(0, 0)
    game_over_text.color("gold")
    game_over_text.write(f"Game Over\nScore: {score}\nClick to restart", align="center", font=("Courier New", 32, "bold"))
    screen.onclick(lambda x, y: restart_game())

def game_over_function():
    global game_over, player_move_allowed
    game_over = True
    player_move_allowed = False
    for obstacle in obstacles:
        obstacle.hideturtle()
    obstacles.clear()
    show_game_over_screen()



def main_game_loop():
    global score
    if not game_over:
        if random.randint(1, 50) == 1:
            create_obstacle()
        move_obstacles()
        for obstacle in obstacles:
            if player.distance(obstacle) < 20:
                player.color("red")
                game_over_function()
                return  # Salir del bucle si el juego ha terminado
            if obstacle.xcor() < -screen_width / 2:
                # Reposicionar obstáculo fuera de la pantalla en el lado derecho
                obstacle.setx(screen_width / 2)
                # Aumentar la puntuación cada vez que un obstáculo sale de la pantalla
                score += 1
                update_score()

    screen.update()
    if not game_over:
        screen.ontimer(main_game_loop, 10)  # Volver a llamar al bucle principal después de un intervalo de tiempo
  # Volver a llamar al bucle principal después de un intervalo de tiempo

# Mostrar el menú de inicio
show_start_screen()

# Iniciar el bucle de eventos de la pantalla
screen.mainloop()