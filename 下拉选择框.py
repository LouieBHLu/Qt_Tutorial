import sys
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QFontComboBox, QLineEdit, QMessageBox, QVBoxLayout


class Demo(QWidget):
    choice = 'a'
    choice_list = ['b', 'c', 'd', 'e']

    def __init__(self):
        super(Demo, self).__init__()

        self.combobox_1 = QComboBox(self)                   # 1
        self.combobox_2 = QFontComboBox(self)               # 2

        self.lineedit = QLineEdit(self)                     # 3

        self.v_layout = QVBoxLayout()

        self.layout_init()
        self.combobox_init()

    def layout_init(self):
        self.v_layout.addWidget(self.combobox_1)
        self.v_layout.addWidget(self.combobox_2)
        self.v_layout.addWidget(self.lineedit)

        self.setLayout(self.v_layout)

    def combobox_init(self):
        self.combobox_1.addItem(self.choice)              # 4
        self.combobox_1.addItems(self.choice_list)        # 5
        self.combobox_1.currentIndexChanged.connect(lambda: self.on_combobox_func(self.combobox_1))   # 6
        # self.combobox_1.currentTextChanged.connect(lambda: self.on_combobox_func(self.combobox_1))  # 7

        self.combobox_2.currentFontChanged.connect(lambda: self.on_combobox_func(self.combobox_2))
        # self.combobox_2.currentFontChanged.connect(lambda: self.on_combobox_func(self.combobox_2))

    def on_combobox_func(self, combobox):                                                             # 8
        if combobox == self.combobox_1:
            QMessageBox.information(self, 'ComboBox 1', '{}: {}'.format(combobox.currentIndex(), combobox.currentText()))
        else:
            self.lineedit.setFont(combobox.currentFont())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())