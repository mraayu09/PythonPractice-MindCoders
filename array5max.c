#include<stdio.h>
int main()
{
    int a[5],i,max,sec_max;
    printf("enter the elements");
    for(i=0;i<=4;i++)
    scanf("%d",&a[i]);
    max=a[0];
    for(i=0;i<=4;i++)
    {
        if (a[i]>max)
        max=a[i];
    }

    sec_max=1;
    for(i=0;i<=4;i++)
    {
        if(a[i]<max && a[i]>sec_max)
        sec_max=a[i];
    }
    printf("\n biggest %d",max);
    printf("\n second biggest %d",sec_max);

}