import serial
from parse import zeroer
from time import sleep


class Controller:

    global arduino

    def __init__(self, port, baudrate):
        self.arduino = None
        self.port = port
        self.baudrate = baudrate

    def connect(self):
        self.arduino = serial.Serial(self.port, self.baudrate)
        #Time for arduino to initialise
        sleep(2)
        if self.arduino:
            print
            print "Arduino successfully connected!"
            print

    def disconnect(self):
        self.arduino.close()
        print
        print "Arduino successfully disconnected!"
        print

    def isConnected(self):
        try:
            return self.arduino.isOpen()
        except:
            return False

    def read(self, chars):
        return self.arduino.read(chars)

    def setPin(self, pin, value):
        command = "s" + str(zeroer(pin, 2)) + str(zeroer(value, 3)) + " "
        self.arduino.write(command)
        print "Command: " + command
        sleep(0.001)
