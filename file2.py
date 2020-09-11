# a=open("E:\\python text\\python.txt",'r+')
# print(a.readline())
# a.write("，但是")
# a.close()
#
# f=open("E:\\python text\\b.txt",'r')
# b=f.readlines()
# print(b)
# f.close()
# b=f.read()
# print(b)
# f.close()
#
# f=open("E:\\python text\\b.txt",'r')
# for line in f:
#     print(line)=
# f.close()

f=open("E:\\python text\\b.txt",'w')
f.write("像风走过八千里，不问归期。\n")
f.write("二月花开，三秋落叶。")
print(f)
f.close()

c=["我还是喜欢你，像风走了八千里，不问归期。"
   "\n二月花开，三秋叶落，它见过哭泣的鱼。"
   "\n我还是喜欢你，像鱼看罢半夜雨，泪藏水底，没有痕迹，不必提起。"]
h=open("E:\\python text\\b.txt",'w')
h.writelines(c)
print(h)
h.close()