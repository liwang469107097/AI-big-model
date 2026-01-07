import streamlit as st
import ollama as ol

st.title('黑马智聊机器人')

# 初始化，判断是否有历史数据，添加数据
if 'messages' not in st.session_state:
    st.session_state['messages'] = [
        {'role':'assistant', 'content':'有什么能够帮助您'}
    ]

# 遍历循环显示所有历史信息
for message in st.session_state['messages']:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

# 获取输入内容
prompt = st.chat_input('输入想要询问的内容.')

# 判断内容不为空时，执行以下代码
if prompt:
    # 追加输入内容到session state缓存里
    st.session_state['messages'].append({'role':'user', 'content':prompt})
    # chat_mesage 指定用户及显示对应头像，markdown 以markdown格式显示输入内容
    st.chat_message('user').markdown(prompt)
    # 把输入的问题投喂给语言大模型，获取反馈
    response = ol.chat(model='qwen2:0.5b',
                           messages=[{'role': 'user', 'content': prompt}])
    # 把获取的反馈追加进缓存里
    st.session_state['messages'].append({'role': response.message.role, 'content': response.message.content})
    # 申明用户类型，输出反馈内容
    with st.chat_message('assistant'):
        st.markdown(response.message.content)


# 备注： 在命令行里输入 sreamlit run python脚本名.py 运行程序。
# streamlit run .\黑马聊天机器人\聊天机器人.py