MAX_QSIZE = 10
class CircularQueue :
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.items = [None]*MAX_QSIZE
    def isEmpty(self): return self.front == self.rear
    def isFull(self): return self.front == (self.rear+1)%MAX_QSIZE
    def clear(self): self.front = self.rear
    def enqueue(self, item):
        if not self.isFull():
            self.rear = (self.rear+1)%MAX_QSIZE
            self.items[self.rear] = item
    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front+1)%MAX_QSIZE
            return self.items[self.front]
    def peek(self):
        if not self.isEmpty():
            return self.items[(self.front+1) %MAX_QSIZE]
    def size(self):
        return (self.rear - self.front + MAX_QSIZE) % MAX_QSIZE
    def display(self):
        out = []
        if self.front < self.rear:
            out = self.items[self.front+1:self.rear+1]
        else:
            out = self.items[self.front+1:MAX_QSIZE] + self.items[0:self.rear+1]
        print("[f=%s,r=%d] ==> "%(self.front, self.rear), out )
'''
q = CircularQueue()
for i in range(8): q.enqueue(i)
q.display()
for i in range(5): q.dequeue()
q.display()
for i in range(8,14): q.enqueue(i)
q.display()
'''
map = [['1','1','1','1','1','1'],
       ['e','0','0','0','0','1'],
       ['1','0','1','0','1','1'],
       ['1','0','1','0','01','1'],
       ['1','0','1','0','0','x'],
       ['1','1','1','1','1','1']]
MAZE_SIZE = 6

def isValidpos(x, y):
    if x < 0 or y < 0 or x >= MAZE_SIZE or y >= MAZE_SIZE:
        return False
    else:
        return map[y][x] == '0' or map[y][x] == 'x'

def BFS():
    que = CircularQueue()
    que.enqueue((0, 1))
    print("BFS : ")

    while not que.isEmpty():
        here = que.dequeue()
        print(here, end='->')
        x,y = here
        if (map[y][x] == 'x'):
            return True
        else:
            map[y][x] = '.'
            if isValidpos(x, y-1):
                que.enqueue((x, y-1))
            if isValidpos(x, y+1):
                que.enqueue((x, y+1))
            if isValidpos(x-1, y):
                que.enqueue((x-1, y))
            if isValidpos(x+1, y):
                que.enqueue((x+1, y))
    return False
'''
MAX_SIZE = 6
result = BFS()
if result:
    print ('--> 미로탐색 성공')
else:
    print('--> 미로탐색 실패')
'''
class CircularDeque(CircularQueue):
    def __init__(self):
        super().__init__()
    def addRear(self, item): self.enqueue(item)
    def deleteFront(self): return self.dequeue()
    def getFront(self): return self.peek()
    def addFront(self, item):
        if not self.isFull():
            self.items[self.front] = item
            self.front = self.front - 1
            if self.front < 0 : self.front = MAX_QSIZE - 1
    def deleteRear(self):
        if not self.isEmpty():
            item = self.items
            self.rear = self.rear - 1
            if self.front < 0 : self.rear= MAX_QSIZE - 1
            return item
    def getRear(self):
        return self.items[self.rear]
'''
dq = CircularDeque()
for i in range(9):
    if i%2 == 0 : dq.addRear(i)
    else: dq.addRear(i)
dq.display()
for i in range(2): dq.deleteFront()
for i in range(3): dq.deleteRear()
dq.display()
for i in range(9,14): dq.addFront(i)
dq.display()
'''