from threading import Event, Thread, activeCount
from deprecated.keyboard import PressKey, ReleaseKey
from serial import Serial
from time import sleep
from tkinter import StringVar

NONE = 0x80
SHIFT = 0x81
CTRL = 0x82
ALT = 0x83

SER_THREADS = []


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


class ThreadWrapper:
    def __init__(self, event: Event, thread: Thread) -> None:
        self.thread = thread
        self.event = event

    def stop(self):
        self.event.set()
        self.thread.join()


class SerialThread(Thread):
    def __init__(self, event: Event, port: str, baudrate=9600):
        super(SerialThread, self).__init__()
        self.event = event
        self.port = port
        self.baudrate = baudrate

    def run(self):
        ser = Serial(self.port, self.baudrate, timeout=0)
        while ser.is_open:
            # Kill loop
            if self.event.is_set():
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


def startThread(dropdown_port: StringVar):
    port = dropdown_port.get()
    event = Event()
    thread = SerialThread(event, port)
    thread.start()
    SER_THREADS.append(ThreadWrapper(event, thread))


def killThread():
    if SER_THREADS:
        container = SER_THREADS.pop()
        container.stop()


def on_close(root):
    killThread()
    root.destroy()


def readSerial(port: StringVar, baudrate=9600):
    port = port.get()
    ser = Serial(port, baudrate, timeout=0)
    while ser.is_open:
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
