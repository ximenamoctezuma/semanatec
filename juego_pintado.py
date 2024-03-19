#José Armando Benvenuto Valerdi - A00832948
#Ximena Moctezuma Armendáriz - A01722050
#Jesús Daniel Martínez García - A00833591

from turtle import *  # Importa todas las funciones de la biblioteca Turtle
from freegames import vector  # Importa el módulo vector de la biblioteca freegames
import math  # Importa el módulo math para operaciones matemáticas

# Función para dibujar una línea desde el punto de inicio hasta el punto final
def line(start, end):
    "Draw line from start to end."  # Docstring explicando la función
    up()  # Levanta el lápiz del lienzo
    goto(start.x, start.y)  # Mueve el lápiz al punto de inicio
    down()  # Baja el lápiz al lienzo
    goto(end.x, end.y)  # Dibuja una línea hasta el punto final

# Función para dibujar un cuadrado desde el punto de inicio hasta el punto final
def square(start, end):
    "Draw square from start to end."  # Docstring explicando la función
    up()  # Levanta el lápiz del lienzo
    goto(start.x, start.y)  # Mueve el lápiz al punto de inicio
    down()  # Baja el lápiz al lienzo
    begin_fill()  # Comienza a rellenar la forma
    for _ in range(4):  # Dibuja los cuatro lados del cuadrado
        forward(end.x - start.x)  # Avanza la distancia entre los puntos en el eje x
        left(90)  # Gira 90 grados hacia la izquierda
    end_fill()  # Finaliza el relleno del cuadrado

# Función para dibujar un círculo desde el punto de inicio hasta el punto final
def draw_circle(start, end):
    "Draw circle from start to end."  # Docstring explicando la función
    radius = math.sqrt((end.x - start.x)**2 + (end.y - start.y)**2)  # Calcula el radio del círculo
    up()  # Levanta el lápiz del lienzo
    goto(start.x, start.y - radius)  # Mueve el lápiz al punto de inicio del círculo
    down()  # Baja el lápiz al lienzo
    color(fill_color())  # Establece el color de relleno según la función fill_color
    begin_fill()  # Comienza a rellenar la forma
    circle(radius)  # Dibuja un círculo con el radio calculado
    end_fill()  # Finaliza el relleno del círculo

# Función para dibujar un rectángulo desde el punto de inicio hasta el punto final
def rectangle(start, end):
    "Draw rectangle from start to end."  # Docstring explicando la función
    up()  # Levanta el lápiz del lienzo
    goto(start.x, start.y)  # Mueve el lápiz al punto de inicio
    down()  # Baja el lápiz al lienzo
    begin_fill()  # Comienza a rellenar la forma
    for _ in range(2):  # Dibuja dos lados del rectángulo
        forward(end.x - start.x)  # Avanza la distancia entre los puntos en el eje x
        left(90)  # Gira 90 grados hacia la izquierda
        forward(end.y - start.y)  # Avanza la distancia entre los puntos en el eje y
        left(90)  # Gira 90 grados hacia la izquierda
    end_fill()  # Finaliza el relleno del rectángulo

# Función para dibujar un triángulo desde el punto de inicio hasta el punto final
def triangle(start, end):
    "Draw triangle from start to end."  # Docstring explicando la función
    up()  # Levanta el lápiz del lienzo
    goto(start.x, start.y)  # Mueve el lápiz al punto de inicio
    down()  # Baja el lápiz al lienzo
    begin_fill()  # Comienza a rellenar la forma
    for _ in range(3):  # Dibuja los tres lados del triángulo
        goto(end.x, end.y)  # Mueve el lápiz al punto final
        goto(start.x, start.y)  # Dibuja una línea al punto de inicio
    end_fill()  # Finaliza el relleno del triángulo

# Función para obtener el color de relleno actual
def fill_color():
    "Get the current fill color."  # Docstring explicando la función
    current_color = pencolor()  # Obtiene el color de dibujo actual
    if current_color == 'green':  # Si el color actual es verde
        return 'green'  # Devuelve 'green'
    elif current_color == 'blue':  # Si el color actual es azul
        return 'blue'  # Devuelve 'blue'
    else:  # Para otros colores
        return 'black'  # Devuelve 'black'

# Función para manejar el clic del mouse
def tap(x, y):
    "Store starting point or draw shape."  # Docstring explicando la función
    start = state['start']  # Obtiene el punto de inicio actual

    if start is None:  # Si no hay un punto de inicio
        state['start'] = vector(x, y)  # Almacena el punto de inicio
    else:  # Si ya hay un punto de inicio
        shape = state['shape']  # Obtiene la función de dibujo seleccionada
        end = vector(x, y)  # Obtiene el punto final del dibujo
        shape(start, end)  # Dibuja la forma usando el punto de inicio y el punto final
        state['start'] = None  # Reinicia el punto de inicio

# Función para almacenar un valor en el estado
def store(key, value):
    "Store value in state at key."  # Docstring explicando la función
    state[key] = value  # Almacena el valor en el estado bajo la clave especificada

# Estado inicial
state = {'start': None, 'shape': line}  # Define el estado inicial con un punto de inicio vacío y la forma de dibujo como una línea
setup(420, 420, 370, 0)  # Configura la ventana de dibujo
onscreenclick(tap)  # Asigna la función tap al clic del mouse
listen()  # Escucha los eventos de teclado
onkey(undo, 'u')  # Deshace la última acción con la tecla 'u'
onkey(lambda: color('black'), 'K')  # Cambia el color del lá
