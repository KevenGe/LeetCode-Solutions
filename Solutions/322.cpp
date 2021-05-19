#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;


// Method 1
//class Solution {
//public:
//    int coinChange(vector<int> &coins, int amount) {
//        vector<int> vec(amount + 1, INT_MAX / 10);
//        vec[0] = 0;
//        for (auto coin:coins) {
//            for (int i = coin; i < vec.size(); i++) {
//                vec[i] = min(vec[i], vec[i - coin] + 1);
//            }
//        }
//        return vec[amount] == INT_MAX/10 ? -1: vec[amount];
//    }
//};


// Method 2
class Solution {
public:
    int coinChange(vector<int> &coins, int amount) {
        vector<int> dp(amount + 1, INT_MAX/10);
        dp[0] = 0;

        for (int i = 1; i <= amount; i++) {
            for (auto coin: coins) {
                if (i - coin >= 0) {
                    dp[i] = min(dp[i], dp[i - coin] + 1);
                }
            }
        }

        return dp[amount] == INT_MAX/10 ? -1:dp[amount];
    }
};

int main() {
    return 0;
}