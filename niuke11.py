"""反转字符串"""
# class Solution:
#     def solve(self,str):
#         # write code her
#         len_s=len(str)
#         if len_s>1000:
#             return
#         str1=""
#         for i in str:
#             str1=i+ str1
#         return str1

"""跳台阶"""
class Solution:
    def jumpFloor(self, number):
        if number==0:
            return 0
        elif number==1:
            return 1
        elif number==2:
            return 2
        a,b=1,2
        m=3
        while m <=number:
            count = a+b
            a=b
            b=count
            m=m+1
        return count

