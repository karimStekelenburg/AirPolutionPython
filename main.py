import serial

class Serializer():
    def __init__(self, port, baut, timeout):
        self.serial = serial.Serial(port, baut, timeout=timeout)
        self.start_char = 'S'
        self.end_char = 'E'
        self.stopped = False

        self.command = ""


    def sendPositions(self, flPos, fmPos, frPos, mlPos, mmPos, mrPos, blPos, bmPos, brPos):
        command = 'POS'+ str(flPos) + str(fmPos) + str(frPos) + str(mlPos) + str(mmPos) + str(mrPos) + str(blPos) + str(bmPos)
        self.serial.write(command.encode('utf-8'))

    def moveSingleStepper(self, stepperId, direction, steps):
        command = "MVE" + ':' + stepperId + ',' + direction + ',' + steps + ':' + self.end_char;
        self.serial.write(command)

    def calibrate(self):
        command = "CAL";
        self.serial.write(command)

    def stop(self):
        command = "STP";
        self.serial.write(command)


if __name__ == '__main__':
    s = Serializer('/dev/tty.usbmodem1421', 9600, 1)

    while True:
        s.sendPositions(10,20,10,30,20,10,30,40,50)
        print(s.serial.readline())
