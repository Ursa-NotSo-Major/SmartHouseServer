import module
import controller
import os
from time import sleep
import parse

if __name__ == "__main__":

    contr = controller.Controller()
    if contr.connectArduino():
        settings = [1, 'Hall', ['Light', 'Intercom', '1 Socket', '2 Socket'], [1, 0, 0, 0]]
        hallNode = module.Module(settings)
        hallNode.printInformation()
        print contr.analogRead(0)

    contr.isConnected()