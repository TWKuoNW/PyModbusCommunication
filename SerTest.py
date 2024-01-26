import serial.tools.list_ports as COM_PORT_LIST

ports = COM_PORT_LIST.comports()
print(ports)

options = []
for port, desc, hwid in sorted(ports):
    options.append(desc)

print(type(port))
print(options)