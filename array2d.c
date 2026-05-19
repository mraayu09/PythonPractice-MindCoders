#include<stdio.h>
void main()
{
    int i,j;
    int a[3][3]={{1,2,3},{2,3,4},{4,5,6}};

    printf("elements of 2d array is \n");
    for(i=0;i<=2;i++)
    {
        for(j=0;j<=2;j++)
        printf("%d",a[i][j]);

     printf("\n");
    }

}