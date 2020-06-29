//
// Created by lenovo on 2020/6/27.
//
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


class Solution {
public:
    int firstMissingPositive(vector<int> &nums) {
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] <= 0) {
                nums[i] = nums.size() + 1;
            }
        }

        for (int i = 0; i < nums.size(); ++i) {
            if (abs(nums[i]) <= nums.size() && nums[abs(nums[i]) - 1] >0 ) {
                nums[abs(nums[i]) - 1] = -nums[abs(nums[i]) - 1];
            }
        }

        for (int i = 0; i < nums.size(); ++i) {
            if(nums[i] > 0){
                return i+1;
            }
        }

        return nums.size()+1;
    }
};

int main() {

    vector<int> ans;
//    ans.push_back(3);
//    ans.push_back(4);
    ans.push_back(1);
    ans.push_back(1);

    Solution so;
    cout << so.firstMissingPositive(ans) << endl;

    return 0;
}