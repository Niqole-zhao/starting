import turtle
turtle.setup()
"""第一颗心"""
turtle.color("red")
turtle.setheading(135)
turtle.fd(100)
turtle.right(-180)
turtle.circle(50,-180)
turtle.left(90)
turtle.circle(50,-180)
turtle.right(180)
turtle.fd(100)
"""第二颗心"""
turtle.penup()
turtle.goto(100,30)
turtle.pendown()
turtle.setheading(135)
turtle.fd(100)
turtle.right(-180)
turtle.circle(50,-180)
turtle.left(90)
turtle.circle(50,-180)
turtle.right(180)
turtle.fd(100)
"""箭头"""
turtle.penup()
turtle.right(45)
turtle.fd(190)
turtle.pendown()
turtle.right(-205)
turtle.fd(320)
turtle.done()