# def word(s1,s2):
#     alist=list(s2)
#     pos1=0
#     still=True
#     while pos1<len(s1) and still:
#         pos2=0
#         found=False
#         while pos2<len(alist) and not found:
#             if s1[pos1]==alist[pos2]:
#                 found =True
#             else:
#                 pos2=pos2+1
#         if found:
#             alist[pos2]=None
#         else:
#             still=False
#         pos1=pos1+1
#     return still
#

# print(word("abcde","acdb"))
"""kiki算数"""
# a,b=map(int,input().split()) #map() 会根据提供的函数对指定序列做映射。此处用map是为了将输入的两个数都转换为整数型
# sum=a+b
# if sum>=100:
#     c=sum%100
#     # if c[-2]==0:
#     #     sum_kiki=c[-1]
#     # else:
#     #     sum_kiki=c[-1,-3]
# print(sum)
# print(c)

"""序列中删除指定参数"""
N=input()
data=list(input().strip().split())
x=input()
if x in data:
    data.remove(x)
    print(*data)
    print(x)

