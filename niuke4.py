"""将四位数反向输出"""
# a=input("Enter a int (1000<=n<=9999):")
# def reverse_string(self,a):
#     if len(a)<=4:
#         reversed_a="".jion(reversed(a))
#         return reversed_a
#         return a
# print(' '.join(a))

# a=list(input("Enter a int (1000<=n<=9999):"))
# a.reverse()
# print(''.join(a))

"""你能活多少秒"""
# age=int(input("Enter your age(0<age<200): "))
# s=int(3.156e7*age)
# print("You can live ",s,"'s")

"""时间转换"""
s=int(input("Enter the seconds in 0< seconds < 100,000,000: "))
m=s//60#分钟数m
h=m//60#小时数m
s1=s%60#除去分钟数后剩下的秒数为s1
m1=m%60#除去小时数后剩下的分钟数为s1
print(h,"\t",m1,"\t",s1)