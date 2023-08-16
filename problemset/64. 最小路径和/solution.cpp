#include <iostream>
#include <vector>
#include <limits.h>
#include <algorithm>
using namespace std;

class Solution
{
public:
    int minPathSum(vector<vector<int> > &grid)
    {
        int n = grid.size();
        if (n == 0)
        {
            return 0;
        }

        int m = grid[0].size();

        int *dp = new int[m + 1];
        // int dp[100];
        fill(dp, dp + m + 1, INT_MAX);
        dp[0] = grid[0][0];

        for (int j = 1; j < m; ++j)
        {
            dp[j] = min(dp[j], dp[j - 1] + grid[0][j]);
        }

        for (int i = 1; i < n; ++i)
        {
            dp[0] = dp[0] + grid[i][0];
            for (int j = 1; j < m; ++j)
            {
                dp[j] = min(dp[j], dp[j-1]) + grid[i][j];
            }
        }
        return dp[m-1];
    }
};

int main()
{
    vector<vector<int> > res;

    vector<int> tmp1;
    tmp1.push_back(1);
    tmp1.push_back(3);
    tmp1.push_back(1);
    res.push_back(tmp1);


    vector<int> tmp2;
    tmp2.push_back(1);
    tmp2.push_back(5);
    tmp2.push_back(1);
    res.push_back(tmp2);

    
    vector<int> tmp3;
    tmp3.push_back(4);
    tmp3.push_back(2);
    tmp3.push_back(1);
    res.push_back(tmp3);

    Solution so;
    so.minPathSum(res);

    return 0;
}