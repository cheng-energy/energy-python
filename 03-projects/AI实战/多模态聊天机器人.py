# 利用mem0ai实现记忆的练习
import os
from mem0 import Memory
import ollama
from openai import OpenAI




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





# 发起流式对话请求
stream = ollama.chat(
    model='my:latest',  # 替换成你的本地模型名，如 'deepseek-r1:8b'
    messages=[{"role": "user", "content": "你是谁啊，你会什么呢"}],
    stream=True
)

print("> ", end="")
# 迭代处理每一个数据块
n = 0
m = 0
for chunk in stream:
    # 获取助手回复的主要文本内容
    content = chunk['message']['content']
    if content:
        m += 1
        if m == 1:
            print(f'\n[回答]\n{content}', end='', flush=True,)  # 实时打印，不换行
        if n > 1:
            print(content,flush=True,end='')


    if 'thinking' in chunk['message']:
        thinking = chunk['message']['thinking']
        if thinking:
            n += 1
            if n <= 1:
                print(f"\n[思考]\n {thinking}", end='')
            else:
                print(thinking,end='')






