import sys
import webbrowser
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from ResaltarSintaxis import ResaltarSintaxis
from Numeros import Numeros

from LexicoJson import AnalizadorLexicoJson
from LexicoCss import AnalizadorLexicoCss
from LexicoHtml import AnalizadorLexicoHtml
from LexicoAritmetica import AnalizadorLexicoAritmetica
from SintacticoAritmetica import AnalizadorSintactico


class Ui_Ventana(object):
    def setupUi(self, Ventana):
        self.ruta = ""
        self.reporte = []

        Ventana.setWindowTitle("ML Web Editor")
        Ventana.setObjectName("Ventana")
        Ventana.resize(850, 600)

        self.centralwidget = QtWidgets.QWidget(Ventana)
        self.centralwidget.setObjectName("centralwidget")

        Ventana.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(Ventana)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")

        self.addMenuArchivo(Ventana)
        self.addMenuAnalisis(Ventana)
        self.addMenuReporte(Ventana)
        self.addMenuAyuda(Ventana)

        Ventana.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Ventana)
        self.statusbar.setObjectName("statusbar")
        Ventana.setStatusBar(self.statusbar)

        self.editor = Numeros(self.centralwidget)
        self.editor.setGeometry(QtCore.QRect(10, 10, 460, 500))
        self.editor.setObjectName("editor")
        self.editor.setStyleSheet(
            """QPlainTextEdit {background-color: #31598D;
                           color: #000;
                           font-family: Courier;}""")
        self.resaltado = ResaltarSintaxis(self.editor)

        self.consola = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.consola.setGeometry(QtCore.QRect(485, 10, 350, 500))
        self.consola.setStyleSheet(
            """QPlainTextEdit {background-color: #333;
                           color: #08F606;
                           font-family: Courier;}""")
        self.consola.setObjectName("consola")
        self.consola.setReadOnly(True)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 520, 800, 20))
        self.label.setObjectName("label")
        self.label.setText("Proyecto realizado por Edgar Cil - 201503600")
        self.label.setAlignment(Qt.AlignCenter)

        self.Eventos()
        Ventana.show()
    # END

    def addMenuArchivo(self, Ventana):
        # Nuevo
        self.itemNuevo = QtWidgets.QAction("&Nuevo", Ventana)
        self.itemNuevo.setStatusTip("Crear nuevo archivo")
        self.itemNuevo.setShortcut("Ctrl+N")

        # Abrir
        self.itemAbrir = QtWidgets.QAction("&Abrir", Ventana)
        self.itemAbrir.setStatusTip("Abrir archivo")
        self.itemAbrir.setShortcut("Ctrl+O")

        # Guardar
        self.itemGuardar = QtWidgets.QAction("&Guardar", Ventana)
        self.itemGuardar.setStatusTip("Guardar cambios")
        self.itemGuardar.setShortcut("Ctrl+S")

        # Guardar como
        self.itemGuardarComo = QtWidgets.QAction("&Guardar como", Ventana)
        self.itemGuardarComo.setStatusTip("Guardar archivo")
        self.itemGuardarComo.setShortcut("Ctrl+G")

        # Salir
        self.itemSalir = QtWidgets.QAction("&Salir", Ventana)
        self.itemSalir.setStatusTip("Cerrar programa")

        # Agregar items al menu archivo
        self.mArchivo = QtWidgets.QMenu("&Archivo", self.menubar)
        self.mArchivo.addAction(self.itemNuevo)
        self.mArchivo.addAction(self.itemAbrir)
        self.mArchivo.addAction(self.itemGuardar)
        self.mArchivo.addAction(self.itemGuardarComo)
        self.mArchivo.addSeparator()
        self.mArchivo.addAction(self.itemSalir)

        self.menubar.addAction(self.mArchivo.menuAction())
    # END

    def addMenuAnalisis(self, Ventana):
        # Analisis Json
        self.itemAnalisis = QtWidgets.QAction("&Analizar Archivo", Ventana)
        self.itemAnalisis.setStatusTip("Analizar archivo")

        self.menuAnalisis = QtWidgets.QMenu("&Analisis", self.menubar)
        self.menuAnalisis.addAction(self.itemAnalisis)

        self.menubar.addAction(self.menuAnalisis.menuAction())
    # END

    def addMenuReporte(self, Ventana):
        # Reporte Json
        self.itemRepJs = QtWidgets.QAction("&Reporte Javascript", Ventana)
        self.itemRepJs.setStatusTip("Reporte Javascript")

        # Reporte CSS
        self.itemRepCSS = QtWidgets.QAction("&Reporte CSS", Ventana)
        self.itemRepCSS.setStatusTip("Reporte CSS")

        # Reporte Html
        self.itemRepHtml = QtWidgets.QAction("&Reporte Html", Ventana)
        self.itemRepHtml.setStatusTip("Reporte Html")

        # Reporte Sintactico
        self.itemRepSintactico = QtWidgets.QAction(
            "&Reporte Sintactico", Ventana)
        self.itemRepSintactico.setStatusTip("Reporte Sintactico")

        # Reporte Errores
        self.itemRepError = QtWidgets.QAction("&Reporte Errores", Ventana)
        self.itemRepError.setStatusTip("Reporte Errores")

        self.mReporte = QtWidgets.QMenu("&Reporte", self.menubar)
        self.mReporte.addAction(self.itemRepJs)
        # self.mReporte.addAction(self.itemRepCSS)
        # self.mReporte.addAction(self.itemRepHtml)
        self.mReporte.addAction(self.itemRepSintactico)
        self.mReporte.addSeparator()
        self.mReporte.addAction(self.itemRepError)

        self.menubar.addAction(self.mReporte.menuAction())
    # END

    def addMenuAyuda(self, Ventana):
        # Informacion
        self.itemInfor = QtWidgets.QAction("&Informacion", Ventana)
        self.itemInfor.setStatusTip("Informacion")

        # Manuales
        self.itemManuales = QtWidgets.QAction("&Manual de usuario", Ventana)
        self.itemManuales.setStatusTip("Manual de usuario")

        self.mAyuda = QtWidgets.QMenu("&Ayuda", self.menubar)
        self.mAyuda.addAction(self.itemManuales)
        self.mAyuda.addAction(self.itemInfor)

        self.menubar.addAction(self.mAyuda.menuAction())
    # END

    def Eventos(self):
        self.itemNuevo.triggered.connect(self.NuevoArchivo)
        self.itemAbrir.triggered.connect(self.AbrirArchivo)
        self.itemGuardar.triggered.connect(self.GuardarArchivo)
        self.itemGuardarComo.triggered.connect(self.GuardarArchivoComo)
        self.itemSalir.triggered.connect(self.Salir)

        self.itemAnalisis.triggered.connect(self.Analizar)

        self.itemRepJs.triggered.connect(self.ReporteJson)
        self.itemRepCSS.triggered.connect(self.ReporteCSS)
        self.itemRepHtml.triggered.connect(self.ReporteHtml)
        self.itemRepSintactico.triggered.connect(self.ReporteSintactico)
        self.itemRepError.triggered.connect(self.ReporteError)

        self.itemInfor.triggered.connect(self.Informacion)
    # END

    def NuevoArchivo(self):
        self.ruta = ""
        self.editor.clear()
    # END

    def AbrirArchivo(self):
        archivo = QtWidgets.QFileDialog.getOpenFileName(None, 'Abrir Archivo',
                                                        '/home/daniel/Desktop', "Javascript (*.js);;CSS (*.css);;HTML (*.html);;RMT (*.rmt)")[0]

        if archivo != '':
            with open(archivo, 'r') as file:
                self.ruta = archivo
                if (self.ruta.find(".js") != -1):
                    self.itemRepCSS.setEnabled(False)
                    self.itemRepHtml.setEnabled(False)
                    self.itemRepSintactico.setEnabled(False)
                    self.itemRepJs.setEnabled(True)
                elif (self.ruta.find(".css") != -1):
                    self.itemRepCSS.setEnabled(True)
                    self.itemRepHtml.setEnabled(False)
                    self.itemRepSintactico.setEnabled(False)
                    self.itemRepJs.setEnabled(False)
                elif (self.ruta.find(".html") != -1):
                    self.itemRepCSS.setEnabled(False)
                    self.itemRepHtml.setEnabled(True)
                    self.itemRepSintactico.setEnabled(False)
                    self.itemRepJs.setEnabled(False)
                elif (self.ruta.find(".rmt") != -1):
                    self.itemRepCSS.setEnabled(False)
                    self.itemRepHtml.setEnabled(False)
                    self.itemRepSintactico.setEnabled(True)
                    self.itemRepJs.setEnabled(False)
                self.editor.clear()
                self.editor.insertPlainText(file.read())
    # END

    def GuardarArchivo(self):
        if self.ruta == '':
            self.GuardarArchivoComo()
        else:
            with open(self.ruta, 'w') as archivo:
                archivo.write(self.editor.toPlainText())
    # END

    def GuardarArchivoComo(self):
        archivo = QtWidgets.QFileDialog.getSaveFileName(None, 'Guardar como ...',
                                                        '/home/daniel/Desktop', "Javascript (*.js);;CSS (*.css);;HTML (*.html);;RMT (*.rmt)")

        if archivo[0] != '':
            with open(archivo[0], 'w') as file:
                file.write(self.editor.toPlainText())
                self.ruta = archivo[0]
                if (self.ruta.find(".js") != -1):
                    self.itemRepCSS.setEnabled(False)
                    self.itemRepHtml.setEnabled(False)
                    self.itemRepSintactico.setEnabled(False)
                    self.itemRepJs.setEnabled(True)
                    self.itemRepError.setEnabled(True)
                elif (self.ruta.find(".css") != -1):
                    self.itemRepCSS.setEnabled(True)
                    self.itemRepHtml.setEnabled(False)
                    self.itemRepSintactico.setEnabled(False)
                    self.itemRepJs.setEnabled(False)
                    self.itemRepError.setEnabled(True)
                elif (self.ruta.find(".html") != -1):
                    self.itemRepCSS.setEnabled(False)
                    self.itemRepHtml.setEnabled(True)
                    self.itemRepSintactico.setEnabled(False)
                    self.itemRepJs.setEnabled(False)
                    self.itemRepError.setEnabled(True)
                elif (self.ruta.find(".rmt") != -1):
                    self.itemRepCSS.setEnabled(False)
                    self.itemRepHtml.setEnabled(False)
                    self.itemRepSintactico.setEnabled(True)
                    self.itemRepJs.setEnabled(False)
                    self.itemRepError.setEnabled(False)
    # END

    def Salir(self):
        sys.exit(app.exec_())
    # END

    def Analizar(self):
        if(self.ruta.find('.js') != -1):
            # Analisis json
            analisis = AnalizadorLexicoJson(
                self.editor.toPlainText(), self.consola, self.ruta.split("/")[len(self.ruta.split("/"))-1])
            bandera = analisis.analizarJson()
            if (not bandera):
                self.editor.setPlainText(analisis.getEntrada())
            pass
        elif(self.ruta.find('.css') != -1):
            # Analisis css
            analisis = AnalizadorLexicoCss(self.editor.toPlainText(
            ), self.consola, self.ruta.split("/")[len(self.ruta.split("/")) - 1])
            bandera = analisis.analizarCss()
            if (not bandera):
                self.editor.setPlainText(analisis.getEntrada())
        elif(self.ruta.find('.html') != -1):
            # Analisis html
            analisis = AnalizadorLexicoHtml(self.editor.toPlainText(
            ), self.consola, self.ruta.split("/")[len(self.ruta.split("/")) - 1])
            bandera = analisis.analizarHtml()
            if (not bandera):
                self.editor.setPlainText(analisis.getEntrada())
        elif(self.ruta.find('.rmt') != -1):
            # Analisis sintactico
            self.consola.insertPlainText(
                "\n\n***********************************\n  COMENZANDO ANALISIS SINTACTICO\n***********************************\n")

            sintactico = AnalizadorSintactico(self.consola)
            self.reporte.clear()
            linea = 1
            for line in self.editor.toPlainText().split("\n"):
                if (len(line) > 0):
                    resultado = sintactico.parser(line)
                    if (resultado == True):
                        self.reporte.append(
                            {"Numero": linea, "Linea": linea, "Expresion": line, "Resultado": "Incorrecto"})
                    else:
                        self.reporte.append(
                            {"Numero": linea, "Linea": linea, "Expresion": line, "Resultado": "Correcto"})
                linea += 1

            self.consola.insertPlainText(
                "***********************************\n  FINALIZO ANALISIS SINTACTICO\n***********************************\n")

            # Generacion de reporte
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
                    <h1>Reporte de Analisis Sintactico</h1>
                    <table class="table">
                    <thead>
                        <tr>
                        <th scope="col">No</th>
                        <th scope="col">Linea</th>
                        <th scope="col">Expresion</th>
                        <th scope="col">Resultado</th>
                        </tr>
                    </thead>
                    <tbody>'''

            contador = 1
            for e in self.reporte:
                cadena += '<tr><th scope="row">' + str(e["Numero"]) + \
                    '</th><td>' + str(e["Linea"]) + '</td><td>' + \
                    str(e["Expresion"]) + '</td><td>' + \
                    e["Resultado"] + '</td></tr>'
                contador += 1

            cadena += '''</tbody>
                            </table>
                        </div><script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.1/jquery.min.js" integrity="sha512-bLT0Qm9VnAYZDflyKcBaQ2gg0hSYNQrJ8RilYldYQ1FxQYoCLtUjuuRuZo+fjqhx/qtq/1itJ0C2ejDxltZVFg==" crossorigin="anonymous"></script>
                                    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
                                    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
                                    <script src="https://unpkg.com/bootstrap-table@1.17.1/dist/bootstrap-table.min.js"></script>
                                </body>
                            </html>'''
            file = open(
                "/home/daniel/Desktop/Reportes/ReporteAritmetica.html", "w+")
            file.write(cadena)
            file.close()

            # lexico = AnalizadorLexicoAritmetica(
            #    self.editor.toPlainText(), self.consola)
            # print(lexico.scanner())
        else:
            self.consola.insertPlainText(
                "Error: Debe abrir o guardar el archivo para analizar\n")
    # END

    def ReporteJson(self):
        webbrowser.open_new_tab(
            "/home/daniel/Desktop/Reportes/ReporteJson.pdf")
    # END

    def ReporteCSS(self):
        pass
    # END

    def ReporteHtml(self):
        pass
    # END

    def ReporteSintactico(self):
        webbrowser.open_new_tab(
            "/home/daniel/Desktop/Reportes/ReporteAritmetica.html")
    # END

    def ReporteError(self):
        webbrowser.open_new_tab("/home/daniel/Desktop/Reportes/errores.html")
    # END

    def Informacion(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)

        msg.setText(
            "USAC\nFacultad de Ingenieria\nEscuela de Ciencias y Sistemas\nOrganizacion de Lenguajes y Compiladores 1\nSeccion A")
        msg.setInformativeText(
            "Proyecto realizado por: Edgar Daniel Cil Peñate con carnet 201503600\n")
        msg.setWindowTitle("Informacion")
        #msg.setDetailedText("The details are as follows:")

        msg.exec()
    # END


if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    app = QtWidgets.QApplication(sys.argv)
    Ventana = QtWidgets.QMainWindow()
    ui = Ui_Ventana()
    ui.setupUi(Ventana)
    sys.exit(app.exec_())
