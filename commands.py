from threading import Thread
from keyboard import PressKey, ReleaseKey
from serial import Serial
from time import sleep
from tkinter import StringVar

NONE = 0x80
SHIFT = 0x81
CTRL = 0x82
ALT = 0x83


def NormalPress(keycode: int) -> None:
    PressKey(keycode)
    sleep(0.1)
    ReleaseKey(keycode)


def ModPress(keycode: int, mod: int) -> None:
    if mod == SHIFT:
        mod = 0x10
    elif mod == CTRL:
        mod = 0x11
    elif mod == ALT:
        mod = 0xA4
    PressKey(mod)
    PressKey(keycode)
    sleep(0.1)
    ReleaseKey(keycode)
    ReleaseKey(mod)


KILL = False

def killThread(thread: Thread ):
    global KILL
    KILL = not KILL
    thread.join()

def on_close(root, thread: Thread):
    if thread.is_alive():
        killThread(thread=thread)
    root.destroy()

def readSerial(port: StringVar, baudrate=9600):
    print(port)
    port = port.get()
    print(port)

    ser = Serial(port, baudrate, timeout=0)
    while ser.is_open:
        if KILL:
            return 
        while ser.in_waiting:
            data = ser.readline().decode("utf-8")
            data = data[:-1]
            mod = int(data[:8], 2)
            keycode = data[-8:]
            keycode = int(keycode, 2)
            if mod == NONE:
                NormalPress(keycode=keycode)
            else:
                ModPress(keycode, mod)
        sleep(0.1)


