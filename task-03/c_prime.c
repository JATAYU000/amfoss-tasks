#include<stdio.h>
int main()
{
    int x;
    printf("Enter the range: ");
    scanf("%d\n",&x);
    
    for(int i = 2;i<=x;i++)
    {
        
        int y = 0;
        for(int j = 2 ; j<i/2 ; j++)
        {   
            //printf("\ni: %d j: %d\n",i,prime[j]);
            if(i%j == 0)
            {   
                y = 1;
                break;
            }
            else
            {
                y = 0;
            }
        }
    
        if(y==0)
        {
            printf("%d, ",i);
        }
    }
    return 0;
}