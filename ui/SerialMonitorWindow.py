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

        self.show_timestamp = True
        self.scroll_to_bottom = True

        self.received_data.connect(self.process_data)

        self.closeMonitor.clicked.connect(self.close)
        self.clearMonitor.clicked.connect(self.clear_monitor)
    
        self.timestampCheck.clicked.connect(self.toggle_timestamp)
        self.timestampCheck.setChecked(self.show_timestamp)
        self.scrollBottomCheck.clicked.connect(self.toggle_scroll_bottom)
        self.scrollBottomCheck.setChecked(self.scroll_to_bottom)

    def toggle_timestamp(self):
        self.show_timestamp = not self.show_timestamp

    def toggle_scroll_bottom(self):
        self.scroll_to_bottom = not self.scroll_to_bottom

    def clear_monitor(self):
        self.serialText.setText("")

    def process_data(self, data):
        # Append data to serial monitor 
        if (self.show_timestamp):
            data = f'{datetime.now().isoformat()} | {data}'
        current_text = self.serialText.text()
        new_text = current_text + data
        self.serialText.setText(new_text)

        if (self.scroll_to_bottom):
            # scroll to bottom of scroll view
            self.scrollArea.verticalScrollBar().setValue(self.scrollArea.verticalScrollBar().maximum())
