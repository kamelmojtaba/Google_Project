import sys, os
from MainWindow import Ui_Form
from Score import Ui_Score
from PyQt5.QtCore import QUrl
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow, Ui_Form):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.player = QMediaPlayer()
        self.path = os.path.dirname(os.path.realpath(__file__))
        self.score = ScoreWidget()
        self.qutions = {
            1 : "Little interest or pleasure in doing things?",
            2 : "Feeling down, depressed, or hopeless?",
            3 : "Trouble falling or staying asleep, or sleeping too much?",
            4 : "Feeling tired or having little energy?",
            5 : "Poor appetite or overeating?",
            6 : "Feeling bad about yourself — or that you are a failure or have let yourself or your family down?",
            7 : "Trouble concentrating on things, such as reading the newspaper or watching",
            8 : "Moving or speaking so slowly that other people could have noticed? Or so fidgety or restless that you have been moving a lot more than usual?",
            9 : "Thoughts that you would be better off dead, or thoughts of hurting yourself in some way?"
        }


        self.points = {
            "Yes" : 3,
            "No" : 0,
            "Some Times" :2,
            "Maybe" : 1
        }

        # function part
        self.pushButton_2.clicked.connect(self.nextQ) # next q button
        self.pushButton_3.clicked.connect(self.toClose) # next q button
        self.pushButton.clicked.connect(self.play) # play q button

        self.number = 2 # conter
        self.qNumber = 1 
        self.total = 0

    def nextQ(self):
        ops = [self.op1,
            self.op2,
            self.op3,
            self.op4
            ]
        
        for i in ops:
            if i.isChecked():
                if self.number >= 10:
                    self.score.label_2.setText(str(self.total))
                    # print(self.total)

                    if self.total in range(1, 5):
                        self.score.label_3.setText("You are normally not need deression treatment")
                        # print(self.total)

                    if self.total in range(5, 10):
                        self.score.label_3.setText("Watchful waiting, repeat PHQ-9 at follow--up")
                        # print(self.total)

                    if self.total in range(14, 20):
                        self.score.label_3.setText("Moderate, Treatment plan, consider counseling, follow up and/or pharmacotherpy")
                        # print(self.total)

                    if self.total in range(15, 20):
                        self.score.label_3.setText("Moderately Severe, Active treatment with pharmacotherapy and/or psychotherapy")
                        # print(self.total)

                    if self.total in range(20, 28):
                        self.score.label_3.setText('''Severe, Immediate initiation of pharmacotheray and, if severe impairment
                        or poor resonse to therapy, expedited referral to a mental health
                        specialist for psychtherapy and/or collabrative mangement''')
                        # print(self.total)

                    self.score.show()
                    break

                # print(i.text() + "is Checked")
                self.total += self.points[i.text()]
                self.label_2.setText(self.qutions[self.number])
                self.number += 1
            


    def toClose(self):
        self.close()

    def play(self):
        # self.pushButton_2.
        # print(os.getcwd())
        full_file_path = os.path.join(os.getcwd(), 'app/sound/' + str(self.qNumber) + ".mp3")
        url = QUrl.fromLocalFile(full_file_path)
        content = QMediaContent(url)
        self.qNumber += 1

        self.player.setMedia(content)
        self.player.play()


class ScoreWidget(QMainWindow, Ui_Score):
    def __init__(self, *args, obj=None, **kwargs):
        super(QWidget, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.toClose)

        
    def toClose(self):
        self.close()

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()