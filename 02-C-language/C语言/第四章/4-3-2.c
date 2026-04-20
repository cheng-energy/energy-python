#include<stdio.h>
int main ()
{
    int a,b,c,d;
    printf("请输入不相等的四个整数:");
    scanf("%d,%d,%d,%d",&a,&b,&c,&d);
    if (a > b)
    {
        if (a > c)
        {
            if (a > d)
            {
            printf("最大的数是：%d",a);
            }
            else if (a < d)
            {
                printf("最大的数是：%d",d);
            }
        }
        else if(a < c)
        {
            if (c > d)
            {
                printf("最大的数是：%d",c);
            }
            else if (c < d)
            {
                printf("最大的数是:%d",d);
            }
        }
    }
    else if(a < b)
    {
        if (b > c)
        {
            if (b > d)
            {
                printf("最大的数是:%d",b);
            }
            if (b < d )
            {
                printf("最大的数是：%d",d);
            }
        }
        else if (b < c)
        {
            if (c > d)
            {
                printf("最大的数是：%d",c);
            }
            else if (c  < d )
            {
                printf("最大的数是：%d",d);
            }
        }
    }
    return 0;
}














