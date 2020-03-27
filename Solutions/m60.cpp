#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution
{
public:
    vector<double> twoSum(int n)
    {
        double dp[70] = {0.0};
        fill(dp, dp + 70, 0.0);

        for (int i = 1; i <= 6; ++i)
        {
            dp[i] = 1.0 / 6;
        }

        for (int i = 2; i <= n; ++i)
        {
            for (int j = i * 6; j >= i; --j)
            {
                double sum = 0;
                for (int z = j - 1; z >= j - 6 && z >= i - 1; --z)
                {
                    sum += dp[z];
                }
                dp[j] = sum / 6;
            }
        }

        // sort(dp + n, dp + n * 6+1);
        vector<double> res;
        for (int i = n; i <= n * 6; ++i)
        {
            res.push_back(dp[i]);
        }
        return res;
    }
};

int main()
{
    Solution so;
    so.twoSum(1);
    return 0;
}