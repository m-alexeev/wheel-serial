import sys
from utils import fill_combos
from ui.window import MainWindow
from PyQt6 import QtWidgets

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()

def execute_mainloop():
    fill_combos(window=window)
    
    window.show()
    app.exec()


if __name__ == "__main__":
    execute_mainloop()