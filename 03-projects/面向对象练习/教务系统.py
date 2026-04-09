"""
使用面向对象的方法完成下面需求
1.添加学生成绩:根据输入的学生姓名,语文,数学,英语成绩记录在系统
2.修改学生成绩:根据学生的姓名,修改对应学生的成绩
3.删除学生成绩:根据输入的学生的姓名,删除对应的学生的成绩
4.查询学生的成绩:根据输入的学生的姓名,查找对应的学生成绩,并输出
5.展示全部学生的成绩:展示教务系统中所有的学生的成绩
"""
#学生的类
class Student:
    def __init__(self,name,chinese,math,english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english
    def __str__(self):
        return f'姓名：{self.name} | 语文成绩：{self.chinese} | 数学成绩：{self.math} | 英语成绩：{self.english}'
    def update_score(self,chinse = None,math = None,english = None):
        if chinse is not None:
            self.chinese = chinse
        if math is not None:
            self.math = math
        if english is not None:
            self.english = english
# 教务管理系统
class EduManagement():
    system_version = 1.0
    system_name = '教务管理系统'


    def __init__(self,):
        self.student_list = []
    # 添加学生信息
    def add_student(self):
        name = input("请输入学生姓名")
        for s in self.student_list:
            if s.name == name:
                print("系统中已经存在该学生信息，请不要重复录入")
                return
        chinese = int(input("请输入学生语文成绩"))
        math = int(input("请输入学生数学成绩"))
        english = int(input("请输入英语成绩"))
        if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
            stu = Student(name,chinese,math,english)
            self.student_list.append(stu)
            print('学生信息录入成功')
        else:
            print('输入的学生成绩不合理，请重新输入')


        # 修改学生成绩
    def update_student(self):
        name = input("请输入要修改学生姓名")
        for s in self.student_list:
            if s.name == name:
                print(f'当前成绩{s}')
                chinese = int(input("请输入修改后的学生语文成绩"))
                math = int(input("请输入修改后的学生数学成绩"))
                english = int(input("请输入修改后的英语成绩"))
                if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
                    s.update_score(chinese,math,english)
                    print('成绩修改成功')
                    return
                else:
                    print('输入的学生成绩不合理，请重新输入')
                    return
        print('学生不存在，修改失败')

        # 删除学生信息
    def delete_student(self):
        name = input("请输入要删除学生姓名")
        for s in self.student_list:
            if s.name == name:
                self.student_list.remove(s)
                print('学生信息删除成功')
                return
        print('未找到该学生，删除失败')
    # 查询学生成绩
    def index_student(self):
        name = input("请输入要查询的学生姓名：")
        for s in self.student_list:
            if s.name == name:
                print(f'学生信息如下\n:{s}')
            print('输入的学生姓名有误')
    # 查询全部的学生信息
    def index_all(self):
        for s in self.student_list:
            print(f'所有学生成绩如下:\n{s}')
    def run(self):
        print('\n欢迎使用狗屎教务系统\n')

        while True:
            print()
            print('|--------------------------------------------------------------|')
            print('|1.添加学生 2.修改学生 3.删除学生 4.查询指定学生 5.查询所有学生 6.退出系统 |')
            print('|--------------------------------------------------------------|')
            print()
            choice = input('请选择要进行的操作，输入1-6\n')
            match choice:
                case "1":
                    self.add_student()
                case "2":
                    self.update_student()
                case "3":
                    self.delete_student()
                case "4":
                    self.index_student()
                case "5":
                    self.index_all()
                case "6":
                    print('拜拜')
                    break
                case _:
                    print('输入错误，请输入1-6')
if __name__ == '__main__':
    edu_management = EduManagement()
    edu_management.run()











