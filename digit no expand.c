#include<stdio.h>
void main()
{
    int n,unit,ten,hun,thou;
    printf("enter the 4 digit number");
    scanf("%d",&n);
    unit=n%10;
    unit=unit*1;
    n=n/10;
    ten=n%10;
    ten=ten*10;
    n=n/10;
    hun=n%10;
    hun=hun*100;
    n=n/10;
    thou=n%10;
    thou=thou*1000;
    printf("\n thousand=%d",thou);
    printf("\nhundred=%d",hun);
    printf("\ntenth=%d",ten);
    printf("\n unit=%d",unit);

}