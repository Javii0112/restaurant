import numpy
arreglo_restaurant = numpy.zeros((3,3), int)

lista_rut =[]
lista_nombre = []
lista_correo = []

def compra_entrada():
    for x in range(3):
        print (f"fila {x+2}: \t", end="")
        for y in range(3):
            print(arreglo_restaurant[x][y], end="")
    print()





def validar_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opcion: "))
            if opcion in(1, 2, 3, 4, 5, 6):
                return opcion
            else:
                print("ERROR LA OPCION DEBE ESTAR ENTRE 1 Y 6!")
        except:
            print("ERROR INGRESAR UN NÚMERO ENTERO")

def validar_rut():
    while True:
        try:
            rut = int(input("Ingrese su rut(sin puntos ni guion): "))
            if rut >= 1000000 and rut <= 99999999:
                return rut
            else:
                print("ERROR EL RUT DEBE ESTAR SIN PUNTOS NI GUION")
        except:
            print("ERROR DEBE INGRESAR UN NUMERO ENTERO!")
        lista_rut.append(rut)

def validar_nombre():
    while True:
        nombre = input("Ingrese su nombre: ")
        if len(nombre.strip())>=3 and nombre.isalpha():
            return nombre
        else:
            print("ERROR EL NOMBRE DEBE TENER COMO MINIMO 3 LETRAS!")
        lista_nombre.append(nombre)
def validar_correo():
    while True:
        correo = input("Ingrese su correo: ")
        if "@" in correo:
            return correo
        else:
            print("ERROR EL CORREO DEBE INGRESAR SU CORREO CON EL @!")
        lista_correo.append(correo)

del validar_entrada():
