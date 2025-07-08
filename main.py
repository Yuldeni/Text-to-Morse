from morse import morse_dict

palabra = input("Ingresa la palabra/frase que quieras traducir a Código Morse: \n").upper()
for letra in palabra:
    print(morse_dict[letra], end=" ")