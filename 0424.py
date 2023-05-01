class Node:
    def __init__(self, elem, link=None):
        self.data = elem
        self.link = link
class LinkedStack:
    def __init__(self):
        self.top = None
    def isEmpty(self):return self.top == None
    def clear(self):self.top = None
    def push(self, item):
        n = Node(item, self.top)
        self.top = n
    def pop(self):
        if not self.isEmpty():
            n = self.top
            self.top = n.link
            return n.data
    def peek(self):
        if not self.isEmpty():
            return self.top.data
    def size(self):
        node = self.top
        count = 0
        while not node == None:
            node = node.link
            count += 1
        return count
    def display(self, msg = 'LinkedStack : '):
        print(msg, end=' ')
        node = self.top
        while not node == None:
            print(node.data, end='->')
            node = node.link
        print('None')
'''
odd = LinkedStack()
even = LinkedStack()
for i in range(10):
    if i % 2 == 0:
        even.push(i)
    else:
        odd.push(i)
even.display(' 스택 even push 5회 : ')
odd.display(' 스텍 odd push 5회 : ')
print('스택 even peek :', even.peek())
print('스택 odd peek :', odd.peek())
for i in range(2):
    even.pop()
for i in range(3):
    odd.pop()
even.display(' 스택 even pop 2회 : ')
odd.display(' 스텍 odd pop 3회 : ')
'''
class LinkedList:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head == None
    def clear(self):
        self.head = None
    def size(self):
        node = self.head
        count = 0
        while not node == None:
            node = node.link
            count += 1
        return count
    def display(self, msg = 'LinkedList : '):
        print(msg, end=' ')
        node = self.head
        while not node == None :
            print(node.data, end='->')
            node = node.link
        print('None')
    def getNode(self, pos):
        if pos < 0: return None
        node = self.head
        while pos > 0 and node != None:
            node = node.link
            pos -= 1
        return node
    def getEntry(self, pos):
        node = self.getNode(pos)
        if node == None : return None
        else : return node.data
    def replace(self, pos, elem):
        node = self.getNode(pos)
        if node != None:
            node.data = elem
    def find(self, data):
        node = self.head
        while node is not None:
            if node.data == data:
                return node
            node = node.link
        return node
    def insert(self, pos, elem):
        before = self.getNode(pos-1)
        if before == None:
            self.head = Node(elem, self.head)
        else:
            node = Node(elem, before.link)
            before.link = node
    def delete(self, pos):
        before = self.getNode(pos-1)
        if before == None:
            if self.head is not None:
                self.head = self.head.link
        elif before.link != None:
            before.link = before.link.link
'''
s = LinkedList()
s.display('단순 연결 리스트로 구현한 리스트(초기상태) : ')
s.insert(0,10)
s.insert(0,20)
s.insert(1,30)
s.insert(s.size(),40)
s.insert(2,50)
s.display('단순연결리스트로 구현한 리스트(삽입x5) : ')
s.replace(2,90)
s.display('단순연결리스트로 구현한 리스트(교체x1) : ')
s.delete(2)
s.delete(s.size()-1)
s.delete(0)
s.display('단순연결리스트로 구현한 리스트(삭제x3) : ')
'''
class CircularLinkedQueue:
    def __init__(self):
        self.tail = None
    def isEmpty(self):
        return self.tail == None
    def clear(self):
        self.tail = None
    def peek(self):
        if not self.isEmpty():
            return self.tail.link.data
    def enqueue(self, item):
        n = Node(item, None)
        if self.isEmpty():
            n.link = n
            self.tail = n
        else:
            n.link = self.tail.link
            self.tail.link = n
            self.tail = n
    def dequeue(self):
        if not self.isEmpty():
            d = self.tail.link.data
            if self.tail.link == self.tail:
                self.tail = None
            else:
                self.tail.link = self.tail.link.link
            return d
    def size(self):
        if self.isEmpty():
            return 0
        else:
            count = 1
            n = self.tail.link
            while not n == self.tail:
                n = n.link
                count += 1
            return count
    def display(self, msg=' CircularLinkedQueue : '):
        print(msg, end=' ')
        if not self.isEmpty():
            n = self.tail.link
            while not n == self.tail:
                print(n.data, end='->')
                n = n.link
            print(n.data, end='->')
            print('None')
'''
q = CircularLinkedQueue()
for i in range(8):
    q.enqueue(i)
q.display("연결된 큐 8번 삽입 : ")
for i in range(5):
    q.dequeue()
q.display("연결된 큐 5번 삭제 : ")
for i in range(8,14):
    q.enqueue(i)
q.display("연결된 큐 뒤쪽 6번 삽입 : ")
'''