#include <stdio.h>
#include <stdlib.h>
using namespace std;

int tr[1000];
int lowbit(int i) {return (i & -i);}

void add(int pos, int val){
    for (int i = pos; i < 1000; i += lowbit(i)) tr[i] += val;
}

int sum(int pos){
    int res = 0;
    for (int i = pos; i >= 1; i -= lowbit(i)) res += tr[i];
    return res;
}

int n;
int a[100];

int main()
{
    scanf("%d", &n);
    for (int i = 1; i <= n; i ++) scanf("%d", &a[i]);
    int res = 0;
    for (int i = 1; i <= n; i ++){
        res += i - sum(a[i]) - 1;
        add(a[i], 1);
    }
    printf("%d\n", res);
    return 0;
}