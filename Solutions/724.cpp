/*
 * LeetCode 724. 寻找数组的中心索引
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

class Solution {
public:
    int pivotIndex(vector<int> &nums) {
        if (nums.size() < 3) {
            return -1;
        }
        vector<int> tmp(nums);
        int pra = 0;
        for (int i = 0; i < nums.size(); ++i) {
            pra += nums[i];
            tmp[i] = pra;
        }
        for (int i = 0; i < nums.size(); ++i) {
            if (i == 0 && tmp[nums.size()] - tmp[0] == 0) {
                return i;
            } else if (i == nums.size() - 1 && tmp[nums.size() - 2] == 0) {
                return i;
            } else if (tmp[i - 1] == tmp[nums.size() - 1] - tmp[i]) {
                return i;
            }
        }
        return -1;
    }
};

int main() {
    vector<int> vec;
    vec.push_back(1);
    vec.push_back(7);
    vec.push_back(3);
    vec.push_back(6);
    vec.push_back(5);
    vec.push_back(6);

    Solution so;
    cout << so.pivotIndex(vec) << endl;
    return 0;
}
