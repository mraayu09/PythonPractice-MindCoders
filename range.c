#include<stdio.h>
void main()
{
    int n;
    printf("enter n");
    scanf("%d",&n);

    if ((n>=5 && n<=10)||(n>=15 && n<=20))
      printf("n is in the range");

    else
      printf("out of range");

}