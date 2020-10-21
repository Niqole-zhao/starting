from pythonds.basic.stack import Stack
infixexpr="3+(6*7-2)+2*3"
def infixToPostfix(infixexpr):
    prec = {}
    prec["*"]=3
    prec["/"]=3
    prec["+"]=2
    prec["-"]=2
    prec["("]=1
    opStack=Stack()
    postfixList=[]
    tokenList = infixexpr.split()
    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token=="(":
            opStack.push(token)
        elif token ==")":
            topToken = opStack.pop()
            while topToken !="(":
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while(not opStack.isEmpty()) and \
                (prec[opStack.peek()] >=prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return "".join(postfixList)
print(infixToPostfix(infixexpr))


# expression = "3+6*7-2+2*3"
# """isnumeric() 方法检测字符串是否只由数字组成。这种方法是只针对unicode对象。是数字返回Ture,不是返回False"""
# def middle2behind(expresssion):
#     result = []             # 结果列表
#     stack = []              # 栈
#     for item in expression:
#         if item.isnumeric():      # 如果当前字符为数字那么直接放入结果列表
#             result.append(item)
#         else:                     # 如果当前字符为一切其他操作符
#             if len(stack) == 0:   # 如果栈空，直接入栈
#                 stack.append(item)
#             elif item in "(*/":   # 如果当前字符为（，直接入栈
#                 stack.append(item)
#                 """#遇到一个运算符，从栈中弹出具有相等或更高优先级别的运算符，将它们添加到后缀表达式末尾。
#                 因此此处不需要“+-”运算符"""
#             elif item == ')':     # 如果右括号则全部弹出（碰到左括号停止）
#                 t = stack.pop()
#                 while t != '(':
#                     result.append(t)
#                     t = stack.pop()
#             # 如果当前字符为加减且栈顶为乘除，则开始弹出
#             elif item in '+-' and stack[len(stack)-1] in '*/':
#                 if stack.count('(') == 0:           # 如果有左括号，弹到左括号为止
#                     while stack:
#                         result.append(stack.pop())
#                 else:                               # 如果没有左括号，弹出所有
#                     t = stack.pop()
#                     while t != '(':
#                         result.append(t)
#                         t = stack.pop()
#                     stack.append('(')
#                 stack.append(item)  # 弹出操作完成后将‘+-’入栈
#             else:
#                 stack.append(item)# 其余情况直接入栈（如当前字符为+，栈顶为+-）
#
#     # 表达式遍历完了，但是栈中还有操作符不满足弹出条件，把栈中的东西全部弹出
#     while stack:
#         result.append(stack.pop())
#     # 返回字符串
#     return "".join(result)
# print(middle2behind(expression))