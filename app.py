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
    QLabel
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

        self.angleLabel = QLabel('Angle:', parent=self.frame)
        self.angleLabel.setGeometry(20, 0, 200, 30)

        self.slider = QSlider(parent=self.frame)
        self.slider.setGeometry(QRect(0, 15, 100, 50))
        self.slider.setOrientation(Qt.Horizontal)
        self.slider.setTickInterval(1)
        self.slider.setMinimum(0)
        self.slider.setMaximum(360)
        self.slider.valueChanged.connect(self.slider_changed)

        self.speed_slider = QSlider(parent=self.frame)
        self.speed_slider.setGeometry(QRect(0, 40, 100, 50))
        self.speed_slider.setOrientation(Qt.Horizontal)
        self.speed_slider.setTickInterval(1)
        self.speed_slider.setMinimum(0)
        self.speed_slider.setMaximum(100)
        self.speed_slider.valueChanged.connect(self.speed_slider_changed)

        self.textEdit = QLineEdit(self.frame)
        self.textEdit.setGeometry(QRect(115, 20, 50, 20))
        self.textEdit.setText(str(0))
        self.textEdit.textChanged.connect(self.textChanged)
        self.textEdit.setValidator(QIntValidator(0, 360, self))

        self.speed_textEdit = QLineEdit(self.frame)
        self.speed_textEdit.setGeometry(QRect(115, 50, 50, 20))
        self.speed_textEdit.setText(str(0))
        self.speed_textEdit.textChanged.connect(self.speed_textChanged)
        self.speed_textEdit.setValidator(QIntValidator(0, 100, self))



        self.startButton = QPushButton(parent=self.frame, text="start")
        self.startButton.setGeometry(120, 90, 50, 20)
        self.startButton.clicked.connect(self.startButtonClicked)

        self.zeroButton = QPushButton(parent=self.frame, text="zero")
        self.zeroButton.setGeometry(60, 90, 50, 20)
        self.zeroButton.clicked.connect(self.zeroButtonClicked)

        self.show()

    def zeroButtonClicked(self):
        self.vm.zeroArm()
        print('zero clicked')

    def startButtonClicked(self):
        self.vm.sendAngleStart()
        print('button clicked: ' + str(self.vm.getAngle()))

    def slider_changed(self):
        value = self.slider.value()
        self.vm.setAngle(value)
        self.textEdit.setText(str(self.vm.getAngle()))

    def speed_slider_changed(self):
        pass

    def speed_textChanged(self):
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