//
// Created by lenovo on 2020-09-18.
//

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
private:

    int helper(vector<int> &nums, int left, int right, int target) {
        if(left > right){
            return -1;
        }

        int middle = (left + right) / 2;
        if (nums[middle] == target) {
            return middle;
        } else if (nums[middle] >= nums[left]) {
            // left side is sorted.
            if (target >= nums[left] && target <= nums[middle]) {
                return helper(nums, left, middle - 1, target);
            } else {
                return helper(nums, middle + 1, right, target);
            }
        } else {
            // right side is sorted.
            if(target <= nums[right] && target > nums[middle]){
                return helper(nums, middle + 1, right, target);
            }else{
                return helper(nums, left, middle - 1, target);
            }
        }
    }

public:
    int search(vector<int> &nums, int target) {
        return helper(nums, 0, nums.size() - 1, target);
    }
};

//class Solution {
//public:
//    int search(vector<int> &nums, int target) {
//        int n = (int) nums.size();
//        if (!n) {
//            return -1;
//        }
//        if (n == 1) {
//            return nums[0] == target ? 0 : -1;
//        }
//        int l = 0, r = n - 1;
//        while (l <= r) {
//            int mid = (l + r) / 2;
//            if (nums[mid] == target) return mid;
//            if (nums[0] <= nums[mid]) {
//                if (nums[0] <= target && target < nums[mid]) {
//                    r = mid - 1;
//                } else {
//                    l = mid + 1;
//                }
//            } else {
//                if (nums[mid] < target && target <= nums[n - 1]) {
//                    l = mid + 1;
//                } else {
//                    r = mid - 1;
//                }
//            }
//        }
//        return -1;
//    }
//};

int main() {
    return 0;
}