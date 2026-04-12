# Streamlit 
- 基于python代码快速构建一个Web网站-----无需前端技术（为数据工程师和机器学习工程师设计）
- 官网：https://streamlit.io/
- 从官网的文件操作中查看怎么用
- 调用streamlit提供的API来构建Web应用
- 通过streamlit run 'XXX.py来运行程序'----终端运行，一次enter未打开就多点一次

注意：如果设计到特别复杂的Web开发这个是不行的

## 段落文字
- st.write('')
## 展示图片
- 首先需要有对应的资源(图片)
- st.image('文件路径')
- 其余参数可以去官网自行查找
## 引入音频
- st.audio('文件路径')
## logo
st.logo('文件路径')
## 表格
```py
# 表格的引入
student_data = {
    '姓名':['CHX','SXJ'],
    '爱好':['SXJ','CHX'],
    '日常':['玩耍','学习'],
    '食物':['拼好饭','食堂饭']
}
st.table(student_data)
```
- st.table()-可以传入很多种的数据，具体可以光标放在代码上面提取文档查看
## 输入框---很多种，可以查看官方文档
```py
name = st.text_input('请总结你才表格中获得的结果')
st.write(f'你获得的结果是：{name}')
```
还可以指定类型，type='password'
## 单选按钮
- st.radio()
```py
love = st.radio('你觉得CHX喜欢SXJ吗',['喜欢','超级喜欢',':rainbow[超级超级喜欢]'],index=2)# index的作用是默认勾选哪个，目前是超级喜欢
st.write(f'你的想法是：{love}')
```
## 页面设置--Configuration
```python
import streamlit as st

st.set_page_config(
    page_title="超级页面",
    page_icon="🧊",
    layout="wide",  #控制整个网页布局，wide是占据整个区域
    initial_sidebar_state="expanded",  #控制的是侧边栏的状态，目前没有 侧边栏
    menu_items={
        'Get Help': 'https://github.com/',
        'Report a bug': "https://github.com/",
        'About': "#https://github.com/"  #点击这个菜单可以跳转到GitHub
    }# 菜单的信息，可以是空字典
)
```
# AI学习鞭策者
## 安装AI插件，lingma
- alt+p可以获取AI的主动提示























