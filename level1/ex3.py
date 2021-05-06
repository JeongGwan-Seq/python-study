#1 리스트 list1 = []
list1=[1,2,3,4,5]
list2=[5,6,7,8]

print('='*50 )

print(list1[2])

print('='*50 )

list3 = list1+list2

print(list3)

list4 = [
    list1,
    list2
]

print(list4)

list1.append(10)

print(list1)

del list1[0]

print(list1)
list1.remove(2)


print(list1)


list6 = list(range(10))
print(list6)

list7 = list(range(1,12))

print(list7)



# 3 스칼라
# [1,2,3] 벡터
# 2차원 matrix , 3차원 tensor 




#2 튜플 - 읽기 전용 변수
tuple1 = (1,2,3)
print(tuple1)

tuple2 = (4,5,6)

tuple3 = tuple1 + tuple2
print(tuple3)

tuple4 = [

    tuple1,
    tuple2
]

print(tuple4)


list10 = list(tuple1)

print(list10)


PS C:\Users\KW2012-357\Desktop\kiswire> git remote add origin https://github.com/JeongGwan-Seq/python-study.git
PS C:\Users\KW2012-357\Desktop\kiswire> git push origin master
info: please complete authentication in your browser...
Enumerating objects: 6, done.
Counting objects: 100% (6/6), done.
Delta compression using up to 8 threadshe
Compressing objects: 100% (5/5), done.
Writing objects: 100% (6/6), 1.30 KiB | 148.00 KiB/s, done.
Total 6 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/JeongGwan-Seq/python-study.git
 * [new branch]      master -> master
PS C:\Users\KW2012-357\Desktop\kiswire> 

#3 딕셔너리

