
class grupo:
  #-Grupo debe ser una clase (tiene una lista de estudiantes, enlace a una función para generar exámenes, crear grupos)

  #id_grupo= '000'
  #estudiantes=[]

  def __init__(self):
    self.id_grupo=input('Ingrese el codigo del grupo: ')
    self.estudiantes=[]
    temp=int(input('cuantos estudiantes hay en su clase: '))
    while temp>len(self.estudiantes):
      self.estudiantes.append(input('ingrese el codigo y el nombre de los estudiantes: '))
    #return self.estudiantes, self.id_grupo
  
  def getEstudiantes(group):
    #group=grupo()
    est=''
    for i in range(len(group.estudiantes)):
      est= est+'\n'+group.estudiantes[i]
    return est


  def getID(group):
    return group.id_grupo
'''
  def set():
    group = grupo()
    group.id_grupo=input('Ingrese el codigo del grupo: ')
    group.estudiantes=[]
    temp=int(input('cuantos estudiantes hay en su clase: '))
    while temp>len(grupo.estudiantes):
      group.estudiantes.append(input('ingrese el codigo y el nombre de los estudiantes: '))
    return group
'''