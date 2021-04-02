import sys
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QFontComboBox, QLineEdit, QMessageBox, QVBoxLayout


class ComboBox(QWidget):
    choice = 'a'
    choice_list = ['b', 'c', 'd', 'e']

    def __init__(self):
        super(ComboBox, self).__init__()

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

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QSpinBox, QDoubleSpinBox, QHBoxLayout


class SpinBox(QWidget):
    def __init__(self):
        super(SpinBox, self).__init__()
        self.spinbox = QSpinBox(self)
        self.spinbox.setRange(-99, 99)                                                      # 1
        self.spinbox.setSingleStep(1)                                                       # 2
        self.spinbox.setValue(66)                                                           # 3
        self.spinbox.valueChanged.connect(self.value_change_func)                           # 4

        # 浮点型
        self.double_spinbox = QDoubleSpinBox(self)                                          # 5
        self.double_spinbox.setRange(-99.99, 99.99)
        self.double_spinbox.setSingleStep(0.01)
        self.double_spinbox.setValue(66.66)

        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.spinbox)
        self.h_layout.addWidget(self.double_spinbox)
        self.setLayout(self.h_layout)

    def value_change_func(self):
        decimal_part = self.double_spinbox.value() - int(self.double_spinbox.value())       # 6
        self.double_spinbox.setValue(self.spinbox.value() + decimal_part)                   # 7


if __name__ == '__main__':
    app = QApplication(sys.argv)
    spinbox = SpinBox()
    spinbox.show()
    sys.exit(app.exec_())
