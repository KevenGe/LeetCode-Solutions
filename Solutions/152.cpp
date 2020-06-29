/*
 * LeetCode 152. 乘积最大子数组
 *
 * Author: Keven Ge
 * Date: 2020-05-15
 */

#include <iostream>
#include <cmath>
#include <stack>
#include <unordered_map>
#include <unordered_set>
#include <climits>
#include <vector>
#include <algorithm>

using namespace std;

//class Solution {
//public:
//    int maxProduct(vector<int> &nums) {
//        int fmin = nums[0];
//        int fmax = nums[0];
//        int ans = nums[0];
//
//        for (int i = 1; i < nums.size(); ++i) {
//            fmax = max(nums[i], max(fmax * nums[i], fmin * nums[i]));
//            fmin = min(nums[i], min(fmax * nums[i], fmin * nums[i]));
//            ans = max(ans, fmax);
//        }
//        return ans;
//    }
//};

class Solution {
public:
    int maxProduct(vector<int> &nums) {
        int maxF = nums[0], minF = nums[0], ans = nums[0];
        for (int i = 1; i < nums.size(); ++i) {
            int mx = maxF, mn = minF;
            maxF = max(mx * nums[i], max(nums[i], mn * nums[i]));
            minF = min(mn * nums[i], min(nums[i], mx * nums[i]));
            ans = max(maxF, ans);
        }
        return ans;
    }
};


int main() {
    return 0;
}
