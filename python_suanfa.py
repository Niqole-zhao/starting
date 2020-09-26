sortedLyst=[20,44,48,55,62,66,74,88,93,99]
target=90
def binarSearch(target,sortedLyst):
    left=0
    right=len(sortedLyst) -1
    while left <=right:
        midpoint =(left+right)//2
        if target ==sortedLyst[midpoint]:
            print(binarSearch(sortedLyst[midpoint]))
            return midpoint
        elif target < sortedLyst[midpoint]:
            right = midpoint -1
        else:
            left = midpoint +1
    return -1
