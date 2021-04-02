import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.button = QPushButton('Question', self)
        self.button.clicked.connect(self.show_messagebox)      # 1

    def show_messagebox(self):
        choice = QMessageBox.question(self, '别卷了', '今天月亮下班了吗', 
                                QMessageBox.Yes | QMessageBox.No)  # 2
        if choice == QMessageBox.Yes:
            self.button.setText('睡大觉')
        elif choice == QMessageBox.No:
            self.button.setText('继续卷')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())