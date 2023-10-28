from joystick.constants import BUTTON_INPUTS, JOY_INPUTS
from ui.MainWindow import Ui_MainWindow
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtCore import QFile, QTextStream
import os
import json


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs) -> None:
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.currentSaveFileName = None
        self.actionSave.triggered.connect(self.save_file)
        self.actionOpen.triggered.connect(self.open_file)

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
        
    def _load_config(self,file_name):
        if (not file_name):
            return
        with open(file_name, 'r') as file: 
            saved_config = json.load(file)
            joy_binds = saved_config.get("joystick_binds")
            button_binds = saved_config.get('button_binds')  
            for bind in joy_binds:
                if (joy_binds[bind] != ""):
                    self.joystick_combos[int(bind)].setCurrentText(joy_binds[bind])
            for bind in button_binds: 
                if (button_binds[bind] != ""):
                    self.button_combos[int(bind)].setCurrentText(button_binds[bind]) 
    
    def load_default_config(self):
        if (self.currentSaveFileName == None):
            current_dir = os.getcwd()
            self.currentSaveFileName = 'config.json'

        self._load_config(f"{current_dir}/{self.currentSaveFileName}")
        
            
        
    def save_file(self):
        file_name, _ = QFileDialog.getSaveFileName(self, 'Save File', os.getcwd(), "Json Files (*.json)")
        self.currentSaveFileName = file_name
        print(file_name)
        if (file_name):
            with open(file_name, 'w') as write_file:
                joystick_binds = {
                    i: combo.currentText() for i, combo in enumerate(self.joystick_combos)
                }
                button_binds = {
                    i: combo.currentText() for i, combo in enumerate(self.button_combos)
                }                
                write_file.write(json.dumps({
                    "joystick_binds": joystick_binds, 
                    "button_binds": button_binds
                }, indent=2))                
    
    def open_file(self):
        dialog = QFileDialog()
        file_name, _ = dialog.getOpenFileName(self, "Open File", "", "Json Files (*.json)")
        self._load_config(file_name)
                        
    