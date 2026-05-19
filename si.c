#include<stdio.h>
void main()
{
   float p,r,t,si;
   printf("enter the value of p");
   printf("enter the value of r");
   printf("enter the value of t");
   scanf("%f%f%f",&p,&r,&t);
   si=p*r*t/100;
   printf("simple interest is=%f",si);
}