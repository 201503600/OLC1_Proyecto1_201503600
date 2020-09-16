import sys
import Errores
from LexicoAritmetica import AnalizadorLexicoAritmetica


class AnalizadorSintactico:
    def __init__(self, consola):
        self.numPreAnalisis = 0
        self.preAnalisis = {}
        self.tokens = []
        self.entrada = ""
        self.consola = consola
        self.error = False
    # END

    def parser(self, entrada):
        #print("entrada: " + entrada + " longitud:" + str(len(entrada)))
        if (len(entrada) > 0):
            lexico = AnalizadorLexicoAritmetica(entrada, self.consola)
            self.tokens = lexico.scanner()
            self.numPreAnalisis = 0
            self.preAnalisis = self.tokens[0]
            self.error = False
            self.E()
        else:
            self.consola.insertPlainText("Error: No hay texto para analizar\n")
        return self.error
    # END

    def E(self):
        self.T()
        self.EP()
    # END

    def EP(self):
        if (self.preAnalisis["tipo"] == "mas"):
            self.match("mas")
            self.T()
            self.EP()
        elif (self.preAnalisis["tipo"] == "menos"):
            self.match("menos")
            self.T()
            self.EP()
    # END

    def T(self):
        self.F()
        self.TP()
    # END

    def TP(self):
        if (self.preAnalisis["tipo"] == "multiplicacion"):
            self.match("multiplicacion")
            self.F()
            self.TP()
        elif (self.preAnalisis["tipo"] == "division"):
            self.match("division")
            self.F()
            self.TP()
    # END

    def F(self):
        if (self.preAnalisis["tipo"] == "para"):
            self.match("para")
            self.E()
            self.match("parc")
        elif (self.preAnalisis["tipo"] == "numero"):
            self.match("numero")
        else:
            self.match("menos")
            self.match("numero")
    # END

    def match(self, tipo):
        if (tipo != self.preAnalisis["tipo"]):
            self.error = True

        if (self.preAnalisis["tipo"] != "end"):
            self.numPreAnalisis += 1
            self.preAnalisis = self.tokens[self.numPreAnalisis]
    # END
