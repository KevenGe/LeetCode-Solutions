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
        } else if (nums.size() == 3) {
            return max(max(nums[0], nums[1]), nums[2]);
        } else {
            vector<int> ans1(nums.size());
            ans1[0] = nums[0];
            ans1[1] = max(nums[0], nums[1]);
            for (int i = 2; i < nums.size(); ++i) {
                ans1[i] = max(ans1[i - 2] + nums[i], ans1[i - 1]);
            }

            vector<int> ans2(nums.size());
            ans2[1] = nums[1];
            ans2[2] = max(nums[1], nums[2]);
            for (int i = 3; i < nums.size(); ++i) {
                ans2[i] = max(ans2[i - 2] + nums[i], ans2[i - 1]);
            }

//            cout << ans1[nums.size()-1] << endl;
//            cout << ans2[nums.size() - 3] + nums[nums.size() - 1] << endl;
            return max(ans1[nums.size() - 2], ans2[nums.size() - 3] + nums[nums.size() - 1]);
        }
    }
};


int main() {
    vector<int> vec;
    vec.push_back(6);
    vec.push_back(6);
    vec.push_back(4);
    vec.push_back(8);
    vec.push_back(4);
    vec.push_back(3);
    vec.push_back(3);
    vec.push_back(10);

    Solution so;
    cout << so.rob(vec) << endl;
    return 0;
}
