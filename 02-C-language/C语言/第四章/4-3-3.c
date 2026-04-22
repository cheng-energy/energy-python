#include<stdio.h>
#include<math.h>
int main()
{
	double a,b,c,deita,x1,x2;
	printf("请输入一元二次方程的系数：");
	scanf("%lf,%lf,%lf",&a,&b,&c);
	if (a == 0){
		x1 = x2 = -c/b;
		printf("x1 = x2 = %.2lf\n ",x1);
	} 
	else 
	{
		deita = (b*b)- (4* a*c) ; 
		if (deita > 0)
		{
			x1 = (-b+sqrt(deita)) / 2*a;
			x2 = (-b-sqrt(deita)) / 2*a;
			printf("方程有两个不相等的实数根：");
			printf("x1 = %.2lf \n",x1);
			printf("x2 = %.2lf \n",x2); 
		}
		else if (deita == 0)
		{
			x1 = x2 = -b/(2*a); 
			printf("方程有一个实数根：");
			printf("x1 = x2 = %.2lf\n",x1);
		}
		else
		{
			printf("这个方程没有实数根,有复数根");
			 
		}
	}
	return 0;
}