import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QTreeWidget, QTreeWidgetItem, QLabel, QHBoxLayout


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(500, 300)
        self.label = QLabel('No Click')                         # 1

        self.tree = QTreeWidget(self)                           # 2
        self.tree.setColumnCount(2)
        self.tree.setHeaderLabels(['Install Components', 'Test'])
        self.tree.itemClicked.connect(self.change_func)

        self.preview = QTreeWidgetItem(self.tree)               # 3
        self.preview.setText(0, 'Preview')

        # self.preview = QTreeWidgetItem()
        # self.preview.setText(0, 'Preview')
        # self.tree.addTopLevelItem(self.preview)

        self.qt5112 = QTreeWidgetItem()                         # 4
        self.qt5112.setText(0, 'Qt 5.11.2 snapshot')
        self.qt5112.setCheckState(0, Qt.Unchecked)
        self.preview.addChild(self.qt5112)

        choice_list = ['macOS', 'Android x86', 'Android ARMv7', 'Sources', 'iOS']
        self.item_list = []
        for i, c in enumerate(choice_list):                     # 5
            item = QTreeWidgetItem(self.qt5112)
            item.setText(0, c)
            item.setCheckState(0, Qt.Unchecked)
            self.item_list.append(item)

        self.test_item = QTreeWidgetItem(self.qt5112)           # 6
        self.test_item.setText(0, 'test1')
        self.test_item.setText(1, 'test2')
        self.test_item.setCheckState(0, Qt.Unchecked)

        self.tree.expandAll()                                   # 7

        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.tree)
        self.h_layout.addWidget(self.label)
        self.setLayout(self.h_layout)

    def change_func(self, item, column):
        self.label.setText(item.text(column))                   # 8

        print(item.text(column))
        print(column)
        if item == self.qt5112:                                 # 9
            if self.qt5112.checkState(0) == Qt.Checked:
                [x.setCheckState(0, Qt.Checked) for x in self.item_list]
            else:
                [x.setCheckState(0, Qt.Unchecked) for x in self.item_list]
        else:                                                   # 10
            check_count = 0
            for x in self.item_list:
                if x.checkState(0) == Qt.Checked:
                    check_count += 1

            if check_count == 5:
                self.qt5112.setCheckState(0, Qt.Checked)
            elif 0 < check_count < 5:
                self.qt5112.setCheckState(0, Qt.PartiallyChecked)
            else:
                self.qt5112.setCheckState(0, Qt.Unchecked)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())