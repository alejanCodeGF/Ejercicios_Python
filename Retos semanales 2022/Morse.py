# Enunciado: Crea un programa que sea capaz de transformar texto natural a código morse y viceversa.
# - Debe detectar automáticamente de qué tipo se trata y realizar la conversión.
# - En morse se soporta raya "—", punto ".", un espacio " " entre letras o símbolos y dos espacios entre palabras "  ".
# - El alfabeto morse soportado será el mostrado en https://es.wikipedia.org/wiki/Código_morse.


# Me rindo xd, que lo arregle el Alejandro de mañana (error al devolver el normal-morse, y error total al hacer el morse)
# Replantearme el problema y arreglarlo, no esta bien planteado

def func_natural_morse(t):
    lista_letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 
                    'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ', ', '.', '?', '/', '-', '(', ')']
    lista_morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', 
                    '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '.----', '..---', '...--', '....-', '.....', 
                    '-....', '--...', '---..', '----.', '-----', '--..--', '.-.-.-', '..--..', '-..-.', '-....-', '-.--.', '-.--.-']
    dic_natural_morse = {}
    tipo_texto = 1 # 0 es natural, 1 es morse
    morse = "-. /"
    texto_final = ""
    if t == '':
        return 
    for letra in t: # Detector de morse o natural
        if letra not in morse:
            tipo_texto = 0
            break
    if tipo_texto: # Si está en morse
        lista_palabras = t.split('/')
        lista_palabras = t.split(' ')
        for i in range(len(lista_palabras)):
            print (i)
            if lista_palabras[i] == '':# or lista_palabras[i] == '/':
                lista_palabras.pop(i)
        for i in range(len(lista_letras)):
            dic_natural_morse[lista_morse[i]] = lista_letras[i]
        print(lista_palabras)
        for pi in lista_palabras:
            pass
            #texto_final += dic_natural_morse[pi]
        return texto_final
    else: # Si no esta en morse
        t = t.upper()
        lista_palabras = t.split(' ')
        for i in range(len(lista_letras)):
            dic_natural_morse[lista_letras[i]] = lista_morse[i]
        for pi in range(len(lista_palabras)):
            varstring = ""
            for letra in lista_palabras[pi]:
                varstring += dic_natural_morse[letra]
                varstring += ' '
            lista_palabras[pi] = varstring 
        texto_final = '/ '.join(lista_palabras)
        return texto_final

a = func_natural_morse("Chocapic. Es una marca de cereales?")
b = func_natural_morse(a)
#print(a)
print(b)