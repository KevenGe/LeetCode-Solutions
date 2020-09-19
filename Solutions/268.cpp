#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    static int missingNumber(vector<int> &nums) {
        int t = 0;
        for (int i = 0; i <= nums.size(); i++) {
            t = t ^ i;
        }

        for (int i = 0; i < nums.size(); i++) {
                t = t ^ nums[i];
        }
        return t;
    }
};

int main() {
    return 0;
}