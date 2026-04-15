
# request 库

##### 知识点：
- headers参数的使用
- 发送带参数的请求
- headers中携带cookie
- cookiejar的转换方法
- 超时参数timeout的使用
- 使用verify参数忽略CA证书
- requests 模块发送post请求
- 利用request.session进行状态保持

---
## 库的介绍
- 官方文档[https://requests.readthedocs.io/projects/cn/zh-cn/latest/index.html?highlight=%E5%8F%A6%E7%B1%BB%E6%95%B0%E6%8D%AE#requests-http]
- 官方的中文文档，可以直接自学

## response响应对象
- requests相当于用你的电脑给对应的网页发送一个request来请求获取数据
- response则是网页响应给你的回答
1. 网络上传输的所有字符串都是bytes类型的
- response.text = response.content.decode('推测的编码格式')
### context和text
1. response.text
    - 类型：str
    - 编码类型：requests会根据HTTP头部对响应的编码形式进行推测，然后按照推测的进行解码


2. response.content
    - 类型:bytes
    - 指定类型：没有指定
    - 可以使用decode来挑选编码格式
        - 可以选择：utf8 ,gbk ,gb2312,ascii,iso-8859-1等
### 响应对象常用的方法和属性
- response.url  有时候响应的url和请求的url不一定一样
- response.status-code 响应的状态码（就是404，200（成功））之类的
- response.request.headers  响应对应的请求头（就是request的请求头），网页一般对于浏览器才会响应
```py
rl = 'https://www.baidu.com'
response = requests.get(url)
print(response.request.headers)
# {'User-Agent': 'python-requests/2.33.1', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}  User-agent:说明这个代码目前就是以python模块的形式请求百度网页
```
- response.headers   响应头
```py
# {'Cache-Control': 'private, no-cache, no-store, proxy-revalidate, no-transform', 'Content-Encoding': 'gzip', 'Content-Length': '1145', 'Content-Type': 'text/html', 'Pragma': 'no-cache', 'Server': 'bfe', 'Set-Cookie': 'BDORZ=27315; max-age=86400; domain=.baidu.com; path=/', 'Date': 'Tue, 14 Apr 2026 13:53:21 GMT'}
```
- response.request.cookies 响应对应的请求的cookie，返回cookijar的类型
- response.cookies   返回响应对象的cookie，cookijar的类型
- response.json()   自动把json内容转化成python对象，字典或者列表
```md
# Cookie 是什么？
**Cookie 就是网站给你贴的一张「小纸条」**，存在你电脑/手机里

## 举个例子
你去一家奶茶店：
1. 第一次去：你报手机号，店员**记住你**
2. 给你一张**会员卡**
3. 下次你再来，不用报信息，店员一看卡就认识你

**Cookie = 这张会员卡**

## 放到互联网里
- 你第一次访问网站 → 网站给你发一个**小文本（Cookie）**
- 存在你的浏览器里
- 你下次再访问 → 浏览器自动把 Cookie 带给网站
- 网站就知道：**哦，是你又来了**

---

## Cookie 用来干嘛？
1. **记住登录状态**
   不用每次都输账号密码。
2. **记住你是谁**
   比如：购物车、你看过的内容、你的偏好。
3. **识别身份**
   很多接口、数据、爬虫，**必须带 Cookie 才能访问**。

---

## 对requests帮助
你写代码爬数据/调用接口时：
- 有些数据**不登录看不到**
- 登录后，网站会给你 Cookie
- 你把 Cookie 放进 requests 里
- 网站就认为：**是你本人在访问**
```
```md

# Session = 帮你自动带着 Cookie 逛网站的“浏览器小号”

## 先用人话讲
- **Cookie**：是一张小纸条，证明你是谁。
- **Session**：是一个**持续的对话状态**

你可以这么理解：
- 不用 Session：
  你每发一次请求，就像**换了一个新路人**，网站不认识你
  你要自己手动带 Cookie，很累

- 用 Session：
  你创建一个**会话**，它会**自动保存 Cookie**
  之后所有请求都用这个会话发，网站就知道：
  “哦，还是你，我记得你”

## 生活版比喻
- 不用 Session：
  每次去奶茶店都**换一张新脸**，每次都要重新登录、重新验证。

- 用 Session：
  你办了一张**会员卡 + 专属服务员**，
  服务员全程跟着你，你不用每次都掏卡，他自动帮你刷

## 在 requests 里到底是什么？

requests.Session() 就是创建一个**持久连接的客户端**

它会自动：
1. 保存 Cookie
2. 保持登录状态
3. 复用连接（更快）
4. 统一设置 headers、代理等

## 代码对比一看就懂
### 不用 Session（麻烦）

import requests

# 第一次请求
res1 = requests.get(url1)
# 第二次请求，网站不认识你
res2 = requests.get(url2)

---

### 用 Session
```python
s = requests.Session()  # 创建一个会话

# 登录
s.post(login_url, data={'user':'xx','pwd':'xx'})

# 之后所有请求都自动带 Cookie
res1 = s.get(url1)
res2 = s.get(url2)


- **Cookie**：身份凭证
- **Session**：**维持身份的一整段对话**

- 在 requests 里：**Session = 自动帮你管 Cookie 的工具**
写爬虫、调接口：
**能 Session 就不用普通 requests.get**，更稳、更简单

```


## 发送带请求头的请求
- rewuests.get(url,headers = 请求头)
- 就是把自己伪装成浏览器获取更多的信息。
- 请求头是需要去浏览器网页寻找的----user-agent
  1. 右键检查源代码或者右键检查
  2. 点击net work
  3. 勾选 preserve log ---勾选后刷新页面请求不会被刷新
  4. 刷新页面
  5. 查看Name一栏下和请求的url地址相同的response-注意确定右侧Headers的request method是GET，这样才能对应
- Edg找不到请求头可以用谷歌试试




































