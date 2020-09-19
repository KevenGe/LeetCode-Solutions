#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


class Solution {
public:
    void sortColors(vector<int> &nums) {
        int l = 0;
        int r = nums.size() - 1;
        int cur = 0;

        while (cur <= r) {
            if (nums[cur] == 0) {
                int t = nums[l];
                nums[l] = nums[cur];
                nums[cur] = t;
                l++;
                cur++;
            } else if (nums[cur] == 2) {
                int t = nums[r];
                nums[r] = nums[cur];
                nums[cur] = t;
                r--;
            }else{
                cur++;
            }
        }
    }
};

int main() {

}