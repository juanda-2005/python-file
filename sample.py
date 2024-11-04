def main():
    while True:
        print('Seleccione el proceso que desea aplicar')
        print('1: Ingresar puntuación y comentario')
        print('2: Comprueba los resultados obtenidos hasta ahora.')
        print('3: Finalizar')
        num = input()
        
        if num.isdecimal():
            num = int(num)
            if num == 1:
                ingresar_puntuacion_y_comentario()
            elif num == 2:
                comprobar_resultados()
            elif num == 3:
                finalizar_proceso()
                break
            else:
                print('Introduzca un número del 1 al 3')
        else:
            print('Introduzca un número del 1 al 3')

def ingresar_puntuacion_y_comentario():
    while True:
        print('Por favor, introduzca una puntuación en una escala de 1 a 5')
        point = input()
        
        if point.isdecimal():
            point = int(point)
            
            if 1 <= point <= 5:
                print('Por favor, introduzca un comentario')
                comment = input()
                guardar_datos(point, comment)
                break
            else:
                print('Por favor, introduzca un valor entre el 1 y 5')
        else:
            print('Por favor, introduzca la puntuación en números')

def guardar_datos(point, comment):
    post = f'punto: {point} comentario: {comment}'
    with open("data.txt", 'a') as file_pc:
        file_pc.write(f'{post}\n')
    print("Datos guardados exitosamente.")

def comprobar_resultados():
    print('Resultados hasta la fecha:')
    try:
        with open("data.txt", "r") as read_file:
            print(read_file.read())
    except FileNotFoundError:
        print("No hay resultados hasta la fecha.")

def finalizar_proceso():
    print('Finalizando')

main()