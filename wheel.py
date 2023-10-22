import sys
from PyQt6 import QtWidgets
from MainWindow import Ui_MainWindow
from joy_constants import JOY_LIST, BUTTON_LIST


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs) -> None:
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()

joystick_combos = [
    window.joycombo_1,
    window.joycombo_2,
    window.joycombo_3,
    window.joycombo_4,
    window.joycombo_5, 
    window.joycombo_6,
    window.joycombo_7,
    window.joycombo_8,
]

button_combos = [
    window.buttoncombo_1,
    window.buttoncombo_2,
    window.buttoncombo_3,
    window.buttoncombo_4,
    window.buttoncombo_5,
    window.buttoncombo_6,
    window.buttoncombo_7,
    window.buttoncombo_8,
    window.buttoncombo_9,
    window.buttoncombo_10,
    window.buttoncombo_11,
    window.encodercombo_1,
    window.encodercombo_2,
    window.encodercombo_3,
    window.encodercombo_4,
    window.togglecombo_1,
    window.togglecombo_2,
    window.togglecombo_3,
    window.togglecombo_4,
    window.rotencodercombo_1,
    window.rotencodercombo_2,
    window.rotencodercombo_3,
    window.rotencodercombo_4,
    window.rotencodercombo_5,
    window.rotencodercombo_6,
    window.rotencodercombo_7,
    window.rotencodercombo_8,
    window.rotencodercombo_9,
    window.rotencodercombo_10,
    window.rotencodercombo_11,
    window.rotencodercombo_12,
    window.rotencodercombo_13,
    window.rotencodercombo_14,
    window.rotencodercombo_15,
    window.rotencodercombo_16,
]



for combo in joystick_combos:
    combo.addItems(JOY_LIST)

for combo in button_combos:
    combo.addItems(BUTTON_LIST)

window.show()
app.exec()
