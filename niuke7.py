"""计算问题"""
a,b,c,d=int(input().split())
print((a+b+c)*d)


"""定义电子日历"""
class TDate:
    def __init__(self,month=0,day=0,year=0):
        self.__month = month
        self.__day = day
        self.__year = year
    def pri_a(self):
        print("{}/{}/{}".format(self.__day,self.__month,self.__year))
    def setDate(self,m,d,y):
        self.__month = m
        self.__day = d
        self.__year = y
td = TDate()
a,b,c = map(int,input().split())
td.setDate(y=a,m=b,d=c)
td.pri_a()