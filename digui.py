"""分解质因数"""
# def factory(N):
#     for i in range(2,N):
#         if N%i==0:
#             return factory(i)+factory(int(N/i))
#     else:
#             return [N]
# print(factory(76))
"""循环求1--100的和"""
# def sum(i):
#     sum=0
#     j=1
#     while j<=i:
#         sum =sum+j
#         j +=1
#     return sum
# print(sum(100))

"""递归求1--100的和"""
def sum(n):
    if (n==1):
        return 1
    return n+sum(n-1)
print(sum(100))