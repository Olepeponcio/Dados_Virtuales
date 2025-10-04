"""clase que maneja una lista de objetos dados"""


from dado import Dado
class GameManager:
    def __init__(self):
        self.dados: list[Dado] = []



    def numero_dados(self, num_dados: int,  num_caras):
        """funcion que determina el número de dados y sus caras
        y agrega los objetos dado en la lista"""
        for i in range(num_dados):
            self.dados.append(Dado(num_caras))


    def ronda_de_lanzamiento(self):
        """le pide a cada dado que se lance a sí mismo"""
        valores_obtenidos = {}
        for indice, dado in enumerate(self.dados, start= 1):
            valor = dado.lanzamiento()
            valores_obtenidos[f"Dado {indice}"] = valor

        return valores_obtenidos



if __name__ == "__main__":

    game = GameManager()
    game.numero_dados(2, 6)

    for d in game.dados:
        print(d)

    valores_obtenidos = game.ronda_de_lanzamiento()

    for clave, valor in valores_obtenidos.items():
        print (f"clave: {clave}, valor: {valor}" )



