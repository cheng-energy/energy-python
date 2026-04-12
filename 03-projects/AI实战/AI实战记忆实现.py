"""-------------------------AI学习鞭策者----------------------------"""
import streamlit as st
from openai import OpenAI
import os
import requests

#初始聊天记录
if 'messages' not in st.session_state:
    st.session_state.messages = []

# 系统提示词
system_prompt = "你是新能源领域的超级大佬，你有扎实的新能源领域知识和用python等数据分析的能力，还了解AI的应用例如API调用等，目前你接受了一份工作，就是负责监督我的学习，我是一名双飞本科新能源科学与工程专业的大一学生，我的职业规划与你目前的就业一致，你会毫无保留的帮助我，监督我的学习，要求语气严格"
st.set_page_config(
    page_title="AI学习鞭策者",
    page_icon="🐶",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={}
)

# 设置大标题
st.title(':rainbow[AI学习鞭策者]')
st.logo("D:\\剪辑素材\\动漫图片\\小猫.jpg")
# 设置输入框
prompt = st.chat_input("请输入你的问题")
if prompt:#这里的字符串会自动转化为布尔值，如果空字符串则为False
    st.chat_message("user").write(f"{prompt}")
    st.session_state.messages.append({"role": "user","content": prompt})

# 展示聊天信息
    for message in st.session_state.messages:
        st.chat_message(message["role"]).write(message["content"])  #可代替下面四行代码，妙啊，user和assistant都是role
        # if message["role"] == "user":
        #     st.chat_message("user").write(message["content"])
        # else:
        #     st.chat_message("assistant").write(message["content"])



    # 调用大模型
    client = OpenAI(
        api_key=os.environ.get('DEEPSEEK_API_KEY'),
        base_url="https://api.deepseek.com")

    # noinspection PyTypeChecker
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
            *st.session_state.messages   #解包列表
        ],
        stream=True
    )
    print('---------------大模型返回的结果-----------------')
    # st.chat_message("assistant").write(response.choices[0].message.content)
    # st.session_state.messages.append({"role": " assistant","content": response.choices[0].message.content})   #非流式输出的打印结果

    # 流式输出
    #创建一个空容器,用于展示大模型返回结果
    response_message = st.empty()
    """1.遍历response"""
    full_response = ""
    for chunk in response:

        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            full_response += content
            response_message.chat_message("assistant").write(full_response)
            #这个空组件中之间选择assistant来打印，他就不会因为下面的st.打印出一个对话框了
            # st.chat_message("assistant").write(full_response)不可以放在这里，会重复打印，也可以放在外面，否则还是最后等流式输出结束后打印出内容
        st.session_state.messages.append({"role": " assistant","content": full_response})






























