"""汉诺塔问题"""
# def hanoi(n,a,b,c):    #从a，经过b，移动到c
#     if n>0:
#         hanoi(n-1,a,c,b)  #从a，经过c，移动到b
#         print("moving from %s to %s" %(a,c))
#         hanoi(n-1,b,a,c)    #从b，经过a，移动到c
# hanoi(4,"A","B","C")
"""顺序查找"""
# def linner_search(li,val):
#     for index, x in enumerate(li):
#         if x==val:
#             return index
#     else:                #注意else的缩进
#             return None
# print(linner_search([3.41,4,1,3,6,10], 10))

"""二分查找"""
def binary_search(li,val):
    left = 0
    right = len(li) - 1
    while left <= right:    #说明此时候选区不为空
        mid =(left + right) // 2
        if li[mid] == val:
            return mid
        elif li[mid] > val:
            right = mid - 1
        else:
            left = mid + 1
    else:
        return -1
print(binary_search([1,2,3,4,5,6,7,8,9], 6))