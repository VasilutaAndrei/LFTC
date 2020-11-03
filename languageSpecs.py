import re

operators = ['+', '-', '*', '/', '=', '<', '>', '<=', '==', '>=', '!=', '&&', '||']
separators = [';', '{', '}', '(', ')', ' ', '\n', '[', ']', ',']
reservedWords = ['int', 'char', 'double', 'if', 'else', 'while', 'read', 'print', 'list', 'int_main']
all = operators + separators + reservedWords
codification = {all[i]: i + 2 for i in range(0, len(all))}
codification['identifier'] = 0
codification['constant'] = 1


def isSeparator(char):
    return char in separators


def isOperator(char):
    return char in operators


def isReserved(word):
    return word in reservedWords


def isIdentifier(word):
    return re.match(r'^[a-zA-Z]([a-zA-Z]|[0-9]){0,250}$', word) is not None


def isConstant(token):
    return re.match(r'((\'[a-zA-Z]\'|\'[0-9]\')|(\+|-){0,1}[0-9]*\d$)', token) is not None


def getCodeOfToken(token):
    try:
        return codification[token]
    except:
        raise Exception("The token is not in codification table")
