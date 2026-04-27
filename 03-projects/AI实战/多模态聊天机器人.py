# 利用mem0ai实现记忆的练习
import os
from mem0 import Memory
import ollama
from openai import OpenAI
from pyexpat.errors import messages
from sqlalchemy.sql.functions import user

"""-----------------基于openai来调用本地部署的模型-----------------------"""
# client = OpenAI(
#     base_url='http://localhost:11434/v1/',
#     api_key='ollama'
# )
#
# response = client.chat.completions.create(
#     model='my:latest',
#     messages=[{"role": "user", "content": "你是谁啊，你会什么呢"}],
#     stream = True
# )
# for i in response:
#     content = i.choices[0].delta.content
#     #如果content存在，则打印
#     if content:
#         print(content, end='', flush=True)  # 实时打印，不换行,end的默认值是'\n'打印会换行，flush是强制立即刷新输出缓冲区，不等待缓冲区满或程序结束。流式场景下，确保每个 i一到就立刻显示在屏幕上，达到实时效果。
"""
优点：通用性强
缺点：deep seek的思考部分无法体现，用户等待时间长体验差
"""

# 创建向量数据库
# 这个环境变量对于 embedder 的初始化是必要的，即便用的是 Ollama
os.environ["OPENAI_API_KEY"] = "ollama"

config = {
    # 1. 向量存储：记忆中提取的信息放在哪里
    "vector_store": {
        "provider": "chroma",
        "config": {
            "path":"D:\\code\\本地部署1",
        }
    },

    # 2. ⭐ 大语言模型 (LLM)：谁来理解和记忆对话
    "llm": {
        "provider": "ollama",
        "config": {
            "model": "my:latest",               # 你熟悉的模型名
            "temperature": 0.1,                 # 数值越低，输出越稳定、可预测
            "max_tokens": 2000,
        }
    },

    # 3. ⭐ 嵌入模型 (Embedder)：谁来把文字变成向量，以便搜索记忆
    "embedder": {
        "provider": "ollama",
        "config": {
            "model": "nomic-embed-text",        # 专门做嵌入的模型
            "embedding_dims": 768,              # 模型输出的向量维度，需与模型匹配
        }
    },
}

# 创建记忆实例
m = Memory.from_config(config)



# 下面是使用ollama进行流式输出

# 发起流式对话请求
print('请输入小写的q来开始和鑫君的聊天，或者输入exit结束和鑫君的聊天')
user_think = input('是否开始对话？(输入 q 开始，输入exit退出): ')
if user_think != 'q':
    exit(0)

while True:
    user1 = input('请输入你要说的话：')
    if user1.lower() in ['quit', 'exit', '拜拜']:
        print("退出聊天")
        break
    # 1. 检索记忆（注意新版 API 用法）
    search_result = m.search(user1, filters={"user_id": "cheng"})
    memories = search_result.get("results", [])

        # 2. 构造消息（将记忆作为 user 上下文，避免 system 角色可能被忽略）
    if memories:
        mem_texts = [mem['memory'] for mem in memories]
        context = "关于用户的历史记忆：\n" + "\n".join(mem_texts)
        messages = [{"role": "user", "content": context + "\n\n现在用户问：" + user1}]
    else:
        messages = [{"role": "user", "content": user1}]

    stream = ollama.chat(
        model='my:latest',  # 替换成你的本地模型名，如 'deepseek-r1:8b'
        messages=messages,
        stream=True
    )

    print("> ", end="")
    # 迭代处理每一个数据块
    n = 0
    b = 0
    full_think = ''
    full_content = ''
    full_answer = ''
    for chunk in stream:
        # 获取鑫君回复的主要文本内容
        content = chunk['message']['content']
        if content:
            b += 1
            if b == 1:
                print(f'\n[回答]\n{content}', end='', flush=True)  # 实时打印，不换行

            if b > 1:
                print(content,flush=True,end='')
            full_content += content

        if 'thinking' in chunk['message']:
            thinking = chunk['message']['thinking']
            if thinking:
                n += 1
                if n == 1:
                    print(f"\n[思考]\n {thinking}", end='')
                if n >1:
                    print(thinking,end='')
                full_think += thinking

    full_answer = full_think + full_content



    messages1 = [
        {"role": "user", "content": user1},
        {"role":"assistant","content":full_answer}

    ]
    m.add(messages1,user_id='cheng')







