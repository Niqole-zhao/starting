"""求单位阶跃函数"""
# t=int(input("Plese enter the t and t below to (-1000,1000):"))
# for i in range(t):
#     if t>0:
#         print(θ=1)
#     elif t==0:
#         print(θ=1/2)
#     else:
#         print(θ=0)

"""求期末总成绩"""
experiment=eval(input("Please enter the experimental results:"))
leason=eval(input("Please enter the leason results:"))
process=eval(input("Please enter the process results:"))
test=eval(input("Please enter the test results:"))
sum=experiment*0.2+leason*0.1+process*0.2+test*0.5
print(round(sum,2))