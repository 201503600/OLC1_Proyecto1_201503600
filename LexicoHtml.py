import sys
import os
import Errores


class AnalizadorLexicoHtml:
    def __init__(self, entrada, conso, name):
        self.entrada = entrada
        self.estado = 0
        self.linea = 0
        self.columna = 0
        self.consola = conso
        self.nombre = name
    # END

    def analizarHtml(self):
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
                if (ord(self.entrada[indice]) == 60):
                    if (ord(self.entrada[indice + 1]) == 47):
                        self.estado = 2
                        indice += 1
                    else:
                        self.estado = 1
                    self.columna += 1
                elif (ord(self.entrada[indice]) == 47):
                    self.columna += 1
                    self.estado = 6
                elif (self.entrada[indice] == " "):
                    self.columna += 1
                elif (self.entrada[indice] == "\t"):
                    self.columna += 4
                elif (ord(self.entrada[indice]) == 13):
                    pass
                elif (self.entrada[indice] == "\n"):
                    self.linea += 1
                    self.columna = 0
            elif (self.estado == 1):
                if ((ord(self.entrada[indice]) >= 97 and ord(self.entrada[indice]) <= 122) or (ord(self.entrada[indice]) >= 65 and ord(self.entrada[indice]) <= 90)):
                    self.columna += 1
                    self.estado = 4
                    # self.insertText("S0 -> S5: caracter " +
                    #            self.entrada[indice] + "\n")
                elif (ord(self.entrada[indice]) == 34):
                    self.columna += 1
                    self.estado = 5
                    #self.insertText("S0 -> S10: caracter \"\n")
                elif (ord(self.entrada[indice]) == 61):
                    self.columna += 1
                elif (ord(self.entrada[indice]) == 62):
                    self.columna += 1
                    self.estado = 0
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
            elif (self.estado == 2):  # Estado para reconocer palabras reservadas o id's
                if ((ord(self.entrada[indice]) >= 97 and ord(self.entrada[indice]) <= 122) or (ord(self.entrada[indice]) >= 65 and ord(self.entrada[indice]) <= 90)):
                    self.columna += 1
                    self.estado = 3
                elif (ord(self.entrada[indice]) == 62):
                    self.columna += 1
                    self.estado = 0
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
            elif (self.estado == 3):
                if ((ord(self.entrada[indice]) >= 97 and ord(self.entrada[indice]) <= 122)
                    or (ord(self.entrada[indice]) >= 65 and ord(self.entrada[indice]) <= 90)
                        or (ord(self.entrada[indice]) >= 48 and ord(self.entrada[indice]) <= 57)):
                    self.columna += 1
                    # self.insertText("S5 -> S5: caracter " +
                    #                self.entrada[indice] + "\n")
                else:
                    indice -= 1
                    self.columna += 1
                    self.estado = 2
            elif (self.estado == 4):
                if ((ord(self.entrada[indice]) >= 97 and ord(self.entrada[indice]) <= 122)
                    or (ord(self.entrada[indice]) >= 65 and ord(self.entrada[indice]) <= 90)
                        or (ord(self.entrada[indice]) >= 48 and ord(self.entrada[indice]) <= 57)):
                    self.columna += 1
                    # self.insertText("S5 -> S5: caracter " +
                    #                self.entrada[indice] + "\n")
                else:
                    indice -= 1
                    self.columna += 1
                    self.estado = 1
            elif (self.estado == 5):
                cadena += self.entrada[indice]
                if (ord(self.entrada[indice]) == '\n'):
                    # Se reconoce un error
                    self.insertText("Error lexico en la linea: " + str(self.linea) + ", columna: " +
                                    str(self.columna) + ", no se cerro comilla\n")
                    Errores.error.append(
                        {"tipo": "lexico", "lexema": cadena, "linea": self.linea, "columna": self.columna})
                    cadena = ""
                    self.entrada = self.entrada[:indice] + \
                        "\"" + self.entrada[indice:]
                    self.estado = 0
                    self.linea += 1
                    self.columna = 0
                elif (ord(self.entrada[indice]) == 34):
                    self.estado = 1  # Se reconoce cadena con doble comilla
                    cadena = ""
                    #self.insertText("S10 -> S0: Se reconocio token STRING\n")
                self.columna += 1
            elif (self.estado == 6):
                self.columna += 1
                if (ord(self.entrada[indice]) == 47):
                    self.estado = 7
                else:
                    self.estado = 0
            elif (self.estado == 7):
                self.columna += 1
                if (self.entrada[indice] == '\n'):
                    self.estado = 0
                    self.linea += 1
                    self.columna = 0

            indice += 1
            # Contador para salir del ciclo
            if (indice >= len(self.entrada)):
                break

        # Se verifica si hay errores
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
                    <h1 style="text-align:center">Reporte de errores léxicos Html</h1>
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
