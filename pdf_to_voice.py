import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from gtts import gTTS
import pdfplumber


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.resize(350, 350)

        font = QFont('Times New Roman', 12, 1, False)

        self.choose_btn = QPushButton('Choose file',self)
        self.choose_btn.move(140,100)
        self.choose_btn.setFont(font)
        self.choose_btn.clicked.connect(self.evt_choose_pdf)

        self.play_btn = QPushButton('Play', self)
        self.play_btn.move(80,200)
        self.play_btn.setDisabled(True)
        self.play_btn.setFont(font)
        self.play_btn.clicked.connect(self.evt_play_pdf)

        self.success_label = QLabel(self)
        self.success_label.setFont(font)



    def evt_choose_pdf(self, text):
         file_path, b_ok = QFileDialog\
             .getOpenFileName(self, 'Open TXT', '', 'PDF (*.pdf)')
         if b_ok:
             with pdfplumber.open(file_path) as pdf:
                 pages = [page.extract_text() for page in pdf.pages]

             text = ''.join(pages)
             self.text = text.replace('\n', '')
             print(self.text)
             if len(text) > 0:
                 self.success_label.setText('File succesfully converted!\n'
                                            f' There are {len(text)} symbols')
                 self.success_label.setGeometry(100, 140, 155, 40)
                 self.play_btn.setDisabled(False)
             else:
                 self.success_label.setText('There is no text in PDF!')
             return self.text


    def evt_play_pdf(self):
        tts = gTTS(self.text)
        tts.save('pdftomp3.mp3')
        os.startfile('pdftomp3.mp3')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())