#include <bits/stdc++.h>

using namespace std;

int N;
int pr[100001];

int main()
{
    scanf("%d", &N);
    for(int i=2; i<=100000; i++)
        pr[i]=1;
    for(int i=2; i<=100000; i++) if(pr[i])
        for(int j=i*2; j<=100000; j+=i)
            pr[j]=0;
    for(int i=3; i<=100000; i++)
        pr[i]^=pr[i-1];
    while(N--)
    {
        int x;
        scanf("%d", &x);
        if(pr[x])
            printf("Alice\n");
        else
            printf("Bob\n");
    }
    return 0;
}