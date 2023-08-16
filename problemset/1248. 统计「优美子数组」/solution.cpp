/*
 * 1248
 */

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int numberOfSubarrays(vector<int> &nums, int k) {

        int ans = 0;

        vector<int> dp;
        dp.push_back(-1);
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] % 2 == 1) {
                dp.push_back(i);
            }
        }
        dp.push_back(nums.size());

        for (int i = 1; i + (k - 1) < dp.size() - 1; ++i) {
            ans += (dp[i] - dp[i - 1]) * (dp[i + k] - dp[i + k - 1]);
        }
        return ans;
    }
};

int main() {
    vector<int> vec;
    vec.push_back(2);
    vec.push_back(2);
    vec.push_back(2);
    vec.push_back(1);
    vec.push_back(2);
    vec.push_back(2);
    vec.push_back(1);
    vec.push_back(2);
    vec.push_back(2);
    vec.push_back(2);

    Solution so;
    cout << so.numberOfSubarrays(vec, 2) << endl;
    return 0;
}