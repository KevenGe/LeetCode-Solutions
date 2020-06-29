/*
 * LeetCode 560. 和为K的子数组
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
    int subarraySum(vector<int> &nums, int k) {
        int ans = 0;
        int pra = 0;
        unordered_map<int, int> maps;
        maps.insert(unordered_map<int, int>::value_type(pra, 1));
//        unordered_map<int, int>::iterator it;
        for (int num:nums) {
            pra += num;
            if (maps.find(pra - k) != maps.end()) {
                ans += maps[pra-k];
            }

            if (maps.find(pra) != maps.end()) {
                maps[pra]++;
            }else{
                maps.insert(unordered_map<int, int>::value_type(pra, 1));
            }
        }
        return ans;
    }
};

int main() {

    vector<int> vec;
    vec.push_back(1);
    vec.push_back(1);
    vec.push_back(1);
    vec.push_back(1);

    Solution so;
    cout << so.subarraySum(vec, 2) << endl;

    return 0;
}
