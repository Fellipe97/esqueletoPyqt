from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
#nome do arquivo .ui
import untitled
import sys

class Janela(QtWidgets.QMainWindow, untitled.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Janela, self).__init__(parent)
        self.setupUi(self)
        
        self.nome_do_botao.clicked.connect(self.printarNome)
        
    def printarNome(self):
        self.nome_do_campo.setText("Oi Fellipe")

        
def main(): 
    app = QApplication(sys.argv)
    form = Janela()
    form.show()
    app.exec_()   

if __name__ == '__main__':
    main()