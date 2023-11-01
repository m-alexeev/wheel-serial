from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import pyqtSignal
from ui.generated.SerialMonitor import Ui_Frame
from datetime import datetime

class SerialMonitor(QWidget, Ui_Frame):
    """Serial Monitor Window"""
    received_data = pyqtSignal(str)

    def __init__(self): 
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Serial Monitor")

        self.received_data.connect(self.process_data)

        self.closeMonitor.clicked.connect(self.close)
        self.clearMonitor.clicked.connect(self.clear_monitor)
    

    def clear_monitor(self):
        self.serialText.setText("")

    def process_data(self, data):
        # Append data to serial monitor 
        data = f'{datetime.now().isoformat()} | {data}'
        current_text = self.serialText.text()
        new_text = current_text + data
        self.serialText.setText(new_text)

