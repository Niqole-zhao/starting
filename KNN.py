import matplotlib.pyplot as plt  #matplotlib用于数据的展示
import numpy as np
#-------------视觉图分析-------------
a=np.array([[3,104],
          [2,100],
          [1,81],
          [101,10],
          [99,5],
          [98,2]])
for i in range(3):
    plt.plot([18,a[i,0]],[90,a[i,1]],color="r")
    plt.scatter([18,a[i,0]],[90,a[i,1]],color="r")
for i in range (3,6):
    plt.plot([18, a[i, 0]], [90, a[i, 1]], color="b")
    plt.scatter([18, a[i, 0]], [90, a[i, 1]], color="b")
plt.scatter(18,90,color="y")
plt.show()
#-------------KNN核心代码-------------
def KNN(inX,dataSet,labels,k):
"""inX用于分类的输入向量   c
   dataSet输入的训练样本集  a
   labels标签向量    b
   k用于选择的最邻近的数目   4"""
   dataSetSize =dataSet.shape[0]   #用于获取dataSet的行列数，结果为6
   print("dataSetSize:",dataSetSize)
   diffMat =np.tile(inX,(dataSetSize,1))- dataSet  #第一步：计算已知类别
   print(np.tile(inX,(dataSetSize,1)))
   print("diffMat:\n",diffMat)
   sqDiffMat =diffMat **2
   print("sqDiffMat:\n",diffMat)
   aqDistances =sqDiffMat.sum(axis=1)
   print("aqDistances:\n",aqDistances)
   distances=aqDistances**0.5
   print("distances:\n",distances)
   sortedDistlandicies =distances.argsort()   #第二步，从小到大排序
   print("sortdDistIndicies",sortedDistlandicies)
   classCount={}
   for i in range (k):  #选取与当前点距离最小的K个点
       votellabel =labels[sortedDistlandicies[i]]
       print("voteIlabel:",votellabel)
       classCount[votellabel]=classCount.get(votellabel,0)+1
       print("sortedClassCount:",classCount)
    print("items:",classCount.items())
    sortedClassCount = list(classCount.items())
    print("sortedClassCount:",sortedClassCount)
    sortedClassCount.sort(key=lambda x:x[1],reverse=True)
    print(sortedClassCount[0][0])
    return sortedClassCount[0][0]
