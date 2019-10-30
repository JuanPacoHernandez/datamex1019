import sys, random, time, tkinter
from tkinter import *
    #colores
white=(255,255,255)
red=(0,0,0)
    #coord contiene las coordenadas aleatorias en donde se ubica el tablero
coordini=[]
    #bias contiene la desviacion aleatoria que influira en la ubicación del dardo
bias=[]
    #generacion aleatoria de coord y bias
for i in range(2):
       coordini.append(random.randint(100,500))
       bias.append(random.randint(-3,3))

def t(x):
   return time.sleep(x)

    #lista dirección del viento, puntos cardinales
dirvien=['N','S','E','O','NE','SE','NO','SO']
#circulo 1 var
c1x1=coordini[0]-100
c1y1=coordini[1]-100
c1x2=coordini[0]+100
c1y2=coordini[1]+100
#circulo 2 var
c2x1=coordini[0]-70
c2y1=coordini[1]-70
c2x2=coordini[0]+70
c2y2=coordini[1]+70
#circulo 3 var
c3x1=coordini[0]-40
c3y1=coordini[1]-40
c3x2=coordini[0]+40
c3y2=coordini[1]+40
#centro
c4x1=coordini[0]-15
c4y1=coordini[1]-15
c4x2=coordini[0]+15
c4y2=coordini[1]+15
print("\n\n\t\t\tB I E N V E N I D O S...\a")
t(2)
print("\n\n\t\tEste es el clásico juego del Tiro al Blanco...\a")
t(2)
print("\n\nEl tablero de la izquierda tiene una posición aleatoria...\a")
print("\n\nLas puntuaciones son:\n.........................................................\n.\t100 ptos al centro de la diana                  .\n.\t70 ptos antes del primer circulo concentrico\t.\n.\t40 ptos antes del segundo circulo               .\n.\t15 ptos antes del ultimo circulo                .\n.........................................................")
o=1
while o==1:
    alto=600
    ancho=600
    root = Tk()
    root.title('Tiro al blanco')
    canvas = Canvas(width=alto, height=ancho, bg='black')
    canvas.pack(expand=YES,fill=BOTH)
    canvas.create_oval(c1x1,c1y1,c1x2,c1y2, width=2, outline='white')
    canvas.create_oval(c2x1,c2y1,c2x2,c2y2, width=2, outline='white')
    canvas.create_oval(c3x1,c3y1,c3x2,c3y2, width=2, outline='white')
    canvas.create_oval(c4x1,c4y1,c4x2,c4y2, width=2, fill='white')
    canvas.create_line(200,0,200,20, width=5, fill='green')
    canvas.create_line(400,0,400,20, width=5, fill='green')
    canvas.create_line(0,200,20,200, width=5, fill='green')
    canvas.create_line(0,400,20,400, width=5, fill='green')
    canvas.create_line(200,580,200,600, width=5, fill='green')
    canvas.create_line(400,580,400,600, width=5, fill='green')
    canvas.create_line(580,200,600,200, width=5, fill='green')
    canvas.create_line(580,400,600,400, width=5, fill='green')
    input("\n\t\t\tEnter...para continuar")
    print("\n\nPara el lanzamiento del dardo considera que el vector Velocidad del viento\nafecta la exactitud de las coordenadas que propongas...\a")
    t(3)
    print("\n\nConsultando con el Centro Metereologico Nacional los datos del vector\nVelocidad del viento...espera, por favor\a");
    t(2)
    for i in range(5):
          print("...\a")
          t(0.5)
    print("\n\nMagnitud del vector Velocidad del viento= \a\a\a",(bias[0]**2)+(bias[1]**2)**0.5)
    t(0.5)
    d=random.choice(dirvien)
    print("\nDirección del vector Velocidad del viento: \a\a",d)
    t(2)
    print("\n\nAhora, ingresa las coordenadas de tu tiro, pero considera...las lineas verdes\ntienen un rango de 200 entre ellas...\n\a\a\a")
    x=float(input("\n\a\a\aIngresa la coordenada 'X': "))
    y=float(input("\a\a\aIngresa la coordenada 'Y': "))
    #si la direccion del vector es Norte o Noreste, crea una rectangulo(dardo) con coordenadas afectadas por los bias, componentes del Vector
    if d == 'N' or d == 'NE':
      canvas.create_rectangle(x+bias[0]-6,y+bias[1]-6,x+bias[0]+6,y+bias[1]+6, width=2, fill='red')
	#si las coordenadas del dardo caen entre el circulo 4 y el circulo 3, puntuacion es 40

    if d == 'O' or d == 'NO':
      canvas.create_rectangle(x-bias[0]-6,y+bias[1]-6,x-bias[0]+6,y+bias[1]+6, width=2, fill='red')
  
    if d == 'S' or d == 'SO':
      canvas.create_rectangle(x-bias[0]-6,y-bias[1]-6,x-bias[0]+6,y-bias[1]+6, width=2, fill='red')

    if d == 'S' or d == 'SE':
      canvas.create_rectangle(x+bias[0]-6,y-bias[1]-6,x+bias[0]+6,y-bias[1]+6, width=2, fill='red')
        
    input("\n\t\t\tEnter...para salir")
    o=0

    
    

