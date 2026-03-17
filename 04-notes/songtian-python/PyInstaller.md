# PyInstaller库基本介绍（windows+R打开从cmd命令行）
- pyinstaller可以实现将.py后缀的源文件转化成.exe后缀的程序（可执行文件）

## pyinstaller库的使用说明

Pyinstaller它不是python下面的执行指令，是（amd）命令行的执行程序

（amd命令行） pyinstaller -F<文件名>----（这里输入文件名时不需要有<>）
- 会看到目录中生成额外的其他文件，buijd和pycache可以安全删除，dist中可以看到一个exe文件，双击文件可以执行程序


---
常用参数
1. -h   查看帮助
2. --clean 清理打包过程中的临时文件
3. -D或者-onedir  打包成一个文件夹（dist）
4. -F，--onefile  在dist的文件夹只生成可执行文件
5. -i<图标文件名.ico>  指定打包程序使用图标ico的文件

---
打开文件所在目录行的操作：
1. windows+r   然后在出现窗口中输入cmd回车
2. 使用cd: 文件名的方式到达所要打包的文件所在地
3. 输入pyinstaller的使用参数+回车来打包








