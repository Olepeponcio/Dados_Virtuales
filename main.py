"""modulo principal.
instancia la clase gamemanager que instancia a su vez
a la clase objeto
controla el bucle principal"""
from game_manager import GameManager

# instancia gameManager
game = GameManager()
# generar la lista de dados
game.numero_dados(2, 6)
# bucle principal del juego
FIN_JUGADAS = False


def msj_lanzar():
    """Mientras no introduzca los valore requeridos
    preguntará por el lanzamiento"""
    print("¿Lanzar los dados?")
    seleccion = ''
    while not (seleccion.isdigit() and seleccion in ('1', '2')):
        seleccion = input("Elija una opción [1]: Sí, [2]: No: --> ")
    return seleccion


while not FIN_JUGADAS:
    # preguntar al usuario si quiere lanzar
    opcion = msj_lanzar()
    # no--> cierre bucle principa
    if opcion == '2':
        FIN_JUGADAS = True
    else:
        # si --> realiza la ronda
        valor_jugadas = game.ronda_de_lanzamiento()
        # imprime el diccionario en pantalla
        for clave, valor in valor_jugadas.items():
            print(f"clave: {clave}, valor: {valor}")
