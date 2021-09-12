from plant import *
from curso import *
from random import sample, shuffle

class pregunta:
  #-Pregunta debe ser una clase: Tema, id, respuesta correcta, respuestas incorrectas, enunciado. Funciones: ¿get?
  id_pregunta=''
  tema=''
  enunciado=''
  preg=''
  respuestaC=''
  respuestaI=[]
  puntaje=0
  plantillasTemp=[]
  plantilla= ''
  curso=[]
  
#Cuando se ingrese al curso, se guarda el nombre/id en un atributo de pregunta
# y desde pregunta se mira una forma de acceder al dir de ese grupo y 
# consecuentemente al banco de preguntas para acceder a la plantilla

  def __init__(self, grupo):
    curs=pregunta.curso
    pregunta.id_pregunta=input('Ingrese la identificacion de la pregunta (el id con que va a aparecer en el solucionario): ')
    temp=0
    while temp!=1:
      pregunta.tema=input('Escriba el nombre/tema del banco de preguntas, respetando mayúsculas y espacios')
      if curs.dicc.get(pregunta.tema)!=None:
        pregunta.plantillasTemp=pregunta.curso.dicc.get(pregunta.tema) #Bancos de preguntas
        print('Estas son las plantillas disponibles en este banco de preguntas: \n')
        for i in range(len(pregunta.plantillasTemp)):
          print(str(pregunta.plantillasTemp.index(pregunta.plantillasTemp[i])) + '. '+pregunta.plantillasTemp[i].ID_plantilla +' '+ pregunta.plantillasTemp[i].enunciado+ '\n')
        a=int(input('Escribe el ID de la plantilla de la cual quieres generar preguntas: '))
        #ndx=pregunta.plantillasTemp.index(a)
        plantilla=pregunta.plantillasTemp[a]
        temp=1
      else:
        print('El nombre del banco de preguntas es erróneo, por favor intente nuevamente \n')
      
    
    enunKeys=plantilla.oyr.keys() #Gaps enunciados
    theKey=sample(enunKeys, 1) #De aquí se esocge un gap aleatorio
    num=theKey[0]
    vars=plantilla.oyr
    r=vars.get(num)
    pregunta.enunciado=str(plantilla.enunciado)
    pregunta.enunciado=pregunta.enunciado.replace('///', num)
    # De la línea de arriba, se reemplazan los /// con el gap seleccionado
    pregunta.respuestaC=plantilla.oyr[num] #<- La respuesta correcta es el key del gap

    #Configurar el puntaje de la pregunta
    pregunta.puntaje=int(input('Puntaje de esta pregunta: '))

    #Configurar y elegir opciones incorrectas 
    w=int(input('¿Cuántas opciones equivocadas tendrán las preguntas generadas con esta plantilla?'))
    pregunta.respuestaI=sample(plantilla.incorrectas, w)

    #Fusión y aleatorización de las respuestas incorrectas y la correcta
    listaTemp=[]
    listaTemp.append(pregunta.respuestaC)
    for i in range(len(pregunta.respuestaI)):
      listaTemp.append(pregunta.respuestaI[i])
    shuffle(listaTemp)

    opcA=''
    opcB=''
    opcC=''
    opcD=''
    opcE=''
    opcF=''
    opcG=''

    opcA=str(listaTemp[0])
    opcB=str(listaTemp[1])
    if len(listaTemp)>=3:
      opcC=str(listaTemp[2])
    if len(listaTemp)>=4:
      opcD=str(listaTemp[3])
    if len(listaTemp)>=5:
      opcE=str(listaTemp[4])
    if len(listaTemp)>=6:
      opcF=str(listaTemp[5])
    if len(listaTemp)==7:
      opcG=str(listaTemp[6])
    
    #Ensamblar el string para imprimir
    pregunta.preg=pregunta.enunciado

    if opcA!='':
      pregunta.preg= pregunta.preg+'\n a. '+opcA
    if opcB!='':
      pregunta.preg=pregunta.preg+'\n b. '+opcB
    if opcC!='':
      pregunta.preg=pregunta.preg+'\n c. '+opcC
    if opcD!='':
      pregunta.preg=pregunta.preg+'\n d. '+opcD
    if opcE!='':
      pregunta.preg=pregunta.preg+'\n e. '+opcE
    if opcF!='':
      pregunta.preg=pregunta.preg+'\n f. '+opcF
    if opcG!='':
      pregunta.preg=pregunta.preg+'\n g. '+opcG
            
def setCurso(c):
  pregunta.curso=c