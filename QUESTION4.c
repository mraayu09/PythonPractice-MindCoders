#include<stdio.h>
int main()
{
    int pprice,dis,final;
    printf("enter the valur of purchase price");
    scanf("%d",&pprice);
    dis=(pprice*dis)/100;
    if{(pprice>=5000)
        dis=10;};

    else{(pprice<5000)
          dis=5;};
    final=pprice-dis; 
    printf("final price=%d"final);         
}