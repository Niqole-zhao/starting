"""小乐乐与序列"""
list=input().split("\n")
list_new=[]
for i in list:
    if i not in list_new:
        list_new.append(i)
        list_new.sort()
print(list_new)

"""小乐乐改数字"""
list_old=input().split()
list_new=[]
for i in list_old:
    if int(i)%2==0:
        list_new.append(0)
    else:
        list_new.append(1)
print(list_new)

"""小乐乐走台阶"""
n=int(input())
def f(n):
    if n==0:
        return 0
    if n==1:
        return 1
    if n==2:
        return 2
    else:
        return f(n-1)+f(n-2)
print(f(n))