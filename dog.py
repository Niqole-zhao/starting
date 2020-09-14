class Dog():
    """"一次模拟小狗的简单尝试"""
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sit(self):
        """"模拟小狗蹲下时命令"""
        print (self.name.title()+" is now sitting")
    def roll(self):
        """模拟小狗打滚时命令"""
        print ("My dog is "+str(self.age)+"years and it can roll.")

my_dog=Dog("willie",5)
result1=my_dog.sit()
result2=my_dog.roll()