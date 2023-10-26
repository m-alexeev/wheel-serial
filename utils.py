import sys
import glob
import os
import serial
from joystick.constants import JOY_INPUTS, BUTTON_INPUTS
from ui.window import MainWindow
from PyQt6 import QtGui

# https://stackoverflow.com/questions/12090503/listing-available-com-ports-with-python
def serial_ports():
    """Lists serial port names

    :raises EnvironmentError:
        On unsupported or unknown platforms
    :returns:
        A list of the serial ports available on the system
    """
    if sys.platform.startswith("win"):
        ports = ["COM%s" % (i + 1) for i in range(256)]
    elif sys.platform.startswith("linux") or sys.platform.startswith("cygwin"):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob("/dev/tty[A-Za-z]*")
    elif sys.platform.startswith("darwin"):
        ports = glob.glob("/dev/tty.*")
    else:
        raise EnvironmentError("Unsupported platform")

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result



def fill_combos(window: MainWindow):
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
        combo.addItems(JOY_INPUTS)

    for combo in button_combos:
        combo.addItems(BUTTON_INPUTS)
    
    return button_combos, joystick_combos


