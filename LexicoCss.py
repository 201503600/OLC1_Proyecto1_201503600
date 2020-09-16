import sys
import os
import Errores


class AnalizadorLexicoCss:
    def __init__(self, entrada, conso, name):
        self.entrada = entrada
        self.estado = 0
        self.linea = 0
        self.columna = 0
        self.consola = conso
        self.nombre = name
        self.ids = ["color", "background-color", "background-image", "border", "opacity", "background", "text-align", "font-family", "font-style", "font-weight", "font-size", "font", "padding-left", "padding-right", "padding-bottom", "padding-top", "padding", "display",
                    "line-height", "width", "height", "margin-top", "margin-right", "margin-bottom", "margin-left", "margin", "border-style", "display", "position", "bottom", "top", "right", "left", "float", "clear", "max-width", "min-width", "max-height", "min-height"]
    # END

    def analizarCss(self):
        self.linea = 1
        self.columna = 0
        self.estado = 0
        self.consola.clear()
        Errores.error.clear()
        if (len(self.entrada) > 0):
            self.insertText(
                "***********************************\n\tCOMENZANDO EL ANALISIS\n***********************************\n")
            self.inicio()
            self.insertText(
                "***********************************\n\tFINALIZO EL ANALISIS\n***********************************\n")
        else:
            self.insertText("Error: No hay texto por analizar\n")
    # END

    def inicio(self):
        cadena = ""
        indice = 0
        # for indice in range(len(self.entrada)):
        while True:
            if (self.estado == 0):  # Estado inicial
                if (ord(self.entrada[indice]) == 47):
                    cadena += self.entrada[indice]
                    self.columna += 1
                    self.estado = 1
                    self.insertText("S0 -> S1: caracter /\n")
                elif ((ord(self.entrada[indice]) >= 97 and ord(self.entrada[indice]) <= 122) or (ord(self.entrada[indice]) >= 65 and ord(self.entrada[indice]) <= 90)):
                    cadena += self.entrada[indice]
                    self.columna += 1
                    self.estado = 5
                    self.insertText("S0 -> S5: caracter " +
                                    self.entrada[indice] + "\n")
                elif (ord(self.entrada[indice]) >= 48 and ord(self.entrada[indice]) <= 57):
                    cadena += self.entrada[indice]
                    self.columna += 1
                    self.estado = 6
                    self.insertText("S0 -> S6: caracter " +
                                    self.entrada[indice] + "\n")
                elif (ord(self.entrada[indice]) == 45):
                    self.columna += 1
                    self.estado = 9
                    self.insertText("S0 -> S9: caracter -\n")
                elif (ord(self.entrada[indice]) == 34):
                    cadena += self.entrada[indice]
                    self.columna += 1
                    self.estado = 10
                    self.insertText("S0 -> S10: caracter \"\n")
                elif (ord(self.entrada[indice]) == 42):
                    self.columna += 1
                    self.insertText("S0 -> S0: Se reconocio token ASTERISCO\n")
                elif (ord(self.entrada[indice]) == 40):
                    self.columna += 1
                    self.insertText("S0 -> S0: Se reconocio token PARA\n")
                elif (ord(self.entrada[indice]) == 41):
                    self.columna += 1
                    self.insertText("S0 -> S0: Se reconocio token PARC\n")
                elif (ord(self.entrada[indice]) == 59):
                    self.columna += 1  # Se reconoce token ;
                    self.insertText(
                        "S0 -> S0: Se reconocio token PUNTO_COMA\n")
                elif (ord(self.entrada[indice]) == 35):
                    self.columna += 1  # Se reconoce token #
                    self.insertText("S0 -> S0: Se reconocio token NUMERAL\n")
                elif (ord(self.entrada[indice]) == 37):
                    self.columna += 1  # Se reconoce token %
                    self.insertText(
                        "S0 -> S0: Se reconocio token PORCENTAJE\n")
                elif (ord(self.entrada[indice]) == 123):
                    self.columna += 1  # Se reconoce token {
                    self.insertText("S0 -> S0: Se reconocio token LLAVEC\n")
                elif (ord(self.entrada[indice]) == 125):
                    self.columna += 1  # Se reconoce token }
                    self.insertText("S0 -> S0: Se reconocio token LLAVEA\n")
                elif (ord(self.entrada[indice]) == 46):
                    self.columna += 1  # Se reconoce token .
                    self.insertText("S0 -> S0: Se reconocio token PUNTO\n")
                elif (ord(self.entrada[indice]) == 58):
                    self.columna += 1  # Se reconoce token :
                    self.insertText("S0 -> S0: Se reconocio token DPUNTOS\n")
                elif (ord(self.entrada[indice]) == 44):
                    self.columna += 1  # Se reconoce token ,
                    self.insertText("S0 -> S0: Se reconocio token COMA\n")
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
                    self.insertText("S0 -> S0: Error lexico en la linea: " + str(self.linea) + ", columna: " +
                                    str(self.columna) + ", lexema: " + self.entrada[indice] + "\n")
                    Errores.error.append(
                        {"tipo": "lexico", "lexema": self.entrada[indice], "linea": self.linea, "columna": self.columna})
                    self.columna += 1
                    #self.entrada.replace(self.entrada[indice], ' ', 1)
                    self.estado = 0
            # Estado para reconocer comentarios (unilinea y multilinea) y simbolo division
            elif (self.estado == 1):
                if (ord(self.entrada[indice]) == 47):
                    self.columna += 1
                    self.estado = 2
                    self.insertText("S1 -> S2: caracter /\n")
                elif (ord(self.entrada[indice]) == 42):
                    cadena += self.entrada[indice]
                    self.columna += 1
                    self.estado = 3
                    self.insertText("S1 -> S3: caracter *\n")
                else:  # Se reconoce error
                    #self.insertText("Se reconoce token /\n")
                    self.insertText("S1 -> S0: Error lexico en la linea: " + str(self.linea) + ", columna: " +
                                    str(self.columna) + ", lexema: /\n")
                    Errores.error.append(
                        {"tipo": "lexico", "lexema": "/", "linea": self.linea, "columna": self.columna})
                    cadena = ""
                    #self.entrada.replace(self.entrada[indice], ' ', 1)
                    self.estado = 0
                    indice -= 1
            elif (self.estado == 2):  # Estado para comentarios unilinea
                self.columna += 1
                if (self.entrada[indice] == '\n'):
                    self.estado = 0  # Se reconoce el comentario unilinea
                    self.linea += 1
                    self.columna = 0
                    cadena = ""
                    self.insertText(
                        "S2 -> S0: Se reconocio token COMENTARIO_UNILINEA\n")
            elif (self.estado == 3):  # Estado para comentario multilinea
                cadena += self.entrada[indice]
                if (ord(self.entrada[indice]) == 42):
                    self.estado = 4
                    self.insertText("S3 -> S4: caracter *\n")
                else:
                    self.insertText("S3 -> S3: caracter " +
                                    self.entrada[indice] + "\n")
                self.columna += 1
            elif (self.estado == 4):
                # Se reconoce el token comentario multilinea
                cadena += self.entrada[indice]
                self.columna += 1
                if (ord(self.entrada[indice]) == 47):
                    self.estado = 0  # Se reconoce el comentario multilinea
                    cadena = ""
                    self.insertText(
                        "S4 -> S0: Se reconocio token COMENTARIO_MULTILINEA\n")
                elif (ord(self.entrada[indice]) != 42):
                    if (ord(self.entrada[indice]) == 10):
                        self.linea += 1
                        self.columna = 0
                    self.estado = 3
                    self.insertText(
                        "S4 -> S3: caracter " + self.entrada[indice] + "\n")
            elif (self.estado == 5):  # Estado para reconocer palabras reservadas o id's
                cadena += self.entrada[indice]
                if ((ord(self.entrada[indice]) >= 97 and ord(self.entrada[indice]) <= 122)
                    or (ord(self.entrada[indice]) >= 65 and ord(self.entrada[indice]) <= 90)
                    or (ord(self.entrada[indice]) >= 48 and ord(self.entrada[indice]) <= 57)
                        or ord(self.entrada[indice]) == 45):
                    self.columna += 1
                    self.insertText("S5 -> S5: caracter " +
                                    self.entrada[indice] + "\n")
                else:
                    self.estado = 0  # Se reconoce la palabra reservada o id
                    if(self.verificarReservada(cadena)):
                        self.insertText(
                            "S5 -> S0: Se reconocio token PALABRA RESERVADA\n")
                    else:
                        self.insertText("S5 -> S0: Se reconocio token ID\n")
                    cadena = ""
                    #self.insertText("S5 -> S0 con " + self.entrada[indice] + "\n")
                    indice -= 1
            elif (self.estado == 6):  # Estado para reconocer numeros
                cadena += self.entrada[indice]
                if (ord(self.entrada[indice]) >= 48 and ord(self.entrada[indice]) <= 57):
                    self.columna += 1
                    self.insertText("S6 -> S6: caracter " +
                                    self.entrada[indice] + "\n")
                elif (ord(self.entrada[indice]) == 46):
                    self.columna += 1
                    self.estado = 7
                    self.insertText("S6 -> S7: caracter .\n")
                else:
                    self.estado = 0  # Se reconoce el numero entero
                    cadena = ""
                    indice -= 1
                    self.insertText("S6 -> S0: Se reconocio token ENTERO\n")
            elif (self.estado == 7):
                if (ord(self.entrada[indice]) >= 48 and ord(self.entrada[indice]) <= 57):
                    cadena += self.entrada[indice]
                    self.columna += 1
                    self.estado = 8
                    self.insertText("S7 -> S8: caracter " +
                                    self.entrada[indice] + "\n")
                else:
                    # Se reconoce un error
                    self.insertText("S7 -> S0: Error lexico en la linea: " + str(self.linea) + ", columna: " +
                                    str(self.columna) + ", lexema: " + cadena + "\n")
                    Errores.error.append(
                        {"tipo": "lexico", "lexema": cadena, "linea": self.linea, "columna": self.columna})
                    cadena = ""
                    # self.entrada = self.entrada[:indice] + \
                    #    "0" + self.entrada[indice:]
                    self.estado = 0
                    indice -= 1
            elif (self.estado == 8):
                if (ord(self.entrada[indice]) >= 48 and ord(self.entrada[indice]) <= 57):
                    cadena += self.entrada[indice]
                    self.columna += 1
                    self.insertText("S8 -> S8: caracter " +
                                    self.entrada[indice] + "\n")
                else:
                    self.estado = 0  # Se reconoce el numero decimal
                    cadena = ""
                    self.insertText("S8 -> S0: Se reconocio token DECIMAL\n")
                    indice -= 1
            elif (self.estado == 9):  # Estado para reconocer signo negativo
                if (ord(self.entrada[indice]) >= 48 and ord(self.entrada[indice]) <= 57):
                    cadena = "-"
                    cadena += self.entrada[indice]
                    self.columna += 1
                    self.estado = 6
                    self.insertText("S9 -> S6: caracter " +
                                    self.entrada[indice] + "\n")
                elif ((ord(self.entrada[indice]) >= 97 and ord(self.entrada[indice]) <= 122) or (ord(self.entrada[indice]) >= 65 and ord(self.entrada[indice]) <= 90)):
                    cadena = "-"
                    cadena += self.entrada[indice]
                    self.columna += 1
                    self.estado = 5
                    self.insertText("S9 -> S5: caracter " +
                                    self.entrada[indice] + "\n")
                else:
                    self.insertText("S9 -> S0: Error lexico en la linea: " + str(
                        self.linea) + ", columna: " + str(self.columna) + ", lexema: -\n")
                    self.estado = 0
                    indice -= 1
            elif (self.estado == 10):
                cadena += self.entrada[indice]
                if (ord(self.entrada[indice]) == '\n'):
                    # Se reconoce un error
                    self.insertText("S10 -> S0: Error lexico en la linea: " + str(self.linea) + ", columna: " +
                                    str(self.columna) + ", no se cerro comilla\n")
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
                    self.insertText("S10 -> S0: Se reconocio token STRING\n")
                self.columna += 1
            indice += 1
            if (indice >= len(self.entrada)):
                break
        if (len(Errores.error) > 0):
            # Generar reporte de errores
            self.repError()
            self.insertText(
                "Error: El analisis finalizo con uno o varios errores\n")
            return False
        else:
            # Generar directorio
            self.generarDirectorio()
            return True
    # END

    def getEntrada(self):
        return self.entrada
    # END

    def insertText(self, texto):
        self.consola.insertPlainText(texto)
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
                    <h1 style="text-align:center">Reporte de errores léxicos CSS</h1>
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

    def verificarReservada(self, cadena):
        for id in self.ids:
            if (id == cadena):
                return True
        return False
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
