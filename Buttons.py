import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox, QVBoxLayout

class CheckButton(QWidget):
    def __init__(self):
        super(CheckButton, self).__init__()
        self.checkbox1 = QCheckBox('Checkbox 1', self)
        self.checkbox2 = QCheckBox('Checkbox 2', self)
        self.checkbox3 = QCheckBox('Checkbox 3', self)

        self.v_layout = QVBoxLayout()

        self.checkbox_init()
        self.layout_init()

    def layout_init(self):
        self.v_layout.addWidget(self.checkbox1)
        self.v_layout.addWidget(self.checkbox2)
        self.v_layout.addWidget(self.checkbox3)

        self.setLayout(self.v_layout)

    def checkbox_init(self):
        self.checkbox1.setChecked(True)                                                             # 1
        # self.checkbox1.setCheckState(Qt.Checked)                                                  # 2
        self.checkbox1.stateChanged.connect(lambda: self.on_state_change_func(self.checkbox1))      # 3

        self.checkbox2.setChecked(False)
        # self.checkbox2.setCheckState(Qt.Unchecked)
        self.checkbox2.stateChanged.connect(lambda: self.on_state_change_func(self.checkbox2))

        self.checkbox3.setTristate(True)                                                            # 4
        self.checkbox3.setCheckState(Qt.PartiallyChecked)                                           # 5
        self.checkbox3.stateChanged.connect(lambda: self.on_state_change_func(self.checkbox3))      

    def on_state_change_func(self, checkbox):                                                       # 6
        print('{} was clicked, and its current state is {}'.format(checkbox.text(), checkbox.checkState()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = CheckButton()
    demo.show()
    sys.exit(app.exec_())