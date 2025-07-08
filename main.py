#Importar diccionarios con letras en Código Morse
from morse import morse_dict, texto_dict

#Imprime mensajes de bienvenida
print('''
  _______            _            _                _____          _ _               __  __                     
 |__   __|          | |          | |              / ____|        | (_)             |  \/  |                    
    | |_ __ __ _  __| |_   _  ___| |_ ___  _ __  | |     ___   __| |_  __ _  ___   | \  / | ___  _ __ ___  ___ 
    | | '__/ _` |/ _` | | | |/ __| __/ _ \| '__| | |    / _ \ / _` | |/ _` |/ _ \  | |\/| |/ _ \| '__/ __|/ _ |
    | | | | (_| | (_| | |_| | (__| || (_) | |    | |___| (_) | (_| | | (_| | (_) | | |  | | (_) | |  \__ \  __/
    |_|_|  \__,_|\__,_|\__,_|\___|\__\___/|_|     \_____\___/ \__,_|_|\__, |\___/  |_|  |_|\___/|_|  |___/\___|
                                                                       __/ |                                   
                                                                      |___/                                    
''')
print("¡Bienvenido al Traductor de Código Morse!")

def pedir_datos():
    '''Recoge la decisión del usuario sobre el tipo de traducción: de texto a Morse o viceversa.'''
    
    #Permite seguir preguntando en caso de que el usuario ingrese una opción inadecuada.
    decision = True
    while decision:
        try: 
            choice = int(input("\nIngresa 1 si quieres traducir texto a Código Morse.\n" \
                                "Ingresa 2 si quieres traducir Código Morse a texto. \n"))

            #Si la decisión está dentro de las opciones, termina el bucle y regresa el resultado.
            if choice == 1 or choice == 2:
                decision = False
                return choice
            else:
                print("Ingresaste un valor distinto. Inténtalo de nuevo.")

        except ValueError:
            print("Ingresaste un valor distinto. Inténtalo de nuevo.")

def texto_a_morse():
    '''Transforma una cadena de texto en Código Morse.'''

    palabra = input("Ingresa la palabra/frase que quieras traducir a Código Morse: \n").upper()
    for letra in palabra:
        print(morse_dict[letra], end=" ")

def morse_a_texto():
    '''Transforma una cadena de Código Morse en texto.'''

    morse = input("Ingresa el Código Morse que quieres traducir a texto. Escribe un espacio entre cada letra y tres espacios entre palabras: \n")

    #Separa y guarda la cadena en palabras separadas (mediante 3 espacios)
    palabras_morse = morse.split("   ")

    #Guarda las letras de cada palabra por separado. Se crea una lista por cada palabra.
    letras_morse = []
    for palabra in palabras_morse:
        letras_morse.append(palabra.split(" "))

    #Guarda la palabra conforme se descifre.
    palabra_final = ""
    #Recorre cada palabra
    for i in range(0, len(letras_morse)):
        #Recorre cada letra de la palabra actual
        for letra in letras_morse[i]:
            palabra_final += texto_dict[letra]
        palabra_final += " "
    print(f"La palabra final es: {palabra_final}")

#Ciclo principal. Permite que siga hasta que el usuario lo desee.
on = True
while on:
    #Guarda el resultado de la decisión del usuario.
    resultado = pedir_datos()

    #Dependiendo de la decisión, se efectúa la función correspondiente.
    if resultado == 1:
        texto_a_morse()
    if resultado == 2:
        morse_a_texto()
    
    #Al terminar, se pregunta al usuario si quiere continuar usando el programa.
    pregunta_on = int(input("\n¿Quieres traducir otra cosa? (1=Sí, 2=No): " ))
    #Termina la ejecución del programa
    if pregunta_on != 1:
        on = False