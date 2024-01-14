from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton,
                             QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QListWidget, QComboBox)

app = QApplication([])
window = QWidget()

window.resize(250,250)
window.move(560,225)

text = QLabel('Сума:')
text1 = QLabel('У валюту:')
text2 = QLabel('Результат:')
text3 = QLabel(' ')
button1 = QPushButton('Конвертувати')

c = QComboBox()
list1 = ['eur','usd','frank']
c.addItems(list1)

line = QLineEdit()

v = QVBoxLayout()
v.addWidget(text)
v.addWidget(line)
v.addWidget(text1)
v.addWidget(c)
v.addWidget(text2)
v.addWidget(text3)
v.addWidget(button1)
window.setLayout(v)


def add_task():
    t = line.text()
    f = c.currentText()
    if f == 'eur':
        r = int(t) * 41,45
        text3.setText(str(r))
    elif f == 'usd':
        r = int(t) * 37,80
        text3.setText(str(r))
    elif f == 'frank':
        r = int(t) * 44,33
        text3.setText(str(r))
button1.clicked.connect(add_task)




window.show()
app.exec_()
