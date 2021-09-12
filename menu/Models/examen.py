from pregunta import *
from curso import *
from grupo import *
from main import cursos

class examen:
  id_examen=0
  Estudiante=""
  #Tema=""
  can_preguntas=0
  listaTemp=[]
  imp=''
  

def exam(grupo):
  examen.id_examen=int(input('Ingrese el id del examen: '))
  examen.can_preguntas=int(input('¿Cuántas preguntas va a tener la evaluación?'))
  
  #Agregar cada pregunta al examen
  while examen.can_preguntas>0:
    examen.listaTemp.append(pregunta(grupo))
    examen.can_preguntas=examen.can_preguntas-1

  #Aleatorizar el orden de las preguntas
  shuffle(examen.listaTemp)

  #Configurar el string que se va a imprimir
  for i in range(len(examen.listaTemp)):
    examen.imp=examen.imp+ str(examen.listaTemp[i].id_pregunta)+'. ' + str(examen.listaTemp[i].preg)+'\n'
    

    
#función paa generar exámenes

def autoExam(group):
  group=grupo()
  tempN=''
  for i in range(len(group.estudiantes)):
        tempN=group.estudiantes[i] + '.txt'
        var=open(tempN, 'w+')
        exam(group)
        var.write(group.estudiantes[i] +'\n'+examen.imp)
        return None