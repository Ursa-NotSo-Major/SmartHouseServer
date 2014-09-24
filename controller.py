import serial
from parse import zeroer
from time import sleep


class Controller:

    global arduino

    def __init__(self, port, baudrate):
        self.arduino = None
        self.port = port
        self.baudrate = baudrate

    def connectArduino(self):
        self.arduino = serial.Serial(self.port, self.baudrate, timeout=1)
        #Time needed to init serial connection
        sleep(2)
        if self.arduino:
            print "Arduino successfully connected"

    def disconnectArduino(self):
        if self.arduino.isOpen():
            self.arduino.close()
            print "Arduino successfully disconnected"
        else:
            print "The connection is closed."

    def isConnected(self):
            return self.arduino.isOpen()

    def readLine(self):
        return self.arduino.readline()

    def read(self, chars):
        return self.arduino.read(chars)

    def write(self, command):
        self.arduino.write(command + '\r')

    def setPin(self, pin, value):
        command = "s" + str(zeroer(pin, 2)) + str(zeroer(value, 3)) + " "
        self.arduino.write(command)
        print "Command: " + command
        sleep(0.001)
