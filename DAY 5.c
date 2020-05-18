# c-programming-hackerrank
#include<stdio.h>
#include<math.h>
main()
{
    int arr[100][100];
    int n,i,j;
    int sum=0,sum1=0;
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
      for(j=0;j<n;j++)
    {
        scanf("%d",&arr[i][j]);
    }  
    sum = sum + arr[i][i];
        sum1 = sum1 + arr[i][n-1-i];
    }
     
    int total;
    total=abs(sum1-sum);
    printf("%d",total);

}
