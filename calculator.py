import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from string import *
from random import choice
import pyperclip

class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.resize(300, 350)

        self.generate_btn = QPushButton('GENERATE', self)
        font = QFont('Times New Roman', 12, 12, False)
        self.generate_btn.setFont(font)
        self.generate_btn.move(105,160)
        self.generate_btn.clicked.connect(self.generate_password)

        self.copy_button = QPushButton('COPY',self)
        self.copy_button.move(115,270)
        self.copy_button.clicked.connect(self.copy_password)
        self.copy_button.setDisabled(True)

        validator = QIntValidator(self)
        validator.setBottom(8)
        validator.setTop(16)

        self.dim_edit = QLineEdit(self)
        self.dim_edit.setValidator(validator)
        self.dim_edit.setGeometry(125,100,45,30)
        self.dim_edit.setText('8')


        self.genlabel = QLabel('Введите размерность \n'
                                '        от 8 до 16: ', self)
        self.genlabel.move(80,50)
        self.genlabel.setFont(font)
        self.passlabel = QLabel('Password: ', self)
        self.passlabel.move(60, 230)
        self.passlabel.setFont(font)

        self.success_label = QLabel('',self)
        self.success_label.setGeometry(135,300,50,15)
        self.success_label.setFont(font)

        self.pass_line = QLineEdit(self)
        self.pass_line.setPlaceholderText('Your password is...')
        self.pass_line.move(130,230)
        self.pass_line.resize(100,20)
        self.pass_line.setReadOnly(True)



    def generate_password(self):
        dim = int(self.dim_edit.text())
        if dim >= 16:
            dim = 16
        elif dim <=8:
            dim = 8

        start_list = ascii_letters + digits + punctuation
        x = 0
        password_list = []
        while x < dim:
            password_list.append(choice(start_list))
            x += 1
        pass_string = ''.join(str(symb) for symb in password_list)
        self.pass_line.setText(pass_string)
        self.copy_button.setDisabled(False)
        self.success_label.setText('')

    def copy_password(self):
        pyperclip.copy(self.pass_line.text())
        self.success_label.setText('Success!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())