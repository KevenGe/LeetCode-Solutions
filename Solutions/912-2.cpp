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
        sort(nums.begin(), nums.end());
        return nums;
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
