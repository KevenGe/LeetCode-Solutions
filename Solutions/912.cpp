#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// leetcode 912
// 快速排序

class Solution {
public:
    vector<int> sortArray(vector<int> &nums) {
        // 使用快速排序！
        helper(nums, 0, nums.size() - 1);
        return nums;
    }

    void helper(vector<int> &nums, int left, int right) {

        if(left >= right){
            return;
        }

        int ori_left = left;
        int ori_right = right;

        int target = right;
//        right = right - 1;
        while (left < right) {
            while (nums[left] <= nums[target] && left < right) {
                left++;
            }

            while (nums[right] >= nums[target] && left < right) {
                right--;
            }

            if (left < right) {
                int temp = nums[left];
                nums[left] = nums[right];
                nums[right] = temp;
            }
        }

        if(left == right && left != target){
            int temp = nums[left];
            nums[left] = nums[target];
            nums[target] = temp;
        }

        this->helper(nums, ori_left, left - 1);
        this->helper(nums, left + 1, ori_right);
    }
};

int main() {
    vector<int> vec;
//    vec.push_back(1);
//    vec.push_back(4);
//    vec.push_back(3);
    vec.push_back(6);
    vec.push_back(5);
//    vec.push_back(2);

    Solution so;
    so.sortArray(vec);
    for(int x: vec){
        cout << x << endl;
    }
    return 0;
}
