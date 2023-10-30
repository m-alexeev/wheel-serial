from ui.generated.comDialog import Ui_Dialog
from PyQt6.QtWidgets import QDialog
from utils import serial_ports

class ComDialog(QDialog, Ui_Dialog):
    """Dialog for selecting the desired com port"""

    def __init__(self, parent: None) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self._populate_combo_box()
        self.com_port = None
    
    def _populate_combo_box(self):
        com_ports = serial_ports()
        self.portCombo.addItems(com_ports)

    def accept(self) -> None:
        if (self.portCombo.currentIndex() > -1):
            self.com_port = self.portCombo.currentText()
        return super().accept()

