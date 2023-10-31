from PyQt6.QtWidgets import QDialog
from ui.generated.SerialMonitor import Ui_Dialog


class SerialMonitorDialog(QDialog, Ui_Dialog):
    """Serial Monitor Window"""

    def __init__(self, parent = None): 
        super().__init__(parent)
        self.setupUi(self)

        self.closeMonitor.clicked.connect(self.close)
        self.clearMonitor.clicked.connect(self.clear_monitor)
    
    def clear_monitor(self):
        pass