"""小乐乐转换成绩"""
none=1
while(none):
    N=int(input("Please enter the achievement："))
    if N<100 and N>0:
        none=0
if N <60:
    print("E")
elif N<70:
    print("D")
elif N<80:
    print("C")
elif N<90:
    print("B")
elif N<100:
    print("A")

"""我是大v"""
for i in range(3):
    str = ''
    for j in range(5-i):
        if i == j or i + j == 4 :
            str += 'v'
        else :
            str += ' '
    print(str)

"""小飞机"""
a="*"
print("{: ^12}".format(a*2))
print("{: ^12}".format(a*2))
print(a*12)
print(a*12)
print("{: ^12}".format(a*2))
print("{: ^12}".format(a*2))


a="*"
for i in range(6):
    if i<2:
        print("{: ^12}".format(a * 2))
    elif 2<i<5:
        print(a * 12)
    else:
        print("{: ^12}".format(a * 2))