""""一维数据用列表表示"""
# ls=["北京","上海","天津","重庆"]
# f=open("E:\\python text\\city.txt","w")
# b="，".join(ls)
# print(b,type(b))
# f.write(".".join(ls))#join前面为点号，不是逗号；join()用于将序列中的元素以指定的字符连接生成新的字符串
# f.close()

""""csv是一种通用的文件格式"""
# ls=["北京","上海","天津","重庆"]
# f=open("E:\\python text\\city.csv","w")
# f.write(",".join(ls))
# f.close

# ls=["北京","上海","天津","重庆"]
# f=open("E:\\python text\\city.csv","r")
# ls=f.read()
# print(ls)
# ls_now=ls.split(':')#a.split()能够通过指定分隔符对字符串进行切片，返回列表
# f.close()
# print(ls_now)


""""二维数据的存储，二维数据的表示：列表嵌套列表"""
# ls=[["居民消费价格指数","102","102.4","102"],
#     ["食品","103","134","213"],
#     ["医疗","124","323","344"]]
# f=open("E:\\python text\\cpi.csv","w")
# for row in ls:
#     f.write(",".join(row)+"\n")
# f.close

""""将二维数据返回到列表中"""
f=open("E:\\python text\\cpi.csv","r")
ls=[]
for line in f:
    a=line.strip('\n')
    print(a)
    b=a.split(',')
    print(b)
    ls.append(b)
    # ls.append(line.strip('\n').split(','))
f.close()
print(ls)