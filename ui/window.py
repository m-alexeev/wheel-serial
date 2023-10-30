from joystick.constants import BUTTON_INPUTS, JOY_INPUTS
from ui.generated.MainWindow import Ui_MainWindow
from ui.baudDialogWindow import BaudDialog
from ui.comDialogWindow import ComDialog
from ui.closeDialogWindow import CloseDialog
from ui.serialWorker import SerialWorker
from PyQt6 import QtWidgets
from PyQt6.QtCore import QThread
from PyQt6.QtWidgets import QFileDialog
from utils import serial_ports
import os
import json
import enum


class AppState(enum.Enum):
    RUNNING = 1
    STOPPED = 2

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs) -> None:
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle("Wheel Binding Configurator")

        self.currentSaveFile = None

        # Action bindings
        self.actionSave.triggered.connect(self.save_file)
        self.actionOpen.triggered.connect(self.open_file)
        self.actionSaveAs.triggered.connect(self.save_as_file)
        self.actionClose.triggered.connect(self.exit)
        self.actionBaud.triggered.connect(self.baud_rate_dialog)
        self.actionCom.triggered.connect(self.com_port_dialog)
        self.actionRun.triggered.connect(self.start_driver)
        self.actionStop.triggered.connect(self.stop_driver)

        self.serialThread = QThread()
        self.serialWorker = SerialWorker()
        self.serialWorker.moveToThread(self.serialThread)


        self.unsaved_changes = False
        self.com_port = serial_ports()[0]
        self.baud_rate = 9600
        self.state = AppState.STOPPED

        self.initialize_combos()

        self.load_default_config()

    def initialize_combos(self):
        self.joystick_combos = [
            self.joycombo_1,
            self.joycombo_2,
            self.joycombo_3,
            self.joycombo_4,
            self.joycombo_5,
            self.joycombo_6,
            self.joycombo_7,
            self.joycombo_8,
        ]

        self.button_combos = [
            self.buttoncombo_1,
            self.buttoncombo_2,
            self.buttoncombo_3,
            self.buttoncombo_4,
            self.buttoncombo_5,
            self.buttoncombo_6,
            self.buttoncombo_7,
            self.buttoncombo_8,
            self.buttoncombo_9,
            self.buttoncombo_10,
            self.buttoncombo_11,
            self.encodercombo_1,
            self.encodercombo_2,
            self.encodercombo_3,
            self.encodercombo_4,
            self.togglecombo_1,
            self.togglecombo_2,
            self.togglecombo_3,
            self.togglecombo_4,
            self.rotencodercombo_1,
            self.rotencodercombo_2,
            self.rotencodercombo_3,
            self.rotencodercombo_4,
            self.rotencodercombo_5,
            self.rotencodercombo_6,
            self.rotencodercombo_7,
            self.rotencodercombo_8,
            self.rotencodercombo_9,
            self.rotencodercombo_10,
            self.rotencodercombo_11,
            self.rotencodercombo_12,
            self.rotencodercombo_13,
            self.rotencodercombo_14,
            self.rotencodercombo_15,
            self.rotencodercombo_16,
        ]

        for combo in self.joystick_combos:
            combo.addItems(JOY_INPUTS)

        for combo in self.button_combos:
            combo.addItems(BUTTON_INPUTS)

    def start_driver(self):
        self.serialWorker.stop_flag = False
        self.serialThread.started.connect(self.serialWorker.run)
        self.serialWorker.completed.connect(self.driver_completed)
        
        self.serialThread.start()
        self.state = AppState.RUNNING
        self.driverStateLabel.setText(self.state.name)
    
    def stop_driver(self):
        if (self.serialThread and self.serialThread.isRunning):
            self.serialWorker.stop_flag = True
        self.state = AppState.STOPPED
        self.driverStateLabel.setText(self.state.name)
    
    def driver_completed(self):
        print("Thread Completed")

    def _load_config(self, file_name):
        if not os.path.isfile(file_name):
            return
        with open(file_name, "r") as file:
            saved_config = json.load(file)
            joy_binds = saved_config.get("joystick_binds")
            button_binds = saved_config.get("button_binds")
            for bind in joy_binds:
                if joy_binds[bind] != "":
                    self.joystick_combos[int(bind)].setCurrentText(joy_binds[bind])
            for bind in button_binds:
                if button_binds[bind] != "":
                    self.button_combos[int(bind)].setCurrentText(button_binds[bind])

        # Set current combo box state
        for combo in self.joystick_combos:
            combo.currentIndexChanged.connect(self.on_combo_box_changed)

        for combo in self.button_combos:
            combo.currentIndexChanged.connect(self.on_combo_box_changed)

    def load_default_config(self):
        if self.currentSaveFile == None:
            home_dir = os.path.expanduser("~")
            self.currentSaveFile = os.path.join(home_dir, "wheel_binds.json")

        self._load_config(self.currentSaveFile)

    def _write_to_file(self):
        if self.currentSaveFile:
            with open(self.currentSaveFile, "w") as write_file:
                joystick_binds = {
                    i: combo.currentText()
                    for i, combo in enumerate(self.joystick_combos)
                }
                button_binds = {
                    i: combo.currentText() for i, combo in enumerate(self.button_combos)
                }
                write_file.write(
                    json.dumps(
                        {
                            "joystick_binds": joystick_binds,
                            "button_binds": button_binds,
                        },
                        indent=2,
                    )
                )
            self.unsaved_changes = False
            self.setWindowTitle("Wheel Binding Configurator")

    def save_file(self):
        if not self.currentSaveFile:
            file_name, _ = QFileDialog.getSaveFileName(
                self, "Save File", os.getcwd(), "Json Files (*.json)"
            )
            self.currentSaveFile = file_name

        self._write_to_file()

    def save_as_file(self):
        file_name, _ = QFileDialog.getSaveFileName(
            self, "Save File", os.getcwd(), "Json Files (*.json)"
        )
        self.currentSaveFile = file_name

        self._write_to_file()

    def open_file(self):
        dialog = QFileDialog()
        file_name, _ = dialog.getOpenFileName(
            self, "Open File", "", "Json Files (*.json)"
        )
        self._load_config(file_name)


    def closeEvent(self, evnt):
        if self.unsaved_changes:
            closeDialog = CloseDialog(self)
            res = closeDialog.exec()
            # Don't close window if dialog answer was no
            if res == 0:
                evnt.ignore()

    def on_combo_box_changed(self):
        self.setWindowTitle("Wheel Binding Configurator *")
        self.unsaved_changes = True

    def exit(self):
        closeDialog = CloseDialog(self)
        accepted = closeDialog.exec()

        if accepted:
            self.close()

    def _receive_baudrate(value):
        print(value)

    def baud_rate_dialog(self):
        baud_dialog = BaudDialog(self)
        accepted = baud_dialog.exec()
        if (accepted):
            self.baud_rate = int(baud_dialog.baud_rate)
        print(self.baud_rate)

    def com_port_dialog(self):
        com_port_dialog = ComDialog(self)
        accepted = com_port_dialog.exec()
        if (accepted):
            self.com_port = com_port_dialog.com_port
        print(self.com_port)




