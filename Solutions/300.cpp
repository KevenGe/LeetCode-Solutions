#include <iostream>
#include <algorithm>
#include <vector>
#include <stack>
#include <climits>

using namespace std;

class Solution {
public:
    int lengthOfLIS(vector<int> &nums) {
        if(nums.size() == 0){
            return 0;
        }


        int len = 1;
        vector<int> d(nums.size() + 1, 0);
        d[1] = nums[0];
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] > d[len]) {
                len += 1;
                d[len] = nums[i];
            } else {
                int t = bs(d, len, nums[i]);
                d[t] = nums[i];
            }
        }
        return len;
    }

    int bs(vector<int> vec, int len, int target) {
        int l = 1;
        int r = len;
        while (l <= r) {
            int m = (l + r) / 2;
            if (vec[m] >= target) {
                if (m == 1 || (m > 1 && vec[m - 1] < target)) {
                    return m;
                }
                r = m - 1;
            } else {
                l = m + 1;
            }
        }
        return -1;
    }
};

void runTest(){
    vector<int> vec;
    vec.push_back(10);
    vec.push_back(9);
    vec.push_back(2);
    vec.push_back(5);
    vec.push_back(3);
    vec.push_back(7);
    vec.push_back(101);
    vec.push_back(18);

    Solution so;
    cout << so.lengthOfLIS(vec) << endl;
}

int main() {
    runTest();
    return 0;
}