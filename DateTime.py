from datetime import date
import sys
from PyQt5.QtCore import QDate, QTime, QDateTime
from PyQt5.QtWidgets import QApplication, QWidget, QDateTimeEdit, QDateEdit, QTimeEdit, QVBoxLayout

EMOTION = {                                                                     # 1 
    '周一': '(╯°Д°)╯︵ ┻━┻',
    '周二': '(╯￣Д￣)╯╘═╛',
    '周三': '╭(￣▽￣)╯╧═╧',
    '周四': '_(:з」∠)_',
    '周五': '(๑•̀ㅂ•́) ✧',
    '周六': '( ˘ 3˘)♥',
    '周日': '(;′༎ຶД༎ຶ`)'
}


class Date(QWidget):
    def __init__(self):
        super(Date, self).__init__()
        self.calendar = QCalendarWidget(self)   
        self.calendar.setMinimumDate(QDate(1946, 2, 14))                        # 2
        self.calendar.setMaximumDate(QDate(6666, 6, 6))                         # 3
        # self.calendar.setDateRange(QDate(1946, 2, 14), QDate(6666, 6, 6))
        # self.calendar.setFirstDayOfWeek(Qt.Monday)                            # 4
        # self.calendar.setSelectedDate(QDate(1946, 2, 14))                     # 5
        self.calendar.setGridVisible(True)                                      # 6
        self.calendar.clicked.connect(self.show_emotion_func)                   # 6

        print(self.calendar.minimumDate())                                      # 7
        print(self.calendar.maximumDate())
        print(self.calendar.selectedDate())

        self.label = QLabel(self)                                               # 8
        self.label.setAlignment(Qt.AlignCenter)

        weekday = self.calendar.selectedDate().toString('ddd')                  # 9
        self.label.setText(EMOTION[weekday])

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.calendar)
        self.v_layout.addWidget(self.label)
        
        self.setLayout(self.v_layout)
        self.setWindowTitle('QCalendarWidget')

    def show_emotion_func(self):                                                # 10
        weekday = self.calendar.selectedDate().toString('ddd')
        self.label.setText(EMOTION[weekday])


class DateEdit(QWidget):
    def __init__(self):
        super(DateEdit, self).__init__()    
        self.datetime_1 = QDateTimeEdit(self)                                           # 1
        self.datetime_1.dateChanged.connect(lambda: print('Date Changed!'))

        self.datetime_2 = QDateTimeEdit(QDateTime.currentDateTime(), self)              # 2
        self.datetime_2.setDisplayFormat('yyyy-MM-dd HH:mm:ss')
        self.datetime_2.timeChanged.connect(lambda: print('Time Changed!'))
        print(self.datetime_2.date())
        print(self.datetime_2.time())
        print(self.datetime_2.dateTime())

        self.datetime_3 = QDateTimeEdit(QDateTime.currentDateTime(), self)              # 3
        self.datetime_3.dateTimeChanged.connect(lambda: print('DateTime Changed!'))
        self.datetime_3.setCalendarPopup(True)

        self.datetime_4 = QDateTimeEdit(QDate.currentDate(), self)                      # 4
        self.datetime_5 = QDateTimeEdit(QTime.currentTime(), self)

        self.date = QDateEdit(QDate.currentDate(), self)                                # 5
        self.date.setDisplayFormat('yyyy/MM/dd')
        print(self.date.date())

        self.time = QTimeEdit(QTime.currentTime(), self)                                # 6
        self.time.setDisplayFormat('HH:mm:ss')
        print(self.time.time())

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.datetime_1)
        self.v_layout.addWidget(self.datetime_2)
        self.v_layout.addWidget(self.datetime_3)
        self.v_layout.addWidget(self.datetime_4)
        self.v_layout.addWidget(self.datetime_5)
        self.v_layout.addWidget(self.date)
        self.v_layout.addWidget(self.time)

        self.setLayout(self.v_layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # Date = Date()
    # Date.show()
    date_edit = DateEdit()
    date_edit.show()
    sys.exit(app.exec_())