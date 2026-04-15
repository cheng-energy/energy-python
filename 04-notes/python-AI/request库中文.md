# Requests 库官方文档（完整中文翻译）
Requests 是一门优雅简洁、专为人类设计的 Python HTTP 库。你当前查看的是开发版文档。

## 保持更新
接收新版本与即将推出项目的更新。
加入邮件列表。

如果你喜欢这个项目，欢迎表达感谢！

关注 @kennethreitz

## 其他项目
Kenneth Reitz 的更多项目：
- edmsynths.com
- pipenv
- pep8.org
- httpbin.org
- The Python Guide
- Maya：人性化的日期时间处理库
- Records：人性化的 SQL 库
- Legit：人性化的 Git 库
- Tablib：表格数据集库

## 翻译版本
英语、法语、德语、日语、中文、葡萄牙语、意大利语、西班牙语

---

# 目录
- 开发接口
- 主要接口
- 异常
- 请求会话
- 低级类
- 更低级的类
- 身份验证
- 编码
- Cookie
- 状态码查询
- 迁移到 1.x
- 迁移到 2.x
- 快速搜索

---

# 主要接口
Requests 的所有功能都可以通过以下 7 个方法访问。它们全部都会返回一个 Response 对象实例。

## requests.request(method, url, **kwargs)
构造并发送一个 Request 请求。

### 参数
- method：新 Request 对象的请求方法
- url：新 Request 对象的请求地址
- params：（可选）字典或字节类型，作为请求的查询字符串发送
- data：（可选）字典、元组列表 `[(key, value)]`（会被表单编码）、字节或类文件对象，作为请求体发送
- json：（可选）JSON 数据，作为请求体发送
- headers：（可选）随请求一同发送的 HTTP 请求头字典
- cookies：（可选）字典或 CookieJar 对象，随请求发送
- files：（可选）字典，格式为 `'name': 类文件对象`（或 `{'name': 文件元组}`），用于多部分编码上传。
  文件元组可以是：
  - 二元组：`(文件名, 文件对象)`
  - 三元组：`(文件名, 文件对象, 内容类型)`
  - 四元组：`(文件名, 文件对象, 内容类型, 自定义请求头)`
  其中 content-type 为字符串，用于指定文件类型；custom_headers 为类字典对象，用于为该文件添加额外请求头
- auth：（可选）身份验证元组，用于启用基础认证、摘要认证或自定义 HTTP 认证
- timeout（浮点数或元组）：（可选）等待服务器发送数据的超时秒数，可为浮点数，或 `(连接超时, 读取超时)` 元组
- allow_redirects（布尔值）：（可选）布尔值，启用/禁用 GET/OPTIONS/POST/PUT/PATCH/DELETE/HEAD 请求的重定向，默认为 True
- proxies：（可选）字典，将协议映射到代理服务器 URL
- verify：（可选）布尔值，控制是否验证服务器 TLS 证书；或字符串，指定 CA 证书包路径，默认为 True
- stream：（可选）若为 False，响应内容会被立即下载
- cert：（可选）字符串类型为 SSL 客户端证书文件路径（.pem）；元组类型为 `(证书文件, 密钥文件)`

### 返回
Response 对象

### 返回类型
requests.Response

### 用法
```python
import requests
req = requests.request('GET', 'http://httpbin.org/get')
<Response [200]>
```

## requests.head(url, **kwargs)
发送 HEAD 请求。

### 参数
- url：新 Request 对象的请求地址
- **kwargs：request 方法可接收的可选参数

### 返回
Response 对象

### 返回类型
requests.Response

## requests.get(url, params=None, **kwargs)
发送 GET 请求。

### 参数
- url：新 Request 对象的请求地址
- params：（可选）字典或字节类型，作为请求的查询字符串发送
- **kwargs：request 方法可接收的可选参数

### 返回
Response 对象

### 返回类型
requests.Response

## requests.post(url, data=None, json=None, **kwargs)
发送 POST 请求。

### 参数
- url：新 Request 对象的请求地址
- data：（可选）字典（会被表单编码）、字节或类文件对象，作为请求体发送
- json：（可选）JSON 数据，作为请求体发送
- **kwargs：request 方法可接收的可选参数

### 返回
Response 对象

### 返回类型
requests.Response

## requests.put(url, data=None, **kwargs)
发送 PUT 请求。

### 参数
- url：新 Request 对象的请求地址
- data：（可选）字典（会被表单编码）、字节或类文件对象，作为请求体发送
- json：（可选）JSON 数据，作为请求体发送
- **kwargs：request 方法可接收的可选参数

### 返回
Response 对象

### 返回类型
requests.Response

## requests.patch(url, data=None, **kwargs)
发送 PATCH 请求。

### 参数
- url：新 Request 对象的请求地址
- data：（可选）字典（会被表单编码）、字节或类文件对象，作为请求体发送
- json：（可选）JSON 数据，作为请求体发送
- **kwargs：request 方法可接收的可选参数

### 返回
Response 对象

### 返回类型
requests.Response

## requests.delete(url, **kwargs)
发送 DELETE 请求。

### 参数
- url：新 Request 对象的请求地址
- **kwargs：request 方法可接收的可选参数

### 返回
Response 对象

### 返回类型
requests.Response

---

# 异常
- requests.RequestException：处理请求时发生未明确归类的异常
- requests.ConnectionError：发生连接错误
- requests.HTTPError：发生 HTTP 错误
- requests.URLRequired：发起请求需要一个有效的 URL
- requests.TooManyRedirects：重定向次数过多
- requests.ConnectTimeout：尝试连接远程服务器时请求超时
  触发该错误的请求可以安全重试
- requests.ReadTimeout：服务器在指定时间内未发送任何数据
- requests.Timeout：请求超时
  捕获该异常将同时捕获 ConnectTimeout 和 ReadTimeout

---

# 请求会话
## class requests.Session
Requests 会话对象。

提供 Cookie 持久化、连接池和统一配置功能。

### 基础用法
```python
import requests
s = requests.Session()
s.get('http://httpbin.org/get')
<Response [200]>
```

### 上下文管理器用法
```python
with requests.Session() as s:
    s.get('http://httpbin.org/get')
<Response [200]>
```

### 属性与方法
- auth = None：附加到请求的默认身份验证元组或对象
- cert = None：SSL 客户端证书默认值，字符串为证书路径（.pem），元组为 `(证书, 密钥)`
- close()：关闭所有适配器，从而关闭会话
- cookies = None：包含当前会话所有有效 Cookie 的 CookieJar，默认为 RequestsCookieJar
- delete(url, **kwargs)：发送 DELETE 请求，返回 Response 对象
- get(url, **kwargs)：发送 GET 请求，返回 Response 对象
- get_adapter(url)：返回指定 URL 对应的连接适配器
- get_redirect_target(resp)：接收 Response，返回重定向 URI 或 None
- head(url, **kwargs)：发送 HEAD 请求，返回 Response 对象
- headers = None：不区分大小写的字典，会话中每个请求都会发送这些请求头
- hooks = None：事件处理钩子
- max_redirects = None：允许的最大重定向次数，超出则抛出 TooManyRedirects，默认为 30
- merge_environment_settings(url, proxies, stream, verify, cert)：检查环境变量并合并配置
- mount(prefix, adapter)：为指定前缀注册连接适配器，适配器按前缀长度降序排序
- options(url, **kwargs)：发送 OPTIONS 请求，返回 Response 对象
- params = None：附加到每个请求的查询参数字典，值可为列表以表示多值参数
- patch(url, data=None, **kwargs)：发送 PATCH 请求，返回 Response 对象
- post(url, data=None, json=None, **kwargs)：发送 POST 请求，返回 Response 对象
- prepare_request(request)：构造用于传输的 PreparedRequest 并返回，合并 Request 与会话配置
- proxies = None：协议到代理 URL 的映射字典
- put(url, data=None, **kwargs)：发送 PUT 请求，返回 Response 对象
- rebuild_auth(prepared_request, response)：重定向时移除身份验证信息避免泄露，智能重新应用认证
- rebuild_method(prepared_request, response)：重定向时根据规范或浏览器行为修改请求方法
- rebuild_proxies(prepared_request, proxies)：结合环境变量重新评估代理配置
- request(...)：构造、预处理并发送请求，返回 Response 对象
- resolve_redirects(...)：接收 Response，返回 Response 或 Request 生成器
- send(request, **kwargs)：发送指定的 PreparedRequest
- stream = None：响应内容流式传输默认值
- trust_env = None：是否信任环境变量中的代理、默认认证等配置
- verify = None：SSL 验证默认值

---

# 低级类
## class requests.Request
用户创建的 Request 对象，用于构造 PreparedRequest 后发送至服务器。

### 参数
- method：使用的 HTTP 方法
- url：请求地址
- headers：要发送的请求头字典
- files：用于多部分上传的 `{文件名: 文件对象}` 字典
- data：附加到请求的请求体，字典会被自动表单编码
- json：附加到请求的 JSON 数据（未指定 files 或 data 时生效）
- params：追加到 URL 的查询参数字典
- auth：身份验证处理器或 `(用户名, 密码)` 元组
- cookies：字典或 CookieJar 对象
- hooks：回调钩子字典，内部使用

### 用法
```python
import requests
req = requests.Request('GET', 'http://httpbin.org/get')
req.prepare()
<PreparedRequest [GET]>
```

- deregister_hook(event, hook)：注销已注册的钩子，存在则返回 True
- prepare()：构造并返回用于传输的 PreparedRequest
- register_hook(event, hook)：正确注册钩子

## class requests.Response
Response 对象，包含服务器对 HTTP 请求的响应内容。

### 属性与方法
- apparent_encoding：由 chardet 库检测出的编码
- close()：将连接释放回连接池，调用后不可再访问底层 raw 对象
- content：响应内容，字节格式
- cookies = None：服务器返回的 CookieJar
- elapsed = None：从发送请求到接收响应的耗时
- encoding = None：访问 r.text 时使用的解码编码
- headers = None：不区分大小写的响应头字典
- history = None：请求历史中的 Response 列表，按旧到新排序
- is_permanent_redirect：若为永久重定向则返回 True
- is_redirect：若为规范可自动处理的重定向则返回 True
- iter_content(chunk_size=1, decode_unicode=False)：迭代读取响应数据，stream=True 时避免一次性加载大文件
- iter_lines(chunk_size=512, decode_unicode=None, delimiter=None)：按行迭代响应数据，非线程安全
- json(**kwargs)：返回响应的 JSON 编码内容，无效 JSON 会抛出 ValueError
- links：返回响应头中解析的链接（如有）
- next：返回重定向链中的下一个 PreparedRequest（如有）
- ok：状态码小于 400 时返回 True
- raise_for_status()：若发生 HTTP 错误则抛出 HTTPError
- raw = None：响应的类文件对象，高级用法，需设置 stream=True
- reason = None：HTTP 状态文本描述，如 Not Found、OK
- request = None：对应的 PreparedRequest 对象
- status_code = None：HTTP 状态码，如 404、200
- text：响应内容，Unicode 字符串格式
- url = None：重定向后的最终 URL

---

# 更低级的类
## class requests.PreparedRequest
完全可修改的预处理请求对象，包含将发送到服务器的精确字节数据。

可由 Request 对象生成或手动创建。

### 用法
```python
import requests
req = requests.Request('GET', 'http://httpbin.org/get')
r = req.prepare()
<PreparedRequest [GET]>

s = requests.Session()
s.send(r)
<Response [200]>
```

- body = None：发送到服务器的请求体
- deregister_hook(event, hook)：注销钩子
- headers = None：HTTP 请求头字典
- hooks = None：回调钩子字典
- method = None：要发送的 HTTP 方法
- path_url：构建要使用的路径 URL
- prepare(...)：使用给定参数预处理整个请求
- prepare_auth(auth, url='')：预处理 HTTP 认证数据
- prepare_body(data, files, json=None)：预处理 HTTP 请求体数据
- prepare_content_length(body)：根据请求方法与请求体设置 Content-Length
- prepare_cookies(cookies)：预处理 HTTP Cookie 数据
- prepare_headers(headers)：预处理 HTTP 请求头
- prepare_hooks(hooks)：预处理钩子
- prepare_method(method)：预处理 HTTP 方法
- prepare_url(url, params)：预处理 HTTP URL
- register_hook(event, hook)：注册钩子
- url = None：要发送请求的 HTTP URL

## class requests.adapters.BaseAdapter
基础传输适配器

- close()：清理适配器相关资源
- send(request, stream=False, timeout=None, verify=True, cert=None, proxies=None)：发送 PreparedRequest，返回 Response

## class requests.adapters.HTTPAdapter
urllib3 内置 HTTP 适配器，实现传输适配器接口，供 Session 内部使用。

### 参数
- pool_connections：缓存的 urllib3 连接池数量
- pool_maxsize：连接池中保存的最大连接数
- max_retries：每个连接的最大重试次数，仅针对 DNS 失败、套接字连接、连接超时，数据已发送后不重试
- pool_block：连接池无可用连接时是否阻塞

### 用法
```python
import requests
s = requests.Session()
a = requests.adapters.HTTPAdapter(max_retries=3)
s.mount('http://', a)
```

- add_headers(request, **kwargs)：添加连接所需请求头，v2.0 后默认无操作，用于子类重写
- build_response(req, resp)：从 urllib3 响应构建 Response 对象
- cert_verify(conn, url, verify, cert)：验证 SSL 证书
- close()：释放内部状态，关闭连接池
- get_connection(url, proxies=None)：获取指定 URL 的 urllib3 连接
- init_poolmanager(connections, maxsize, block=False, **pool_kwargs)：初始化 urllib3 连接池管理器
- proxy_headers(proxy)：返回通过代理发送的请求头
- proxy_manager_for(proxy, **proxy_kwargs)：返回指定代理的 urllib3 ProxyManager
- request_url(request, proxies)：获取最终请求 URL，代理场景使用完整 URL，否则仅使用路径
- send(...)：发送 PreparedRequest，返回 Response

---

# 身份验证
- requests.auth.AuthBase：所有身份验证实现的基类
- requests.auth.HTTPBasicAuth：为请求附加 HTTP 基础认证
- requests.auth.HTTPProxyAuth：为请求附加 HTTP 代理认证
- requests.auth.HTTPDigestAuth：为请求附加 HTTP 摘要认证

---

# 编码
- requests.utils.get_encodings_from_content(content)：从字符串内容中提取编码
- requests.utils.get_encoding_from_headers(headers)：从响应头中提取编码
- requests.utils.get_unicode_from_response(r)：以 Unicode 格式返回请求内容

---

# Cookie
- requests.utils.add_dict_to_cookiejar(cj, cookie_dict)：将字典键值对添加到 CookieJar
- requests.utils.cookiejar_from_dict(cookie_dict, cookiejar=None, overwrite=True)：从字典创建 CookieJar

## class requests.cookies.RequestsCookieJar
兼容类，继承 cookielib.CookieJar，同时提供字典接口。
是 Requests 会话的默认 CookieJar，支持序列化，部分字典操作时间复杂度为 O(n)。

- add_cookie_header(request)：为请求添加正确的 Cookie 请求头
- clear(domain=None, path=None, name=None)：清除指定 Cookie，无参数则清空全部
- clear_expired_cookies()：清除所有过期 Cookie
- clear_session_cookies()：清除所有会话 Cookie
- copy()：返回当前 CookieJar 的副本
- extract_cookies(response, request)：从响应中提取 Cookie
- get(name, default=None, domain=None, path=None)：类字典 get 方法，支持域名与路径
- get_dict(domain=None, path=None)：返回符合条件的普通 Python 字典
- items()/iteritems()：类字典键值对方法
- keys()/iterkeys()：类字典键方法
- values()/itervalues()：类字典值方法
- list_domains()：列出 Jar 中所有域名
- list_paths()：列出 Jar 中所有路径
- make_cookies(response, request)：从响应提取 Cookie 对象序列
- multiple_domains()：存在多个域名时返回 True
- pop()/popitem()：类字典弹出方法
- set(name, value, **kwargs)：类字典设置方法，支持域名与路径
- set_cookie_if_ok(cookie, request)：策略允许时设置 Cookie
- setdefault()：类字典默认值方法
- update(other)：从其他 CookieJar 或字典更新当前 Jar

## class requests.cookies.CookieConflictError
CookieJar 中存在多个匹配条件的 Cookie 时抛出

---

# 状态码查询
## requests.codes
```python
requests.codes['temporary_redirect']  # 307
requests.codes.teapot                 # 418
requests.codes['\o/']                # 200
```

---

# 迁移到 1.x
本节介绍 0.x 与 1.x 的主要差异，降低升级成本。

## API 变化
- Response.json 现为可调用方法，不再是响应体属性
```python
import requests
r = requests.get('https://github.com/timeline.json')
r.json()   # JSON 解码失败会抛出异常
```
- Session API 变更：Session 对象不再需要参数，首字母大写，兼容小写 session
```python
s = requests.Session()
s.auth = auth
s.headers.update(headers)
r = s.get('http://httpbin.org/headers')
```
- 除 response 外，所有请求钩子均被移除
- 认证助手拆分为独立模块，如 requests-oauthlib、requests-kerberos
- 流式请求参数从 prefetch 改为 stream，逻辑反转，读取原始响应必须设置 stream=True
```python
r = requests.get('https://github.com/timeline.json', stream=True)
for chunk in r.iter_content(8192):
    ...
```
- requests 方法的 config 参数被移除，相关配置在 Session 中设置，日志级别通过 logging 配置

## 许可
开源协议从 ISC 变更为 Apache 2.0，确保对 Requests 的贡献同样受 Apache 2.0 保护。

---

# 迁移到 2.x
相比 1.0，破坏性变更较少，但仍有需注意事项。

## API 变化
- 异常处理行为修改：RequestException 现为 IOError 子类，而非 RuntimeError
- 无效 URL 转义序列抛出 RequestException 子类异常，而非 ValueError
```python
requests.get('http://%zz/')  # 抛出 requests.exceptions.InvalidURL
```
- 分块编码错误导致的 httplib.IncompleteRead 改为 ChunkedEncodingError
- 代理 API 调整：代理 URL 必须携带协议头
```python
proxies = {
  "http": "http://10.10.1.10:3128",
}
```

## 行为变化
- 请求头字典的键统一为原生字符串：Python 2 为字节串，Python 3 为 Unicode
- 请求头的值必须为字符串，v2.11.0 后强制执行，建议避免使用 Unicode 作为请求头值