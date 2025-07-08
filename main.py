from morse import morse_dict, texto_dict

print("""
  _______            _            _                _____          _ _               __  __                     
 |__   __|          | |          | |              / ____|        | (_)             |  \/  |                    
    | |_ __ __ _  __| |_   _  ___| |_ ___  _ __  | |     ___   __| |_  __ _  ___   | \  / | ___  _ __ ___  ___ 
    | | '__/ _` |/ _` | | | |/ __| __/ _ \| '__| | |    / _ \ / _` | |/ _` |/ _ \  | |\/| |/ _ \| '__/ __|/ _ |
    | | | | (_| | (_| | |_| | (__| || (_) | |    | |___| (_) | (_| | | (_| | (_) | | |  | | (_) | |  \__ \  __/
    |_|_|  \__,_|\__,_|\__,_|\___|\__\___/|_|     \_____\___/ \__,_|_|\__, |\___/  |_|  |_|\___/|_|  |___/\___|
                                                                       __/ |                                   
                                                                      |___/                                    
""")
print("¡Bienvenido al Traductor de Código Morse!")

def pedir_datos():
    decision = True
    while decision:
        try: 
            choice = int(input("\nIngresa 1 si quieres traducir texto a Código Morse.\n" \
                                "Ingresa 2 si quieres traducir Código Morse a texto. \n"))

            if choice == 1 or choice == 2:
                decision = False
                return choice
            else:
                print("Ingresaste un valor distinto. Inténtalo de nuevo.")

        except ValueError:
            print("Ingresaste un valor distinto. Inténtalo de nuevo.")

def texto_a_morse():
    palabra = input("Ingresa la palabra/frase que quieras traducir a Código Morse: \n").upper()
    for letra in palabra:
        print(morse_dict[letra], end=" ")

def morse_a_texto():
    palabra_final = ""
    morse = input("Ingresa el Código Morse que quieres traducir a texto. Escribe un espacio entre cada letra y tres espacios entre palabras: \n")

    palabras_morse = morse.split("   ")
    letras_morse = []
    for palabra in palabras_morse:
        letras_morse.append(palabra.split(" "))

    for i in range(0, len(letras_morse)):
        for letra in letras_morse[i]:
            palabra_final += texto_dict[letra]
        palabra_final += " "
    print(f"La palabra final es: {palabra_final}")

on = True

while on:
    resultado = pedir_datos()
    if resultado == 1:
        texto_a_morse()
    if resultado == 2:
        morse_a_texto()
    
    pregunta_on = int(input("\n¿Quieres traducir otra cosa? (1=Sí, 2=No): " ))
    if pregunta_on != 1:
        on = False