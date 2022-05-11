import sys
from appVM import appViewModel
from PyQt5.QtGui import QPixmap, QIntValidator
from PyQt5.QtCore import pyqtSlot, QRect, Qt 
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QSlider,
    QFrame,
    QLineEdit,
    QLabel,
    QGridLayout
)

class App(QWidget):
    def __init__(self, title=" "):
        super().__init__()
        self.title = title
        self.left = 1440
        self.top = 0
        self.width = 500 
        self.height = 500 
        self.vm = appViewModel()

        self.widget()
    
    def widget(self):
        self.setWindowTitle(self.title)

        self.resize(self.width, self.height)
        self.move(self.left, self.top)

        self.frame = QFrame(self)
        self.frame.setGeometry(QRect(40, 40, 250, 180))

        self.angleLabel = QLabel(u'\N{DEGREE SIGN} Angle', parent=self.frame)
        self.angleLabel.setGeometry(180, 25, 200, 30)

        self.speedLabel= QLabel('% Speed', parent=self.frame)
        self.speedLabel.setGeometry(180, 60, 200, 30)

        self.slider = QSlider(parent=self.frame)
        self.slider.setGeometry(QRect(0, 15, 100, 50))
        self.slider.setOrientation(Qt.Horizontal)
        self.slider.setTickInterval(1)
        self.slider.setMinimum(0)
        self.slider.setMaximum(360)
        self.slider.valueChanged.connect(self.slider_changed)

        self.speed_slider = QSlider(parent=self.frame)
        self.speed_slider.setGeometry(QRect(0, 50, 100, 50))
        self.speed_slider.setOrientation(Qt.Horizontal)
        self.speed_slider.setTickInterval(1)
        self.speed_slider.setMinimum(0)
        self.speed_slider.setMaximum(100)
        self.speed_slider.valueChanged.connect(self.speed_slider_changed)

        self.textEdit = QLineEdit(self.frame)
        self.textEdit.setGeometry(QRect(115, 30, 50, 20))
        self.textEdit.setText(str(0))
        self.textEdit.textChanged.connect(self.textChanged)
        self.textEdit.setValidator(QIntValidator(0, 360, self))

        self.speed_textEdit = QLineEdit(self.frame)
        self.speed_textEdit.setGeometry(QRect(115, 65, 50, 20))
        self.speed_textEdit.setText(str(0))
        self.speed_textEdit.textChanged.connect(self.speed_textChanged)
        self.speed_textEdit.setValidator(QIntValidator(0, 100, self))

        self.startButton = QPushButton(parent=self.frame, text="start")
        self.startButton.setGeometry(120, 100, 50, 20)
        self.startButton.clicked.connect(self.startButtonClicked)

        self.zeroButton = QPushButton(parent=self.frame, text="zero")
        self.zeroButton.setGeometry(60, 100, 50, 20)
        self.zeroButton.clicked.connect(self.zeroButtonClicked)

        self.pidFrame = QFrame(self)
        self.pidFrame.setGeometry(QRect(300, 40, 200, 160))
        gridLayout = QGridLayout()
        self.pidFrame.setLayout(gridLayout)

        self.multLabel= QLabel('Mult')
        self.multLabel.setGeometry(QRect(0, 0, 50, 20))
        gridLayout.addWidget(self.multLabel, 0, 1)

        self.divLabel= QLabel('Div')
        gridLayout.addWidget(self.divLabel, 0, 0)

        self.Ilabel = QLabel('I')
        gridLayout.addWidget(self.Ilabel, 1, 0, 1, -1)

        self.iDivText = QLineEdit("ID")
        self.iDivText.setValidator(QIntValidator(0, 100, self))
        gridLayout.addWidget(self.iDivText, 2, 0)

        self.iMultText = QLineEdit("IM")
        self.iMultText.setValidator(QIntValidator(0, 100, self))
        gridLayout.addWidget(self.iMultText, 2, 1)

        self.Ilabel = QLabel('P')
        gridLayout.addWidget(self.Ilabel, 3, 0, 1, -1)

        self.pDivText = QLineEdit("PD")
        self.pDivText.setValidator(QIntValidator(0, 100, self))
        gridLayout.addWidget(self.pDivText, 4, 0)

        self.pMultText = QLineEdit("PM")
        self.pMultText.setValidator(QIntValidator(0, 100, self))
        gridLayout.addWidget(self.pMultText, 4, 1)

        self.pidButton = QPushButton(text="set")
        gridLayout.addWidget(self.pidButton)

        self.show()

    def zeroButtonClicked(self):
        self.vm.zeroArm()

    def startButtonClicked(self):
        self.vm.sendAngleStart()

    def slider_changed(self):
        value = self.slider.value()
        self.vm.setAngle(value)
        self.textEdit.setText(str(self.vm.getAngle()))

    def speed_slider_changed(self):
        value = self.speed_slider.value()
        self.vm.setSpeed(value)
        self.speed_textEdit.setText(str(self.vm.getSpeed()))

    def speed_textChanged(self):
        value = self.speed_textEdit.text()
        if value != '':
            self.vm.setSpeed(int(value))
            self.speed_slider.setValue(self.vm.getSpeed())
        pass

    def textChanged(self):
        value = self.textEdit.text()
        if value != '':
            self.vm.setAngle(int(value))
            self.slider.setValue(self.vm.getAngle())

def main():
    app = QApplication([])
    w = App(title="Robot Dashboard")
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()