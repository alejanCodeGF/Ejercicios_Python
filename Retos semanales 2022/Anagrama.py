# Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Boolean) según sean o no anagramas.
# Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
# NO hace falta comprobar que ambas palabras existan.
# Dos palabras exactamente iguales no son anagrama.

def func_anagrama(pal1, pal2):
    if pal1 == pal2[::-1]:
        return True
    return False

print(func_anagrama("amor","roma"))
print(func_anagrama("amor","pollo"))