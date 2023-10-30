from PyQt6.QtCore import QObject, pyqtSignal
from time import sleep

class SerialWorker(QObject):
    completed = pyqtSignal()
    received_input = pyqtSignal(str)
    
    stop_flag = False

    def run(self):
        # READ serial port
        while not self.stop_flag: 
            print('Running')
        else:
            self.completed.emit()
    