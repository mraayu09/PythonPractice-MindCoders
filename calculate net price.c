#include<stdio.h>
void main()
{
    int product,quant;
    float price,netprice;
    printf("enter the name of product\n");
    printf("enter the quantity of product\n");
    printf("enter the price of product");
    scanf("%d%d%f",&product,&quant,&price);
    netprice=quant*price;
    printf("\n total price= %f",netprice);
}
