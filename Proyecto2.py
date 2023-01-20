import turtle
import time
import random

posponer =0.1

#marcador
score = 0
high_score = 0

#configuracion de ventana
wn = turtle.Screen()
wn.title("Juego de Snake")
wn.bgcolor("black")
wn.setup(width = 600, height=600)
wn.tracer(0)

# cabeza de snake
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = "stop"
cabeza.color("#2196f3")

#Comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.penup()
comida.goto(0,100)
comida.color("#ee369d")

#cuerpo
segmentos = []

#texto
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write("Score: 0            High Score: 0", align= "center", font= ("coursier",24,"normal"))

#funciones

def arriba():
    cabeza.direction = "up"
def abajo():
    cabeza.direction= "down"
def derecha():
    cabeza.direction= "right"
def izquierda():
    cabeza.direction= "left"
def mov():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)

    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)

    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)
   
    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)

#Teclado

wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(izquierda, "Left")
wn.onkeypress(derecha, "Right")

while True:
    wn.update()
    #colicion bordes
    if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
        time.sleep(1)
        cabeza.goto(0,0)
        cabeza.direction = "stop"

        #esconder los segmentos
        for segmento in segmentos:
            segmento.goto(2000,2000)

        #lipiar lista de segmentos
        segmentos.clear()    

        #resetar marcador
        score = 0
        texto.clear() 
        texto.write(f"Score: {score}            High Score: {high_score }",
                align= "center", font= ("coursier",24,"normal"))  


    #colicion comida
    if cabeza.distance(comida) < 20:
       x = random.randint(-280,280)
       y = random.randint(-280,280)
       comida.goto(x,y)

       nuevo_segmento = turtle.Turtle()
       nuevo_segmento.speed(0)
       nuevo_segmento.shape("square")
       nuevo_segmento.penup()
       nuevo_segmento.color("#1465bb")
       segmentos.append(nuevo_segmento)

       #Aumentar marcador
       score += 10

       if score > high_score:
           high_score = score
 
           texto.clear() 
           texto.write(f"Score: {score}            High Score: {high_score }",
                   align= "center", font= ("coursier",24,"normal"))  

    #mover el cuerpo de la serpiente
    totalseg = len(segmentos)
    for index in range(totalseg -1, 0, -1):
        x = segmentos[index - 1].xcor()
        y = segmentos[index - 1].ycor() 
        segmentos[index].goto(x,y)

    if totalseg > 0:
         x = cabeza.xcor()
         y = cabeza.ycor()
         segmentos[0].goto(x,y) 

    mov()
    #coliciones con el cuerpo
    for segmento in segmentos:
        if segmento.distance(cabeza) < 20:
            time.sleep(1)
            cabeza.goto(0,0)
            cabeza.direction = "stop"

            #esconder los sementos
            for segmento in segmentos:
                segmento.goto(2000,2000)

            segmentos.clear()  

            #resetar marcador
            score = 0
            texto.clear() 
            texto.write(f"Score: {score}            High Score: {high_score }",
                    align= "center", font= ("coursier",24,"normal"))  
  
    time.sleep(posponer)