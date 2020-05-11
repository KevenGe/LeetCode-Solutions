/*
 * This is LeetCode 45 跳跃游戏 II
 * ==============================
 *
 * Author: Keven Ge
 * Date: 2020-05-04
 *
 */

#include <iostream>
#include <vector>
#include <algorithm>
#include <limits.h>

using namespace std;

//
//class Solution {
//public:
//    int jump(vector<int> &nums) {
//        int ans = 0;
////        vector<int> dp(nums.size(), INT_MAX);
//        int *dp = new int[nums.size()];
//        fill(dp, dp + nums.size(), INT_MAX);
//        dp[0] = 1;
//        for (int i = 0; i <= nums.size() - 1; ++i) {
//            if (dp[i] != INT_MAX) {
//                for (int j = i + 1; j <= i + nums[i] && j <= nums.size() - 1; ++j) {
//                    dp[j] = min(dp[j], dp[i] + 1);
//                }
//            } else {
//                break;
//            }
//        }
//        return dp[nums.size() - 1] - 1;
//    }
//};

class Solution {
public:
    int jump(vector<int>& nums) {
        int maxPos = 0, n = nums.size(), end = 0, step = 0;
        for (int i = 0; i < n - 1; ++i) {
            if (maxPos >= i) {
                maxPos = max(maxPos, i + nums[i]);
                if (i == end) {
                    end = maxPos;
                    ++step;
                }
            }
        }
        return step;
    }
};


int main() {
    vector<int> vec;
    vec.push_back(2);
    vec.push_back(3);
    vec.push_back(1);
    vec.push_back(1);
    vec.push_back(4);

    Solution so;
    cout << so.jump(vec) << endl;
    return 0;
}