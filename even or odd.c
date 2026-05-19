#include<stdio.h>
void main()
{
    int num,unit;
    printf("enter the 3 digit num");
    scanf("%d",&num);
    unit=num%10;
    if ((unit%2)==0)
       printf("number is even");
    else
       printf("number is odd");   


}