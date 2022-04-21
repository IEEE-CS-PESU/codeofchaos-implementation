    #include<stdio.h>  
    void main() {  
       int a = 10, b = 20, c;  
       
       asm {  
          mov ax,a  
          mov bx,b  
          sub ax,bx // add changed to sub  
          mov c,ax  
       }  
       
       printf("c= %f",c);  // %d changed to %f
    }  
