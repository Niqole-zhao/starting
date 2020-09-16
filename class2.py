class Car():
    ""'"汽车目前价值估计程序'
    def __init__(self,make,model,year):#self必不可少且必须位于其他形参前面
                                       #下划线是一种约定，避免python默认的方法与普通方法的名称冲突
        self.make=make#可通过对象访问的变量称为属性
        self.model=model
        self.year=year
        self.this_year=2018
    def mod_this_year(self,new_year):
        self.this_year = new_year

    def detection(self):#方法detection
        duration=self.this_year-self.year
        price=30- 2*duration
        long_name ="你的"+self.make+self.model \
                   +"到目前已经行驶了"+str(duration) \
                   +"年，"+"目前价值"+str(price)+"万"
        return long_name

class ElectricCar(Car):  #父类位于子类前面
    def __init__(self,make,model,year):
        #super将父类和子类函数关联起来，让python调用ElectricCar父类的方法__init__()
        super().__init__(make,model,year)
    def battery(self,capacity):
        self.capacity_num=capacity
        print("您选择的电池容量为：",self.capacity_num,"kWh")
    def detection(self):
        duration =self.this_year - self.year
        price = 30 - duration - (500/self.capacity_num)
        long_name ="你的"+self.make+self.model +"到目前已经行驶了"+str(duration)
        "年,"+"目前价值"+str(price)+"万"
        return long_name

my_tesla=ElectricCar("Tesla ","model a",2017)
print(my_tesla.year)
my_tesla.battery(100)
result=my_tesla.detection()
print(result)