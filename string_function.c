#include<stdio.h>
// length function
int len(char s[])
{
    int n=0;
    while(s[n]!= '\0')
    n++;
    return n;
}

// copy function 
void copy(char *s2,char *s1)
{
    while(*s1 != '\0')
    {
        *s2=*s1;
        s1++;
        s2++;
    }
    *s2 = '\0';
}

//reverse function





//compare function
void comp(char *s1,char *s2)
{
    while(*s1)
}

//upper case
void upper(char *s)
{
    while(*s != '\0')
    {
        if(*s>=97 && *s<=122)
        *s =*s-32;
        s++;
    }
}

//lower case
void lower(char *s)
{
    while(*s != '\0')
    {
        if(*s>=65 && *s<=90)
        *s = *s+32;
        s++;
    }
}

//