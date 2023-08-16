#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>

using namespace std;

class Solution
{
public:
    int rob(vector<int> &nums)
    {
        if (nums.size() == 0)
        {
            return 0;
        }
        else if (nums.size() == 1)
        {
            return nums[0];
        }
        else
        {
            vector<int> dp(nums.size(), 0);
            dp[0] = nums[0];
            dp[1] = max(nums[0], nums[1]);

            for (int i = 2; i < nums.size(); i++)
            {
                dp[i] = max(dp[i - 1], nums[i] + dp[i - 2]);
            }
            return dp[nums.size() - 1];
        }
    }
};

int main()
{
    return 0;
}