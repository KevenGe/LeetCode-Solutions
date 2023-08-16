/******************************************************************************
 *  力扣解题
 *
 * @brief 力扣题目
 * @author Keven Ge
 * @date 2020-07-01
 *
 *****************************************************************************/

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

/**
 * @brief 动态规划
 */
//class Solution {
//public:
//    int findLength(vector<int> &A, vector<int> &B) {
//        int n = A.size();
//        int m = B.size();
//        vector<vector<int> > dp(n + 1, vector<int>(m + 1, 0));
//        int ans = 0;
//        for (int i = n - 1; i >= 0; i--) {
//            for (int j = m - 1; j >= 0; j--) {
//                if (A[i] == B[j]) {
//                    dp[i][j] = dp[i + 1][j + 1] + 1;
//                } else {
//                    dp[i][j] = 0;
//                }
//                ans = max(ans, dp[i][j]);
//            }
//        }
//        return ans;
//    }
//};


/**
 * @brief Rabin-Karp 方法
 */
class Solution {
private:
    const int base = 113;
    const int mod = 1000000009;
public:
    int findLength(vector<int> &A, vector<int> &B) {

    }

    /**
     * @brief 快速幂方法
     *
     * @param x 底
     * @param n
     * @return
     */
    long long qpow(long long x, long long n) const {
        long long ret = 1;
        while (n) {
            if (n & 1) {
                ret = ret * x % mod;
            }
            x = x * x % mod;
            n = n >> 1;
        }
        return ret;
    }
};

int main() {
    return 0;
}