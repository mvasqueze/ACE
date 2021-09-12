class plant:
  ID_plantilla = ""
  incorrectas=[]
  enunciado=""
  oyr={}

  def __init__ (self):
    ##sacar el tema atraves del get del banco de plantilla
    plant.ID_plantilla=input('Ingrese el codigo de la plantilla a crear: ')
    plant.enunciado=input('Ingrese el enunciado de la plantilla a crear: (el espacio a rellenar debe estar escrito y separado entre espacios como: /// ) ')
    x=int(input('¿Cuántas variantes de la plantilla quiere hacer? (Cuántas preguntas basadas en esta plantilla)'))
    
    #Definir cuántas variaciones de la plantilla se van a dar
    temp=0
    while temp<x:
      Opcion=input('Escriba una posible opcion para rellenar el espacio en blanco: ')
      Respuesta=input('Ingrese la respuesta a la anterior opcion ')
      plant.oyr[Opcion] = Respuesta
      temp=temp+1
    print(plant.oyr)

    ##agregar la respuesta a la lista de posibles respuestas
    cantidad_malas=int(input('Ingrese cantidad de opciones incorrectas para la respuesta. (minimo 3, máximo 7)'))
    if cantidad_malas<3:
      while cantidad_malas<3:
          cantidad_malas=int(input('Cantidad menor a la necesitada, ingrese un numero mayor o igual a 3'))
    bucle=0
    while bucle<cantidad_malas:
      opcion=input("ingreso opcion incorrecta: ")
      plant.incorrectas.append(opcion)
      bucle=bucle+1