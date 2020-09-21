"""计算"""
a=40
c=212
answer=(-8+22)*a-10+c//2
print(answer)

"""求最高分"""
cort=input("请输入程序设计基础，高数，英语三门课的成绩，用空格分隔：")
a=cort[0:2]
b=cort[3:5]
c=cort[6:8]
if a>=b and a>=c:
    print("三门课中最高分为：",a)
elif b>=a and b>=c:
    print("三门课中最高分为：", b)
else:
    c>=a and c>=b
    print("三门课中最高分为：", c)

"说祝福的话"
n=eval(input("The times for said （1<=n<=20):"))
print("Happy new year! Good luck!\n"*n)