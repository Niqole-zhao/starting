"""选择排序简单版"""
# def simple_sort(li):
#     li_new = []
#     for i in range(len(li)):    #需要遍历的次数
#         min_val = min(li)    #找最小的数
#         li_new.append(min_val)
#         li.remove(min_val)
#     return li_new
# li=[3,2,4,1,5,6,7,8,9]
# print("原来列表：",li)
# print("排序后列表：",simple_sort(li))

"""选择排序较好版"""
# def better_sort(li):
#     for i in range(len(li)-1):   #i表示第几轮
#         min_loc = i
#         for j in range(i+1,len(li)):
#             if li[j] < li[min_loc]:
#                 min_loc = j
#                 li[i], li[min_loc] = li[min_loc], li[i]
#
# li=[3,4,2,1,5,6,8,7,9]
# print("原来列表：",li)
# better_sort(li)
# print("排序后列表：",li)

"""插入排序"""
def insert_sort(li):
    for i in range(1,len(li)):     #i表示摸到的牌的下标
        tmp=li[i]
        j = i-1    #j表示手里的牌的下标
        while j >= 0 and li[j] > tmp:
            li[j+1] = li[j]
            j -= 1
        li[j+1] = tmp