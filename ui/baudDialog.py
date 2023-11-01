from ui.generated.baudDialog import Ui_Dialog
from PyQt6.QtWidgets import QDialog


class BaudDialog(QDialog, Ui_Dialog):
    """Dialog for selecting com port baudrate"""

    def __init__(self, parent: None) -> None:
        super().__init__(parent)
        self.setupUi(self)

        self._populate_combo_box()
        self.baud_rate = None

    def _populate_combo_box(self):
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
        if self.baudCombo.currentIndex() > -1:
            self.baud_rate = self.baudCombo.currentText()
        return super().accept()
