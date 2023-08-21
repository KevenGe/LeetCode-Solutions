#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution
{
  public:
    int numberOfWays(int startPos, int endPos, int k)
    {
        int l = abs(endPos - startPos);
        if (k < l || (k - l) % 2 != 0)
        {
            return 0;
        }

        l = (k - l) / 2;

        const int MOD = 1e9 + 7;
        vector<vector<int>> dp(k + 1, vector<int>(l + 1, 0));
        for (int i = 0; i <= k; i++)
        {
            dp[i][0] = 1;
        }
        for (int i = 0; i <= l; i++)
        {
            dp[i][i] = 1;
        }

        for (int i = 1; i <= k; i++)
        {
            for (int j = 1; j <= min(l, i - 1); j++)
            {
                dp[i][j] = (dp[i - 1][j] + dp[i - 1][j - 1]) % MOD;
            }
        }

        return dp[k][l];
    }
};
