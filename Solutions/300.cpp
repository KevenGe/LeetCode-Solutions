#include <iostream>
#include <vector>
#include <limits.h>
#include <algorithm>
using namespace std;

class Solution
{
public:
    int lengthOfLIS(vector<int> &nums)
    {
        int *dp = new int[nums.size()];
        fill(dp, dp + nums.size(), INT_MAX);

        for (int x : nums)
        {
            *lower_bound(dp, dp + nums.size(), x) = x;
        }

        return lower_bound(dp, dp + nums.size(), INT_MAX) - dp;
    }
};

int main()
{
    return 0;
}