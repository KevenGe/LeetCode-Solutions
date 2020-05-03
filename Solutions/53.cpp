/*
 * LeetCode 53
 *
 * Date: 2020-05-03
 * Author: Keven Ge
 */
#include <iostream>
#include <vector>
#include <unordered_set>
#include <algorithm>
#include <limits.h>

using namespace std;

class Solution {
public:
    int maxSubArray(vector<int> &nums) {
        int max_sum = INT_MIN; // the result for the function.
        int cur_sum = 0;   // the current sum for the function.
        for (int num:nums) {
            if(cur_sum >=0){
                cur_sum += num;
            }else{
                cur_sum = num;
            }

            max_sum = max(max_sum, cur_sum);
        }
        return max_sum;
    }
};


int main() {
    return 0;
}
