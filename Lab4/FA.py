class FiniteAutomata:
    def __init__(self):
        self.states = []
        self.alphabet = []
        self.startingSymbol = ''
        self.finalStates = []
        self.transitions = []

    def addState(self, state):
        self.states.append(state)

    def addAlphabet(self, alphabet):
        self.alphabet.append(alphabet)

    def setStartingSymbol(self, symbol):
        self.startingSymbol = symbol

    def addFinalState(self, state):
        self.finalStates.append(state)

    def addTransition(self, transition):
        self.transitions.append(transition)

    def getStates(self):
        return self.states

    def getAlphabet(self):
        return self.alphabet

    def getStartingSymbol(self):
        return self.startingSymbol

    def getFinalStates(self):
        return self.finalStates

    def getTransition(self):
        return self.transitions

    def checkSequence(self):
        sequence = input()
        isOK = True
        lastTr = ''
        for l in sequence:
            if l not in self.alphabet:
                print('Invalid symbol <' + l + '>')
                return
            isAccepted = False
            for tr in self.transitions:
                if l == tr[0][1] and (lastTr == '' or lastTr == tr[0][0]):
                    isAccepted = True
                    lastTr = tr[1]
                    print(tr)
                    break
            if not isAccepted:
                print('No transitions found for (' + lastTr + ', ' + l + ')')
                isOK = False
        if isOK:
            print('The sequence <' + sequence + '> is accepted.')
        else:
            print('The sequence <' + sequence + '> is not accepted.')

    def __str__(self):
        return 'Set of states\n' + str(self.states) + '\nAlphabet\n' + str(self.alphabet) + '\nStarting symbol\n' + str(self.startingSymbol) + '\nFinal states\n' + str(self.finalStates) + '\nTransitions\n' + str(self.transitions)
