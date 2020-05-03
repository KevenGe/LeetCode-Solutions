/*
 * LeetCode 55
 */

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    bool canJump(vector<int> &nums) {
        int max_far = 0;
        for (int i = 0; i < nums.size(); ++i) {
            if (i <= max_far) {
                max_far = max(max_far, i + nums[i]);
                if (max_far >= nums.size() - 1) {
                    return true;
                }
            }
        }
        return false;
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
    cout << so.canJump(vec) << endl;
    return 0;
}