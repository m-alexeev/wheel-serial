from ui.generated.baudDialog import Ui_Dialog
from PyQt6.QtWidgets import QDialog

"""
BaudDialog

Dialog screen for selecting baud rates of the serial port

Author: Mikhail Alexeev
Last Modified: Nov 1, 2023
"""


class BaudDialog(QDialog, Ui_Dialog):
    """Dialog for selecting com port baudrate"""

    def __init__(self, parent: None) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self._populate_combo_box()
        self.baud_rate = None

    def _populate_combo_box(self):
        """
        Function for prepopulating the dropdown with some most used baudrates
        """
        baud_rates = [
            "110",
            "300",
            "600",
            "1200",
            "2400",
            "4800",
            "9600",
            "14400",
            "19200",
            "38400",
            "57600",
            "115200",
            "128000",
            "256000",
        ]
        self.baudCombo.addItems(baud_rates)

    def accept(self) -> None:
        """
        Extended accept function that is called from the default accept action
        of a dialog. Extended to only set a baudrate if one is selected
        """
        if self.baudCombo.currentIndex() > -1:
            self.baud_rate = self.baudCombo.currentText()
        return super().accept()
