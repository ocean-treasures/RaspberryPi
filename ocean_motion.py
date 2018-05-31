import serial
from serial.tools import list_ports


class Motor(serial.Serial):

    def __init__(self, name, timeout=0):
        self.device = Motor.find_device(name)
        super().__init__(self.device, timeout=timeout, write_timeout=timeout)

    @staticmethod
    def find_device(name):
        for device in list_ports.comports():
            if device.device.find(name) > -1:
                return device.device

    def up(self, steps):
        cmd = "U{}\r\n".format(steps)
        self.write(cmd.encode())

    def down(self, steps):
        cmd = "D{}\r\n".format(steps)
        self.write(cmd.encode())


motor = Motor(Motor.find_device('/'))
