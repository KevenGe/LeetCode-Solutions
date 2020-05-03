// 33
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int search(vector<int> &nums, int target) {
        if (nums.size() == 0) {
            return -1;
        } else if (nums.size() == 1) {
            return nums[0] == target ? 0 : -1;
        } else {
            int l = 0;
            int r = nums.size() - 1;

            while (l <= r) {
                int m = (l + r) / 2;
                if (nums[m] == target) {
                    return m;
                } else {
                    if (nums[l] <= nums[m]) {
                        if (nums[l] <= target && nums[m] >= target) {
                            r = m - 1;
                        } else {
                            l = m + 1;
                        }
                    } else {
                        if (nums[m] <= target && nums[r] >= target) {
                            l = m+1;
                        } else {
                            r = m-1;
                        }
                    }
                }
            }
            return -1;
        }
        return -1;
    }
};

int main() {
    vector<int> vec;
    vec.push_back(3);
    vec.push_back(1);

    Solution so;
    cout << so.search(vec, 3) << endl;
    return 0;
}
