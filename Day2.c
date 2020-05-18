#include<stdio.h>
main()
{
    int arr[1000];
    int n,sum=0;
    scanf("%d",&n);
    int i;
    for (i=0;i<n;i++)
    {
        scanf("%d",&arr[i]);
    }
    for (i=0;i<n;i++)
    {
        sum=sum+arr[i];
    }
    printf("%d",sum);
}
