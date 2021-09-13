#-Banco de preguntas debe ser una clase: nombre, Tema, plantillas. Métodos: get tema, get plantillas
from plant import *

class bdp:
  #nombre=""
  #Lista_plantillas=[]
  #insertar a la base de datos
  
#-plants: id, tema, enunciado, voids, respuestas correctas, respuestas relleno
  def set():
    #get de pregunta???
    #bdp.nombre=input('Ingrese el nombre del banco (el tema) ')
    Lista_plantillas=[]
    bucle = False
    var=0
    while bucle== False: 
      var=int(input('Ingrese 1 si quiere añandir una plantilla, ingrese 2 si quiere parar de añadir plantillas'))
      if var==1:
        #bdp.Lista_plantillas.append(plant())
        Lista_plantillas.append(plant())
      if var==2:
        bucle = True
    #return bdp.Lista_plantillas 
    return Lista_plantillas 

    #dicc=[diccCalculo{}, diccCalculo2{}]

    #diccCalculo=
    # {Algebra}:{Plant1, P2, P3...}={
    #
    # {Derivadas}:{Plant1, P2, P3...}
    # }