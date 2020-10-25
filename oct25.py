"""冒泡排序"""
import random      #调用random随机生成数模块
import time
now_time=time.time
def bubble_sort(li):
    for i in range(len(li)-1):   #第i轮
        for j in range(len(li)-1-1):
            if li[j] >li[j+1]:    #如果箭头所指的数，大于箭头后面的数
                li[j], li[j+1] = li[j+1], li[j]
li=[random.randint(0,10000) for i in range (1000)]   #random.randint(参数1，参数2)，函数返回参数1和参数2之间的任意整数，1.2必须为整数
print(li)
bubble_sort(li)
print(li)
end_time=time.time()
print(now_time)
print(end_time)