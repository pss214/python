import time

#반복구조
'''
def power_iter(x,n): 
    result =1.0
    for i in range(n):
        result *=x
    return result

def power(x,n): #순환구조
    if n==0: return 1
    elif n%2 ==0:
        return power(x*x,n//2)
    else:
        return x*power(x*x, (n-1)/2)
    
print('fast power_iter(2, 500) : '+str(power_iter(2,500)))
print('fast power(2, 500) : '+str(power(2,500)))

start = time.time()
for i in range(100000):
    power(2.0, 500)
end = time.time()
print('빠른 순환 =', end-start)

start = time.time()
for i in range(100000):
    power_iter(2.0, 500)
end = time.time()
print('느린 순환 =', end-start)
'''

#피보나치 수열 순환 구조
'''
def fib(n): 
    if n==0: return 0
    elif n==1: return 1
    else:
        return (fib(n-1))+fib(n-2)
    
def fib_iter(n):
    if n<2: return n
    last = 0
    current =1
    for i in range(2,n+1):
        tem = current
        current += last
        last = tem
    return current

print('순환 fib :', str(fib(6)))
print('반복 fib :', str(fib_iter(6)))

start = time.time()
for i in range(100000):
    str(fib(6))
end = time.time()
print('순환 시간 =', end-start)

start = time.time()
for i in range(100000):
    str(fib_iter(6))
end = time.time()
print('반복 시간 =', end-start)
'''
#하노이탑 
'''
def hanoi_tower(n,a,tmp,to):
    if n==1:
        print('원판 1: %s -->%s'%(a,to))
    else:
        hanoi_tower(n-1,a,to,tmp)
        print('원판 %d: %s -->%s'%(n,a,to))
        hanoi_tower(n-1,tmp,a,to)

hanoi_tower(4,'A','b','c')
'''

#반복
'''
dan = int(input('구구단 단 입력 : '))
for n in range(1,10,1):
    print('%2d x %2d =%2d'%(dan,n,dan*n))

n=1
while n<10:
    print('%2d x %2d =%2d'%(dan,n,dan*n))
    n +=1
'''

#딕션
'''
myDict={'A':12,'B':22,'C':52,'D':26,'E':99}
for e in myDict:
    print('키 = %s, 값 = %d '%(e,myDict[e]))
'''

#문자열
'''
hobby ='테니스'
age=21
score=4.5
msg1='당신의 학점은 %4.1f입니다'% score
msg2='취미=%s, 나이=%d, 학점=%f'%(hobby,age,score)
print(msg1)
print(msg2)
print(msg1[0])
print(msg1[-1])
'''

#딕셔너리
'''
map={'김연아':'피겨','류현진':'야구','쿠드롱':'당구','메시':'축구'}
print(map)
print('쿠드롱이 뭐하는 사람이지 ? ',map['쿠드롱'])
map['나달']='테니스'
map.update({'최민영':'여자친구','고진영':'골프'})
print(map)
'''

#리스트
'''
big3=[]
lotto=[23,34,11,42,9]
big4=['제이플라','도티','대도서관','보람튜브']
print('lotto[1]',lotto[1])
big4[2]='블랙핑크'
print(big4)
big3.append('알라딘')
big3.append('엘사')
big3.append('안나')
big3.extend(big4)
print(big3)
print(big3.index('엘사'))
big3.reverse()
print(big3)
big3.sort(reverse=True)#오름차순#reverse=true내림차순
print(big3)
'''

#사용자 정의 함수
def find_a(A):
    max=A[0]
    for i in range(1, len(A)):
        if max<A[i]:
            max=A[i]
    return max
lst=[5,3,8,4,9,1,6,2,7]
print('max = ',find_a(lst))

