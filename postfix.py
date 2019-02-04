class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]


def splitTokens(exprStr):
    tokens = []
    val = 0
    valProcessing = False
    for c in exprStr:
        if c == ' ':
            continue
        if c in '0123456789':
            val = val * 10 + int(c)
            valProcessing = True
        else:
            if valProcessing:
                tokens.append(val)
                val = 0
            valProcessing = False
            tokens.append(c)
    if valProcessing:
        tokens.append(val)

    return tokens


def infixToPostfix(tokenList):
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }

    opStack = ArrayStack()
    postfixList = []

    for i in range(len(tokenList)):
        if str(tokenList[i]) in '*/+-()':
            if opStack.isEmpty():
                opStack.push(tokenList[i])
            else:
                if tokenList[i]=='(':
                    opStack.push(tokenList[i])
                elif tokenList[i]==')':
                    while opStack.peek()!='(':
                        postfixList.append(opStack.pop())
                    opStack.pop()
                elif prec[opStack.peek()] >= prec[tokenList[i]]:
                    postfixList.append(opStack.pop())
                    opStack.push(tokenList[i])
                else:
                    opStack.push(tokenList[i])
        else:
            postfixList.append(tokenList[i])
    while opStack.isEmpty()!=True:
        postfixList.append(opStack.pop())

    return postfixList


def postfixEval(tokenList):
    cal=ArrayStack()
    for i in range(len(tokenList)):
        if str(tokenList[i]) in '+-*/':
            n2=cal.pop()
            n1=cal.pop()
            if str(tokenList[i])=='+':
                cal.push(n1+n2)
            elif str(tokenList[i]) == '-':
                cal.push(n1 - n2)
            elif str(tokenList[i]) == '*':
                cal.push(n1 * n2)
            elif str(tokenList[i]) == '/':
                cal.push(n1 / n2)
        else:
            cal.push(tokenList[i])
    return cal.peek()

def solution(expr):
    tokens = splitTokens(expr)
    postfix = infixToPostfix(tokens)
    val = postfixEval(postfix)
    return val

print(solution("(5 - 3)"))