#include <iostream>
#include <algorithm>
using namespace std;

class Solution
{
public:
    int longestCommonSubsequence(string text1, string text2)
    {
        int dp[1001][1001] = {0}; // i = text1, j = text2
        for (int i = 1; i <= text1.length(); ++i)
        {
            for (int j = 1; j <= text2.length(); ++j)
            {
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j]);
                if (text1[i - 1] == text2[j - 1])
                {
                    dp[i][j] = max(dp[i - 1][j - 1] + 1, dp[i][j]);
                }
                // if (text1[i - 1] == text2[j - 1])
                // {
                //     dp[i][j] = max(dp[i - 1][j - 1] + 1, dp[i][j - 1], dp[i - 1][j]);
                // }
                // else
                // {
                //     dp[i][j] = max(dp[i][j - 1], dp[i - 1][j]);
                // }
            }
        }
        return dp[text1.length()][text2.length()];
    }
};

int main()
{
    cout << " " << endl;
    return 0;
}