import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem


class Demo(QTableWidget):                               # 1
    def __init__(self):
        super(Demo, self).__init__()
        self.setRowCount(6)                             # 2
        self.setColumnCount(6)
        # self.table = QTableWidget(6, 6, self)

        print(self.rowCount())                          # 3
        print(self.columnCount())

        self.setColumnWidth(0, 30)                      # 4
        self.setRowHeight(0, 30)

        self.setHorizontalHeaderLabels(['h1', 'h2', 'h3', 'h4', ' h5', 'h6'])   # 5
        self.setVerticalHeaderLabels(['t1', 't2', 't3', 't4', 't5', 't6'])

        # self.setShowGrid(False)                       # 6

        self.item_1 = QTableWidgetItem('Hi')            # 7
        self.setItem(0, 0, self.item_1)

        self.item_2 = QTableWidgetItem('Bye')           # 8
        self.item_2.setTextAlignment(Qt.AlignCenter)
        self.setItem(2, 2, self.item_2)

        self.setSpan(2, 2, 2, 2)                        # 9

        print(self.findItems('Hi', Qt.MatchExactly))    # 10
        print(self.findItems('B', Qt.MatchContains))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())