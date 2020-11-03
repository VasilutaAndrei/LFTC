from hashTable import HashTable


class SymbolTable:
    def __init__(self):
        self.symTable = HashTable(40)

    def getSymTable(self):
        return self.symTable

    def getHashAtIndex(self, index):
        return self.symTable.hashTable[index]

    def addSymbol(self, key):
        position = self.symTable.add(key)
        return position

    def getTokenPosition(self, token):
        return self.symTable.getPosition(token)
