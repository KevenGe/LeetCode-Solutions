//
// Created by lenovo on 2020-07-30.
//

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

/**
 * @brief 函数
 */
class Solution {
public:
    static int integerBreak(int n) {
        vector<int> dp(n + 1, 0);
        dp[0] = 0;
        dp[1] = 1;
        for (int i = 2; i <= n; i++) {
            for (int j = 1; j < i; j++) {
                dp[i] = max(dp[i], max(j * (i - j), j * dp[i - j]));
            }
        }
        return dp[n];
    }
};

int main() {
    return 0;
}