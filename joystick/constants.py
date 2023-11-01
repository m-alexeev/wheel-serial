from pyvjoy import HID_USAGE_X, HID_USAGE_RX, HID_USAGE_Y, HID_USAGE_RY

MIN = 0x1
MAX = 0x8000

ON = 0x1
OFF = 0x0

NUM_BUTTONS = 40

BUTTON_INPUTS = [f"Button {i + 1}" for i in range(NUM_BUTTONS)]

JOY_INPUTS = [
    "Left Joystick | Up",
    "Left Joystick | Down",
    "Left Joystick | Left",
    "Left Joystick | Right",
    "Right Joystick | Up",
    "Right Joystick | Down",
    "Right Joystick | Left",
    "Right Joystick | Right",
]

INPUT_AXIS_MAPPING = {
    "Left": {
        "Left": {"axis": HID_USAGE_X, "value": MIN},
        "Right": {"axis": HID_USAGE_X, "value": MAX},
        "Up": {"axis": HID_USAGE_Y, "value": MIN},
        "Down": {"axis": HID_USAGE_Y, "value": MAX},
    },
    "Right": {
        "Left": {"axis": HID_USAGE_RX, "value": MIN},
        "Right": {"axis": HID_USAGE_RX, "value": MAX},
        "Up": {"axis": HID_USAGE_RY, "value": MIN},
        "Down": {"axis": HID_USAGE_RY, "value": MAX},
    },
}
