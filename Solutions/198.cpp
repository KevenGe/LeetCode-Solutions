#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int rob(vector<int> &nums) {
        if (nums.empty()) {
            return 0;
        } else if (nums.size() == 1) {
            return nums[0];
        } else if (nums.size() == 2) {
            return max(nums[0], nums[1]);
        } else {
            vector<int> ans(nums.size());
            ans[0] = nums[0];
            ans[1] = max(nums[0], nums[1]);
            for (int i = 2; i < nums.size(); ++i) {
                ans[i] = max(ans[i - 2] + nums[i], ans[i - 1]);
            }
            return ans[nums.size() - 1];
        }
    }
};


int main() {
    vector<int> vec;
    vec.push_back(1);
    vec.push_back(2);
    vec.push_back(3);
    vec.push_back(1);

    Solution so;
    cout << so.rob(vec) << endl;
    return 0;
}
