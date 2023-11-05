from driver.inputHandler import InputHandler
from time import sleep
from serial import Serial
from PyQt6.QtCore import QThread, pyqtSignal

"""
SerialWorker

Worker Thread that runs separately from UI thread
to avoid blocking and reads the serial port sending
updates to caller

Author: Mikhail Alexeev
Last Modified: Nov 1, 2023
"""


class SerialWorker(QThread):
    completed = pyqtSignal()
    received_input = pyqtSignal(str)

    stop_flag = False

    def __init__(self, port, baudrate) -> None:
        super().__init__()
        self.port = port
        self.baudrate = baudrate
        # self.inputHandler = InputHandler()

    def set_port(self, port):
        self.port = port

    def set_baudrate(self, baudrate):
        self.baudrate = baudrate

    def run(self):
        # READ serial port
        ser = Serial(self.port, self.baudrate, timeout=0)
        while not self.stop_flag:
            while ser.is_open and not self.stop_flag:
                while ser.in_waiting:
                    # Reading COM Port
                    data = ser.readline().decode('utf-8')
                    # self.inputHandler.process_input("")
                    self.received_input.emit(data)
                    sleep(0.1)
        else:
            self.completed.emit()
