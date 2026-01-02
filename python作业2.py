# ## **基础循环题**
#
# 1. **计算1到100的和**：使用while循环计算1+2+3+...+100的和

# sum = 0
# i = 1
# while i <= 100:
#     sum += i
#     i += 1
# print(sum)

# 2. **倒计时程序**：使用while循环从10倒数到1，然后打印"发射！"

# i = 10
# while i > 0:
#     print(i)
#     i -= 1
# print('发射！')

# 3. **统计字母**：输入一个字符串，使用for循环统计其中字母'a'出现的次数

# str = input('输入字符串：')
# count = 0
# for chr in str:
#     if chr == 'a':
#         count += 1
# print(f'字母a出现的次数：{count}')

# ## **break/continue应用(循环使用for)**
#
# 1. **找到第一个7的倍数**：从1开始循环，找到100以内第一个能被7整除的数后停止

# for i in range(1,101):
#     if i % 7 == 0:
#         print(f'第一个7的倍数是：{i}')
#         break

# 2. **跳过特定数字**：打印1-20中所有不是3的倍数的数字

# for i in range(1, 21):
#     if i % 3 == 0:
#         continue
#     print(i)

# 3. **密码验证**：使用while循环模拟密码验证（正确密码设为"123456"），最多尝试3次

# i = 3
# while i > 0:
#     password = input('请输入密码：')
#     if password == '123456':
#         print('密码正确,登录成功...')
#         break
#     i -= 1
#     if i == 0:
#         print(f'已达到当天最大输入次数，请明天再尝试！！！')
#     else:
#         print(f'密码错误,请重新输入。还可尝试次数：{i}')

# 4. **计算到100但跳过某些数**：计算1到100的和，但当和超过200时停止

# sum = 0
# for i in range(1, 101):
#     sum += i
#     if sum > 200:
#         print(f'计算值从1到{i},当前和为：{sum}')
#         break

#
# ## **字符串基础操作**
#
# 1. **字符串反转**：输入一个字符串，使用循环将其反转输出

# 解法一：
# str = input('请输入任意值：')
# print(f'反转值为：{str[::-1]}')

# 解法二：
# str = input('请输入任意值：')
# new_str = ''
# i = len(str) -1
# while i >= 0:
#     new_str += str[i]
#     i -= 1
# print(new_str)


# 2. **检查回文**：判断一个字符串是否是回文（正读反读都一样）

# 解法一：
# str = input('请输入任意值：')
# i = 0 # 循环值，位置索引
# end = len(str) // 2 # 字符串长度一半的值
# reversed_str = str[len(str)-1:len(str)-end-1:-1] # 截取原字符串长度一半的反转值
# while i < end: # 从0开始到字符串长度一半的值进行循环。
#     # 判断字符串与反转字符串对应位置的字符是否一致
#     # 如果全部一致则判定为回文
#     # 如果对应位置的字符一致则位置索引加一
#     # 否则判定为非回文
#     if str[i] == reversed_str[i] and i == end - 1:
#         print('该字符串是回文')
#         break
#     elif str[i] == reversed_str[i]:
#         i += 1
#     else:
#         print('该字符串不是回文')
#         break

# 解法二：
# str = input('请输入任意值：')
# reversed_str = str[::-1]
# len = len(str)
# for i in range(0, len):
#     if str[i] == reversed_str[i] and i == len -1:
#         print('该字符串是回文')
#         break
#     elif str[i] == reversed_str[i]:
#         continue
#     else:
#         print('该字符串不是回文')
#         break

# 解法三：
# str = input('请输入任意值：')
# if str == str[::-1]:
#     print('该字符串是回文')
# else:
#     print('该字符串不是回文')

# 3. **提取用户名**：从邮箱地址（如"user@example.com"）中提取@符号前的用户名

# str = 'user@example.com'
# at_pos = str.find('@')
# print(f'用户名：{str[:at_pos]}')

#
# ## **字符串索引和切片**
#
# 1. **提取首尾字符**：输入一个字符串，提取并打印第一个和最后一个字符
#
# str = input('输入任意值：')
# print(f'第一个字符为：{str[:1]}\n最后一个字符为：{str[-1:-2:-1]}')

# 2. **字符串分段**：将字符串"PythonProgramming"分成"Python"和"Programming"两部分

# str = 'PythonProgramming'
# print(f'第一部分：{str[:6]}\n第二部分：{str[6:]}')

# 3. **隔字符提取**：提取字符串中所有奇数位置的字符（索引1,3,5...）

# 解法一：
# str = input('输入任意值：')
# new_str = ''
# for i in range(1,len(str),2):
#     new_str += str[i]
# print(f'奇数位置的字符：{new_str}')

# 解法二：
# str = input('输入任意值：')
# print(str[1::2])


