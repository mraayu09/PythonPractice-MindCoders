#include<stdio.h>
void main()
{
    int num;
    printf("Enter number");
    scanf("%d",&num);
    switch(num%2)
    {
        case 0 : printf("\n number is even");
                 break;

        case 1 : printf("\n number is odd");
                 break;
                          
    }
}