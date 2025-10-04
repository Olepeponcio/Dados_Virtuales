"""clase objeto dado"""

from random import Random


class Dado:
    """genera el objeto dado en base al argumento caras
    y rellena la lista con los valores correspondientes"""
    def __init__(self, caras = 6):
        self.caras: int = caras
        self.valor_caras = []
        # agrega los valores a la lista
        for i in range(caras):
            self.valor_caras.append(i+1)

    def __str__(self):
        return f"num_caras: {self.caras}, dado: {self.valor_caras}"


    def lanzamiento(self):
        """escoge un valor aleatorio y devuelve la cara del dado"""
        return self.valor_caras[Random().randint(0, self.caras)]










