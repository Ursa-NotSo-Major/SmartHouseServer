import node
import controller
import os
from time import sleep

if __name__ == "__main__":

    #Connect controller
    contr = controller.Controller()
    contr.connectArduino()

    #New node
    i = [1, 'Hall', ['Light', 'Intercom', '1 Socket', '2 Socket'], [1, 0, 0, 0]]
    hallNode = node.Node(i)
    hallNode.printInformation()

    contr.setPin(13, hallNode.objects[0])
    
