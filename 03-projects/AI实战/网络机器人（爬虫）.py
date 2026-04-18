import requests
from lxml import html

# 定义URL
url = 'https://www.tiobe.com/tiobe-index/'

# 使用requests库来发送HTTP请求
response = requests.get(url)


with open('爬虫.html','w',encoding='utf8') as f:
    f. write(response.text)
# 把html文件的文本转化成文本对象，后续可以使用xpath语法
data = html.fromstring(response.text)
# 使用Xpath对内容进行解析
head = data.xpath('//*[@id="top20"]/thead/tr/th/text()')
print(head)
#获取表格的其余数据
body_tr = data.xpath('//*[@id="top20"]/tbody/tr')
for tr in body_tr:
    data_td = tr.xpath('./td/text()')
    print(data_td)
