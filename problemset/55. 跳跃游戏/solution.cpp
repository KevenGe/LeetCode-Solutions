//
// Created by lenovo on 2020-09-19.
//

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

/**
 * @brief solution
 */
class Solution {
public:

    /**
     * @brief core function
     * @param nums
     * @return
     */
    bool canJump(vector<int> &nums) {

        int m = 0; ///< the fastest position coule be.
        for (int i = 0; i < nums.size(); i++) {
            if (i <= m) {
                m = max(m, i + nums[i]);
            }
        }
        return m>= nums.size()-1;
    }
};

int main() {
    return 0;
}