class Node:

    def __init__(self, initInformation):
        self.ID = initInformation[0]
        self.name = initInformation[1]
        self.objects = initInformation[2]
        self.objectsState = initInformation[3]

    def refreshNode(self, newValues):
        self.ID = newValues[0]
        self.name = newValues[1]
        self.objects = newValues[2]
        self.objectsState = newValues[3]
        print "_______________________________________________"
        print "   Node ", self.name, "Refreshed"
        self.printInformation()
        print

    def refreshState(self, newStates):
        self.objectsState = newStates
        print "_______________________________________________"
        print "   States in Node", '-', self.ID, self.name, '-',  "Refreshed"
        print

    def printInformation(self):
        print "_______________________________________________"
        print "Node ID:", self.ID
        print "Node Name:", self.name
        print "Objects in Node:", self.objects
        print
        for i in range(len(self.objects)):
            print self.objects[i], ":", self.objectsState[i]
        print
