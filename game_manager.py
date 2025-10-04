"""clase que maneja una lista de objetos dados"""

from dado import Dado


class GameManager:
    """clase que instancia a la clase dado
    genera una lista de dados según argumentos  de entrada
    pide a cada objeto de la lista que se lance a sí mismo"""
    def __init__(self):
        self.dados: list[Dado] = []

    def numero_dados(self, num_dados: int, num_caras):
        """funcion que determina el número de dados y sus caras
        y agrega los objetos dado en la lista"""
        for _ in range(num_dados):
            self.dados.append(Dado(num_caras))

    def ronda_de_lanzamiento(self):
        """le pide a cada dado que se lance a sí mismo"""
        valores_obtenidos = {}
        for indice, dado in enumerate(self.dados, start=1):
            valor = dado.lanzamiento()
            valores_obtenidos[f"Dado {indice}"] = valor

        return valores_obtenidos
