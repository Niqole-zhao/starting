#类的第一个名称大写，易于让读者发现是类，不是函数
class Car():
    def __init__(self,make,model,year):#self必不可少且必须位于其他形参前面
                                       #下划线是一种约定，避免python默认的方法与普通方法的名称冲突
        self.make=make#可通过对象访问的变量称为属性
        self.model=model
        self.year=year
    def detection(self):
        duration=2018-self.year
        price__=  30- 2*duration
        long_name ="你的"+self.make+self.model \
                   +"到目前已经行驶了"+str(duration) \
                   +"年，"+"目前价值"+str(price)+"万"
        return long_name

my_car=  Car("Audi","A4",2013)
print(my_car.year)
result=my_car.detection()
print(result)
your_car=  Car("奔驰","c200",2012)
result=my_car.detection()
print(result)
a=[1,2,3,4]
a.count()