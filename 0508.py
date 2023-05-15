# 순차 탐색
from typing import Any


def sequential_search(A, key, low, high):
    for i in range(low, high):
        if A[i].key == key:
            return i
    return None
'''
A= [2,6,11,13,18,20,22,27,29,30,34,38,41,42,45,47]
key = 47
low = 0
high = len(A)
ret = sequential_search(A,key,low,high)
print("찾는 값은 %d번째 있습니다."%ret)
'''

def binary_search(A,key,low,high):
    if low <= high :
        middle = (low+high)//2
        if key == A[middle]:
            return middle
        elif key < A[middle]:
            return binary_search(A, key,low, middle-1)
        else:
            return binary_search(A, key,middle+1,high)
    return None
'''
A= [2,6,11,13,18,20,22,27,29,30,34,38,41,42,45,47]
key = 11
low = 0
high = len(A)
ret = binary_search(A,key,low,high)
print("찾는 값은 %d번째 있습니다."%ret)
'''

def binary_search_iter(A,key,low,high):
    while(low<=high):
        middle = (low+high)//2
        if key == A[middle]:
            return middle
        elif key < A[middle]:
            low = middle + 1
        else:
            high = middle - 1
    return None

'''
A= [2,6,11,13,18,20,22,27,29,30,34,38,41,42,45,47]
key = 45
low = 0
high = len(A)
ret = binary_search_iter(A,key,low,high)
print("찾는 값은 %d번째 있습니다."%ret)
'''

def bogan_search(A,key,low,high):
    while(low<=high):
        middle = int(low + (high-low)*(key-A[low])/(A[high]-A[low]))
        if key == A[middle]:
            return middle
        elif key < A[middle]:
            low = middle + 1
        else:
            high = middle - 1
    return None
'''
A = [2,6,11,13,18,20,22,27,29,30,34,38,41,42,45,47]
key = 45
low = 0
high = len(A)-1
ret = bogan_search(A,key,low,high)
print("찾는 값은 %d번째 있습니다."%ret)
'''

def hashFn(key):
    sum = 0
    M = 25
    for c in key:
        sum += ord(c)
        return sum%M

'''
ret = hashFn('ABC')
print("해시함수 리턴 값 : %d " %ret)
'''

class Entry:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
    def __str__(self):
        return str('%s:%s'%(self.key, self.value))
class SequentialMap:
    def __init__(self) -> None:
        self.table = []
    def size(self):
        return len(self.table)
    def display(self, msg):
        print(msg)
        for entry in self.table:
            print(" ", entry)
    def insert(self, key, value):
        self.table.append(Entry(key,value))
    def search(self, key):
        pos = sequential_search(self.table, key, 0, self.size()-1)
        if pos is not None:
            return self.table[pos]
        else:
            return None
    def delete(self, key):
        for i in range(self.size()):
            if self.table[i].key == key:
                self.table.pop(i)
                return

map = SequentialMap()
map.insert('data','자료')
map.insert('structure','구조')
map.insert('swquential search','선형탐색')
map.insert('game','게임')
map.insert('binary search','이진탐색')
map.display('나의 단어장 : ')

print('탐색 : game -->', map.search('game'))
print('탐색 : over -->', map.search('over'))
print('탐색 : data -->', map.search('data'))
map.delete('game')
map.display('나의 단어장 : ')

class Node:
    def __init__(self, data, link=None) -> None:
        self.data = data
        self.link = link
class HashChainMap:
    def __init__(self, M) -> None:
        self.table = [None]*M
        self.M=M
    def hashFn(self, key):
        sum = 0
        for c in key:
            sum += ord(c)
        return sum
    def insert(self, key, value):
        idx = self.hashFn(key)
        self.table[idx] = Node(Entry(key,value), self.table[idx])
    def search(self, key):
        idx = self.hashFn(key)
        n = self.table[idx]
        while n is not None:
            if n.data.key ==key:
                return n.data
            n = n.link
        return None
    def delete(self, key):
        idx = self.hashFn(key)
        n = self.table[idx]
        before = None
        while n is not None:
            if n.data.key == key:
                if before == None:
                    self.table[idx]=n.link
                else:
                    before.link = n.link
                return
            before = n
            n = n.link
    def display(self, msg):
        print(msg)
        for idx in range(len(self.table)):
            n = self.table[idx]
            if n is not None:
                print('[%2d] -> '%idx, end=' ')
                while n is not None:
                    print(n.data, end='->')
                    n = n.link
                print()

'''
d = {}
d['data'] ='자료'
d['structure'] ='구조'
d['sequenial search'] ='선형검색'
d['game'] ='게임'
d['binary serach'] ='이진탐색'
print('나의 단어장 : ')
print(d)
if d.get('game'): print('탐색: game --> ', d['game'])
if d.get('over'): print('탐색: over --> ', d['over'])
if d.get('data'): print('탐색: data --> ', d['data'])
d.pop('game')
print('나의 단어장 : ')
print(d)
'''

    