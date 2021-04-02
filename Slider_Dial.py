import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QLabel, QVBoxLayout, QHBoxLayout


class Slider(QWidget):
    def __init__(self):
        super(Slider, self).__init__()
        self.slider_1 = QSlider(Qt.Horizontal, self)                                       # 1
        self.slider_1.setRange(0, 100)                                                     # 2
        self.slider_1.valueChanged.connect(lambda: self.on_change_func(self.slider_1))     # 3

        self.slider_2 = QSlider(Qt.Vertical, self)
        self.slider_2.setMinimum(0)                                                        # 4
        self.slider_2.setMaximum(100)                                                      # 5
        self.slider_2.valueChanged.connect(lambda: self.on_change_func(self.slider_2))

        self.label = QLabel('0', self)                                                     # 6
        self.label.setFont(QFont('Arial Black', 20))

        self.h_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()

        self.h_layout.addWidget(self.slider_2)
        self.h_layout.addStretch(1)
        self.h_layout.addWidget(self.label)
        self.h_layout.addStretch(1)

        self.v_layout.addWidget(self.slider_1)
        self.v_layout.addLayout(self.h_layout)
        
        self.setLayout(self.v_layout)

    def on_change_func(self, slider):                                                       # 7
        if slider == self.slider_1:
            self.slider_2.setValue(self.slider_1.value())
            self.label.setText(str(self.slider_1.value()))
        else:
            self.slider_1.setValue(self.slider_2.value())
            self.label.setText(str(self.slider_2.value()))

import sys
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QDial, QLabel, QHBoxLayout


class Dial(QWidget):
    def __init__(self):
        super(Dial, self).__init__()
        self.setWindowTitle('QDial')                            # 1

        self.dial = QDial(self)
        self.dial.setFixedSize(100, 100)                        # 2
        self.dial.setRange(0, 100)   
        self.dial.setValue(50)                           # 3
        self.dial.setNotchesVisible(True)                       # 4
        self.dial.valueChanged.connect(self.on_change_func)     # 5

        self.label = QLabel('50', self)
        self.label.setFont(QFont('Arial Black', 20))

        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.dial)
        self.h_layout.addWidget(self.label)

        self.setLayout(self.h_layout)

    def on_change_func(self):
        self.label.setText(str(self.dial.value()))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # demo = Demo()
    # demo.show()
    dial = Dial()
    dial.show()
    sys.exit(app.exec_())