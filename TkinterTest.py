import tkinter as tk
from tkinter import ttk
import serial.tools.list_ports as COM_PORT_LIST

def on_select(event):
    selected_value = combobox_comport.get()
    label.config(text=f"Selected: {selected_value}")

root = tk.Tk()
root.title("Tkinter Combobox Example")

label = tk.Label(root, text="Selected: ")
label.pack(pady=10)

ports = COM_PORT_LIST.comports()
options = []
for port, desc, hwid in sorted(ports):
    options.append(desc)

combobox_comport = ttk.Combobox(root, values=options)
combobox_comport.pack(pady=10)
combobox_comport.set("Select an option") 
combobox_comport.bind("<<ComboboxSelected>>", on_select)

root.mainloop()