class ProgramInternalForm:
    def __init__(self):
        self.pif = []

    def add(self, code, index):
        self.pif.append((code, index))

    def get(self, index):
        return self.pif[index]

    def getLen(self):
        return len(self.pif)

    def __str__(self):
        return str(self.pif)

