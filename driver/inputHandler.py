from enum import Enum
from time import sleep
from pyvjoy.vjoydevice import VJoyDevice

"""
Input Handler

Handles serial input and executes joystick command

Author: Mikhail Alexeev
Last Modified: Nov 1, 2023
"""
ON = 0x1
OFF = 0x0

class InputType(Enum):
    BUTTON = 1
    JOYSTICK = 2


class InputHandler():
    def __init__(self, v_joy_device: VJoyDevice) -> None:
        self.v_joy = v_joy_device
        
    def process_input(self, data: str):
        input, value = data.split("|")
        if (input.upper() == InputType.BUTTON.name):
            self.button_press(value)
        if (input.upper() == InputType.JOYSTICK.name):
            axis, position = value.split("-")
            self.joystick_press(int(axis), int(position))
        
    def joystick_press(self, axis: int, position: int):
        self.v_joy.set_axis(axis, position)
        sleep(0.05)
        self.v_joy.reset()
    
    def button_press(self, button_id: int):
        self.v_joy.set_button(button_id, ON)
        sleep(0.05)
        self.v_joy.set_button(button_id, OFF)