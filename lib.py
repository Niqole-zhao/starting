import time   #打开time 库的入口
# time.time()  #ctrl
# lctime=time.localtime()#使用time库里面的localtime 这一方法
# first_time=time.time()
# a=0
# for i in range(1000):
#     a +=1
# print(a)
# last_time=time.time()
# print(last_time-first_time)
# print(time.gmtime())   #用户不能直接使用gmtime,gmtime获取的是世界统一时间，不是当地时间
# print(time.ctime())   #获取当前时间对应的易读字符串表示，内部会调用localtime（）以输出当地时间

"""时间格式化"""
# t =time.localtime()
# print(t)
# print(time.mktime(t))#将struct_time对象t转换为时间戳，t代表当地时间
#
# t=time.localtime()
# a=time.strftime("%Y-%m-%d %H:%M:%S",t)
# print(a)
# """strptime()与strftime()方法完全相反，
# strptime()用来提取字符串中的时间，可以灵活作为time模块的输入接口
# strftime()时间格式化最有效的方法，几乎可以以任何通用格式输出时间，用格式字符表达时间"""
# timeString="2018-06-01 12:55:20"
# a=time.strptime(timeString,'%Y-%m-%d %H:%M:%S')
# print(a)

"""程序计时"""
"""time.sleep（）推迟调用线程的运行，表示程序挂起的时间，时间参数设置在（）内"""
# star_time=time.time()
# time.sleep(2)
# last_time=time.time()
# print(last_time-star_time)

"""time.perf_counter()时间精度高于time.time()"""
# a1=time.perf_counter()   #第一次运行时时系统随机分配的时间，要知道运行时间需要用第二个减去第一个时间
# # a2=time.perf_counter()
# # print(a1,a2)
# b1=time.time()
# a2=time.perf_counter()
# b2=time.time()
# print("perf_counter起始时间：",a1,"结束时间：",a2,"间距:",a2-a1)
# print("time起始时间：",b1,"结束时间：",b2,"间距:",b2-b1)

"""模拟进度条显示"""
scale=50
print("-----程序开始执行")
star_time=time.perf_counter()
for i in range(scale+1):
    a="*"*i
    b="."*(scale-i)
    c=(i/scale)*100
    dur=time.perf_counter()-star_time
    print('\r{:^3.0f}%[{}->{}]{:.2f}s'.format(c,a,b,dur),end="")   #\r将光标位置回退到本行开头位置
    time.sleep(0.2)
print("\n-----程序执行结束")