from serial import Serial
import time
# -x-x-x-x--x--x--x--x
class ArduinoController():

    def __init__(self, port: str, steppers: dict, **kwargs):
        self.port = port
        self.steppers = steppers
        self.baudrate = kwargs.get('baudrate', 9600)
        self.timeout = kwargs.get('timeout', 1)
        self.serial = Serial(self.port, self.baudrate, timeout=self.timeout)

    def confirmContact(self):
        byte_received = False
        while not byte_received:
            byte = self.serial.read()
            if byte == b'A':
                print('first contact attempt received')
                byte_received = True
        self.serial.flush()
        self.serial.write(b'A')
        self.serial.write(b'Mooie test gek');

        while True:
            self.serial.flush()
            print(self.serial.readline());


if __name__ == '__main__':
    x = ArduinoController('/dev/tty.usbmodem1411', {'sokd': None})
    x.confirmContact()
