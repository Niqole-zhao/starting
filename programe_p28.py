"""求球体的直径、圆周长、表面积和体积"""
# r=float(input("输入球体的半径："))
# R=2*r
# S=4*3.14*R**2
# V=4/3*3.14*R**3
# print("球体的直径是：",R)
# print("球体的表面积是：",round(S,2))
# print("球体的体积是：",round(V,2))

"""雇员周薪求解问题"""
# nlist1=(float(input("请输入每小时正常工资：")))
# nlist2=(float(input("请输入本周加班总时间：")))
# nsalary=nlist1
# otime=nlist2
# ntime=8*5
# oslary= nsalary*1.5
# wsalary= nsalary*ntime+ oslary*otime
# print(wsalary)

"""球的弹跳距离"""
flow=float(input("请输入初始高度（即球下落高度）："))
times=int(input("允许球弹跳次数："))
d=""
if times>=0:
    for s in range (0,flow):
        d +=flow+flow*0.6**times
print("球的弹跳距离是")

"""求取π的近似值"""
def appi(n):
    value=0
    b=1
    for i in range(n):
        value +=b*(2*i-1)*-1
        b=b*-1
    return value*4