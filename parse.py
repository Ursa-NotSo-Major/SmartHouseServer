def zeroer(string, val):
    string = str(string)
    for i in range(0, int(val) - len(string)):
        string = "0" + string
    return str(string)


def fromServerToController(array):
    string = ""
    for i in range(0, len(array)):
        string += str(array[i])
    return string