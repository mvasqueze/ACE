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
  #respuestaI=[]
  puntaje=0
  #plantillasTemp=[]
  plantilla= ''
  
#Cuando se ingrese al curso, se guarda el nombre/id en un atributo de pregunta
# y desde pregunta se mira una forma de acceder al dir de ese grupo y 
# consecuentemente al banco de preguntas para acceder a la plantilla

  def __init__(self,curso, grupo):
    self.plantillasTemp=[]
    self.curso = curso
    self.grupo = grupo
    curs=self.curso
    self.id_pregunta=input('Ingrese la identificacion de la pregunta (el id con que va a aparecer en el solucionario): ')
    temp=0
    while temp!=1:
      self.tema=input('Escriba el nombre/tema del banco de preguntas, respetando mayúsculas y espacios')
      if curs.dicc.get(self.tema)!=None:
        self.plantillasTemp=self.curso.dicc.get(self.tema) #Bancos de preguntas
        for i in range(len(self.plantillasTemp)):
          print('Estas son las plantillas disponibles en este banco de preguntas: \n')
        
        for i in range(len(self.plantillasTemp)):
          print(str(self.plantillasTemp.index(self.plantillasTemp[i])) + '. '+self.plantillasTemp[i].ID_plantilla +' '+ self.plantillasTemp[i].enunciado+ '\n')
        plantillaNoEncontrada = True
        while plantillaNoEncontrada:
          a=input('Escribe el ID de la plantilla de la cual quieres generar preguntas: ')
          i = 0
          while plantillaNoEncontrada and i < len(self.plantillasTemp):
            if self.plantillasTemp[i].ID_plantilla == a:
              ndx = i
              plantillaNoEncontrada = False
            else:
              i = i+1
          if plantillaNoEncontrada:
            print("El ID de la plantilla no coincide con ninguno, vulva a intentar con uno correcto")
        self.plantilla=self.plantillasTemp[ndx]
        temp=1
      else:
        print('El nombre del banco de preguntas es erróneo, por favor intente nuevamente \n')
      
    
    enunKeys=self.plantilla.oyr.keys() #Gaps enunciados
    theKey=sample(enunKeys, 1) #De aquí se esocge un gap aleatorio
    num=theKey[0]
    vars=self.plantilla.oyr
    r=vars.get(num)
    self.enunciado=str(self.plantilla.enunciado)
    self.enunciado=self.enunciado.replace('///', num)
    # De la línea de arriba, se reemplazan los /// con el gap seleccionado
    self.respuestaC=self.plantilla.oyr[num] #<- La respuesta correcta es el key del gap

    #Configurar el puntaje de la pregunta
    self.puntaje=int(input('Puntaje de esta pregunta: '))

    #Configurar y elegir opciones incorrectas 
    w=int(input('¿Cuántas opciones equivocadas tendrán las preguntas generadas con esta plantilla?'))
    self.respuestaI=sample(self.plantilla.incorrectas, w)

    #Fusión y aleatorización de las respuestas incorrectas y la correcta
    listaTemp=[]
    listaTemp.append(self.respuestaC)
    for i in range(len(self.respuestaI)):
      listaTemp.append(self.respuestaI[i])
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
    self.preg=self.enunciado

    if opcA!='':
      self.preg= self.preg+'\n a. '+opcA
    if opcB!='':
      self.preg=self.preg+'\n b. '+opcB
    if opcC!='':
      self.preg=self.preg+'\n c. '+opcC
    if opcD!='':
      self.preg=self.preg+'\n d. '+opcD
    if opcE!='':
      self.preg=self.preg+'\n e. '+opcE
    if opcF!='':
      self.preg=self.preg+'\n f. '+opcF
    if opcG!='':
      self.preg=self.preg+'\n g. '+opcG
            
#def setCurso(self, c):
#  self.curso=c
