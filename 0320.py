#사용자 정의 함수
'''
def find_max(A):
    max=A[0]
    for i in range(1,len(A)):
        if max < A[i]:
            max = A[i]
    return max

def find_min_max(A):
    min = A[0]
    max = A[0]
    for i in range(1, len(A)):
        if max < A[i] : max = A[i]
        if min > A[i] : min = A[i]
    return min, max 

data = [5,3,8,4,9,1,6,2,7]
print('max = ',find_max(data))
x, y = find_min_max(data)
print("(min,max) = ",(x,y))
'''

#디폴트 인수(step=1)
'''
def sum_range(begin, end, step = 1):
    sum = 0
    for n in range(begin, end, step):
        sum += n
    return sum
print("sum = ", sum_range(1,10))
print("sum = ", sum_range(1,10,2))

#키워드 인수
print("sum = ", sum_range(step=3, begin=1, end=10))
print("game", end=" ")
'''

#변수의 범위
'''
items = [1,3,5]
def sum():
    test = [2,4,6]
    print(items)
    print(test)
    if test[0] == 2:
        sam = [1,2,3]
        print(sam)
    else:
        sam2 = [4,5,6]
        print(sam2)
    #print(sam) 지역변수x
    #print(sam2)

sum()
print(items)
#print(test) 전역변수x
'''

#part 2
'''
def calc_perimeter(radius):
    global perimeter
    print("파이 값 : ",pi)
    perimeter = 2*pi*radius

pi = 3.141592
perimeter = 0
calc_perimeter(10)
print("원의 둘레(r=10) = ", perimeter)
'''

#모듈과 이름 공간
'''
import min_max
import sum

data = [5,3,8,4,9,1,6,2,7]
print("(min,max) = ", min_max.find_min_max(data))
print("sum = ", sum.sum_range(1,10))
'''
#part 2
'''
from min_max import *
from sum import *
data = [5,3,8,4,9,1,6,2,7]
print("(min,max) = ", find_min_max(data))
print("sum = ", sum_range(1,10))
'''

#클래스
'''
class Car :
    def __init__(self, color, speed=0) :
        self.color=color
        self.speed=speed
    def speedUp(self): 
        self.speed += 10
    def speedDown(self): 
        self.speed -= 10
    def __eq__(self, carB) :#연산자 중복
        return (self.color == carB.color) and (self.speed == carB.speed)
    def isEqual(self, carB):
        return self.color == carB.color
    def __str__(self) -> str: #문자 연산자
        return 'color = %s, speed %d' %(self.color,self.speed)
car1 = Car('black',0)
car2 = Car('red', 120)
car3 = Car('yellow',30)
car4 = Car('blue',0)
car5 = Car('green')#디폴트 인수 사용
print('speed = ', car2.speed)
car2.speedUp()
print('speed = ', car2.speed)
car3.color = 'skyblue'
print('color = ', car3.color)
car6 = Car('red')

#연산자 중복
print("car3 == car6 : ", car2.__eq__(car6)) 
print("car3 == car6 : ", car2.isEqual(car6)) 
#문자열로 변환 연산자
print("[car3] :", car3)

#상속
class SuperCar(Car):
    def __init__(self, color, speed=0, bTurbo = True):
        super().__init__(color, speed)
        self.bTurbo = bTurbo
    def speedUp(self):
        if self.bTurbo:
            self.speed += 50
        else:
            super().speedUp()
    def __str__(self):
        if self.bTurbo:
            return '[%s] [speed = %d] 터포모드'%(self.color, self.speed)
        else:
            return '[%s] [speed = %d] 일반모드'%(self.color, self.speed)
            
s1 = SuperCar("Gold", 0, True)
s2 = SuperCar("White", 0, False)

s1.speedUp()
s2.speedUp()
print("슈퍼카1 :", s1)
print("슈퍼카2 :", s2)
'''

#리스트
'''
#l = list
l = [1,2,3,4,5]
l.append(6)
l.append(7)
l.insert(0,0)
#l.delete(2)
print(l)
'''

#part 2
'''
items = []
def insert(pos, elem):
    items.insert(pos,elem)
def delete(pos):
    return items.pop(pos)
def getEntry(pos):
    return items[pos]
def isEmpty():
    return len(items) == 0
def size():
    return len(items)
def clear():
    global items
    items = []
def find():
    return items.index(items)
def replace(pos, elem):
    items[pos] = elem
def sort():
    items.sort()
def merge(lst):
    items.append(lst)
def display(msg='ArrayList'):
    print(msg, size(), items)


display('파이썬 리스트로 구현한 리스트 테스트')
insert(0,10); insert(0,20); insert(1,30)
insert(size(),40); insert(2,50)
display('파이썬 리스트로 구현한 리스트 삽입x5')
sort()
display('파이썬 리스트로 구현한 리스트 정렬')
replace(2,90)
display('파이썬 리스트로 구현한 리스트 교체후')
delete(2); delete(size()-1); delete(0)
display('파이썬 리스트로 구현한 리스트 삭제후')
lst = [1,2,3]
merge(lst)
display('파이썬 리스트로 구현한 리스트 머지후')
clear()
display('파이썬 리스트로 구현한 리스트 클리어후')
'''