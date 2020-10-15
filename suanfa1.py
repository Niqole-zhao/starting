import time
star_time=time.time()
for a in range (1001):
    for b in range(1001):
        c=1000-a-b
        if  a**2+b**2==c**2:
            print(a,b,c)
print('end')
end_time=time.time()
print(end_time-star_time)
"""错误解法，原因：a,b,c不能选择同时在一个for函数中，
因为需要在满足a的情况下求b,c，在满足a,b情况下求c"""
# for a,b,c in range(1001):
#     if a+b+c==1000 and a**2+b**2==c**2:
#         print(a,b,c)
