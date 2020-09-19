#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    static void nextPermutation(vector<int> &nums) {

        // 找到可以进行更改的下标
        int index=-1;
        for (int i = nums.size() - 1; i >= 1; i--) {
            if (nums[i - 1] < nums[i]) {
                index = i - 1;
//                restart = false;
                break;
            }
        }

        // 替换
        if(index != -1){
            for (int i = nums.size() - 1; i >= 1; i--) {
                if (nums[index] < nums[i]) {
                    int t = nums[index];
                    nums[index] = nums[i];
                    nums[i] = t;
                    break;
                }
            }
        }

        // 排序（冒泡）
        for (int i = index + 1; i < nums.size(); i++) {
            for (int j = nums.size() - 1; j > index + 1; j--) {
                if (nums[j - 1] > nums[j]) {
                    int t = nums[j - 1];
                    nums[j - 1] = nums[j];
                    nums[j] = t;
                }
            }
        }
    }
};

int main() {
    vector<int> nums;
    nums.push_back(1);
    nums.push_back(3);
    nums.push_back(2);

    Solution so;
    so.nextPermutation(nums);

    for(auto x:nums){
        cout << x << endl;
    }
    return 0;
}