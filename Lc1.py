"""二叉树的最大深度"""
class Solution:
    def maxDepth(self,root):
        if root is None:
            return 0
        return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))

"""二叉树的最小深度"""
class Solution:
    def mindepth(self,root):
        if root is None:
            return 0
        return 1+min(self.mindepth(root.left),self.mindepth(root.right))



"""罗马数字转换为整数"""
class Solution:
    def romanToInt(self , s ):
        c={"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
        ans=0
        for i in range(len(s)-1):
            if c[s[i]]<c[s[i+1]]:
                ans -=c[s[i]]
            else:
                ans +=c[s[i]]
        ans +=c[s[-1]]
        return ans