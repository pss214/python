class Stack:
    def __init__(self):
        self.top = []
    def isEmpty(self):
        return len(self.top) == 0
    def push(self,item):
        self.top.append(item)
    def pop(self):
        if not self.isEmpty():
            return self.top.pop(-1)
    def peek(self):
        if not self.isEmpty():
            return self.top[-1]
    def size(self): return len(self.pop)
    def clear(self):
        self.top = []
    def __str__(self):
        return str(self.top[::-1])
    
def checkBrackets(statement):
    stack = Stack()
    for ch in statement:
        if ch in ('{[('):
            stack.push(ch)
        elif ch in ('}',']',')'):
            if stack.isEmpty():
                return False
            else :
                left = stack.pop()
                if (ch == "}" and left !="{" or \
                    ch == "]" and left !="[" or \
                    ch == ")" and left !="("):
                    return False
    return stack.isEmpty()
'''
str = ('{A[(i+1)]=0}', 'if((i==0)&&(j==0)','A[(i+1)=0')
for s in str:
    m = checkBrackets(s)
    print(s, '-->', m)
'''
def checkBracketsV2(lines):
    stack = Stack()
    for line in lines:
        for ch in line:
            if ch in ('{[('):
                stack.push(ch)
            elif ch in ('}',']',')'):
                if stack.isEmpty():
                    return False
                else :
                    left = stack.pop()
                    if (ch == "}" and left !="{" or \
                        ch == "]" and left !="[" or \
                        ch == ")" and left !="("):
                        return False
    return stack.isEmpty()
'''
filename = "ArrayStack.h"
infile = open(filename, "r",encoding = 'UTF8')
lines = infile.readlines()
infile.close()

result = checkBracketsV2(lines)
print(filename, '-->', result)
'''
def evalPostfix(expr):
    s = Stack()
    for token in expr:
        if token in "+-*/":
            val2 = s.pop()
            val1 = s.pop()
            if (token == '+'): s.push(val1 + val2)
            elif (token == '-'): s.push(val1 - val2)
            elif (token == '*'): s.push(val1 * val2)
            elif (token == '/'): s.push(val1 / val2)
        else:
            s.push(float(token))
    return s.pop()

infix1 = ['8','/','3','-','3','+','3','2','*','+']
infix2 = ['1','2','/','4','*','1','4','/', '*']
print(infix1,'-->',evalPostfix(infix1))
print(infix2,'-->',evalPostfix(infix2))


def precedence(op):
    if op == '(' or op == ')':return 0
    elif op == '+' or op == '-':return 1
    elif op == '*' or op == '-':return 2
    else:
        return -1
def Infix2Postfix(expr):
    s = Stack()
    output=[]
    for term in expr:
        if term in '(':
            s.push('(')
        elif term in ')':
            op = s.pop()
            if op == '(': break
            else:
                output.append(op)
        elif term in '+-*/':
            while not s.isEmpty():
                op = s.peek()
                if(precedence(term)) <= precedence(op):
                    output.append(op)
                    s.pop()
                else: break
            s.push(term)
        else:
            output.append(term)
    while not s.isEmpty():
        output.append(s.pop())
    return output
infix1 = '8/2-3+(3*2)'
infix2 = ['1','/','2','*','4','*','(','1','/','4',')']
postfix1 = Infix2Postfix(infix1)
postfix2 = Infix2Postfix(infix2)
#result1 = evalPostfix(infix1)
#result2 = evalPostfix(infix2)
print('중위표기 : ',infix1)
#print('후위표기 : ', result1)
print('중위표기 : ',infix2)
#print('후위표기 : ', result2)
