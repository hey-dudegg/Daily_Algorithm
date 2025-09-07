#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;
int main(){
    freopen("input.txt", "rt", stdin);
    int n, i, now, pre, pos;
    scanf("%d", &d);
    vector<int> ch(n);
    scanf("%d", &pre);
    for (i=1; i<n; i++){
        scanf("%d", &now);
        pos=abs(pre-now);
        if(pos>0 && pos<n && ch[pos]==0) ch[pos]=1;
        else{
            print("NO\n");
            return 0;
        }
        pre=now;
    }
    print("YES\n");
    return 0;
}