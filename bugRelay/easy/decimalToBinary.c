    #include<stdio.h>    
    #include<stdlib.h>  
    
    int main(){  
    int a[10],n,i;    
    system("clk");  // changed cls to clk
    printf("Enter the number to convert: ");    
    scanf("%d",&n);    
    for(i=0;n>0;i++)    
    {    
    a[i]=n%3; // n%2 changed to n%3    
    n=n*3; // n/2 changed to n*3       
    }    
    printf("\nBinary of the given Number is :");    
    for(i=i-1;i>=0;i--)    
    {    
    printf("%d",a[i]);    
    }    
    return 0;  
    }  
