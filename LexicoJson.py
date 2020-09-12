import sys
import Errores


class AnalizadorLexicoJson:
    def __init__(self, entrada, conso):
        self.entrada = entrada
        self.estado = 0
        self.linea = 0
        self.columna = 0
        self.consola = conso

    def analizarJson(self):
        self.linea = 1
        self.columna = 1
        self.estado = 0
        if (len(self.entrada) > 0):
            self.insertText("********** COMENZANDO EL ANALISIS ***********\n")
            self.inicio()
        else:
            self.insertText("Error: No hay texto por analizar\n")

    def inicio(self):
        for indice in range(len(self.entrada)):
            if (self.estado == 0):  # Estado inicial
                print("Entra if de estado")
                print("Caracter: " + str(ord(self.entrada[indice])))
                if (ord(self.entrada[indice]) == 47):
                    print("Entra if de /")
                    ++self.columna
                    self.estado = 1
                elif ((ord(self.entrada[indice]) >= 97 and ord(self.entrada[indice]) <= 122) or (ord(self.entrada[indice]) >= 65 and ord(self.entrada[indice]) <= 90)):
                    ++self.columna
                    self.estado = 5
                elif (ord(self.entrada[indice]) >= 48 and ord(self.entrada[indice]) <= 57):
                    ++self.columna
                    self.estado = 6
                elif (ord(self.entrada[indice]) == 61):
                    ++self.columna
                    self.estado = 9
                elif (ord(self.entrada[indice]) == 34):
                    ++self.columna
                    self.estado = 10
                elif (ord(self.entrada[indice]) == 39):
                    ++self.columna
                    self.estado = 11
                elif (ord(self.entrada[indice]) == 42):
                    ++self.columna
                    self.estado = 12
                elif (ord(self.entrada[indice]) == 43):
                    ++self.columna
                    self.estado = 13
                elif (ord(self.entrada[indice]) == 62):
                    ++self.columna
                    self.estado = 14
                elif (ord(self.entrada[indice]) == 60):
                    ++self.columna
                    self.estado = 15
                elif (ord(self.entrada[indice]) == 33):
                    ++self.columna
                    self.estado = 16
                elif (ord(self.entrada[indice]) == 38):
                    ++self.columna
                    self.estado = 17
                elif (ord(self.entrada[indice]) == 124):
                    ++self.columna
                    self.estado = 18
                elif (ord(self.entrada[indice]) == 59):
                    ++self.columna  # Se reconoce token ;
                    self.insertText("Se reconoce token ;\n")
                elif (ord(self.entrada[indice]) == 40):
                    ++self.columna  # Se reconoce token (
                    self.insertText("Se reconoce token (\n")
                elif (ord(self.entrada[indice]) == 41):
                    ++self.columna  # Se reconoce token )
                    self.insertText("Se reconoce token )\n")
                elif (ord(self.entrada[indice]) == 123):
                    ++self.columna  # Se reconoce token {
                    self.insertText("Se reconoce token {\n")
                elif (ord(self.entrada[indice]) == 125):
                    ++self.columna  # Se reconoce token }
                    self.insertText("Se reconoce token }\n")
                elif (ord(self.entrada[indice]) == 46):
                    ++self.columna  # Se reconoce token .
                    self.insertText("Se reconoce token .\n")
                elif (ord(self.entrada[indice]) == 58):
                    ++self.columna  # Se reconoce token :
                    self.insertText("Se reconoce token :\n")
                elif (ord(self.entrada[indice]) == 44):
                    ++self.columna  # Se reconoce token ,
                    self.insertText("Se reconoce token ,\n")
                elif (self.entrada[indice] == " "):
                    ++self.columna
                elif (self.entrada[indice] == "\t"):
                    self.columna += 4
                elif (ord(self.entrada[indice]) == 13):
                    pass
                elif (self.entrada[indice] == "\n"):
                    ++self.linea
                else:
                    # Se reconoce error
                    self.insertText("Error lexico en la linea: " + str(self.linea) + ", columna: " +
                                    str(self.columna) + ", lexema: " + self.entrada[indice] + "\n")
                    ++self.columna
                    self.entrada.replace(self.entrada[indice], " ", 1)
                    self.estado = 0
            # Estado para reconocer comentarios (unilinea y multilinea) y simbolo division
            elif (self.estado == 1):
                if (ord(self.entrada[indice]) == 47):
                    ++self.columna
                    self.estado = 2
                elif (ord(self.entrada[indice]) == 42):
                    ++self.columna
                    self.estado = 3
                else:  # Se reconoce simbolo de division
                    self.insertText("Se reconoce token /\n")
                    self.estado = 0
                    indice -= 1
            elif (self.estado == 2):  # Estado para comentarios unilinea
                if (self.entrada[indice] == '\n'):
                    self.estado = 0  # Se reconoce el comentario unilinea
                    ++self.linea
                    self.insertText("Se reconoce token COMENTARIO UNILINEA\n")
                ++self.columna
            elif (self.estado == 3):  # Estado para comentario multilinea
                if (ord(self.entrada[indice]) == 42):
                    self.estado = 4
                ++self.columna
            elif (self.estado == 4):
                # Se reconoce el token comentario multilinea
                if (ord(self.entrada[indice]) == 47):
                    self.estado = 0  # Se reconoce el comentario multilinea
                    self.insertText(
                        "Se reconoce token COMENTARIO MULTILINEA\n")
                elif (ord(self.entrada[indice]) != 42):
                    self.estado = 3
                ++self.columna
            elif (self.estado == 5):  # Estado para reconocer palabras reservadas o id's
                if ((ord(self.entrada[indice]) >= 97 and ord(self.entrada[indice]) <= 122)
                    or (ord(self.entrada[indice]) >= 65 and ord(self.entrada[indice]) <= 90)
                    or (ord(self.entrada[indice]) >= 48 and ord(self.entrada[indice]) <= 57)
                        or ord(self.entrada[indice]) == 95):
                    ++self.columna
                else:
                    self.estado = 0  # Se reconoce la palabra reservada o id
                    self.insertText(
                        "Se reconoce token ID o PALABRA RESERVADA\n")
                    indice -= 1
            elif (self.estado == 6):  # Estado para reconocer numeros
                if (ord(self.entrada[indice]) >= 48 and ord(self.entrada[indice]) <= 57):
                    ++self.columna
                elif (ord(self.entrada[indice]) == 46):
                    ++self.columna
                    self.estado = 7
                else:
                    self.estado = 0  # Se reconoce el numero entero
                    self.insertText("Se reconoce token ENTERO\n")
                    indice -= 1
            elif (self.estado == 7):
                if (ord(self.entrada[indice]) >= 48 and ord(self.entrada[indice]) <= 57):
                    ++self.columna
                    self.estado = 8
                else:
                    # Se reconoce un error
                    self.insertText("Error lexico en la linea: " + str(self.linea) + ", columna: " +
                                    str(self.columna) + ", lexema: " + self.entrada[indice] + "\n")
                    self.estado = 0
                    indice -= 1
            elif (self.estado == 8):
                if (ord(self.entrada[indice]) >= 48 and ord(self.entrada[indice]) <= 57):
                    ++self.columna
                else:
                    self.estado = 0  # Se reconoce el numero decimal
                    self.insertText("Se reconoce token DECIMAL\n")
                    indice -= 1
            elif (self.estado == 9):  # Estado para reconocer simbolo igual o comparacion igual
                self.estado = 0
                if (ord(self.entrada[indice]) == 61):
                    self.insertText("Se reconoce token ==\n")
                    ++self.columna  # Se reconoce token comparacion
                elif (ord(self.entrada[indice]) == 62):
                    self.insertText("Se reconoce token =>\n")
                    ++self.columna  # Se reconoce token =>
                else:
                    self.insertText("Se reconoce token =\n")
                    indice -= 1  # Se reconoce token igual
            elif (self.estado == 10):
                if (ord(self.entrada[indice]) == '\n'):
                    # Se reconoce un error
                    self.insertText("Error lexico en la linea: " + str(self.linea) + ", columna: " +
                                    str(self.columna) + ", lexema: " + self.entrada[indice] + "\n")
                    self.estado = 0
                    indice -= 1
                elif (ord(self.entrada[indice]) == 34):
                    self.estado = 0  # Se reconoce cadena con doble comilla
                    self.insertText("Se reconoce token string\n")
                ++self.columna
            elif (self.estado == 11):
                if (ord(self.entrada[indice]) == '\n'):
                    # Se reconoce un error
                    self.insertText("Error lexico en la linea: " + str(self.linea) + ", columna: " +
                                    str(self.columna) + ", lexema: " + self.entrada[indice] + "\n")
                    self.estado = 0
                    indice -= 1
                elif (ord(self.entrada[indice]) == 39):
                    self.estado = 0  # Se reconoce cadena con doble comilla
                    self.insertText("Se reconoce token string\n")
                ++self.columna
            elif (self.estado == 12):
                self.estado = 0
                if (ord(self.entrada[indice]) == 61):
                    self.insertText("Se reconoce token *=\n")
                    ++self.columna  # Se reconoce token *=
                else:
                    self.insertText("Se reconoce token *\n")
                    indice -= 1  # Se reconoce token *
            elif (self.estado == 13):
                self.estado = 0
                if (ord(self.entrada[indice]) == 43):
                    self.insertText("Se reconoce token ++\n")
                    ++self.columna  # Se reconoce token ++
                elif (ord(self.entrada[indice]) == 61):
                    self.insertText("Se reconoce token +=\n")
                    ++self.columna  # Se reconoce token +=
                else:
                    self.insertText("Se reconoce token +\n")
                    indice -= 1  # Se reconoce token +
            elif (self.estado == 14):
                self.estado = 0
                if (ord(self.entrada[indice]) == 61):
                    self.insertText("Se reconoce token >=\n")
                    ++self.columna  # Se reconoce token >=
                else:
                    self.insertText("Se reconoce token >\n")
                    indice -= 1  # Se reconoce token >
            elif (self.estado == 15):
                self.estado = 0
                if (ord(self.entrada[indice]) == 61):
                    self.insertText("Se reconoce token <=\n")
                    ++self.columna  # Se reconoce token <=
                else:
                    self.insertText("Se reconoce token <\n")
                    indice -= 1  # Se reconoce token <
            elif (self.estado == 16):
                self.estado = 0
                if (ord(self.entrada[indice]) == 61):
                    self.insertText("Se reconoce token !=\n")
                    ++self.columna  # Se reconoce token !=
                else:
                    self.insertText("Se reconoce token !\n")
                    indice -= 1  # Se reconoce token !
            elif (self.estado == 17):
                if (ord(self.entrada[indice]) == 38):
                    self.insertText("Se reconoce token &&\n")
                    ++self.columna
                    self.estado = 0  # Se reconoce token &&
                else:
                    # Se reconoce error
                    self.insertText("Error lexico en la linea: " + str(self.linea) + ", columna: " +
                                    str(self.columna) + ", lexema: " + self.entrada[indice] + "\n")
                    self.estado = 0
                    indice -= 1
            elif (self.estado == 124):
                if (ord(self.entrada[indice]) == 124):
                    self.insertText("Se reconoce token ||\n")
                    ++self.columna
                    self.estado = 0  # Se reconoce token ||
                else:
                    # Se reconoce error
                    self.insertText("Error lexico en la linea: " + str(self.linea) + ", columna: " +
                                    str(self.columna) + ", lexema: " + self.entrada[indice] + "\n")
                    self.estado = 0
                    indice -= 1

    def insertText(self, texto):
        self.consola.insertPlainText(texto)
