from PyQt5.QtWidgets import QApplication, QPushButton, QMessageBox

def automate_task():
    msg = QMessageBox()
    msg.setWindowTitle("Automatisation")
    msg.setText("Tâche exécutée !")
    msg.exec_()

app = QApplication([])
button = QPushButton("Lancer la tâche")
button.clicked.connect(automate_task)
button.show()
app.exec_()


# https://www.riverbankcomputing.com/static/Docs/PyQt5/installation.html
# pip install PyQt5
# https://pypi.org/project/PyQt-builder/
# https://doc.qt.io/qtforpython-6/
# qt designer
# https://doc.qt.io/qt-6/qtdesigner-manual.html