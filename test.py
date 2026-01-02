# 猜数字
# import random
#
# random = random.randint(1, 100)
#
# while True:
#     input_num = int(input('输入随机数'))
#     if input_num > random:
#         print('猜大了')
#     elif input_num < random:
#         print('猜小了')
#     else:
#         print('猜对了')
#         break
#
# # 巩固练习
# i = 1
# while i <= 10:
#     if i % 3 == 0:
#         # 在这里填写代码, 使得循环分别输出2次, 7次, 13次Hello World
#         break
#     print(f'hello world {i}')
#     i += 1

# 综合案例：for循环 用户名+密码
#
# c_username = 'admin'
# c_password = 'admin888'
#
# for i in range(4):
#     username = input('输入用户名')
#     password = input('输入密码')
#     if i == 3:
#         print('超过登录上限')
#         break
#     elif username == c_username and password == c_password:
#         print('登录成功')
#         break
#     else:
#         print('登录失败')


"""
列表案例
求相邻元素最大值.编写一个程序，求一个正整数列表中每对相邻元素的最大值。
 例如, 输入: [7 8 9 5 6 7 2 3] 输出: [8, 9, 9, 6, 7, 7, 3]
"""

# numbers = [7, 8, 9, 5, 6, 7, 2, 3]
#
# result = []
#
# for i in range(len(numbers)-1):
#     cur_value = numbers[i]
#     next_value = numbers[i+1]
#     result.append(max(cur_value,next_value))
# print(result)

'''
给定列表original_list其中包含1, 2, 2, 3, 4, 4, 5, 6, 6, 7元素，现在通过编写程序对列表中的数据进行去重
'''

# original_list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
#
# unique_list = []
#
# for item in original_list:
#     if item not in unique_list:
#         unique_list.append(item)
#
# print(unique_list)

# 元组案例
'''
编写一个程序来提取嵌套元组中的唯一元素。
例如: 在嵌套元组((1,2,3),(2,4,6),(2,3,5))中, 2重复出现了3次，3重复出现了2次，但我们的输出列表只会包含2、3一次。
即：[1, 2, 3, 4, 5, 6]
'''

# original_tuple = ((1,2,3),(2,4,6),(2,3,5))
# unique_tuple = set()
#
# for item in original_tuple:
#     for inner_item in item:
#         unique_tuple.add(inner_item)
#
# unique_list = list(unique_tuple)
#
# print(original_tuple)
# print(unique_tuple)
# print(unique_list)

'''
巩固练习
给定一个元组my_tuple，里面包含1, 2, 3, 4, 5, 6, 7, 8, 9元素，要求统计数字元组中, 奇数的个数
'''
# my_tuple = (1,2,3,4,5,6,7,8,9)
# od_cnt = 0
#
# for item in my_tuple:
#     if item % 2 == 1:
#         od_cnt += 1
#
# print(od_cnt)


'''
字典案例
给定一个字符串my_string，现在要求统计每个字符出现的次数
'''
# my_string = 'hello world'
# result = {}
#
# for ele in my_string:
#     if ele in result:
#         result[ele] += 1
#     else:
#         result[ele] = 1
#
# for key, value in result.items():
#     print(f'字符{key}出现{value}次')


'''
巩固练习
需求: 编写一个程序将字符串转换为字典例如:输入: '5=Five 6=Six 7=Seven'   输出: {'5': 'Five', '6': 'Six', '7': 'Seven'}
'''
# my_string = '5=Five 6=Six 7=Seven'
# split_string = my_string.split(' ')
# my_dict = {}
#
# for char1 in split_string:
#     c_index = char1.index('=')
#     my_dict[char1[:c_index]] = char1[c_index+1:]
#
# print(my_dict)

# 第二种解法
# my_string = '5=Five 6=Six 7=Seven'
# split_string = my_string.split()
# my_dict = {}
#
# for char1 in split_string:
#     key,value = char1.split('=')
#     my_dict[key] = value
#
# print(my_dict)

'''
编写一个程序来统计缺失的数字并返回它们的总和。缺失的数字是指给定列表中两个极端（最大和最小数字）之间没有出现的数字。
'''
# numbers = [2, 5, 3, 7, 5, 7]
# max_num = max(numbers)
# min_num = min(numbers)
#
# sum = 0
# n = min_num
#
# while n >= min_num and n < max_num:
#     if n not in numbers:
#         sum += n
#     n += 1
#
# print(sum)


"""
统计英文文章中单词出现的频率
it was the best of times it was the worst of times.
it was the age of wisdom it was the age of foolishness. 
"""

# wordstring = """
# it was the best of times it was the worst of times.
# it was the age of wisdom it was the age of foolishness.
# """
# temp = wordstring.replace('.','')
# temp_str = temp.split()
# dict = {}
# sum = 0
# for word in temp_str:
#     if word in dict:
#         dict[word] += 1
#     else:
#         dict[word] = 1
# print(dict)





# # 1. 筛选偶数：从1到50中筛选出所有偶数，并存入列表
# list1 = [i for i in range(0, 51, 2) if i > 0]
# print(list1)
# # 2. 类型转换：将字符串列表 ["1", "2", "3", "4", "5"] 转换为整数列表
# list2 = ["1", "2", "3", "4", "5"]
# list3 = [int(x) for x in list2]
# print(list3)


# 反转文件内容.按行读取文件内容, 对每行的内容进行反转后, 写到另1个文件中.
# 例如:数据源文件: a.txt

import os

# with open('a.txt','r',encoding='utf-8') as f_in,open('b.txt','w',encoding='utf-8') as f_out:
#     while True:
#         line = f_in.readline().strip()
#         if line:
#             new_line = line[::-1]
#             f_out.write(new_line+'\n')
#         else:
#             break

# with open('a.txt','r',encoding='utf-8') as f_in, open('b.txt','w',encoding='utf-8') as f_out:
#     lines = f_in.readlines()
#     for line in lines:
#         new_line = line.strip()[::-1]
#         f_out.write(new_line+'\n')



# 巩固练习
# 拷贝文件并改名.例如: 把 a.py文件 拷贝到 a[备份].txt 文件中
# file_name = 'test.py'
# index = file_name.rfind('.')
# filename = file_name[:index]
# filename += '[备份].txt'
# with open(file_name,'r',encoding='utf-8') as f_in, open(filename,'w',encoding='utf-8') as f_out:
#     data = f_in.read()
#     f_out.write(data)

import streamlit as st

st.title('Streamlit教程')

"# 1级标题"
"## 2级标题"
"### 3级标题"
"#### 4级标题"
"##### 5级标题"
"###### 6级标题"