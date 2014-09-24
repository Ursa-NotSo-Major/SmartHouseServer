import node, controller
from time import sleep
import os, glob

if __name__ == "__main__":

    #Connect controller
    contr = controller.Controller()
    contr.connectArduino()
    print contr.isConnected()

    #New node
    i = [1, 'Hall', ['Light', 'Intercom', '1 Socket'], [1, 0, 1]]
    hallNode = node.Node(i)
    hallNode.printInformation()
    contr.setPin(13, hallNode.objectsState[0])

