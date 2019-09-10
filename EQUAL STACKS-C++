#include <bits/stdc++.h>
using namespace std;
int com(vector<int>,vector<int>,vector<int>);
int main() 
{
    int n1,n2,n3;
    cin>>n1>>n2>>n3;
    vector<int> a,b,c;
    for(int i=0;i<n1;i++)
    { 
        int k; cin>>k;
        a.push_back(k);
    }
    for(int i=0;i<n2;i++)
    { 
        int k; cin>>k;
        b.push_back(k);
    }
    for(int i=0;i<n3;i++)
    { 
        int k; cin>>k;
        c.push_back(k);
    }
    reverse(a.begin(),a.end());
    reverse(b.begin(),b.end());
    reverse(c.begin(),c.end());
    for(int i=1;i<n1;i++)
    {
        a[i]=a[i-1]+a[i];
    }
    for(int i=1;i<n2;i++)
    {
        b[i]=b[i-1]+b[i];
    }
    for(int i=1;i<n3;i++)
    {
        c[i]=c[i-1]+c[i];
    }
    reverse(a.begin(),a.end());
    reverse(b.begin(),b.end());
    reverse(c.begin(),c.end());
    int l;
    if(((n1==n2) && (n1==n3)) || ( (n1<n2) && (n1<n3)))
    {
        l=com(a,b,c);
    }
    else if((n2<n1) && (n2<n3)) {l=com(b,a,c);}
    else {l=com(c,a,b);}
    cout<<l;
    return 0;
}

int com(vector<int> a,vector<int> b,vector<int> c)
{
    for(int i=0;i<a.size();i++){
        int x=a[i];
        int f=0,g=0;
        for(int j=0;j<b.size();j++)
        {
            if(x==b[j])
            {
                f=1; break;
            }
        }
        if(f)
        {
        for(int k=0;k<c.size();k++)
            {
                if(x==c[k])
                {
                    g=1; break;
                }
            }
        }
        if(f && g)
        { 
            return x; break;
        }
    }
    return 0;
}
