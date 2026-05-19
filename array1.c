#include<stdio.h>
void main()
{
    int a[5],i;
    printf("enter the elements of array");
    for(i=0;i<=4;i++)
    scanf("%d",&a[i]);
    printf("\n elements of array");
    for(i=0;i<=4;i++)
    printf("%d",a[i]);
}