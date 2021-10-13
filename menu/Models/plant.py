class plant:
  ID_plantilla = ""
  #incorrectas=[]
  enunciado=""
  oyr={}
  plantilla=()
  ('id', 'oyr')
  #plantilla[1].oyr[num]

  def __init__ (self):
    self.incorrectas = []
    self.oyr={}
    self.plantilla=()
    ##sacar el tema atraves del get del banco de plantilla
    self.ID_plantilla=input('Ingrese el codigo de la plantilla a crear: ')
    self.enunciado=input('Ingrese el enunciado de la plantilla a crear: (el espacio a rellenar debe estar escrito y separado entre espacios como: /// ) ')
    x=int(input('¿Cuántas variantes de la plantilla quiere hacer? (Cuántas preguntas basadas en esta plantilla) '))
    
    self.oyr={}

    #Definir cuántas variaciones de la plantilla se van a dar
    temp=0
    while temp<x:
      Opcion=input('Escriba una posible opcion para rellenar el espacio en blanco: ')
      Respuesta=input('Ingrese la respuesta a la anterior opcion ')
      self.oyr[Opcion] = Respuesta
      temp=temp+1
    print(self.oyr)

    self.incorrectas=[]
    ##agregar la respuesta a la lista de posibles respuestas
    cantidad_malas=int(input('Ingrese cantidad de opciones incorrectas para la respuesta. (minimo 3, máximo 7) '))
    if cantidad_malas<3:
      while cantidad_malas<3:
          cantidad_malas=int(input('Cantidad menor a la necesitada, ingrese un numero mayor o igual a 3'))
    bucle=0
    while bucle<cantidad_malas:
      opcion=input("ingreso opcion incorrecta: ")
      self.incorrectas.append(opcion)
      bucle=bucle+1
