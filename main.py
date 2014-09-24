import node
import controller
from time import sleep

if __name__ == "__main__":

    #Connect controller
    contr = controller.Controller("/dev/tty.usbmodemfa131", 9600)
    contr.connect()
    print contr.isConnected()

    sleep(1)
    contr.disconnect()
    print contr.isConnected()



    # #New node
    # i = [1, 'Hall', ['Light', 'Intercom', '1 Socket'], [1, 0, 1]]
    # hallNode = node.Node(i)
    # hallNode.printInformation()


