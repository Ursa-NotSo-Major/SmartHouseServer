import serial
import glob
from parse import zeroer
from time import sleep


class Controller:

    global arduino
    global port

    def __init__(self):
        #Automatic port search
        tty = glob.glob("/dev/tty.*")
        for i in tty:
            if "usbmodem" in i:
                self.port = i

        self.arduino = None
        self.baudrate = 9600
        self.timeout = 1

    def connectArduino(self):
        try:
            self.arduino = serial.Serial(port=self.port, baudrate=self.baudrate, timeout=self.timeout)
            #Time needed to init serial connection
            sleep(2)
            if self.arduino:
                print "Arduino successfully connected"
        except:
            print "Failed to connect arduino"

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

    def digitalRead(self, pin):
        p = str(zeroer(pin, 2))
        self.arduino.write("c" + p + "d ")
        return int(self.arduino.readline())

    def analogRead(self, pin):
        p = str(zeroer(pin, 2))
        self.arduino.write("c" + p + "a ")
        return self.arduino.readline()