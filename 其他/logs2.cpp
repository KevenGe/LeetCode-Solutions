/**
 * 长亭笔试 L题
 *
 */

#include <iostream>
#include <algorithm>
#include <vector>
#include <unordered_map>
#include <string>
#include <cstdio>

using namespace std;
const int MAXN = 1e7+10;
typedef unsigned long long ull;
ull data[MAXN];

int main() {
    //freopen("D:\\My Studying\\Algorithm\\Leetcode\\forCLion\\t.txt","r",stdin);
    //freopen("D:\\My Studying\\Algorithm\\Leetcode\\forCLion\\out.txt","w",stdout);
    int T;
    scanf("%d", &T);
    while (T--) {
        int N;
        scanf("%d", &N);
//        vector<uint64_t> data(N);
        for (int i = 0; i < N; i++) {
            // cin >> data[i];
            scanf("%lld",&data[i]);
        }
        sort(data, data+N);
        int M;
        scanf("%d", &M);
        ull start,end;
        for (ull i = 0; i < M; i++) {
            // cin >> start >> end;
          scanf("%lld", &start);
          scanf("%lld", &end);
          ull* startIter = lower_bound(data, data+N, start);
          ull* endIter = upper_bound(data, data+N, end);
          printf("%d\n",endIter-startIter);
        }
    }
    return 0;
}