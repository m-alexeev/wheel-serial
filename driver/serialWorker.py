from PyQt6.QtCore import QThread, pyqtSignal
from serial import Serial
from time import sleep

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
            sleep(0.5)
            # while ser.is_open and not self.stop_flag:
            #     while ser.in_waiting:
            #         # Reading COM Port
            #         data = ser.readline().decode('utf-8')
            #         self.received_input.emit(data)                    
        else:
            self.completed.emit()
    