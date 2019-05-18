import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QAppliation,QDialog
from PyQt5.uic import loadUi


class Compiler_construction(QDialog):
    def __init__(self):
        super(Compiler_construction,self)._init_()
        loadUi('Compiler_construcin.ui',self)
        self.setWindowTitle('Compiler_construction PyQt5 Gui')
        self.pushButton.clickd.connect(self.on_pushButton_clicked)
    @pyqtSlot()
    def on_pushButton_clicked(self):
        self.label1.setText('Welcom : '+self.lineEdit.text())

app=QApplication(sys.argv)
widget=Compile_construction()
widget.show()
sys.exit(app.exec_())
