import node
import controller
import os
from time import sleep


def speak(line):

    cmd = """osascript -e 'say "%s" with stopping current speech'""" % line
    os.system(cmd)

if __name__ == "__main__":

    #Connect controller
    contr = controller.Controller()
    contr.connectArduino()

    #New node
    i = [1, 'Hall', ['Light', 'Intercom', '1 Socket', '2 Socket'], [1, 0, 0, 0]]
    hallNode = node.Node(i)
    hallNode.printInformation()

    contr.setPin(13, hallNode.objectsState[0])
    print contr.digitalRead(13)
    contr.setPin(13, 0)
    print contr.digitalRead(13)
