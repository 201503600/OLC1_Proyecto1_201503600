# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prueba.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from ResaltarSintaxis import ResaltarSintaxis
from Numeros import Numeros
from LexicoJson import AnalizadorLexicoJson

class Ui_Ventana(object):
    def setupUi(self, Ventana):
        self.ruta = "" 

        Ventana.setObjectName("Ventana")
        Ventana.resize(850, 500)

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
                           color: #fff;
                           font-family: Courier;}""")
        self.consola.setObjectName("consola")

        self.Eventos()
        Ventana.show()

    def addMenuArchivo(self, Ventana) :
        #Nuevo
        self.itemNuevo = QtWidgets.QAction("&Nuevo", Ventana)
        self.itemNuevo.setStatusTip("Crear nuevo archivo")
        self.itemNuevo.setShortcut("Ctrl+N")

        #Abrir
        self.itemAbrir = QtWidgets.QAction("&Abrir", Ventana)
        self.itemAbrir.setStatusTip("Abrir archivo")
        self.itemAbrir.setShortcut("Ctrl+O")

        #Guardar
        self.itemGuardar = QtWidgets.QAction("&Guardar", Ventana)
        self.itemGuardar.setStatusTip("Guardar cambios")
        self.itemGuardar.setShortcut("Ctrl+S")

        #Guardar como
        self.itemGuardarComo = QtWidgets.QAction("&Guardar como", Ventana)
        self.itemGuardarComo.setStatusTip("Guardar archivo")
        self.itemGuardarComo.setShortcut("Ctrl+G")

        #Salir
        self.itemSalir = QtWidgets.QAction("&Salir", Ventana)
        self.itemSalir.setStatusTip("Cerrar programa")
       
        #Agregar items al menu archivo
        self.mArchivo = QtWidgets.QMenu("&Archivo", self.menubar)
        self.mArchivo.addAction(self.itemNuevo)
        self.mArchivo.addAction(self.itemAbrir)
        self.mArchivo.addAction(self.itemGuardar)
        self.mArchivo.addAction(self.itemGuardarComo)
        self.mArchivo.addSeparator()
        self.mArchivo.addAction(self.itemSalir)

        self.menubar.addAction(self.mArchivo.menuAction())

    def addMenuAnalisis(self, Ventana):
        #Analisis Json
        self.itemAnalisis = QtWidgets.QAction("&Analizar Archivo", Ventana)
        self.itemAnalisis.setStatusTip("Analizar archivo")

        self.menuAnalisis = QtWidgets.QMenu("&Analisis", self.menubar)
        self.menuAnalisis.addAction(self.itemAnalisis)

        self.menubar.addAction(self.menuAnalisis.menuAction())

    def addMenuReporte(self, Ventana):
        #Reporte Json
        self.itemRepJs = QtWidgets.QAction("&Reporte Javascript", Ventana)
        self.itemRepJs.setStatusTip("Reporte Javascript")

        #Reporte CSS
        self.itemRepCSS = QtWidgets.QAction("&Reporte CSS", Ventana)
        self.itemRepCSS.setStatusTip("Reporte CSS")

        #Reporte Html
        self.itemRepHtml = QtWidgets.QAction("&Reporte Html", Ventana)
        self.itemRepHtml.setStatusTip("Reporte Html")

        #Reporte Sintactico
        self.itemRepSintactico = QtWidgets.QAction("&Reporte Sintactico", Ventana)
        self.itemRepSintactico.setStatusTip("Reporte Sintactico")

        #Reporte Errores
        self.itemRepError = QtWidgets.QAction("&Reporte Errores", Ventana)
        self.itemRepError.setStatusTip("Reporte Errores")

        self.mReporte = QtWidgets.QMenu("&Reporte", self.menubar)        
        self.mReporte.addAction(self.itemRepJs)
        self.mReporte.addAction(self.itemRepCSS)
        self.mReporte.addAction(self.itemRepHtml)
        self.mReporte.addAction(self.itemRepSintactico)
        self.mReporte.addSeparator()
        self.mReporte.addAction(self.itemRepError)

        self.menubar.addAction(self.mReporte.menuAction())

    def addMenuAyuda(self, Ventana):
        #Informacion
        self.itemInfor = QtWidgets.QAction("&Informacion", Ventana)
        self.itemInfor.setStatusTip("Informacion")

        #Manuales
        self.itemManuales = QtWidgets.QAction("&Manual de usuario", Ventana)
        self.itemManuales.setStatusTip("Manual de usuario")

        self.mAyuda = QtWidgets.QMenu("&Ayuda", self.menubar)
        self.mAyuda.addAction(self.itemManuales)
        self.mAyuda.addAction(self.itemInfor)

        self.menubar.addAction(self.mAyuda.menuAction())

    def Eventos(self) :
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

    def NuevoArchivo(self):
        self.ruta = ""
        self.editor.clear()

    def AbrirArchivo(self) :
        archivo = QtWidgets.QFileDialog.getOpenFileName(None, 'Abrir Archivo', 
         '/home/daniel/Desktop',"Javascript (*.js);;CSS (*.css);;HTML (*.html);;RMT (*.rmt)")[0]

        if archivo != '' :
            with open(archivo, 'r') as file:
                self.ruta = archivo
                self.editor.insertPlainText(file.read())

    def GuardarArchivo(self) :
        if self.ruta == '':
            self.GuardarArchivoComo()
        else:
            with open(self.ruta, 'w') as archivo:
                archivo.write(editor.toPlainText())

    def GuardarArchivoComo(self) :
        archivo = QtWidgets.QFileDialog.getOpenFileName(None, 'Abrir Archivo', 
         '/home/daniel/Desktop',"Javascript (*.js);;CSS (*.css);;HTML (*.html);;RMT (*.rmt)")

        if archivo != '' :
            with open(archivo, 'w') as file:
                file.write(editor.toPlainText())
                self.ruta = archivo
    
    def Salir(self) :
        sys.exit(app.exec_())

    def Analizar(self):
        if(self.ruta.find('.js') != -1):
            #Analisis json
            analisis = AnalizadorLexicoJson(self.editor.toPlainText())
            analisis.analizarJson()
            pass
        elif(self.ruta.find('.css') != -1):
            #Analisis css
            pass
        elif(self.ruta.find('.html') != -1):
            #Analisis html
            pass
        else:
            #Analisis sintactico
            pass
        pass

    def ReporteJson(self):
        pass

    def ReporteCSS(self):
        pass

    def ReporteHtml(self):
        pass

    def ReporteSintactico(self):
        pass

    def ReporteError(self):
        pass

    def Informacion(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)

        msg.setText("USAC\nFacultad de Ingenieria\nEscuela de Ciencias y Sistemas\nOrganizacion de Lenguajes y Compiladores 1\nSeccion A")
        msg.setInformativeText("Proyecto realizado por: Edgar Daniel Cil Peñate con carnet 201503600\n")
        msg.setWindowTitle("Informacion")
        #msg.setDetailedText("The details are as follows:")

        msg.exec()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Ventana = QtWidgets.QMainWindow()
    ui = Ui_Ventana()
    ui.setupUi(Ventana)
    sys.exit(app.exec_())