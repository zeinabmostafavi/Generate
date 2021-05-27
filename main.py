import sys
import random
from functools import partial
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from PySide6.QtUiTools import QUiLoader
import string


class mainwindow(QWidget):
    def __init__(self):
        super(mainwindow, self).__init__()

        loader = QUiLoader()
        self.ui = loader.load("form.ui")
        self.ui.show()
        self.ui.btn1.clicked.connect(self.generat1)
        self.ui.btn2.clicked.connect(self.generat2)
        self.ui.btn3.clicked.connect(self.generat3)
        self.password = string.ascii_letters + string.digits + \
            string.printable + string.ascii_uppercase

    def generat1(self):
        password = ''.join(random.choice(self.password) for i in range(8))
        self.ui.editor1.setText(password)

    def generat2(self):
        password = ''.join(random.choice(self.password) for i in range(12))
        self.ui.editor2.setText(password)

    def generat3(self):
        password = ''.join(random.choice(self.password) for i in range(16))
        self.ui.editor3.setText(password)


if __name__ == "__main__":
    app = QApplication([])
    window = mainwindow()
    sys.exit(app.exec_())
