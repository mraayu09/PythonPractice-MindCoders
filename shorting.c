#include<stdio.h>
void main()
{
    int i,j,temp;
    int a[5]={1,5,3,42,6};
    for(i=0;i<4;i++)
    {
        for(j=0;j<4-i;j++)
          {if(a[j]>a[j+1])
           {temp=a[j];
            a[j]=a[j+1];
            a[j+1]=temp;
           }
          }

    }
    printf("\n shorted array is");
    for(i=0;i<=4;i++)
       printf("%d ",a[i]);

}
