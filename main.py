import node
import controller
from time import sleep

if __name__ == "__main__":

    #Connect controller
    contr = controller.Controller("/dev/tty.usbmodemfa131", 9600)
    contr.connectArduino()
    print contr.isConnected()

    #New node
    i = [1, 'Hall', ['Light', 'Intercom', '1 Socket'], [1, 0, 1]]
    hallNode = node.Node(i)
    hallNode.printInformation()

    contr.setPin(13, hallNode.objectsState[0])
    sleep(2)
    contr.setPin(13, hallNode.objectsState[1])

