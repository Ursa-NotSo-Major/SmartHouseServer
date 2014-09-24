def zeroer(string, val):
    string = str(string)
    for i in range(0, int(val) - len(string)):
        string = "0" + string
    return str(string)
