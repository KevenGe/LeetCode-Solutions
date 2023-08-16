#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

class Solution {
public:
    int minSubArrayLen(int s, vector<int> &nums) {
        if (nums.size() == 0) {
            return 0;
        }


        int l = 0;
        int r = 0;

        int minLength = INT_MAX;
        int curValue = nums[0];

        while (r + 1 < nums.size()) {
            while (curValue < s && r + 1 < nums.size()) {
                r++;
                curValue += nums[r];
            }

            while (curValue - nums[l] >= s) {

                curValue -= nums[l];
                l++;
            }

            if (curValue >= s) {
                minLength = min(minLength, r - l + 1);

                curValue -= nums[l];
                l++;
            }
        }

        return minLength == INT_MAX ? 0 : minLength;
    }
};

int main() {
    vector<int> nums;
    nums.push_back(2);
    nums.push_back(3);
    nums.push_back(1);
    nums.push_back(2);
    nums.push_back(4);
    nums.push_back(3);

    Solution so;
    cout << so.minSubArrayLen(7, nums) << endl;
    return 0;
}