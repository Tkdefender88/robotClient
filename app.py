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
    QLineEdit
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

        self.slider = QSlider(parent=self.frame)
        self.slider.setOrientation(Qt.Horizontal)
        self.slider.setTickInterval(1)
        self.slider.setMinimum(0)
        self.slider.setMaximum(360)
        self.slider.valueChanged.connect(self.slider_changed)

        self.textEdit = QLineEdit(self.frame)
        self.textEdit.setGeometry(QRect(0, 50, 50, 30))
        self.textEdit.setText(str(0))
        self.textEdit.textChanged.connect(self.textChanged)
        self.textEdit.setValidator(QIntValidator(0, 360, self))

        self.button = QPushButton(parent=self.frame, text="send")
        self.button.setGeometry(100, 0, 50, 20)
        self.button.clicked.connect(self.buttonClicked)

        self.show()

    def buttonClicked(self):
        self.vm.sendAngleStart()
        print('button clicked: ' + str(self.vm.getAngle()))

    def slider_changed(self):
        value = self.slider.value()
        self.vm.setAngle(value)
        self.textEdit.setText(str(self.vm.getAngle()))

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