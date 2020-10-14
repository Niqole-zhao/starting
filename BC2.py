"""小乐乐找数字"""
# n=int(input())
# num=input() #此处不能选择int(input()),因为输入态度数字则不能进行整数格式
# x=int(input())
# y=0
# str=[int(n) for n in num.split()]  #int(n)是指将num中的数进行整数化
# for i in range(n):
#     if x==int(str[i]):
#         y=y+1
# print(y)

"""建立二维数组"""
import numpy
num_list = numpy.zeros((2,4))
print(num_list)
print(type(num_list))
num_list[1][1]=2
print(num_list)

import numpy as np
a = [1,2,3]
b = np.meshgrid(a)
print(b)