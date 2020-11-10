class Scanner:
    def __init__(self):
        self.FA = ''

    def setFA(self, FA):
        self.FA = FA

    def readSetOfStates(self, line):
        for state in line.strip().split(','):
            self.FA.addState(state)

    def readAlphabet(self, line):
        for letter in line.strip().split(','):
            self.FA.addAlphabet(letter)

    def readStartingSymbol(self, line):
        self.FA.setStartingSymbol(line.strip())

    def readFinalStates(self, line):
        for state in line.strip().split(','):
            self.FA.addFinalState(state)

    def readTransition(self, line):
        transition = line.strip().split('=')
        left = transition[0].split(',')
        right = transition[1]
        self.FA.addTransition(((left[0], left[1]), right))
