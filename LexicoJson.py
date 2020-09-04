import sys
import Errores

class AnalizadorLexicoJson:
    def __init__(self, entrada):
        self.entrada = entrada
        self.index = 0

    def analizarJson(self):
        caracter = ''
        if(len(self.entrada) > 0):
            caracter = self.entrada[self.index]
            print(caracter)
        else:
            print("No hay texto por analizar")