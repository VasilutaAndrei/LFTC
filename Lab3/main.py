from PIF import ProgramInternalForm
from symbolTable import SymbolTable
from languageSpecs import *
import re

st = SymbolTable()
pif = ProgramInternalForm()
filename = 'input2'
pif_filename = 'PIF.out'
st_filename = 'ST.out'


def tokenize():
    result = []
    with open(filename) as file:
        re_separator = '('
        for separator in separators:
            re_separator += re.escape(separator) + '|'
        re_separator = re_separator[:-1] + ')'
        for line in file:
            line = line.strip()
            new_line = re.split(re_separator, line)
            result.append(new_line)
    return result


def algorithm():
    lines_array = tokenize()
    for line in lines_array:
        for token in line:
            if token != '':
                if token == ' ':
                    pass
                elif isReserved(token) or isOperator(token) or isSeparator(token):
                    pif.add(getCodeOfToken(token), -1)
                elif isIdentifier(token):
                    pif.add(getCodeOfToken('identifier'), st.addSymbol(token))
                elif isConstant(token):
                    pif.add(getCodeOfToken('constant'), st.addSymbol(token))
                else:
                    raise Exception("Lexical error at line", ''.join(line))


algorithm()

print("Lexically correct")

f = open(pif_filename, "w")
f.write("Codification\n")
f.write(str(codification) + '\n')
f.write("Program Internal Form (code, index)\n")
for x in range(pif.getLen()):
    f.write(str(pif.get(x)) + '\n')
f.close()
print("Program Internal Form exported to " + pif_filename)

f = open(st_filename, "w")
for x in range(st.symTable.getSize()):
    f.write(str(st.getHashAtIndex(x)) + '\n')
f.close()
print("Symbol Table exported to " + st_filename)
