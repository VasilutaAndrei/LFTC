from FA import FiniteAutomata
from Scanner import Scanner

FA = FiniteAutomata()
SC = Scanner()
SC.setFA(FA)


def algorithm():
    with open('FA.in') as f:
        SC.readSetOfStates(f.readline())
        SC.readAlphabet(f.readline())
        SC.readStartingSymbol(f.readline())
        SC.readFinalStates(f.readline())
        while True:
            line = f.readline()
            if not line:
                break
            SC.readTransition(line)
    menu()


def menu():
    switcher = {
        0: lambda: exit(0),
        1: lambda: print(FA.getStates()),
        2: lambda: print(FA.getAlphabet()),
        3: lambda: print(FA.getStartingSymbol()),
        4: lambda: print(FA.getFinalStates()),
        5: lambda: print(FA.getTransition()),
    }
    while True:
        print('0.Exit')
        print('1.Set of states')
        print('2.Alphabet')
        print('3.Starting symbol')
        print('4.Final states')
        print('5.Transitions')
        option = input()[0]
        switcher.get(int(option), 'Invalid option')()


algorithm()
