"""小乐乐是否叫家长"""
# a,b,c = map(int,input().split())
# if (a+b+c)/3>=60:
#     print("No")
# else:
#     print("No")

"""判断奇数和偶数"""
# while True:
#     try:
#         a=input().split()
#         for i in a:
#             if int(i) & 1 == 1:
#                 print("Odd")
#             else:
#                 print("Even")
#     except:
#         break

"""奇偶统计"""
while True:
    try:
        a=input().split()
        b=0
        for i in range(a):
            i=b
            b +=1
            if int(i) & 1 ==1:
                print("Odd")
            else:
                print("Even")
    except:
        break