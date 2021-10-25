from pregunta import *
from curso import *
from grupo import *
#from main import cursos

class examen:
  #id_examen=0
  #Estudiante=""
  #Tema=""
  #can_preguntas=0
  #listaTemp=[]
  #imp=''
  

  def __init__(self, curso, grupo):
    self.listaTemp=[]
    self.imp=''
    self.id_examen=input('Ingrese el id del examen: ')
    self.can_preguntas=int(input('¿Cuántas preguntas va a tener la evaluación?'))
    
    #Agregar cada pregunta al examen
    while self.can_preguntas>0:
      self.listaTemp.append(pregunta(curso,grupo))
      for i in range(len(self.listaTemp)):
        print(self.listaTemp[i])
      self.can_preguntas=self.can_preguntas-1

    #Aleatorizar el orden de las preguntas
    shuffle(self.listaTemp)

    #Configurar el string que se va a imprimir
    for i in range(len(self.listaTemp)):
      self.imp=self.imp+ str(self.listaTemp[i].id_pregunta)+'. ' + str(self.listaTemp[i].preg)+'\n'
      

      
  #función paa generar exámenes

  def autoExam(curso, group):
    #group=grupo()
    tempN=''
    for i in range(len(group.estudiantes)):
          tempN=group.estudiantes[i] + '.txt'
          var=open(tempN, 'w+')
          exam = examen(curso, group)
          var.write(group.estudiantes[i] +'\n'+exam.imp)
          var.close()
    return None