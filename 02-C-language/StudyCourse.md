# C---翁恺

scanf()----------输入函数，例如:

scanf("%d",&price);        输入一个整数，把这个整数赋值给price

## 常量const 示例：

const int change = 100;--------在int前面加const表示为变量change增加不变的属性（常量）
## 变量 ：

直接int加变量名，示例如下：
```C
#include <stdio.h>
#include <windows.h>

int main() {
    SetConsoleCP(CP_UTF8);
    SetConsoleOutputCP(CP_UTF8);
    int a ;
    int b;
    printf("请输两个整数：");
    scanf("%d %d",&a,&b);
    printf("%d + %d = %d\n",a,b,a+b);
    return 0;
}
```
如果输入的字符串，就是会输出莫名其妙的一段数，因为两个变量没有被赋值也没有初始化，内存中有什么就会输出什么

``双精度浮点数（double）
print("%f",...)
scanf("%lf,...)``
``单精度浮点数（float）``
``整数（int）  %d``

## 运算规则：
- C语言中，两个整数运算的结果只能是整数（可能丢失原有的小数点部分，不会四舍五入）

## 表达式（运算符+算子）
### 运算符的优先级（在C语言中赋值也是一个运算符）
- 单目运算的优先级最高（例如a×-b，他会优先把b变成相反数），

















