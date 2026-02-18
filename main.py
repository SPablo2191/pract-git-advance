def menu():
    while True:
        pregunta = input("diga 'si' para salir: ")
        if pregunta == "si":
            print("hola")
            break
        elif pregunta == "error":
            try:
                raise(ValueError("El programa ha fallado"))
            except ValueError as e:
                print(e)
                break
    return

menu()