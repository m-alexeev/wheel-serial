from PyQt6.QtWidgets import QDialog
from ui.generated.closeDialog import Ui_Dialog

class CloseDialog(QDialog, Ui_Dialog):
    """Close dialog."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)