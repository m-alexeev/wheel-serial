import tkinter as tk
from commands import on_close, killThread, startThread
from utils import serial_ports

root = tk.Tk()
root.title("Wheel Serial")
root.eval("tk::PlaceWindow . center")

com_ports = serial_ports()

## Widgets

com_frame = tk.Frame(root).grid(row=0, padx=100, pady=50)
tk.Label(com_frame, text="COM Port").grid(row=0, column=0)
com_ports_choices = tk.StringVar(com_frame)
com_ports_choices.set(com_ports[0])

com_ports_menu = tk.OptionMenu(com_frame, com_ports_choices, *com_ports).grid(
    row=0, column=1, padx=10
)

submit_frame = tk.Frame(root).grid(row=1)

submit_button = tk.Button(
    submit_frame,
    text="Start",
    command=lambda: startThread(com_ports_choices),
    padx=10,
    pady=5,
).grid(row=1, column=1, pady=10)

stop_button = tk.Button(
    submit_frame,
    text="Stop",
    command=lambda: killThread(),
    padx=10,
    pady=5,
).grid(row=1, column=0, pady=10)


root.protocol("WM_DELETE_WINDOW", lambda: on_close(root))
