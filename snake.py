from turtle import Turtle

POSICIONES_INICIALES = [(0, 0), (-20, 0), (-40, 0)]
DISTANCIA_MOVIMIENTO = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():

    def __init__(self):
        self.partesSerpiente = []
        self.creacion_serpiente()
        self.jugando = True

    def creacion_serpiente(self):
        for posicion in POSICIONES_INICIALES:
            self.nueva_parte(posicion)

    def nueva_parte(self, posicion):
        serpiente = Turtle(shape="square")
        serpiente.color("#9AE66E")
        serpiente.penup()
        serpiente.setposition(posicion)
        self.partesSerpiente.append(serpiente)

    def crecer(self):
        self.nueva_parte(self.partesSerpiente[-1].position())

    def movimiento(self):
        for numPartes in range(len(self.partesSerpiente) - 1, 0, -1):
            posX = self.partesSerpiente[numPartes - 1].xcor()
            posY = self.partesSerpiente[numPartes - 1].ycor()
            self.partesSerpiente[numPartes].goto(posX, posY)
        self.partesSerpiente[0].forward(DISTANCIA_MOVIMIENTO)

    def up(self):
        if self.partesSerpiente[0].heading() != DOWN:
            self.partesSerpiente[0].setheading(UP)

    def down(self):
        if self.partesSerpiente[0].heading() != UP:
            self.partesSerpiente[0].setheading(DOWN)

    def left(self):
        if self.partesSerpiente[0].heading() != RIGHT:
            self.partesSerpiente[0].setheading(LEFT)

    def right(self):
        if self.partesSerpiente[0].heading() != LEFT:
            self.partesSerpiente[0].setheading(RIGHT)

    def reset(self):
        for partes in self.partesSerpiente:
            partes.setpos(1000, 1000)
        self.partesSerpiente.clear()
        self.creacion_serpiente()

    def salir_juego(self):
        self.jugando = False
