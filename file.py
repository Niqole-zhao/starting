n=eval(input("请输入您购买的数量："))
if n<=1:
    cost=150
elif 2<=n<=4:
    cost=150*n*0.9
elif 4<n<=10:
    cost=150*n*0.8
else:
    cost=150*n*0.7
cost=int(cost)
print("消费总金额为：",cost)

N=eval(input("请输入一个正整数："))
if N==1:
    flag=False
else:
    flag=True
    for i in range(2,N):
        if N%i==0:
            flag=False
            break
print(flag)

a,b=(0,1)
while a<=100:
    print("end",a)
    a,b=b,a+1