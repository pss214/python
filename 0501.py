class DNode:
    def __init__(self, elem, prev = None, next = None):
        self.data = elem
        self.prev = prev
        self.next = next
class DoublyLinkedDeque:
    def __init__(self):
        self.front = None
        self.rear = None
    def isEmpty(self):return self.front == None
    def clear(self): self.front = self.rear = None
    def size(self):
        n = self.front
        count = 0
        n = self.front
        while not n == self.front:
            n = n.next
            count += 1
            return count
    def display(self, msg='LinkedDeque : '):
        print(msg, end=' ')
        n = self.front
        while not n == None:
            print(n.data, end='->')
            n = n.next
        print('None')
    def addFront(self,item):
        n = DNode(item, None, self.front)
        if self.isEmpty():
            self.front = self.rear = n
        else:
            self.front.prev = n
            self.front = n
    def addRear(self,item):
        n = DNode(item, self.rear, None)
        if self.isEmpty():
            self.front = self.rear = n
        else:
            self.rear.next = n
            self.rear = n
    def deleteFront(self):
        if not self.isEmpty():
            data = self.front.data
            self.front = self.front.next
            if self.front == None:
                self.rear = None
            else:
                self.front.prev = None
            return data
    def deleteRear(self):
        if not self.isEmpty():
            data = self.rear.data
            self.rear = self.rear.prev
            if self.rear == None:
                self.front = None
            else:
                self.rear.next = None
            return data
'''
dq = DoublyLinkedDeque()
for i in range (10):
    if i%2 == 0:
        dq.addRear(i)
    else:
        dq.addFront(i)
dq.display("연결된 덱 홀수 짝수 삽입 : ")
for i in range(2):
    dq.deleteFront()
for i in range(3):
    dq.deleteFront()
dq.display("연결리스트 덱 5번 삭제 : ")
for i in range(9,14):
    dq.addRear(i)
dq.display("연결리스트 덱 뒤쪽 5번 삽입 : ")
'''
# 정렬과 탐색
def printStep(arr, val):
    print("  Step %2d = "% val, end='')
    print(arr)
def selection_sort(a):
    n = len(a)
    for i in range(n-1):
        least = i
        for j in range(i+1, n):
            if(a[j]<a[least]):
                least = j
        a[i], a[least] = a[least], a[i]
        printStep(a, i+1)
'''
print("선택정렬")
data = [5,3,8,4,9,1,6,2,7]
print("Original : ", data)
selection_sort(data)
print("Selection : ",data)
'''
def insertion_sort(a):
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i-1
        while j >= 0 and a[j]>key:
            a[j+1] = a[j]
            j -= 1
        a[j+1]=key
        printStep(a,i)
'''
print("삽입정렬")
data = [5,3,8,4,9,1,6,2,7]
print("Original : ", data)
insertion_sort(data)
print("Selection : ",data)
'''
def bubble_sort(a):
    n = len(a)
    for i in range(n-1, 0, -1):
        b_changed = False
        for j in range(i):
            if( a[j]>a[j+1]):
                a[j], a[j+1] = a[j+1], a[j] 
                b_changed = True
        if not b_changed: break
        printStep(a, n-i)
'''
print("버블정렬")
data = [5,3,8,4,9,1,6,2,7]
print("Original : ", data)
bubble_sort(data)
print("Selection : ",data)
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
class ArrayList:
    def __init__( self ):
        self.items = []
    def insert(self, elem):
        if elem in self.items : return
        for idx in range(len(self.items)):
            if elem < self.items[idx]:
                self.items.insert(idx,elem)
                return
        self.items.append(elem)
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
    def __eq__(self, setB):
        if self.size() != setB.size():
            return False
        for idx in range(len(self.items)):
            if self.items[idx] != setB.items[idx]:
                return False
        return True
    def union(self, setB):
        newSet = Set()
        a = 0
        b = 0
        while a < len(self.items) and b < len(setB.items):
            valueA = self.items[a]
            



items = ArrayList()
items.insert(4)
items.display()