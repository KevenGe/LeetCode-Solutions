//
// Created by Keven Ge on 2020/4/4.
//  接雨水

#include <iostream>
#include <vector>
#include <climits>

using namespace std;

class Solution {
public:
    int trap(vector<int> &height) {
        if(height.empty()){
            return 0;
        }

        // find the heightest the height.
        int max_height = INT_MIN;
        int max_index = INT_MAX;
        for (int i = 0; i < height.size(); ++i) {
            if (max_height < height[i]) {
                max_height = height[i];
                max_index = i;
            }
        }

        int ans = 0;

        // from the left
        int current_height = 0;
        for (unsigned i = 0; i < max_index; ++i) {
            if (height[i] > current_height) {
                ans -= current_height;
                ans += (height[i] - current_height) * (max_index - i - 1);
                current_height = height[i];
            } else {
                ans -= height[i];
            }
        }

        // from the right
        current_height = 0;
        for (unsigned i = height.size() - 1; i > max_index; --i) {
            if (height[i] > current_height) {
                ans -= current_height;
                ans += (height[i] - current_height) * (i - 1 - max_index);
                current_height = height[i];
            } else {
                ans -= height[i];
            }
        }

        return ans;
    }
};

int main() {
    vector<int> vec;
    vec.push_back(0);
    vec.push_back(1);
    vec.push_back(0);
    vec.push_back(2);
    vec.push_back(1);
    vec.push_back(0);
    vec.push_back(1);
    vec.push_back(3);
    vec.push_back(2);
    vec.push_back(1);
    vec.push_back(2);
    vec.push_back(1);

    Solution so;
    cout << so.trap(vec) << endl;
    return 0;
}