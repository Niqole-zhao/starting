"""插入排序"""
import random
import time
a=time.time()
def insert_sort(li):
    for i in range(1,len(li)):   #i表示摸到的牌的下标
        tmp = li[i]
        j = i - 1   #j指的是手里的牌的下标
        while j >= 0 and li[j] > tmp:
            li[j+1] = li[j]
            j -= 1
        li[j+1] = tmp
li = list(range(1000))
random.shuffle(li)    #.shuffle打乱顺序
print("排序前：",li)
insert_sort(li)
print("排序后:",li)
b=time.time()
print(b-a)
