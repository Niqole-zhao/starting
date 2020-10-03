#题目1
def adder(x):
    def wrapper(y):
        return x + y
    return wrapper
adder5 = adder(5)
print(adder5(adder5(6)))

#题目2
import math
a, b, c =input('Enter a,b,c:').split()
s = a + b + c
s = s / 2.0
area =math.sqrt(s*(s-a)*(s-b)*(s-c))
print('The area is:', area)
