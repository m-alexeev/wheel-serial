from driver.serialWorker import SerialWorker
import enum
from joystick.constants import BUTTON_INPUTS, JOY_INPUTS
import json
import os
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QFileDialog, QApplication
from ui.generated.MainWindow import Ui_MainWindow
from ui.baudDialog import BaudDialog
from ui.comDialog import ComDialog
from ui.closeDialog import CloseDialog
from ui.SerialMonitorWindow import SerialMonitor
from utils import serial_ports

"""
MainWindow

Main application GUI module reponsible for driving other modules,
saving and loading user configurations, and altering the wheel bindings
with use of a GUI

Author: Mikhail Alexeev
Last Modified: Nov 1, 2023
"""


class AppState(enum.Enum):
    """
    Enum for defining driver state constants
    """
    RUNNING = 1
    STOPPED = 2


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs) -> None:
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle("Wheel Binding Configurator")

        self._initialize_windows()
        self._initialize_actions()
        self._initialize_defaults()
        self._initialize_worker()
        self._initialize_combos()

        self.load_default_config()

    def _initialize_actions(self):
        """
        Internal function for creating all of the bindings
        """

        # Action bindings
        self.actionSave.triggered.connect(self.save_file)
        self.actionOpen.triggered.connect(self.open_file)
        self.actionSaveAs.triggered.connect(self.save_as_file)
        self.actionClose.triggered.connect(self.exit)

        # Driver Actions
        self.actionBaud.triggered.connect(self.baud_rate_dialog)
        self.actionCom.triggered.connect(self.com_port_dialog)
        self.actionRun.triggered.connect(self.start_driver)
        self.actionStop.triggered.connect(self.stop_driver)

        # Serial Monitor Actions
        self.actionSerialMonitor.triggered.connect(self.show_serial_monitor)

    def _initialize_defaults(self):
        """
        Internal function for defining default module variables
        """

        self.currentSaveFile = None
        self.unsaved_changes = False
        self.com_port = serial_ports()[0]
        self.baud_rate = 9600
        self.state = AppState.STOPPED

    def _initialize_windows(self):
        """
        Internal function for defining extra windows
        """

        self.serial_monitor = None

    def _initialize_worker(self):
        """
        Internal function for defining thread workers
        """

        self.serialWorker = SerialWorker(self.com_port, self.baud_rate)
        self.serialWorker.completed.connect(self.driver_completed)
        self.serialWorker.received_input.connect(self.process_input)

    def _initialize_combos(self):
        """
        Internal function for prepopulating dropdown options
        """

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
        """
        Trigger to start the serial port worker
        """

        # Disable com and baudrate dialogs
        self.actionBaud.setEnabled(False)
        self.actionCom.setEnabled(False)

        # Start Thread
        self.serialWorker.stop_flag = False

        self.serialWorker.start()
        self.state = AppState.RUNNING
        self.driverStateLabel.setText(self.state.name)

    def stop_driver(self):
        """
        Trigger to stop serial port worker
        """

        if self.serialWorker.isRunning:
            self.serialWorker.stop_flag = True
        self.state = AppState.STOPPED
        self.driverStateLabel.setText(self.state.name)

    def driver_completed(self):
        """
        Callback that is executed when serial port worker completes
        """

        print("Thread Completed")
        # Enable com and baudrate dialogs
        self.actionBaud.setEnabled(True)
        self.actionCom.setEnabled(True)

    def _load_config(self, file_name: str):
        """
        Internal function to load user configuration and populate dropdown

        Args:
            file_name: Path to config file
        """

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
        """
        Load default configuration at launch
        """

        if self.currentSaveFile is None:
            home_dir = os.path.expanduser("~")
            self.currentSaveFile = os.path.join(home_dir, "wheel_binds.json")

        self._load_config(self.currentSaveFile)

    def _write_to_file(self):
        """
        Internal function to dump config to a file
        """

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
        """
        Trigger to execute save command
        """

        if not self.currentSaveFile:
            file_name, _ = QFileDialog.getSaveFileName(
                self, "Save File", os.getcwd(), "Json Files (*.json)"
            )
            self.currentSaveFile = file_name

        self._write_to_file()

    def save_as_file(self):
        """
        Trigger to execute Save As command
        """

        file_name, _ = QFileDialog.getSaveFileName(
            self, "Save File", os.getcwd(), "Json Files (*.json)"
        )
        self.currentSaveFile = file_name

        self._write_to_file()

    def open_file(self):
        """
        Trigger to open a file
        """

        dialog = QFileDialog()
        file_name, _ = dialog.getOpenFileName(
            self, "Open File", "", "Json Files (*.json)"
        )
        self._load_config(file_name)

    def closeEvent(self, evnt):
        """
        Overiding main window close event to display a warning popup if file is not saved

        Args:
            evnt: Close event
        """

        if self.unsaved_changes:
            closeDialog = CloseDialog(self)
            res = closeDialog.exec()
            # Don't close window if dialog answer was no
            if res == 0:
                evnt.ignore()

    def on_combo_box_changed(self):
        """
        Trigger to set unsaved changes flag
        """

        self.setWindowTitle("Wheel Binding Configurator *")
        self.unsaved_changes = True

    def baud_rate_dialog(self):
        """
        Trigger to open baudrate dialog
        """

        baud_dialog = BaudDialog(self)
        accepted = baud_dialog.exec()
        if accepted:
            self.baud_rate = int(baud_dialog.baud_rate)
            self.serialWorker.set_baudrate(self.baud_rate)

    def com_port_dialog(self):
        """
        Trigger to open com port selection dialog
        """

        com_port_dialog = ComDialog(self)
        accepted = com_port_dialog.exec()
        if accepted:
            self.com_port = com_port_dialog.com_port
            self.serialWorker.set_port(self.com_port)

    def show_serial_monitor(self):
        """
        Trigger to open serial monitor
        """

        if self.serial_monitor is None:
            self.serial_monitor = SerialMonitor()
            self.serial_monitor.show()
        else:
            self.serial_monitor.close()
            self.serial_monitor = None

    def process_input(self, data: str):
        """
        Callback from worker thread upon receiving input from serial port

        Args:
            data: String data from serial port
        """

        if self.serial_monitor is not None:
            # Send data to serial monitor
            self.serial_monitor.received_data.emit(data)

    def exit(self):
        """
        Exit Trigger
        """
        closeDialog = CloseDialog(self)
        accepted = closeDialog.exec()

        if accepted:
            self.close()
