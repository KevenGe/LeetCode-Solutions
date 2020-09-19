//
// Created by lenovo on 2020-07-05.
//

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    static int pivotIndex(vector<int> &nums) {
        // set the empty status
        if (nums.empty()) {
            return -1;
        }

        // set a extra vector dp in order to store the data.
        vector<int> dp(nums.size(), 0);
        dp[0] = nums[0];
        for (int i = 1; i < nums.size(); ++i) {
            dp[i] = nums[i] + dp[i - 1];
        }

//        // User binary search get the correct answer.
//        int l = 0;
//        int r = nums.size() - 1;
//        while (l <= r) {
//            int m = (l + r) / 2;
//            if (m == 0) {
//                if(dp[nums.size() - 1] - dp[m] == 0){
//                    return m;
//                }else{
//                    return -1;
//                }
//            } else {
//                if (dp[m - 1] == dp[nums.size() - 1] - dp[m]) {
//                    return m;
//                } else if (dp[m - 1] > dp[nums.size() - 1] - dp[m]) {
//                    r = m - 1;
//                } else {
//                    l = m + 1;
//                }
//            }
//        }


        if (dp[nums.size() - 1] - dp[0] == 0) {
            return 0;
        }

        for (int i = 1; i < nums.size(); ++i) {
            if (dp[i - 1] == dp[nums.size() - 1] - dp[i]){
                return i;
            }
        }
        return -1;
    }
};


int main() {
//    vector<int> nums;
//    nums.push_back(-1);
//    nums.push_back(-1);
//    nums.push_back(-1);
//    nums.push_back(-1);
//    nums.push_back(0);
//    nums.push_back(1);
//
//    Solution so;
//    cout << Solution::pivotIndex(nums) << endl;

    int a[3] = {1,2};


    return 0;
}