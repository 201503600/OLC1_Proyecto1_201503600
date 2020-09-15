import sys
import Errores


class AnalizadorLexicoAritmetica:
    def __init__(self, entrada, conso):
        self.entrada = entrada + " "
        self.estado = 0
        self.linea = 0
        self.columna = 0
        self.consola = conso
        self.tokens = []

    # END

    def scanner(self):
        self.linea = 1
        self.columna = 0
        self.estado = 0
        self.consola.clear()
        self.tokens.clear()
        Errores.error.clear()
        # self.consola.insertPlainText(
        #    "***********************************\n  COMENZANDO ANALISIS LEXICO\n***********************************\n")
        self.inicio()
        # self.consola.insertPlainText(
        #    "***********************************\n  FINALIZO ANALISIS LEXICO\n***********************************\n")
        self.tokens.append({"tipo": "end", "valor": ""})
        return self.tokens
    # END

    def inicio(self):
        cadena = ""
        indice = 0
        while True:
            if (self.estado == 0):
                cadena += self.entrada[indice]
                self.columna += 1
                if ((ord(self.entrada[indice]) >= 97 and ord(self.entrada[indice]) <= 122) or (ord(self.entrada[indice]) >= 65 and ord(self.entrada[indice]) <= 90)):
                    self.estado = 1
                elif (ord(self.entrada[indice]) >= 48 and ord(self.entrada[indice]) <= 57):
                    self.estado = 2
                elif (ord(self.entrada[indice]) == 40):
                    self.tokens.append({"tipo": "para", "valor": ""})
                elif (ord(self.entrada[indice]) == 41):
                    self.tokens.append({"tipo": "parc", "valor": ""})
                elif (ord(self.entrada[indice]) == 43):
                    self.tokens.append({"tipo": "mas", "valor": ""})
                elif (ord(self.entrada[indice]) == 45):
                    self.tokens.append({"tipo": "menos", "valor": ""})
                elif (ord(self.entrada[indice]) == 42):
                    self.tokens.append({"tipo": "multiplicacion", "valor": ""})
                elif (ord(self.entrada[indice]) == 47):
                    self.tokens.append({"tipo": "division", "valor": ""})
                elif (self.entrada[indice] == " " or ord(self.entrada[indice]) == 13):
                    pass
                elif (self.entrada[indice] == "\t"):
                    self.columna += 3
                elif (self.entrada[indice] == "\n"):
                    self.linea += 1
                    self.columna = 0
                    #self.tokens.append({"tipo": "finOp", "valor": "end"})
                    cadena = ""
                else:
                    # Se reconoce error
                    self.consola.insertPlainText("Error lexico en la linea: " + str(self.linea) + ", columna: " +
                                                 str(self.columna) + ", lexema: " + self.entrada[indice] + "\n")
                    Errores.error.append(
                        {"tipo": "lexico", "lexema": self.entrada[indice], "linea": self.linea, "columna": self.columna})
                    self.tokens.append({"tipo": "error", "valor": ""})
            elif (self.estado == 1):
                self.columna += 1
                if ((ord(self.entrada[indice]) >= 97 and ord(self.entrada[indice]) <= 122) or (ord(self.entrada[indice]) >= 65 and ord(self.entrada[indice]) <= 90) or (ord(self.entrada[indice]) >= 48 and ord(self.entrada[indice]) <= 57) or ord(self.entrada[indice]) == 95):
                    cadena += self.entrada[indice]
                else:
                    indice -= 1
                    self.columna -= 1
                    self.estado = 0
            elif (self.estado == 2):
                self.columna += 1
                if (ord(self.entrada[indice]) >= 48 and ord(self.entrada[indice]) <= 57):
                    cadena += self.entrada[indice]
                elif (ord(self.entrada[indice]) == 46):
                    cadena += self.entrada[indice]
                    self.estado = 3
                else:
                    indice -= 1
                    self.columna -= 1
                    self.tokens.append({"tipo": "numero", "valor": cadena})
                    self.estado = 0
            elif (self.estado == 3):
                if (ord(self.entrada[indice]) >= 48 and ord(self.entrada[indice]) <= 57):
                    self.columna += 1
                    cadena += self.entrada[indice]
                    self.estado = 4
                else:
                    # Se reconoce error
                    indice -= 1
                    self.estado = 0
                    self.consola.insertPlainText("Error lexico en la linea: " + str(self.linea) + ", columna: " +
                                                 str(self.columna) + ", lexema: " + cadena + "\n")
                    Errores.error.append(
                        {"tipo": "lexico", "lexema": self.entrada[indice], "linea": self.linea, "columna": self.columna})
                    self.tokens.append({"tipo": "error", "valor": ""})
            elif (self.estado == 4):
                if (ord(self.entrada[indice]) >= 48 and ord(self.entrada[indice]) <= 57):
                    cadena += self.entrada[indice]
                    self.columna += 1
                else:
                    indice -= 1
                    self.estado = 0
                    self.tokens.append({"tipo": "numero", "valor": cadena})

            indice += 1
            if (indice >= len(self.entrada)):
                break
    # END

    def getError(self):
        return Errores.error
    # END
