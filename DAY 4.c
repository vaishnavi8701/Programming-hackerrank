# c-programming-hackerrank
#include<stdio.h>
 main()
 {
     long long int arr[100],sum=0;
     int n;
     scanf("%d",&n);
    for(int i=0;i<n;i++)
    {
        scanf("%li",&arr[i]);
    }
   
    for(int i=0;i<n;i++)
    {
        
       
        sum=sum+arr[i];
       
    }
      printf("%li\n",sum);
   
 }
