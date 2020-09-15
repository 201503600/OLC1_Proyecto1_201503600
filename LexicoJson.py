import sys
import os
import Errores
from graphviz import Digraph


class AnalizadorLexicoJson:
    def __init__(self, entrada, conso, name):
        self.entrada = entrada
        self.estado = 0
        self.linea = 0
        self.columna = 0
        self.consola = conso
        self.nombre = name
        self.ids = {}
    # END

    def analizarJson(self):
        self.linea = 1
        self.columna = 0
        self.estado = 0
        self.consola.clear()
        Errores.error.clear()
        if (len(self.entrada) > 0):
            self.insertText(
                "*************************************\n\tCOMENZANDO EL ANALISIS\n*************************************\n")
            self.inicio()
            self.insertText(
                "*************************************\n\tFINALIZO EL ANALISIS\n*************************************\n")
        else:
            self.insertText("Error: No hay texto por analizar\n")
    # END

    def inicio(self):
        cadena = ""
        for indice in range(len(self.entrada)):
            if (self.estado == 0):  # Estado inicial
                if (ord(self.entrada[indice]) == 47):
                    cadena += self.entrada[indice]
                    self.columna += 1
                    self.estado = 1
                elif ((ord(self.entrada[indice]) >= 97 and ord(self.entrada[indice]) <= 122) or (ord(self.entrada[indice]) >= 65 and ord(self.entrada[indice]) <= 90)):
                    cadena += self.entrada[indice]
                    self.columna += 1
                    self.estado = 5
                elif (ord(self.entrada[indice]) >= 48 and ord(self.entrada[indice]) <= 57):
                    cadena += self.entrada[indice]
                    self.columna += 1
                    self.estado = 6
                elif (ord(self.entrada[indice]) == 61):
                    self.columna += 1
                    self.estado = 9
                elif (ord(self.entrada[indice]) == 34):
                    cadena += self.entrada[indice]
                    self.columna += 1
                    self.estado = 10
                elif (ord(self.entrada[indice]) == 39):
                    cadena += self.entrada[indice]
                    self.columna += 1
                    self.estado = 11
                elif (ord(self.entrada[indice]) == 42):
                    self.columna += 1
                    self.estado = 12
                elif (ord(self.entrada[indice]) == 43):
                    self.columna += 1
                    self.estado = 13
                elif (ord(self.entrada[indice]) == 62):
                    self.columna += 1
                    self.estado = 14
                elif (ord(self.entrada[indice]) == 60):
                    self.columna += 1
                    self.estado = 15
                elif (ord(self.entrada[indice]) == 33):
                    self.columna += 1
                    self.estado = 16
                elif (ord(self.entrada[indice]) == 38):
                    cadena += self.entrada[indice]
                    self.columna += 1
                    self.estado = 17
                elif (ord(self.entrada[indice]) == 124):
                    cadena += self.entrada[indice]
                    self.columna += 1
                    self.estado = 18
                elif (ord(self.entrada[indice]) == 59):
                    self.columna += 1  # Se reconoce token ;
                    #self.insertText("Se reconoce token ;\n")
                elif (ord(self.entrada[indice]) == 40):
                    self.columna += 1  # Se reconoce token (
                    #self.insertText("Se reconoce token (\n")
                elif (ord(self.entrada[indice]) == 41):
                    self.columna += 1  # Se reconoce token )
                    #self.insertText("Se reconoce token )\n")
                elif (ord(self.entrada[indice]) == 123):
                    self.columna += 1  # Se reconoce token {
                    #self.insertText("Se reconoce token {\n")
                elif (ord(self.entrada[indice]) == 125):
                    self.columna += 1  # Se reconoce token }
                    #self.insertText("Se reconoce token }\n")
                elif (ord(self.entrada[indice]) == 46):
                    self.columna += 1  # Se reconoce token .
                    #self.insertText("Se reconoce token .\n")
                elif (ord(self.entrada[indice]) == 58):
                    self.columna += 1  # Se reconoce token :
                    #self.insertText("Se reconoce token :\n")
                elif (ord(self.entrada[indice]) == 44):
                    self.columna += 1  # Se reconoce token ,
                    #self.insertText("Se reconoce token ,\n")
                elif (self.entrada[indice] == " "):
                    self.columna += 1
                elif (self.entrada[indice] == "\t"):
                    self.columna += 4
                elif (ord(self.entrada[indice]) == 13):
                    pass
                elif (self.entrada[indice] == "\n"):
                    self.linea += 1
                    self.columna = 0
                else:
                    # Se reconoce error
                    self.insertText("Error lexico en la linea: " + str(self.linea) + ", columna: " +
                                    str(self.columna) + ", lexema: " + self.entrada[indice] + "\n")
                    Errores.error.append(
                        {"tipo": "lexico", "lexema": self.entrada[indice], "linea": self.linea, "columna": self.columna})
                    self.columna += 1
                    self.entrada.replace(self.entrada[indice], " ", 1)
                    self.estado = 0
            # Estado para reconocer comentarios (unilinea y multilinea) y simbolo division
            elif (self.estado == 1):
                if (ord(self.entrada[indice]) == 47):
                    self.columna += 1
                    self.estado = 2
                elif (ord(self.entrada[indice]) == 42):
                    cadena += self.entrada[indice]
                    self.columna += 1
                    self.estado = 3
                else:  # Se reconoce simbolo de division
                    #self.insertText("Se reconoce token /\n")
                    cadena = ""
                    self.estado = 0
                    indice -= 1
            elif (self.estado == 2):  # Estado para comentarios unilinea
                cadena += self.entrada[indice]
                self.columna += 1
                if (self.entrada[indice] == '\n'):
                    self.estado = 0  # Se reconoce el comentario unilinea
                    self.linea += 1
                    self.columna = 0
                    cadena = ""
                    self.agregarExpresion("CommenInline", "//P*S")
                    #self.insertText("Se reconoce token COMENTARIO UNILINEA\n")
            elif (self.estado == 3):  # Estado para comentario multilinea
                cadena += self.entrada[indice]
                if (ord(self.entrada[indice]) == 42):
                    self.estado = 4
                self.columna += 1
            elif (self.estado == 4):
                # Se reconoce el token comentario multilinea
                cadena += self.entrada[indice]
                self.columna += 1
                if (ord(self.entrada[indice]) == 47):
                    self.estado = 0  # Se reconoce el comentario multilinea
                    cadena = ""
                    self.agregarExpresion("CommenMultiline", "/\*.*\*/")
                    #self.insertText("Se reconoce token COMENTARIO MULTILINEA\n")
                elif (ord(self.entrada[indice]) != 42):
                    if (ord(self.entrada[indice]) == 10):
                        self.linea += 1
                        self.columna = 0
                    self.estado = 3
            elif (self.estado == 5):  # Estado para reconocer palabras reservadas o id's
                cadena += self.entrada[indice]
                if ((ord(self.entrada[indice]) >= 97 and ord(self.entrada[indice]) <= 122)
                    or (ord(self.entrada[indice]) >= 65 and ord(self.entrada[indice]) <= 90)
                    or (ord(self.entrada[indice]) >= 48 and ord(self.entrada[indice]) <= 57)
                        or ord(self.entrada[indice]) == 95):
                    self.columna += 1
                else:
                    self.estado = 0  # Se reconoce la palabra reservada o id
                    cadena = ""
                    self.agregarExpresion("Id", "L(L|N|_)*")
                    #self.insertText("Se reconoce token ID o PALABRA RESERVADA\n")
                    indice -= 1
            elif (self.estado == 6):  # Estado para reconocer numeros
                cadena += self.entrada[indice]
                if (ord(self.entrada[indice]) >= 48 and ord(self.entrada[indice]) <= 57):
                    self.columna += 1
                elif (ord(self.entrada[indice]) == 46):
                    self.columna += 1
                    self.estado = 7
                else:
                    self.estado = 0  # Se reconoce el numero entero
                    cadena = ""
                    self.agregarExpresion("Entero", "D+")
                    #self.insertText("Se reconoce token ENTERO\n")
                    indice -= 1
            elif (self.estado == 7):
                if (ord(self.entrada[indice]) >= 48 and ord(self.entrada[indice]) <= 57):
                    cadena += self.entrada[indice]
                    self.columna += 1
                    self.estado = 8
                else:
                    # Se reconoce un error
                    self.insertText("Error lexico en la linea: " + str(self.linea) + ", columna: " +
                                    str(self.columna) + ", lexema: " + cadena + "\n")
                    Errores.error.append(
                        {"tipo": "lexico", "lexema": cadena, "linea": self.linea, "columna": self.columna})
                    cadena = ""
                    self.entrada = self.entrada[:indice] + \
                        "0" + self.entrada[indice:]
                    self.estado = 0
                    #indice -= 1
            elif (self.estado == 8):
                if (ord(self.entrada[indice]) >= 48 and ord(self.entrada[indice]) <= 57):
                    cadena += self.entrada[indice]
                    self.columna += 1
                else:
                    self.estado = 0  # Se reconoce el numero decimal
                    cadena = ""
                    self.agregarExpresion("Decimal", "D+\.D+")
                    #self.insertText("Se reconoce token DECIMAL\n")
                    indice -= 1
            elif (self.estado == 9):  # Estado para reconocer simbolo igual o comparacion igual
                self.estado = 0
                if (ord(self.entrada[indice]) == 61):
                    #self.insertText("Se reconoce token ==\n")
                    self.columna += 1  # Se reconoce token comparacion
                elif (ord(self.entrada[indice]) == 62):
                    #self.insertText("Se reconoce token =>\n")
                    self.columna += 1  # Se reconoce token =>
                else:
                    #self.insertText("Se reconoce token =\n")
                    indice -= 1  # Se reconoce token igual
            elif (self.estado == 10):
                cadena += self.entrada[indice]
                if (ord(self.entrada[indice]) == '\n'):
                    # Se reconoce un error
                    self.insertText("Error lexico en la linea: " + str(self.linea) + ", columna: " +
                                    str(self.columna) + ", lexema: " + cadena + "\n")
                    Errores.error.append(
                        {"tipo": "lexico", "lexema": cadena, "linea": self.linea, "columna": self.columna})
                    cadena = ""
                    self.entrada = self.entrada[:indice] + \
                        "\"" + self.entrada[indice:]
                    self.estado = 0
                    #indice -= 1
                elif (ord(self.entrada[indice]) == 34):
                    self.estado = 0  # Se reconoce cadena con doble comilla
                    cadena = ""
                    self.agregarExpresion("String", "\"[^\n\r]*\"")
                    #self.insertText("Se reconoce token string\n")
                self.columna += 1
            elif (self.estado == 11):
                cadena += self.entrada[indice]
                if (ord(self.entrada[indice]) == '\n'):
                    # Se reconoce un error
                    self.insertText("Error lexico en la linea: " + str(self.linea) + ", columna: " +
                                    str(self.columna) + ", lexema: " + cadena + "\n")
                    Errores.error.append(
                        {"tipo": "lexico", "lexema": cadena, "linea": self.linea, "columna": self.columna})
                    self.entrada = self.entrada[:indice] + \
                        "'" + self.entrada[indice:]
                    cadena = ""
                    self.estado = 0
                    #indice -= 1
                elif (ord(self.entrada[indice]) == 39):
                    self.estado = 0  # Se reconoce cadena con comilla simple
                    cadena = ""
                    self.agregarExpresion("Caracter", "'[^\n\r]*'")
                    #self.insertText("Se reconoce token string\n")
                self.columna += 1
            elif (self.estado == 12):
                self.estado = 0
                if (ord(self.entrada[indice]) == 61):
                    #self.insertText("Se reconoce token *=\n")
                    self.columna += 1  # Se reconoce token *=
                else:
                    #self.insertText("Se reconoce token *\n")
                    indice -= 1  # Se reconoce token *
            elif (self.estado == 13):
                self.estado = 0
                if (ord(self.entrada[indice]) == 43):
                    #self.insertText("Se reconoce token ++\n")
                    self.columna += 1  # Se reconoce token ++
                elif (ord(self.entrada[indice]) == 61):
                    #self.insertText("Se reconoce token +=\n")
                    self.columna += 1  # Se reconoce token +=
                else:
                    #self.insertText("Se reconoce token +\n")
                    indice -= 1  # Se reconoce token +
            elif (self.estado == 14):
                self.estado = 0
                if (ord(self.entrada[indice]) == 61):
                    #self.insertText("Se reconoce token >=\n")
                    self.columna += 1  # Se reconoce token >=
                else:
                    #self.insertText("Se reconoce token >\n")
                    indice -= 1  # Se reconoce token >
            elif (self.estado == 15):
                self.estado = 0
                if (ord(self.entrada[indice]) == 61):
                    #self.insertText("Se reconoce token <=\n")
                    self.columna += 1  # Se reconoce token <=
                else:
                    #self.insertText("Se reconoce token <\n")
                    indice -= 1  # Se reconoce token <
            elif (self.estado == 16):
                self.estado = 0
                if (ord(self.entrada[indice]) == 61):
                    #self.insertText("Se reconoce token !=\n")
                    self.columna += 1  # Se reconoce token !=
                else:
                    #self.insertText("Se reconoce token !\n")
                    indice -= 1  # Se reconoce token !
            elif (self.estado == 17):
                if (ord(self.entrada[indice]) == 38):
                    #self.insertText("Se reconoce token &&\n")
                    self.columna += 1
                    self.estado = 0  # Se reconoce token &&
                else:
                    # Se reconoce error
                    self.insertText("Error lexico en la linea: " + str(self.linea) + ", columna: " +
                                    str(self.columna) + ", lexema: " + cadena + "\n")
                    Errores.error.append(
                        {"tipo": "lexico", "lexema": cadena, "linea": self.linea, "columna": self.columna})
                    self.entrada = self.entrada[:indice] + \
                        "&" + self.entrada[indice:]
                    self.estado = 0
                    #indice -= 1
                cadena = ""
            elif (self.estado == 18):
                if (ord(self.entrada[indice]) == 124):
                    #self.insertText("Se reconoce token ||\n")
                    self.columna += 1
                    self.estado = 0  # Se reconoce token ||
                else:
                    # Se reconoce error
                    self.insertText("Error lexico en la linea: " + str(self.linea) + ", columna: " +
                                    str(self.columna) + ", lexema: " + cadena + "\n")
                    Errores.error.append(
                        {"tipo": "lexico", "lexema": cadena, "linea": self.linea, "columna": self.columna})
                    self.entrada = self.entrada[:indice] + \
                        "|" + self.entrada[indice:]
                    self.estado = 0
                    #indice -= 1
                cadena = ""
        if (len(Errores.error) > 0):
            # Generar reporte de errores
            self.repError()
            self.ids.clear()
            self.insertText(
                "Error: El analisis finalizo con uno o varios errores\n")
            return False
        else:
            # Generar automata
            self.grafo()
            self.generarDirectorio()
            return True
    # END

    def getEntrada(self):
        return self.entrada
    # END

    def insertText(self, texto):
        self.consola.insertPlainText(texto)
    # END

    def agregarExpresion(self, llave, expresion):
        bandera = True
        for key in self.ids:
            if (key == llave):
                bandera = False
                break

        if (bandera):
            self.ids[llave] = expresion
    # END

    def grafo(self):
        dot = Digraph(comment='Grafica de Estados')
        dot.attr('node', shape='circle')
        nodo = 0
        dot.node("S0", "S0")
        for ex in self.ids:
            if (ex == "CommenInline"):
                dot.node("S" + str(nodo + 1), "S" + str(nodo + 1))
                dot.node("S" + str(nodo + 2), "S" + str(nodo + 2))
                dot.node("S" + str(nodo + 2), shape='doublecircle')
                dot.node("S" + str(nodo + 3), "S" + str(nodo + 3))
                dot.node("S" + str(nodo + 3), shape='doublecircle')
                dot.edge("S0", "S" + str(nodo + 1), label="/")
                dot.edge("S" + str(nodo + 1), "S" + str(nodo + 2), label="/")
                dot.edge("S" + str(nodo + 2), "S" + str(nodo + 2), label=".")
                dot.edge("S" + str(nodo + 2), "S" + str(nodo + 3), label="\\n")
                nodo += 3
            elif (ex == "CommenMultiline"):
                dot.node("S" + str(nodo + 1), "S" + str(nodo + 1))
                dot.node("S" + str(nodo + 2), "S" + str(nodo + 2))
                dot.node("S" + str(nodo + 3), "S" + str(nodo + 3))
                dot.node("S" + str(nodo + 4), "S" + str(nodo + 4))
                dot.node("S" + str(nodo + 4), shape='doublecircle')
                dot.edge("S0", "S" + str(nodo + 1), label="/")
                dot.edge("S" + str(nodo + 1), "S" + str(nodo + 2), label="*")
                dot.edge("S" + str(nodo + 2), "S" + str(nodo + 2), label=".")
                dot.edge("S" + str(nodo + 2), "S" + str(nodo + 3), label="*")
                dot.edge("S" + str(nodo + 3), "S" + str(nodo + 4), label="/")
                nodo += 4
            elif (ex == "Id"):
                dot.node("S" + str(nodo + 1), "S" + str(nodo + 1))
                dot.node("S" + str(nodo + 1), shape='doublecircle')
                dot.edge("S0", "S" + str(nodo + 1), label="L")
                dot.edge("S" + str(nodo + 1), "S" + str(nodo + 1), label="L")
                dot.edge("S" + str(nodo + 1), "S" + str(nodo + 1), label="N")
                dot.edge("S" + str(nodo + 1), "S" + str(nodo + 1), label="_")
                nodo += 1
            elif (ex == "Entero"):
                dot.node("S" + str(nodo + 1), "S" + str(nodo + 1))
                dot.node("S" + str(nodo + 1), shape='doublecircle')
                dot.edge("S0", "S" + str(nodo + 1), label="D")
                dot.edge("S" + str(nodo + 1), "S" + str(nodo + 1), label="D")
                nodo += 1
            elif (ex == "Decimal"):
                dot.node("S" + str(nodo + 1), "S" + str(nodo + 1))
                dot.node("S" + str(nodo + 2), "S" + str(nodo + 2))
                dot.node("S" + str(nodo + 3), "S" + str(nodo + 3))
                dot.node("S" + str(nodo + 3), shape='doublecircle')
                dot.edge("S0", "S" + str(nodo + 1), label="D")
                dot.edge("S" + str(nodo + 1), "S" + str(nodo + 1), label="D")
                dot.edge("S" + str(nodo + 1), "S" + str(nodo + 2), label=".")
                dot.edge("S" + str(nodo + 2), "S" + str(nodo + 3), label="D")
                dot.edge("S" + str(nodo + 3), "S" + str(nodo + 3), label="D")
                nodo += 3
            elif (ex == "String"):
                dot.node("S" + str(nodo + 1), "S" + str(nodo + 1))
                dot.node("S" + str(nodo + 2), "S" + str(nodo + 2))
                dot.node("S" + str(nodo + 2), shape='doublecircle')
                dot.edge("S0", "S" + str(nodo + 1), label="\"")
                dot.edge("S" + str(nodo + 1), "S" + str(nodo + 1), label=".")
                dot.edge("S" + str(nodo + 1), "S" + str(nodo + 2), label="\"")
                nodo += 2
            elif (ex == "Caracter"):
                dot.node("S" + str(nodo + 1), "S" + str(nodo + 1))
                dot.node("S" + str(nodo + 2), "S" + str(nodo + 2))
                dot.node("S" + str(nodo + 2), shape='doublecircle')
                dot.edge("S0", "S" + str(nodo + 1), label="'")
                dot.edge("S" + str(nodo + 1), "S" + str(nodo + 1), label=".")
                dot.edge("S" + str(nodo + 1), "S" + str(nodo + 2), label="'")

        dot.render('/home/daniel/Desktop/Reportes/ReporteJson', view=False)
        print("Grafo Generado")
    # END

    def repError(self):
        cadena = '''<!doctype html>
        <html>
            <head>
                <!-- Required meta tags -->
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                <title>Reporte de Error</title>

                <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
                <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.6.3/css/all.css" integrity="sha384-UHRtZLI+pbxtHCWp1t77Bi1L4ZtiqrqD80Kn4Z8NTSRyMA2Fd33n5dQ8lWUE00s/" crossorigin="anonymous">
                <link rel="stylesheet" href="https://unpkg.com/bootstrap-table@1.17.1/dist/bootstrap-table.min.css">
            </head>
            <body>
                <div>
                    <h1>Reporte de errores léxicos JavaScript</h1>
                    <table class="table">
                    <thead>
                        <tr>
                        <th scope="col">No</th>
                        <th scope="col">Linea</th>
                        <th scope="col">Columna</th>
                        <th scope="col">Error</th>
                        </tr>
                    </thead>
                    <tbody>'''

        contador = 1
        for e in Errores.error:
            cadena += '<tr><th scope="row">' + str(contador) + \
                '</th><td>' + str(e["linea"]) + '</td><td>' + \
                str(e["columna"]) + '</td><td>' + e["lexema"] + '</td></tr>'
            contador += 1

        cadena += '''</tbody>
                        </table>
                    </div><script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.1/jquery.min.js" integrity="sha512-bLT0Qm9VnAYZDflyKcBaQ2gg0hSYNQrJ8RilYldYQ1FxQYoCLtUjuuRuZo+fjqhx/qtq/1itJ0C2ejDxltZVFg==" crossorigin="anonymous"></script>
                                <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
                                <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
                                <script src="https://unpkg.com/bootstrap-table@1.17.1/dist/bootstrap-table.min.js"></script>
                            </body>
                        </html>'''
        file = open("/home/daniel/Desktop/Reportes/errores.html", "w+")
        file.write(cadena)
        file.close()
    # END

    def generarDirectorio(self):
        ruta = ""
        linea = self.entrada.split("\n")
        for line in linea:
            if (len(line.split("PATHL:")) > 1):
                ruta = "/home/daniel/Desktop/output" + line.split("output")[1]
                break

        if (ruta != ""):
            os.makedirs(ruta, exist_ok=True)
            ruta += "/" + self.nombre
            file = open(ruta, "w+")
            file.write(self.entrada)
            file.close()
    # END
