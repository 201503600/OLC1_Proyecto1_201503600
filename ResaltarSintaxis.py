from PyQt5.QtGui import QTextCharFormat, QSyntaxHighlighter, QColor, qRgb
from PyQt5.QtCore import QRegExp, Qt


class ResaltarSintaxis (QSyntaxHighlighter):

    def __init__(self, parent=None):
        super(ResaltarSintaxis, self).__init__(parent.document())
        self.Reglas = []

        # PALABRAS RESERVADAS
        reservadasMagenta = QTextCharFormat()
        reservadasMagenta.setForeground(Qt.red)
        listaMagenta = ["\\bvar\\b", "\\bxor\\b", "\\barray\\b", "\\bif\\b"]
        self.Reglas = [(QRegExp(patron), reservadasMagenta)
                       for patron in listaMagenta]

        reservadasAmarillo = QTextCharFormat()
        reservadasAmarillo.setForeground(QColor(Qt.yellow).lighter(70))
        listaAmarillo = ["\\bstring\\b", "\\bchar\\b"]
        self.Reglas += [(QRegExp(patron), reservadasAmarillo)
                        for patron in listaAmarillo]

        reservadasAzul = QTextCharFormat()
        reservadasAzul.setForeground(QColor(Qt.blue).lighter(130))
        listaAzul = ["\\bint\\b", "\\bboolean\\b"]
        self.Reglas += [(QRegExp(patron), reservadasAzul)
                        for patron in listaAzul]

        # IDENTIFICADOR
        identificador = QTextCharFormat()
        identificador.setForeground(Qt.green)
        self.Reglas.append((QRegExp("[A-Za-z][A-Za-z0-9_]*"), identificador))

        # PRIMITIVOS
        digitos = QTextCharFormat()
        digitos.setForeground(Qt.black)
        self.Reglas.append((QRegExp("\\b\d+(.\d+)?\\b"), digitos))

        cadena = QTextCharFormat()
        cadena.setForeground(Qt.black)
        self.Reglas.append((QRegExp("\".*\"|'.*'"), cadena))

        # OPERADORES
        temporales = QTextCharFormat()
        temporales.setForeground(QColor(255, 165, 0))
        self.Reglas.append(
            (QRegExp("\+|-|/|\*|(==)|(\!=)|\!|\(|\)|<|>|(<=)|(>=)|(&&)|(\|\|)"), temporales))

        # COMENTARIOS
        comentario = QTextCharFormat()
        comentario.setForeground(Qt.gray)
        # Comentarios de linea
        self.Reglas.append((QRegExp("//[^\n]*"), comentario))
        # Comentarios multilinea
        self.Reglas.append((QRegExp("\/\*[^*]*\*\/"), comentario))
    # END

    def highlightBlock(self, texto):
        for patron, formato in self.Reglas:
            exp = QRegExp(patron)
            pos = exp.indexIn(texto)

            while pos >= 0:
                cantidad = exp.matchedLength()
                self.setFormat(pos, cantidad, formato)
                pos = exp.indexIn(texto, pos + cantidad)
    # END
