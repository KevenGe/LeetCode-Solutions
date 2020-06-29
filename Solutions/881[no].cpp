/*
 * LeetCode 887 掉落鸡蛋
 * Date: 2020-04-11
 * Author: Keven Ge
 */

#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;

class Solution {
public:
    unordered_map<int, int> memo;
    int dp(int N, int K) {
        if (this->memo.find(N * 100 + K) == this->memo.end()) {
            int ans = 0;
            if (N == 0) {
                ans = 0;
            } else if (K == 1) {
                ans = N;
            } else {
                int lo = 1;
                int hi = N;
                while (lo + 1 < hi) {
                    int x = (lo + hi) / 2;
                    int t1 = dp(K - 1, x - 1);
                    int t2 = dp(K, N - x);

                    if (t1 < t2) {
                        lo = x;
                    } else if (t1 > t2) {
                        hi = x;
                    } else {
                        lo = hi = x;
                    }
                }

                ans = 1 + min(max(dp(K - 1, lo - 1), dp(K, N - lo)),
                              max(dp(K - 1, hi - 1), dp(K, N - hi)));


            }
            this->memo[N * 100 + K] = ans;
        }
        return this->memo[N * 100 + K];
    }

    int superEggDrop(int K, int N) {
        return dp(K, N);
    }
};

int main() {
    return 0;
}