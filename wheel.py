import sys
from ui.window import MainWindow
from PyQt6 import QtWidgets

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()

def execute_mainloop():
    
    window.show()
    app.exec()


if __name__ == "__main__":
    execute_mainloop()