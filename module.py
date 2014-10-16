class Module:

    def __init__(self, settings):
        self.ID = settings[0]
        self.name = settings[1]
        self.objects = settings[2]
        self.objectsState = settings[3]
        self.objectCount = len(self.objects)

    def refreshNode(self, settings):
        self.ID = settings[0]
        self.name = settings[1]
        self.objects = settings[2]
        self.objectsState = settings[3]
        self.objectCount = len(self.objects)
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
        print "Objects count: ", self.objectCount
        print
        for i in range(len(self.objects)):
            print self.objects[i], ":", self.objectsState[i]
        print
