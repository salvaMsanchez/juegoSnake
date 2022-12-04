from turtle import Screen
from snake import Snake
from food import Food
from marcador import Marcador
import time
from turtle import Turtle

pantalla = Screen()
pantalla.setup(width=600, height=600)
pantalla.bgcolor("#753188")
pantalla.title("Snake Game. Realizado por Salvador Moreno")
pantalla.tracer(0)

realizadoPor = Turtle()
serpiente = Snake()
comida = Food()
marcador = Marcador()

pantalla.listen()
pantalla.onkey(serpiente.up, "Up")
pantalla.onkey(serpiente.down, "Down")
pantalla.onkey(serpiente.left, "Left")
pantalla.onkey(serpiente.right, "Right")

realizadoPor.write("Hecho por: Salva Moreno", font=("Courier", 15), align="center")
realizadoPor.penup()
realizadoPor.hideturtle()

serpiente.jugando = True
while serpiente.jugando:
    # Actualización de la pantalla cada 0.1 segundos --> pantalla.tracer(0)
    pantalla.update()
    time.sleep(0.1)

    serpiente.movimiento()

    # Detectar la colisión con la comida
    if serpiente.partesSerpiente[0].distance(comida) < 15:
        comida.comer()
        serpiente.crecer()
        marcador.puntuacion += 1
        marcador.nueva_puntuacion(marcador.puntuacion)

    # Detectar la colisión con las paredes
    if serpiente.partesSerpiente[0].xcor() > 280 or serpiente.partesSerpiente[0].xcor() < -280 or serpiente.partesSerpiente[0].ycor() > 280 or serpiente.partesSerpiente[0].ycor() < -280:
        marcador.reiniciar_puntuacion()
        serpiente.reset()

    # Detectar la colisión con el cuerpo de la serpiente
    for partes in serpiente.partesSerpiente[1:]:
        if serpiente.partesSerpiente[0].distance(partes) < 10:
            marcador.reiniciar_puntuacion()
            serpiente.reset()

    if pantalla.onkey(serpiente.salir_juego, "e"):
        marcador.reiniciar_puntuacion()
        serpiente.jugando = False

pantalla.exitonclick()
