#include<stdio.h>
void main()
{
    int a,b,p=1,i;
    printf("enter value a and b");
    scanf("%d%d",&a,&b);
    for (i=1;i<=b;i++)
    p=p*a;
    printf("power=%d",p);
}