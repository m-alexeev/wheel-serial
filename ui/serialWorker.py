from PyQt6.QtCore import QThread, pyqtSignal
from serial import Serial

class SerialWorker(QThread):
    completed = pyqtSignal()
    received_input = pyqtSignal(str)
    
    stop_flag = False

    def run(self):
        # READ serial port
        ser = Serial()
        while not self.stop_flag: 
            while ser.is_open:
                while ser.in_waiting:
                    data = ser.readline().decode('utf-8')
                    print(data)
        else:
            self.completed.emit()
    