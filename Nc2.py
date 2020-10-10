"""字符串的反转"""
# class Solution:
#     def solve(self,str):
#         # write code her
#         if len(str)>1000:
#             return
#         str1=""
#         for i in str:
#             str1=i+str1
#         return str1
#     print(solve(1,("a b c d")))

# class Solution:
#     def solve(self,str):
#         # write code her
#         if len(str)>1000:
#             return
#         str1=""
#         for i in range (len(str)):
#             str1=str[len(str)+i]
#         return str1
#     print(solve(1,("a b c d")))
"""错误原因，超出str的最大范围"""

"""二叉树最大深度"""
class Solution:
    def maxDepth(self , root ):
        # write code here
        if root is None:
            return 0
        else:
            return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))