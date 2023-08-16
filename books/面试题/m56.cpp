//
// Created by lenovo on 2020/4/29.
//

// 面试题 56
#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

class Solution {
public:
    vector<int> singleNumbers(vector<int> &nums) {
        unordered_set<int> sets;

        for (int num:nums) {
            if (sets.find(num) != sets.end()) {
                sets.erase(num);
            } else {
                sets.insert(num);
            }
        }

        vector<int> ans(2);
        for (int num:sets) {
            ans.push_back(num);
        }

        return ans;
    }
};


int main() {

    return 0;
}
