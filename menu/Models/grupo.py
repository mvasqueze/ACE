
class grupo:
  #-Grupo debe ser una clase (tiene una lista de estudiantes, enlace a una función para generar exámenes, crear grupos)

  id_grupo= '000'
  estudiantes=[]
  
  def getEstudiantes(group):
    group=grupo()
    est=''
    for i in range(len(group.estudiantes)):
      est= est+'\n'+group.estudiantes[i]
    return est


  def getID(group):
    return grupo.id_grupo

  def set():
    grupo.id_grupo=input('Ingrese el codigo del grupo: ')
    grupo.estudiantes=[]
    temp=int(input('cuantos estudiantes hay en su clase: '))
    while temp>len(grupo.estudiantes):
      grupo.estudiantes.append(input('ingrese el codigo y el nombre de los estudiantes: '))
    return grupo.estudiantes, grupo.id_grupo
     