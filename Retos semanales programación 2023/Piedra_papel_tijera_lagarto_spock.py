# Crea un programa que calcule quien gana mΓ‘s partidas al piedra,
# papel, tijera, lagarto, spock.
# - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
# - La funciΓ³n recibe un listado que contiene pares, representando cada jugada.
# - El par puede contener combinaciones de "πΏ" (piedra), "π" (papel),
#   "βοΈ" (tijera), "π¦" (lagarto) o "π" (spock).
# - Ejemplo. Entrada: [("πΏ","βοΈ"), ("βοΈ","πΏ"), ("π","βοΈ")]. Resultado: "Player 2".
# - Debes buscar informaciΓ³n sobre cΓ³mo se juega con estas 5 posibilidades.

# Todos las combinaciones ganan a 2, y pierden contra 2
# Piedra: Gana contra -> Tijeras y Lagarto, Pierde contra -> Papel y Spock
# Papel: Gana contra -> Piedra y Spock, Pierde contra -> Tijera y Lagarto
# Tijera: Gana contra -> Papel y Lagarto, Pierde contra -> Piedra y Spock
# Lagarto: Gana contra -> Papel y Spock, Pierde contra -> Piedra y Tijera
# Spock: Gana contra -> Tijeras y Piedra, Pierde contra -> Papel y Lagarto

def compara_resultados(n1, n2):
    if n1 > n2:
        return("Player 1")
    elif n1 < n2:
        return("Player 2")
    elif n1 == n2:
        return("Tie")

def func_piedra_papel_tijera_lagarto_spock(lpares):
    reglas = {"πΏ": "βοΈπ¦", "π": "πΏπ", "βοΈ": "ππ¦", "π¦": "ππ", "π": "βοΈπΏ"}
    P1 = P2 = 0
    for pares in lpares:
        if pares[0] not in list(reglas.keys()) or pares[1] not in list(reglas.keys()):
            return ("Se ha equivocado al introducir el input, corrijalo y vuelva a probar")
        elif pares[0] == pares[1]:
            pass
        elif pares[0] not in reglas[pares[1]]:
            P1 += 1
        else:
            P2 += 1
    return (compara_resultados(P1, P2))

print(func_piedra_papel_tijera_lagarto_spock([("πΏ","βοΈ"), ("βοΈ","πΏ"), ("π","π"), ("πΏ","βοΈ")]))