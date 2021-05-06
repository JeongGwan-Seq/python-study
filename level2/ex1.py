# 오버로딩 없음

def add(a,b):
    return a+b

print(add(1,2))


def minus(a,b= 5):   # default 값을 지정할 수 있다 
    return a-b

print(minus(10))

def many(*data): # 튜플로 받음
    print(data)

many(1,2,3,4,5)

def keyworkd(**data): #딕셔너리 데이터 받기
    print(data)

keyworkd(id=1, username = 'ssar')



n1=1

def var_test():
    global n1
    n1 = 2

var_test()
print(n1)



