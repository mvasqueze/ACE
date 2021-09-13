from grupo import *
from bdp import *

class curso:
    #id_curso=0
    #nombre=0
    #profesor=0
    #grupos=[]
    #dicc={}
    #Alternativa MySQL: Construir esta clase como una lista/construir otra clase que incluya objetos tipo curso

    def __init__(self):
      self.grupos = []
      self.dicc = {}
      self.id_curso=input('Ingrese el codigo del curso a crear: \n')
      self.nombre=input('Ingrese el nombre de la clase: \n')
      self.profesor=input('Ingrese el nombre del profesor encargado de la clase: \n')
      n=int(input('¿Cuántos grupos desea crear dentro de este curso? \n'))
      while n>len(self.grupos):
        self.grupos.append(grupo())
      temp=int(input('¿Cuántos bancos de pregunta deseas crear para este curso? '))
      while temp>0:
        name=input('Ingrese el nombre del banco (el tema) ')
        lPlantillas=bdp.set()
        self.dicc[name] = lPlantillas
        temp=temp-1
      #return curso.id_curso, curso.nombre
    

    def get(curso):
      print("Estos son los grupos disponibles de este curso: ")
      for i in range(len(curso.grupos)):
       print(curso.grupos[i].id_grupo) #HACER QUE IMPRIMA SOLO EL NOMBRE
      
      print('Estos son los bancos de pregunta disponibles en este curso: ')
      for h in range(len(curso.dicc.keys())):
        temp=list(curso.dicc)
        print(temp[h])
      return curso.id_curso, curso.nombre


    #def setCurso(idC, name, pro):
    #  id_curso=idC
    #  nombre=name
    #  profesor=pro
    #  id_curso=input('Ingrese el codigo del curso a crear: ')
    #  nombre=input('Ingrese el nombre de la clase: ')
    #  profesor=input('Ingrese el nombre del profesor encargdo de la clase: ')
    #  return 

#curso.dicc.add[nombre: lista plantillas]