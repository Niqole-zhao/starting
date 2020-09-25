# def indexOfMin(lyst):
#     minIndex=0
#     currentIndex=1
#     while currentIndex < len(lyst):
#         if lyst[currentIndex] < lyst[minIndex]:
#             minIndex = currentIndex
#         currentIndex +=1
#     return minIndex
#     print(minIndex)

# print('Hello,World!')
# print('__name__value: ', __name__)
# def main():
#     print('This message is from main function')
# if __name__ =='print_func':
#     print("Done!")

"""KIKI喝酸奶"""
n,h,m=map(int,input().split( ))
if m%h==0:
    print(int(n-m/h))
else:
    print(int(n-m//(h+1)))