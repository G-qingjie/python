# from kkk import my_big
import math
# print(my_big(2,1))

# def quadratic(a,b,c):
   
#     k1 = math.sqrt(b*b-4*a*c)
#     x1 = (k1-b)/(2*a)
#     x2 = (-k1-b)/(2*a)
#     return x1,x2

# print(quadratic(2,3,1))
# print(quadratic(1,3,-4))

# 在Python中定义函数，
# 可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，
# 这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：
# 必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

# def product(*numbers):
#     a=1
#     for i in numbers:
#         a=a*i
#     return a

# print(product(5))
# print(product(5,6))
# print(product(5,6,7))
# print(product(5,6,7,9))

# 汉诺塔
# 请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法，例如：

def move(n,a,b,c):
    if n==1:
        print(a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)

print(move(4, 'a', 'b', 'c'))

