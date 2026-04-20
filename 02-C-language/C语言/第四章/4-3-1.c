#include <stdio.h>
#include <math.h>
#define PI 3.1415926
int main()
{
    double y,x;
    printf("请输入x的值:");
    scanf("%lf",&x);
    if(x < PI / 2)
    {
        y = 2 * pow(x,3) + 3*cos(x) +5;
        
    }
    else if (x >= -PI/2 && x <= PI/2)
    {
        y = pow((x-1)/(x+2),3) + 5 * x;
      
    }
    else
    {
        y = pow(x+2*sin(3*x),0.5);
      
    }
    printf("y = %.4f\n",y);
    return 0 ;
}







