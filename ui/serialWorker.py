import typing
from PyQt6.QtCore import QObject, QThread, pyqtSignal
from serial import Serial

class SerialWorker(QThread):
    completed = pyqtSignal()
    received_input = pyqtSignal(str)
    
    stop_flag = False

    def __init__(self, port, baudrate) -> None:
        super().__init__()
        self.port = port 
        self.baudrate = baudrate

    def setPort(self, port):
        self.port = port
    
    def setBaudrate(self, baudrate): 
        self.baudrate = baudrate


    def run(self):
        # READ serial port
        ser = Serial(self.port,  self.baudrate, timeout=0)
        while not self.stop_flag: 
            while ser.is_open and not self.stop_flag:
                while ser.in_waiting:
                    # Reading COM Port
                    data = ser.readline().decode('utf-8')
                    print(data)
        else:
            self.completed.emit()
    