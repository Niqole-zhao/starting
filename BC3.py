"""矩阵相等判定"""
n,m=list(map(int,input().split()))
list1=[]
list2=[]
for i in range(n):
    data1=input().split()
    list1.append(data1)
for j in range(n):
    data2=input().split()
    list2.append(data2)
if list1==list2:
    print("Yes")
else:
    print("No")