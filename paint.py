import turtle
# turtle.setup()#窗口会消失
# turtle.done()#保证窗口一直存在，因此在程序结尾放上turtle.done()这个函数
# turtle.forward(200)  #沿着当前方向前进指定距离,缩写fd
# turtle.backward(200)   #backward()沿着相反方向绘制直线,缩写bk
# turtle.right(90)   #向右旋转90°
# turtle.fd(100)
# turtle.left(45)    #向左旋转45°
# turtle.setheading(120)    #设置当前朝向为angle角度
# turtle.left(45)
# turtle.fd(100)
# turtle.goto(100,100)  #移动到绝对坐标（100,100）处
# turtle.circle(20,360)   #画圆。半径20，，角度360°
# turtle.undo()   #撤销上一步动作

# turtle.speed(10)
# turtle.fd(100)
# turtle.penup()   #penup()提起画笔
# turtle.fd(200)
# turtle.pendown()   #pendown()放下画笔，与penup（）配对使用
# turtle.circle(50,360)
# turtle.pensize(1)
# turtle.fd(100)
# turtle.color("green")   #color()设置画笔颜色
# turtle.pensize(2)
# turtle.fd(100)

"""填充颜色需要begin_fill()和end_fill()合在一起才能实现"""
# turtle.begin_fill()
# turtle.color("red")
# turtle.circle(50,360)
"""color在circle前，则整个图形均为填充的颜色；
在之后，则图形边框为之前画笔颜色"""
# turtle.end_fill()
# print(turtle.filling())
"""filling()返回填充状态，True已填充，Flase未填充。
其中，放在end_fill之后为未填充，在end_fill前面为填充"""
# turtle.fd(200)
# turtle.clear()   #clear()清空窗口，但不改变当前画笔位置
#reset()清空当前窗口，并重置位置等状态为默认值
# turtle.reset()

# turtle.fd(1000)
# turtle.screensize(3000,3000)
#hideturtle()隐藏画笔的turtle形状,showturtle显示画笔形态
turtle.circle(100,360)
turtle.hideturtle()
turtle.showturtle()
print(turtle.isvisible())#isvisible()如果turtle可见返回true，否则返回false
turtle.done()