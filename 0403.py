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

filename = "ArrayStack.h"
infile = open(filename, "r",encoding = 'UTF8')
lines = infile.readlines()
infile.close()

result = checkBracketsV2(lines)
print(filename, '-->', result)