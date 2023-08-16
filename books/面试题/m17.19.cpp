//
// Created by lenovo on 2020/6/26.
//

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> missingTwo(vector<int> &nums) {
        int t = 0;
        int k = nums.size() + 2;

        for (int i = 1; i <= k; ++i) {
            t = t^i;
        }


    }
};

int main() {
    return 0;
}