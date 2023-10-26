from pyvjoy.vjoydevice import VJoyDevice
from time import sleep
from constants import ON, OFF

joystick = VJoyDevice(1)


def joystick_position(joystick: VJoyDevice, axis: int, position: int):
    joystick.set_axis(axis, position)


def press_button(joystick: VJoyDevice, button_id: int):
    joystick.set_button(button_id, ON)
    sleep(0.05)
    joystick.set_button(button_id, OFF)

