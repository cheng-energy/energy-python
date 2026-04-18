import requests
from lxml import html

# 定义URL
url = 'https://www.tiobe.com/tiobe-index/'

# 使用requests库来发送HTTP请求
response = requests.get(url)


with open('爬虫.html','w',encoding='utf8') as f:
    f. write(response.text)
    # 把html文件的文本转化成文本文件
    data = html.fromstring('爬虫.html')
    # 使用Xpath对内容进行解析
    