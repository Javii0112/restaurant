import numpy

import validar as fn



while True:
    print("""Menú
    1. Ver restaurant
    2. Reservar mesa
    3. Carta
    4. Pegar
    5. Cancelar
    6. Salir """)

    opcion = fn.validar_opcion()

    if opcion == 1:
        entrada = fn.compra_entrada()
    elif opcion == 2:
        rut = fn.validar_rut()
        nombre = fn.validar_nombre()
        correo = fn.validar_correo()
    elif opcion == 3:
        pass
    elif opcion == 4:
        pass
    elif opcion == 5:
        pass
    else: 
        break
        
