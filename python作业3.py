print('------------- 第一题 -----------------')
# 第一题:
# 需求: 使用列表推导式生成0-10之间的奇数列表.然后遍历输出每个元素的值.
list1 = [i for i in range(1, 11, 2)]
for l1 in list1:
    print(l1)


print('------------- 第二题 -----------------')
# ## 第二题:
# 定义函数,实现求任意两个数的最大值并返回.最后调用函数测试功能是否实现.


def max_value(a, b):
    if a > b:
        return a
    else:
        return b


m = max_value(20, 12)
print(m)

print('------------- 第三题 -----------------')
# ## 第三题:
# 定义函数,实现求任意个数字的和并返回.最后调用函数测试功能是否实现.


def sum_value(*args):
    sum3 = 0
    for i in args:
        sum3 += i
    return sum3


n = sum_value(1, 2, 3, 4, 5)
print(n)

print('------------- 第四题 -----------------')
# ## 第四题:
# 定义函数,参数是一个列表类型,实现求列表中各个元素的最大值并返回.最后调用函数测试功能是否实现.


def max_list(list4):
    return [max(e) for e in list4]


l4 = [(1, 3, 4), (2, 3, 4), (5, 3, 2, 8)]
result4 = max_list(l4)
print(result4)

print('------------- 第五题 -----------------')
# ## 第五题:
# 定义一个函数`swap(x, y)`，接收两个参数，返回这两个参数交换后的值（返回两个值）。


def swap(x, y):
    x, y = (y, x)
    return x, y


print(swap('苹果', '西瓜'))

print('------------- 第六题 -----------------')
# ## 第六题
# 有一个元组列表`scores = [('Alice', 85), ('Bob', 92),
# ('Charlie', 78), ('David', 90)]`，
# 使用lambda表达式按照分数从高到低排序。

scores = [('Alice', 85), ('Bob', 92), ('Charlie', 78), ('David', 90)]
scores.sort(key=lambda list6: list6[1], reverse=True)
print(scores)

print('------------- 第七题 -----------------')
# ## 第七题
# 思考一下，有这样的一个列表：
# products = [
#     {"name": "电脑", "price": 7000},
#     {"name": "鼠标", "price": 178},
#     {"name": "usb电动小风扇", "price": 59},
#     {"name": "遮阳伞", "price": 36}
# ]
# 然后小明一共有8000块钱，那么他能不能买下这所有商品？如果能，请输出"能"，否则输出"钱不够，不能完成所有商品的购买"。

products = [
    {"name": "电脑", "price": 7000},
    {"name": "鼠标", "price": 178},
    {"name": "usb电动小风扇", "price": 59},
    {"name": "遮阳伞", "price": 36}
]

sum7 = 0

for dict7 in products:
    sum7 += dict7['price']

if sum7 <= 8000:
    print('能')
else:
    print('钱不够，不能完成所有商品的购买')



