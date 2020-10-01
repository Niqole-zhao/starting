A = [1, 3, 2, 4, 5]
for i in range(len(A)):
    min_ind = i
    for j in range (i+1,len(A)):
        if A[min_ind] >A[j]:
            min_ind=j
            A[min_ind],A[i]= A[i],A[min_ind]
print("排序后的数组：")
for i in range(len(A)):
    print("%d" % A[i])


# lyst=[1,3,2,4,5]
# def selectionSort(lyst):
#     i=0
#     while i <len(lyst)-1:
#         minIndex=i
#         j=i+1
#         while j<len(lyst):
#             if lyst[j]>lyst[minIndex]:
#                 minIndex=j
#             j+=1
#         if minIndex !=i:
#             swap(lyst,minIndex,i)
#         i +=1


