from PyQt5.QtWidgets import *
import sys

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(300, 300)                                   # 1
        self.setWindowTitle('demo')                             # 2
        self.button = QPushButton('Start', self)
        self.button.clicked.connect(self.change_text)
        self.button.clicked.connect(self.change_window_size)    # 3
        self.button.clicked.connect(self.change_window_title)   # 4

    def change_text(self):
        print('change text')
        self.button.setText('Stop')
        self.button.clicked.disconnect(self.change_text)

    def change_window_size(self):                               # 5
        print('change window size')
        self.resize(500, 500)
        self.button.clicked.disconnect(self.change_window_size)

    def change_window_title(self):                              # 6
        print('change window title')
        self.setWindowTitle('window title changed')
        self.button.clicked.disconnect(self.change_window_title)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()                                               
    demo.show()                                                 
    sys.exit(app.exec_())


# class Demo(QWidget):
#     def __init__(self):
#         super(Demo, self).__init__()
#         self.button = QPushButton('Start', self)
#         self.button.pressed.connect(self.button.released)  # 1
#         self.button.released.connect(self.change_text)     # 2

#     def change_text(self):
#         if self.button.text() == 'Start':
#             self.button.setText('Stop')
#         else:
#             self.button.setText('Start')


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     demo = Demo()
#     demo.show()
#     sys.exit(app.exec_())

# class Demo(QWidget):                                            # 1
#     def __init__(self):
#         super(Demo, self).__init__()
#         self.button = QPushButton('Start', self)                # 2
#         self.button.clicked.connect(self.change_text)           # 3

#     def change_text(self):
#         print('change text')
#         self.button.setText('Stop')                             # 4
#         self.button.clicked.disconnect(self.change_text)        # 5


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     demo = Demo()                                               # 6
#     demo.show()                                                 # 7
#     sys.exit(app.exec_())


# app = QApplication(sys.argv)
# app.setStyle('Macintosh')
# label = QLabel('<font color="red">Hello</font> <h1>World</h1>')
# window = QWidget()
# layout = QVBoxLayout()
# button1 = QPushButton('Top')
# button1.clicked.connect(on_button_clicked)
# button2 = QPushButton('Bottom')

# layout.addWidget(button1)
# layout.addWidget(button2)
# window.setLayout(layout)
# window.show()
# app.exec_()