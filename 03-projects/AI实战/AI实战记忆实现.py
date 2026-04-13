"""-------------------------AI学习鞭策者----------------------------"""
import streamlit as st
from openai import OpenAI
import os
import requests
import datetime
import json

from requests import delete


# 生成会话标识
def generate_session_id():
    return str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))

def load_session():
    session_list = []
    # 加载sessions目录下的文件
    if os.path.exists('sessions'):
        file_list = os.listdir('sessions')
        for file in file_list:
            if file.endswith('.json'):
                session_list.append(file[:-5])
    session_list.sort(reverse=True)
    return session_list


# 定义保存会话信息的函数
def save_session():
        # 保存当前会话信息
        if st.session_state.current_session:
            # 构建新的会话对象
            session_state = {
                "name": st.session_state.name,
                "emotion": st.session_state.emotion,
                "social_leval": st.session_state.social_leval,
                "messages": st.session_state.messages
            }
        #如果sessions目录不存在就创建
        if not os.path.exists('sessions'):
            os.mkdir('sessions')
        #保存会话数据
        with open(f'sessions/{st.session_state.current_session}.json', 'w',encoding='utf-8') as f:
            json.dump(session_state, f, ensure_ascii=False, indent=2)

# 加载指定的会话信息
def load_value(session_name):
    try:
        if os.path.exists(f'sessions/{session_name}.json'):
            with open(f'sessions/{session_name}.json', 'r',encoding='utf-8') as f:
                session_state = json.load(f)
                st.session_state.name = session_state['name']
                st.session_state.emotion = session_state['emotion']
                st.session_state.social_leval = session_state['social_leval']
                st.session_state.messages = session_state['messages']
                st.session_state.current_session = session_name
    except Exception:
        st.error("加载会话信息失败")
def delete_session(session_name):
    try:
        if os.path.exists(f'sessions/{session_name}.json'):
            os.remove(f'sessions/{session_name}.json')
            #如果删除的是当前会话，则清空当前会话
            if session_name == st.session_state.current_session:
                st.session_state.messages = []
                st.session_state.current_session = generate_session_id()
    except Exception:
        st.error("删除会话信息失败")


#初始聊天记录
if 'messages' not in st.session_state:
    st.session_state.messages = []
# 初始化各种信息
if 'name' not in st.session_state:   #先看session_state里面有没有name这个key，如果没有创建一个
    st.session_state.name = ""         #session_state中的数据在多次会话中是可以共享的
if 'emotion' not in st.session_state:
    st.session_state.emotion = ""
if 'social_leval' not in st.session_state:
    st.session_state.social_leval = ""
#会话的名字
if 'current_session' not in st.session_state:
    now = generate_session_id()  # 获取当前的系统时间
    st.session_state.current_session = now

# 侧边栏的设置，方式一
# st.sidebar.subheader('前辈的信息')
# name = st.sidebar.text_input('前辈的名字：')  # 如果没有sidebar这个输入框会显示在主界面中
# 侧边栏的设置，方式二，with(stream里面的上下文管理器)

with st.sidebar:

    #增加会话管理面板
    st.subheader('AI控制面板')
    #增一个新增会话的按钮
    if st.button('新建会话',width="stretch",icon='🫆'):
        save_session()
        #创建新会话并保存
        if st.session_state.messages is not None:   #如果聊天消息为空,则可以创建新会话
            st.session_state.messages = []
            st.session_state.current_session = generate_session_id()
            save_session()
            st.rerun ()   #重新运行当前页面



    st.text('会话历史')
    session_list = load_session()
    for session in session_list:
        col1,col2 = st.columns([4,1])
        with col1:
            #三元运算符来判断会话记录选择的是哪个
            if st.button(session, width="stretch", icon='😶‍🌫️',key=f"load_{session}",type="primary" if session == st.session_state.current_session else "secondary"):
                # 加载会话信息
                load_value(session)
                st.rerun()

        with col2:
            #删除会话信息
            if st.button("",width="stretch",icon='❌️',key=f"delete_{session}"):
                delete_session(session)
                st.rerun()



    #分隔线
    st.divider()

    st.subheader('前辈的信息')  #
    name = st.text_input('前辈的名字', placeholder='请输入前辈的姓名')
    # 如果上方的设置name的key的时候传入了默认值，想在打开界面的时候直接显示默认值而不是请输入前辈的姓名，可以用value参数例如value="st.session_state.name"
    if name:
        st.session_state.name = name  #如果name有值的话，就把他保存到name这个key中
    # 性格输入框
    emotion = st.text_area('前辈的性格',placeholder='请输入前辈的性格')
    if emotion:
        st.session_state.emotion = emotion
    # 前辈的身份
    social_leval = st.text_area('前辈的地位',placeholder='请输入前辈的社会身份')   #文本域的展示效果，可以输入多行文字
    if social_leval:
        st.session_state.social_leval = social_leval



# 系统提示词
system_prompt = f"""
        你叫{name} ，是我的职场前辈，懂得新能源和AI还有数据分析
        规则：
            1. 
            2. 
            3. 
            4. 
            5. 
            6. 
            7. 
        前辈性格：
            - {emotion}
        你的社会身份:
            - {social_leval}
        你必须严格遵守上述规则来回复用户。
    """
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
    st.session_state.messages.append({"role": "user","content": prompt})

# 展示聊天信息
st.text(f"会话名称：{st.session_state.current_session}")
for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])  #可代替下面四行代码，妙啊，user和assistant都是role
        # if message["role"] == "user":
        #     st.chat_message("user").write(message["content"])
        # else:
        #     st.chat_message("assistant").write(message["content"])

if prompt:
    client = OpenAI(
        api_key=os.environ.get('DEEPSEEK_API_KEY'),
        base_url="https://api.deepseek.com")

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": system_prompt},
            *st.session_state.messages
        ],
        stream=True
    )
    print('---------------大模型返回的结果-----------------')

    response_message = st.empty()
    full_response = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            full_response += content
            response_message.chat_message("assistant").write(full_response)

    st.session_state.messages.append({"role": "assistant", "content": full_response})
    save_session()




























