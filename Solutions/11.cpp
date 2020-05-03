/*
 * LeetCode 11
 */

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int maxArea(vector<int> &height) {
        int area = 0;
        int left = 0;
        int right = height.size()-1;
        while (left < right) {
            if (height[left] <= height[right]) {
                area = max(area, height[left] * (right - left));
                left++;
            } else if (height[left] > height[right]) {
                area = max(area, height[right] * (right - left));
                right--;
            }
        }
        return area;
    }
};

int main() {
    vector<int> height;
    height.push_back(1);
    height.push_back(8);
    height.push_back(6);
    height.push_back(2);
    height.push_back(5);
    height.push_back(4);
    height.push_back(8);
    height.push_back(3);
    height.push_back(7);
    Solution so;
    cout << so.maxArea(height) << endl;
    return 0;
}