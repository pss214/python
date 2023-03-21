'''
a = [10,20]
b = a 
c = input()


print("박성수")
print(c)
'''
#자료 찾기
'''
def find_max(A):
    tmp=A[0]
    for item in A:
        if item > tmp:#최소값은 부등호 반대로 하면됨
            tmp = item
    return tmp

def find_mix(A):
    tmp=A[0]
    for item in A:
        if item < tmp:
            tmp = item
    return tmp

A=[2,3,7,8,9,5,4]
max = find_max(A)
min = find_mix(A)
print('최대값 =',max)
print('최소값 =',min)
'''
#추상자료형
'''
mybag = []

def contains(bag,e): #in 연산자 사용하여 bag 안에 e가 있는지 검사
    return e in bag
def insert(bag,e): #append함수를 사용하여 bag 안에 자료 추가
    bag.append(e)
def remove(bag,e): #remove함수를 사용하여 bag 안에 e를 삭제
    bag.remove(e)
def count(bag): #len함수를 사용하여 몇 개가 있는지 검사
    return len(bag)

insert(mybag,'휴대폰')
insert(mybag,'지갑')
insert(mybag,'손수건')
insert(mybag,'빗')
insert(mybag,'자료구조')
insert(mybag,'야구공')
print('가방 속의 물건 :', mybag)

insert(mybag,'빗')
remove(mybag,'손수건')
print('가방 속의 물건 :', mybag)
'''

#알고리즘의 성능 분석
'''
def insert(bag,e): #실행시간 분석
    bag.append(e)
import time
mybag=[]
start=time.time()
insert(mybag,'축구공')

end=time.time()
print('실행시간 = ', end-start)
'''

#복잡도 분석
# append와 insert중 효율적인 것은 append다 append는 자료 맨 뒤에 넣지만 insert는 자료 맨 앞에 넣는 것이기에 모든 자료를 드러내야해서 효율적인 것은 append.

#빅오 표기법
# 높은 n차항보다 낮은 경우 다 무시한다.

#시간 복자도 분석:순환 알고리즘 (알고리즘이나 함수가 수행도중에 자기 자신을 다시 호출하여 문제를 해결하는 기법(정의 자체가 순환적으로 되있는 경우 적합))

def f(n):
    if n==1:
        return n
    else:
        return n*f(n-1)
fact = f(3)
print('factorial(3) =', fact)
def factorial_for(n):
    result = 1
    for k in range(n, 0, -1):
        result *= k
    return result

fact = factorial_for(3)
print('factorial_for(3) =',fact)

    
