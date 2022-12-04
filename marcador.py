from turtle import Turtle

ALINEAMIENTO = "center"
FUENTE_PUNTUACION = ("Courier", 15, "bold")
FUENTE_GAME_OVER = ("Courier", 25, "bold")

class Marcador(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.puntuacion = 0
        with open("data.txt") as file:
            self.puntuacion_mas_alta = int(file.read())
        self.penup()
        self.hideturtle()
        self.setposition(0, 270)
        self.write(f"Puntuación: {self.puntuacion}. Puntuación más alta: {self.puntuacion_mas_alta}", align=ALINEAMIENTO, font=FUENTE_PUNTUACION)

    def nueva_puntuacion(self, puntuacion):
        self.clear()
        self.write(f"Puntuación: {puntuacion}. Puntuación más alta: {self.puntuacion_mas_alta}", align=ALINEAMIENTO, font=FUENTE_PUNTUACION)

    def reiniciar_puntuacion(self):
        if self.puntuacion > self.puntuacion_mas_alta:
            self.puntuacion_mas_alta = self.puntuacion
        self.puntuacion = 0
        self.clear()
        self.write(f"Puntuación: {self.puntuacion}. Puntuación más alta: {self.puntuacion_mas_alta}", align=ALINEAMIENTO, font=FUENTE_PUNTUACION)
        with open("data.txt", "w") as file:
            file.write(f"{self.puntuacion_mas_alta}")