#include<stdio.h>
void main()
{
    int a,b;
    printf("enter the value of a");
    printf("enter the value of b");
    scanf("%d%d",&a,&b);
    a=a+b;
    b=a-b;
    a=a-b;
    printf("\n A=%d",a);
    printf("\n B=%d",b);

}