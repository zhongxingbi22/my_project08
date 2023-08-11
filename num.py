ef multiply_integers(a, b):
    result = a * b
    return result

# 输入两个整数
num1 = int(input("请输入第一个整数："))
num2 = int(input("请输入第二个整数："))

# 调用函数进行乘法运算并打印结果
product = multiply_integers(num1, num2)
print("结果：", product)
