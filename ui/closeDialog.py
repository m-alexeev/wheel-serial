from PyQt6.QtWidgets import QDialog
from ui.generated.closeDialog import Ui_Dialog

"""
Close Dialog

Dialog screen that prevents and app from closing if 
user has unsaved changes

Author: Mikhail Alexeev
Last Modified: Nov 1, 2023
"""

class CloseDialog(QDialog, Ui_Dialog):
    """Close dialog."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
