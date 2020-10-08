"""绘制六边形"""
# import turtle
# turtle.pensize(1)
# turtle.pencolor("black")
# turtle.speed(3)
# for i in range(1,7):
#     turtle.fd(100)
#     turtle.setheading(i*60)   #turtle.setheading(angele)设置当前朝向为angele角度
# turtle.done()

"""跳台阶"""
# class Solution:
#     def jumpFloor(self, number):
#         # write code here
#         if number==0:
#             return 0
#         elif number==1:
#             return 1
#         elif number==2:
#             return 2
#         a,b=1,2
#         m=3
#         while m<=number:
#             count=a+b
#             a = b
#             b =count
#             m = m+1
#         return count
#     print(jumpFloor("none",5))

"""吃桃子，前n天"""
# n=input("输入天数：")
# def f(n):
#     x=1
#     for i in range (n):
#         x=y
#         y=2*(1+x)
#     print(y)   #错误写法:原因：所写函数中x,y应该用含n的式子代替，对for和if用法不清楚
"""正确写法"""
# def f(n):
#     if n==1:
#         return 1
#     else:
#         return (f(n-1)+1)*2
# print(f(10))

"""吃桃子，第n天"""
def g(n):
    if n==10:
        return 1
    else:
        return 2*g(n+1)+2
print(g(3))
"""当使用return 2*g(n+1)+2时，会发生递归溢出问题"""