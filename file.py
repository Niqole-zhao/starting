a={"ronny":"yang","2017":"0601"}
print("2017" in a)#判断变量是否在字典中
k="ronny"
for k in a:
    print("字典的键和值分别是：{}和{}".format(k,a.get(k)))
a=chr(1001)
b=chr(1002)
c=ord("a")
d=ord("z")
print(a,b,c,d)