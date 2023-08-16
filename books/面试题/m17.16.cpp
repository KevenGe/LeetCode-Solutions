#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution
{
public:
    int massage(vector<int> &nums)
    {
        if (nums.size() <= 2)
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
                return max(nums[0], nums[1]);
            }
        }

        int *dp = new int[nums.size()];
        // fill(dp, dp+nums.size(), 0);

        dp[0] = nums[0];
        dp[1] = nums[1];
        if (nums.size() > 2)
        {
            dp[2] = max(dp[1], dp[0]+nums[2]);
        }

        for (int i = 3; i < nums.size(); ++i)
        {
            dp[i] = max(max(dp[i - 2] + nums[i], dp[i - 1]), dp[i-3]+nums[i]);
        }
        return dp[nums.size() - 1];
    }
};

int main()
{
    vector<int> vec;
    vec.push_back(1);
    vec.push_back(2);
    vec.push_back(3);
    vec.push_back(1);

    Solution so;
    cout << so.massage(vec) << endl;
    return 0;
}