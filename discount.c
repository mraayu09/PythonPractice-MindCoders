#include<stdio.h>
void main()
{
    float cost,dis,netamount;
    printf("enter the cost of the product");
    scanf("%f",&cost);
    
    if (cost>=5000)
       {dis=(cost*10)/100;
       printf("discount price is %d",dis);
       }    
    else
       {dis=0;
        printf("no discount available");
       }
    netamount=cost-dis;
    
    printf("\n final price is %f",netamount);
       
       
}