# import streamlit as st
# import pandas as pd
#
# st.write(st.session_state)


# st.title('Streamlit教程')
#
# "# 1级标题"
# "## 2级标题"
# "### 3级标题"
# "#### 4级标题"
# "##### 5级标题"
# "###### 6级标题"
#
# st.image('D:\Administrator\Pictures\Screenshots\屏幕截图(1).png', width=400)
#
# st.write('dict字典形式的静态表格')
# st.table(data={
#     'name': ['张三', '李四', '王五'],
#     'age': [18, 20, 22],
#     'gender': ['男', '女', '男']
# })
#
#
# # 下面我们没学过pandas 可以先了解能这样用.不用练习!!!
# st.write('pandas中dataframe形式的静态表格')
#
# df = pd.DataFrame(
#     {
#         'name': ['张三', '李四', '王五'],
#         'age': [18, 20, 22],
#         'gender': ['男', '女', '男']
#     }
# )
# st.table(df)
#
# st.write('dict字典形式的可交互表格')
# st.dataframe(data={
#     'name': ['张三', '李四', '王五'],
#     'age': [18, 20, 22],
#     'gender': ['男', '女', '男']
# })
#
#
# # 下面我们没学过pandas 可以先了解能这样用.不用练习!!!
# st.write('pandas中dataframe形式的可交互表格')
# df = pd.DataFrame(
#     {
#         'name': ['张三', '李四', '王五'],
#         'age': [18, 20, 22],
#         'gender': ['男', '女', '男']
#     }
# )
# st.dataframe(df)
#
# st.divider()
#
# name = st.text_input('请输入你的名字：')
#
# if name:
#   st.write(f'你好，{name}')
#
# pwd = st.text_input('密码是多少？', type='password')
#
# age = st.number_input('年龄：')
# st.write(f'你输入的年龄是{age}岁')
# st.number_input('年龄：', step=1)
# st.number_input('年龄：', value=20, min_value=0, max_value=200, step=1)
#
# paragraph = st.text_area("多行内容：")
# if paragraph:
#     st.write(paragraph)
#
# st.divider()
#
# # 使用 st.chat_input 创建一个聊天输入框，提示用户输入问题
# prompt = st.chat_input('请输入您的问题: ')
#
# st.write(f'您的问题是: {prompt}')
#
# # 使用 st.chat_message 创建一个用户消息容器，用于显示用户的消息
# # 'user' 表示这是用户发送的消息
# with st.chat_message('user'):
#     # 在用户消息容器中显示文本 'Hello '
#     st.write('Hello ')
#
# # 使用 st.chat_message 创建一个消息容器，用于显示回复消息
# message = st.chat_message('assistant')
# # 在消息容器中显示文本 'Hello Human'，模拟助手的回复
# message.write('Hello Human')
#
#
# st.form_submit_button('登录')



x = 1
y = 2
x = (x or y)
print(x,y)