#리스트_라인편집기
'''
class ArrayList:
    def __init__( self ):
        self.items = []
    def insert(self, pos, elem):
        self.items.insert(pos,elem)
    def delete(self,pos):
        return self.items.pop(pos)
    def getEntry(self, pos):
        return self.items[pos]
    def isEmpty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)
    def clear(self):
        global items
        self.items = []
    def find(self):
        return self.items.index()
    def replace(self,pos, elem):
        self.items[pos] = elem
    def sort(self):
        self.items.sort()
    def merge(self,lst):
        self.items.append(lst)
    def display(self, msg='ArrayList'):
        print(msg, self.size(), self.items)


        
    
def myLineEditor():
    list = ArrayList()
    while True:
        command = input("[메뉴선택] i-입력, d=삭제, r-변경, p-출력, l-파일읽기, s-저장, q-종료=>")

        if command == 'i':
            pos = int(input("입력행 번호:"))
            str = input(" 입력행 내용:")
            list.insert(pos, str)
        elif command == 'd':
            pos = int(input(" 삭제행 번호:"))
            list.delete(pos)
        elif command == 'r':
            pos = int(input(" 변경행 번호:"))
            str = input(" 변경행 내용:")
            list.replace(pos, str)
        elif command == 'q': return
        elif command == 'p':
            print('Line Editor')
            for line in range (list.size()):
                print('[%2d] '%line, end='')
                print(list.getEntry(line))
            print()
        elif command == 'l':
            filename = 'test.txt'
            infile = open(filename,'r')
            print(infile)
            lines = infile.readlines()
            for line in lines:
                list.insert(list.size(), line.rstrip('\n'))
            infile.close()
        elif command == 's':
            filename = 'test.txt'
            outfile = open(filename, 'w')
            for i in range(list.size()):
                outfile.write(list.getEntry(i)+'\n')
            outfile.close

myLineEditor()
'''


#리스트 비교
'''
class Set:
    def __init__(self):
        self.items=[]
    def size(self):
        return len(self.items)
    def display(self,msg):
        print(msg, self.items)
    def contains(self, item):
        for i in range(len(self.items)):
            if self.items[i] == item:
                return True
        return False
    def insert(self, elem):
        if elem not in self.items:
            self.items.append(elem)
    def delete(self, elem):
        if elem in self.items:
            self.items.remove(elem)
    def union(self, setB):
        setC = Set()
        setC.items = list(self.items)
        for elem in setB.items:
            if elem not in self.items:
                setC.items.append(elem)
        return setC
    def intersect(self, setB):
        setC = Set()
        for elem in setB.items:
            if elem in self.items:
                setC.items.append(elem)
        return setC
    def difference(self, setB):
        setC = Set()
        for elem in self.items:
            if elem not in setB.items:
                setC.items.append(elem)
        return setC
setA = Set()
setA.insert('휴대폰')
setA.insert('지갑')
setA.insert('손수건')
setA.display('setA : ')

setB = Set()
setB.insert('빗')
setB.insert('파이썬 자료구조')
setB.insert('야구공')
setB.insert('지갑')
setB.display('setB : ')

setB.insert('빗')
setA.delete('손수건')
setA.delete('발수건')
setA.display('setA : ')
setB.display('setB : ')

setA.union(setB).display('A∪B')
setA.intersect(setB).display('A∩B')
setA.difference(setB).display('A=B')
'''

top = []
def isEmpty():
    return len(top) == 0
def push(item):
    top.append(item)
def pop():
    if not isEmpty():
        return top.pop(-1)
def peek():
    if not isEmpty():
        return top[-1]
def size(): return len(pop)
def clear():
    global top
    top = []

for i in range(1,6):
    push(i)
print(' push 5회 : ', top)
print(' pop() -> ', pop())
print(' pop() -> ', pop())
print(' push 2회 :', top)

push('홍길동')
push('이순신')
print(' push + 2회 :', top)
print(' pop() -> ', pop())
print(' push 1회 :', top)

class Stack:
    def __init__(self):
        self.top = []
    def isEmpty(self):
        return len(self.top) == 0
    def push(self,item):
        self.top.append(item)
    def pop(self):
        if not isEmpty():
            return self.top.pop(-1)
    def peek(self):
        if not isEmpty():
            return self.top[-1]
    def size(self): return len(self.pop)
    def clear(self):
        self.top = []
    def __str__(self):
        return str(self.top[::-1])

odd = Stack()
even = Stack()
for i in range(10):
    if i%2 == 0: even.push(i)
    else: odd.push(i)
print('스텍 even push 5회 : ', even.top)
print('스텍 odd push 5회 : ', odd.top)
print('스텍 even push peek() : ', even.peek())
print('스텍 odd push peek() : ', odd.peek())
for _ in range(2): even.pop()
for _ in range(3): odd.pop()
print('스텍 even push 2회 : ', even)
print('스텍 odd push 3회 : ', odd)


