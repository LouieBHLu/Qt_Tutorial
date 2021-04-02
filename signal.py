import sys
from PyQt5.QtCore import pyqtSignal                             # 1
from PyQt5.QtWidgets import QApplication, QWidget, QLabel


class Demo(QWidget):
    my_signal = pyqtSignal()                                    # 2

    def __init__(self):
        super(Demo, self).__init__()
        self.label = QLabel('Hello World', self)
        self.my_signal.connect(self.change_text)                # 3

    def change_text(self):
        if self.label.text() == 'Hello World':
            self.label.setText('Hello PyQt5')
        else:
            self.label.setText('Hello World')

    def mousePressEvent(self, QMouseEvent):                     # 4
        self.my_signal.emit()                                   


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
