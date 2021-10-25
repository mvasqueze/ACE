#import mysql.connector
#
#   mydb = mysql.connector.connect(
#     host="localhost",
#     user="yourusername",
#     password="yourpassword",
#     database="mydatabase"
#   )
#   
#   mycursor = mydb.cursor()
#
# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
import pprint
from curso import *
from examen import *
from grupo import *
#from pregunta import setCurso
from plant import *


class Main:
  cursos=[]
  nombres=[]
  c=''

  def crearCurs(self):
    x=int(input('¡Bienvenido, docente! Selecciona la opción a la que quieres ingresar:\n 1.Crear curso\n 2.Ver cursos\n 3.Salir \n'))
    if x==1:
      #crear curso
      # MySQL- Si no hay cursos creados, se crea la tabla cursos; si ya hay creados, se agrega una fila.
      #Código provisional:
      #if len(self.cursos)==0:
        #Crear tabla y agregar una fila en MySQL!!!!!!
        #self.c=curso()
        #c.set()
        #cursos.append(main.c)
        #self.cursos.append(curso())
        
      #else:
        #Agregar una fila a la tabla ya existente en MySQL!!!!!!
        #self.c=curso()
        #main.c.set()
        #self.cursos.append(curso())
      nuevoCurso = curso()
      self.cursos.append(nuevoCurso)
      self.nombres.append(nuevoCurso.nombre)
        
      print('Estos son los cursos que tienes ahora: ')
      for i in range(len(self.cursos)):
        print(self.cursos[i].nombre)
        #self.nombres.append(self.cursos[i].nombre)
      self.grupos()
        #FUNCIÓN PARA VER BANCOS DE PREGUNTA Y LOS GRUPOS EL CURSO!!!!!!!!!!

        
    elif x==2:
      #ver cursos
      print('Estos son los cursos que tienes ahora: ')
      for i in range(len(self.cursos)):
        print(self.cursos[i].nombre)
        #self.nombres.append(self.cursos[i].nombre)
      self.grupos()
        #getgrupo - pedirle grupo a la persona

    elif x==3:
      exit()

      
  def grupos(self):
    
    ndx=0
    temp=0
    cur=''
    while temp!=1:
      x=input("Digita el nombre del curso al cual quieres acceder. Por favor, respeta las mayúsculas y los espacios: \n")
      try:
        ndx = self.nombres.index(x)
        print(self.nombres[ndx])
        cur=self.cursos[ndx]
        curso.get(self.cursos[ndx])
        #ENCONTRAR MANERA DE QUE SE PUEDA ACCEDER A LOS BANCOS DE PREGUNTAS DE CADA CURSO Y QUE MUESTRE
        #              LAS PLANTILLAS (ITERACIÓN 2)
        temp=1
      except:
        ndx = -1
        print("Nombre del curso erróneo. ")
    #setCurso(cur)
    self.menu(cur)
    
        
  def menu(self,course):
    temp=0
    #course=main.c
    self.c = course


    while temp!=1:
      x=input("Digita el ID del grupo al cual quieres acceder. Por favor, respeta las mayúsculas y los espacios: \n")
      li=course.grupos
      var=0
      while var<len(li):
        id=grupo.getID(course.grupos[var])
        if id==x:
          print('El ID del grupo es: '+x+'\nLos estudiantes (y sus códigos) de este curso son: '+grupo.getEstudiantes(course.grupos[var]))
          temp=1
          examen.autoExam(course, course.grupos[var])
          var=len(li)
        elif var==len(li)-1 and id!=x:
          print('El ID introducido es erróneo o no existe. Intente de nuevo.')
          var=var+1

        else:
          var=var+1

      #11/09/2021 -> 
      #           -> DJANGO
      
      temp=1

    
  ##usar la lista para generar preguntas
  def main(self):
    i=1
    while i==1:
      self.crearCurs()  

if __name__== '__main__':
  main_runner = Main()
  main_runner.main()