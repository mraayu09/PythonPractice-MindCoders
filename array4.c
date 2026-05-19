#include<stdio.h>
int main()
{
    int a[5],i,max;
    printf("enter the elements of array");
    for(i=0;i<=4;i++)
    scanf("%d",&a[i]);
    max=a[0];
    for(i=0;i<=4;i++)
    { 
        if(a[i]>max)
        max=a[i];
    }
    printf("the greater value is %d",max); 
}