#include <stdio.h>

int cnt[50001];
int main(){
    freopen("input.txt", "rt", stdin)
    int n, i, j;
    
    scanf("%d", &n);
    
    for(i=1; i<=n; i++){
        for (j=i; j<=n; j=j+1){
            cnt[j]++;
        }
    }
    
    for(i=1; i<=n; i++){
        printf("%d ", cnt[i])
    }
}