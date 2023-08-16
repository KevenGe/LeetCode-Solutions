//
// Created by lenovo on 2020-09-18.
//

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// 顺序法
//class Solution {
//public:
//    int findPeakElement(vector<int> &nums) {
//        for(int i=0;i<nums.size()-1;i++){
//            if(nums[i] > nums[i+1]){
//                return i;
//            }
//        }
//        return nums.size()-1;
//    }
//};

class Solution {
private:
    int helper(vector<int> &nums, int l, int r) {
        if (l == r) {
            return l;
        }

        int m = (l + r) / 2;
        if (nums[m] > nums[m + 1]) {
            return helper(nums, l, m);
        } else {
            return helper(nums, m+1, r);
        }
    }

public:
    // TODO: Binary Finder
    int findPeakElement(vector<int> &nums) {
        return this->helper(nums, 0, nums.size() - 1);
    }
};

void runTest(){
    vector<int> vec;
    vec.push_back(1);
    vec.push_back(2);
    vec.push_back(3);
    vec.push_back(1);

    Solution so;
    cout << so.findPeakElement(vec) << endl;
}

int main() {
    runTest();
    return 0;
}