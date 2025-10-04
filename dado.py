"""clase objeto dado"""

class Dado:
    def __init__(self, caras):
        self.caras: int = caras
        self.valor_caras = []

        for i in range(caras):
            self.valor_caras.append(i+1)

    def __str__(self):
        return f"num_caras: {self.caras}, dado: {self.valor_caras}"








if __name__ == "__main__":

    dado = Dado(6)
    print(dado)



