"""球的弹跳距离"""
# flow=float(input("请输入初始高度（即球下落高度）："))
# times=int(input("允许球弹跳次数："))
# d=0
# rate=0.6
# if times>=0:
#     for s in range(0,times):
#         d +=flow+flow*rate**times
# print("球的弹跳距离是",d)

def bounce_height_recursion(h,n,rate=0.6):
    d=0
    if n >= 0:
        for s in range(0,n):
            d +=h+h*rate**n
            if __name__== "__main__":
                h=int(input("Please enter the hight of the ball:\n"))
                n = int(input("Please enter the bounce times of the ball:\n"))
print(bounce_height_recursion)