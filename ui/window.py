from ui.MainWindow import Ui_MainWindow
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtCore import QFile, QTextStream
import os

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs) -> None:
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.actionSave.triggered.connect(self.save_file)
        self.actionOpen.triggered.connect(self.open_file)
    
    def save_file(self):
        file_name, _ = QFileDialog.getSaveFileName(self, 'Save File', os.getcwd())
        if (file_name):
            with open(file_name, 'w') as write_file:
                # Dump config as a json serialized object
                pass
    
    def open_file(self):
        dialog = QFileDialog()
        file_name, _ = dialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;All Files (*)")

        if (file_name):
            file = QFile(file_name)
            if file.open(QFile.OpenModeFlag.ReadOnly | QFile.OpenModeFlag.Text):
                stream = QTextStream(file)
                # Read file and write changes into combo boxes
                print(stream.readAll())
                file.close()
                
    