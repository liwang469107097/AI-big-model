### 题目1(简答题)
# 请使用自己的话说说Python的优缺点？

- Python优点：简单, 易学,应用广泛
- Python缺点：执行效率慢

### 题目2(简答题)
# 请独立默写出标识符的几条规范。
1. 不能以数字开头
2. 只能有字母、数字和下划线
3. 不能使用关键词
4. 严格区分大小写

### 题目3（实操题）
# 定义小数price、weight、money，输出`苹果单价9.00元／⽄，购买了5.00⽄，
# 需要支付45.00元`。[备注：记得添加必要的注释。]

price = 9.0 # 价格
weight = 5.0 # 重量
money = 45.0 # 费用

print(f'苹果单价{price}元／⽄，购买了{weight}⽄，需要支付{money}元')

### 题目4（实操题）
'''
用户登录系统：用户输入用户名和密码，在控制台格式化输出用户输入的用户名和密码。
[备注：记得规范化变量命名。]效果如下：
> 请输入用户名：Jerry
> 请输入密码：jerry666
> 您好，您输入的用户名是Jerry, 密码是jerry666，欢迎登录系统。
'''
username = input('请输入用户名：')
password = input('请输入密码：')

print(f'您好，您输入的用户名是{username}, 密码是{password}，欢迎登录系统。')

### 题目5（实操题）
'''
已知用户姓名、年龄、体重数据，要求从键盘上录入用户信息，并在控制台格式化输出用户信息，
例如`用户姓名:TOM,年龄:18岁,当前体重是50.55kg。`。[备注：记得规范化变量命名，
以及添加必要的注释。]
'''
username = input('请输入用户名：')
age = int(input('请输入年龄：'))
weight = eval(input('请输入体重：'))

print(f'用户姓名:{username},年龄:{age}岁,当前体重是{weight:.2f}kg。')

### 题目6（实操题）
'''
键盘录入考试成绩score,输出对应成绩等级.
0~60分 不及格
60~70  及格
70~80  良好
80~100 优秀
'''
score = int(input('请输入考试成绩：'))

if score > 80 and score <= 100:
    print('优秀')
elif score > 70 and score <= 80:
    print('良好')
elif score > 60 and score <= 70:
    print('及格')
else:
    print('不及格')

### 题目7（实操题）
'''
在运输货物时，通常是：每吨货物每公里运费P(元)与运输距离S(运输公里数)有关，路途越远，每公里运价越低。运输货物计算公式如下：

'''

weight = eval(input('请输入货物吨数：'))
distance = eval(input('请输入运输公里数：'))

price = 0.0 # 实际运费

if distance >= 500:
    price = weight * distance * 5
elif distance >= 300 and distance < 500:
    price = weight * distance  * 5.5
elif distance >= 200 and distance < 300:
    price = weight * distance  * 6
elif distance >= 150 and distance < 200:
    price = weight * distance  * 7
elif distance >= 100 and distance < 150:
    price = weight * distance  * 8
else:
    price = weight * distance  * 10

if price > 5000:
    price *= 0.95
else:
    price

print(f'应付的实际运费额：{price}')
