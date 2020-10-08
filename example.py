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
class Solution:
    number = input("输入台阶数：")
    def jumpFloor(self, number):
        # write code here
        if number==0:
            return 0
        elif number==1:
            return 1
        elif number==2:
            return 2
        a,b=1,2
        m=3
        while m<=number:
            count=a+b
            a = b
            b =count
            m = m+1
        return count
        print(count)