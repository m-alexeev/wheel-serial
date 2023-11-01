from ui.generated.comDialog import Ui_Dialog
from PyQt6.QtWidgets import QDialog
from utils import serial_ports

"""
ComDialog

Dialog screen for selecting com port from list
of available windows com ports

Author: Mikhail Alexeev
Last Modified: Nov 1, 2023
"""


class ComDialog(QDialog, Ui_Dialog):
    """Dialog for selecting the desired com port"""

    def __init__(self, parent: None) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self._populate_combo_box()
        self.com_port = None

    def _populate_combo_box(self):
        """
        Prepulate com port dropdown
        """
        com_ports = serial_ports()
        self.portCombo.addItems(com_ports)

    def accept(self) -> None:
        """
        Extend dialog accept callback to only
        set com port if a value is selected
        """
        if self.portCombo.currentIndex() > -1:
            self.com_port = self.portCombo.currentText()
        return super().accept()
