"""计算100以内所有数相加的和"""
def sum_recu(x):
    if x>0:
        return x+sum_recu(x-1)
    else:
        return 0

    sum_cycle(100)
    sum = sum_recu(100)
    print(sum)

"""用循环求解"""
def sum_recu(n):
    sum=0
    for i in range(n):
        sum +=i
    sum_recu(100)
    print(sum)

"""map函数"""
# def add(x,y,z):
#     return x+y+z
#
# list1=[1,2,3]
# list2=[1,2,3]
# list3=[1,2,3]
# res=map(add,list1,list2,list3)
# print(list(res))
"""在第一次中分别将list1，list2和list3中的第一项相加，
假如其中有一个列表少一项，用none代替，
在列表中只会输出两个值，没有第三个值"""