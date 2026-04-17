import requests
# 定义URL
url = 'https://www.tiobe.com/tiobe-index/'

# 使用requests库来发送HTTP请求
response = requests.get(url)

# 输出结果到控制台
print(response.text)  # 返回的是前端页面代码