"""更正10月1日排序"""
lyst=[3,2,1,5,4]
def selectionSort(lyst):
    i=0
    while i <len(lyst)-1:
        minIndex=i
        j=i+1
        while j<len(lyst):
            if lyst[j]>lyst[minIndex]:
                minIndex=j
            j+=1
        if minIndex !=i:
            swap(lyst,minIndex,i)
        i +=1
    print(("%d" % lyst[i]))

def swap(lyst,i,j,profiler):
    profiler.exchange()
    temp = lyst[i]
    lyst[i]=lyst[j]
    lyst[j]=temp