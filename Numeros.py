from PyQt5.QtCore import Qt, QRect, QSize, QPoint
from PyQt5.QtWidgets import (QWidget, QPlainTextEdit, QTextEdit,
                             QMainWindow, QAction, qApp, QApplication)
from PyQt5.QtGui import QColor, QPainter, QTextFormat, QKeySequence, QFont


class LineNumberArea(QWidget):
    def __init__(self, editor):
        super().__init__(editor)
        self.codeEditor = editor
    # END

    def paintEvent(self, event):
        self.codeEditor.lineNumberAreaPaintEvent(event)
    # END


class Numeros(QPlainTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ruta = ''
        self.AreaNumeroLinea = LineNumberArea(self)

        self.blockCountChanged.connect(self.actualizarAnchoAreaNumeros)
        self.updateRequest.connect(self.actualizarAreaNumeroLinea)
        self.cursorPositionChanged.connect(self.highlightCurrentLine)
        self.actualizarAnchoAreaNumeros(0)
    # END

    def lineNumberAreaWidth(self):
        # print(1)
        digitos = 1
        maximo = max(1, self.blockCount())
        while maximo >= 10:
            maximo /= 10
            digitos += 1
        esp = 3 + self.fontMetrics().width('9') * digitos
        return esp
    # END

    def actualizarAnchoAreaNumeros(self, _):
        # print(2)
        self.setViewportMargins(self.lineNumberAreaWidth(), 0, 0, 0)
    # END

    def actualizarAreaNumeroLinea(self, rect, dy):
        # print(3)
        if dy:
            self.AreaNumeroLinea.scroll(0, dy)
        else:
            self.AreaNumeroLinea.update(
                0, rect.y(), self.AreaNumeroLinea.width(), rect.height())
        if rect.contains(self.viewport().rect()):
            self.actualizarAnchoAreaNumeros(0)
    # END

    def resizeEvent(self, event):
        # print(4)
        super().resizeEvent(event)
        cr = self.contentsRect()
        self.AreaNumeroLinea.setGeometry(
            QRect(cr.left(), cr.top(), self.lineNumberAreaWidth(), cr.height()))
    # END

    def highlightCurrentLine(self):
        extraSelections = []
        if not self.isReadOnly():
            eleccion = QTextEdit.ExtraSelection()
            color = QColor(Qt.blue).lighter(150)
            eleccion.format.setBackground(color)
            eleccion.format.setProperty(QTextFormat.FullWidthSelection, True)
            eleccion.cursor = self.textCursor()
            extraSelections.append(eleccion)
        self.setExtraSelections(extraSelections)
    # END

    def lineNumberAreaPaintEvent(self, event):
        # print(6)
        painter = QPainter(self.AreaNumeroLinea)
        painter.fillRect(event.rect(), Qt.lightGray)
        bloque = self.firstVisibleBlock()
        numeroBloque = bloque.blockNumber()
        arriba = self.blockBoundingGeometry(
            bloque).translated(self.contentOffset()).top()
        abajo = arriba + self.blockBoundingRect(bloque).height()
        alto = self.fontMetrics().height()

        while bloque.isValid() and (arriba <= event.rect().bottom()):

            if bloque.isVisible() and (abajo >= event.rect().top()):

                num = str(numeroBloque + 1)
                painter.setPen(Qt.black)
                painter.drawText(
                    0, arriba, self.AreaNumeroLinea.width(), alto, Qt.AlignRight, num)

            bloque = bloque.next()
            arriba = abajo
            abajo = arriba + self.blockBoundingRect(bloque).height()
            numeroBloque += 1
    # END
