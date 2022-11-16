def leer_archivo(file_name):
    print(f'Abriste el archivo: {file_name}')
    # Abrir open('','')
    # Procesar read/write
    # Cerrar close()
    # With nos permite agrupar trabajo con archivos
    with open(file_name, 'r') as file:
        lineas = file.readlines()
        for linea in lineas:
            print(linea, end='')
        #while(linea):
         #   print(linea)
          #  linea = file.readline()
    # print('Archivo leido y cerrado')

def agregar_equipo(file_name, equipo):
    with open(file_name, 'a') as file:
        file.write(f"\n{equipo}")
    print("Equipo guardado")

def eliminar_equipo(file_name, equipo):
    with open(file_name, 'r') as file:
        lista_equipos = file.readlines()
    try:
        lista_equipos.remove(equipo)
        print('Equipo eliminado!')
        with open(file_name, 'w') as file:
            file.writelines(lista_equipos)
    except ValueError:
        print('El equipo que deseas eliminar no existe')
    
def actualizar_equipo(file_name, equipo, nuevo_equipo):
    with open(file_name, 'r') as file:
        lista_equipos = file.readlines()
        print(lista_equipos)
    try:
        found= lista_equipos.index(equipo)
        lista_equipos[found]= nuevo_equipo
        print(lista_equipos)
        with open(file_name, 'w') as file:
            file.writelines(lista_equipos)
    except ValueError:
        print('El equipo no se actualizo')
        
    