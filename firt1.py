"""验证两次输入密码是否相等"""
# first=input("")
# second=input("")
# if first==second:
#     print("same")
# else:
#     print("different")

"""小乐乐坐电梯，前面n人"""
# n=int(input())
# a=str((n+1)//12)
# b=str((n+1)%12)
# if b==0:
#     print(a)
# else:
#     print(a+1)
n=int(input())
a=n//12
if (n+1)%12 and a>0:
    t = a*4+2
elif a== 0:
    t = 2
else:
    t= 4*a
print(t)