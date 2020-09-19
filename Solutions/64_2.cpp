#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution
{
public:
    int minPathSum(vector<vector<int>> &grid)
    {
        if (grid.size() == 0)
        {
            return 0;
        }

        vector<int> dp(grid[0].size());
        dp[0] = grid[0][0];
        for (int i = 1; i < grid[0].size(); i++)
        {
            dp[i] = grid[0][i] + dp[i - 1];
        }

        for (int i = 1; i < grid.size(); i++)
        {
            dp[0] = dp[0] + grid[i][0];
            for (int j = 1; j < grid[0].size(); j++)
            {
                dp[j] = min(dp[j - 1], dp[j]) + grid[i][j];
            }
        }

        return dp[grid[0].size() - 1];
    }
};

int main()
{
    return 0;
}
