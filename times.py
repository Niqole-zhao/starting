#斐波那契数列计算
# def fbona(n):
#     a=1
#     b=1
#     for i in range(n):
#         a,b=b,a+b
#     return a
# while(1):
#     n=eval(input("请输入那个需要计算的斐波那契数列："))
#     print(fbona(n))

#计算两个数的平方和、两个数的和
# a=eval(input("请输入a:"))
# b=eval(input("请输入b:"))
# def ff(a,b):
#     return(a**2+b**2,a+b)
# result=ff(a,b)
# print(result)10

""""更正9月18日天传的抛球弹跳实验"""
a=eval(input("请输入球的抛落高度："))
b=eval(input("请输入球的弹跳次数："))
h=0
if b>=0:
    for i in range(0,b):
        h +=a+a*0.6**b
    print("球的运动距离：",h)