/*
重要！
！ 重要
未完成
*/

#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

class Solution
{
public:
    bool isMatch(string s, string p)
    {
        //int dp[100][100] = {0};
        // fill(dp, dp + 100 * 100, 0);
        int **dp = new int *[s.length() + 1];
        for (int j = 0; j <= s.length(); ++j)
        {
            dp[j] = new int[p.length() + 1];
        }
         for (int i = 0; i <= s.length(); ++i)
        {
            for (int j = 0; j <= p.length(); ++j)
            {
                dp[i][j] = 0;
            }
        }

        dp[0][0] = 1;

        for (int j = 0; j < p.length(); ++j)
        {
            if (p[j] == '*' && dp[0][j - 1])
            {
                dp[0][j + 1] = 1;
            }
        }

        for (int i = 0; i < s.length(); ++i)
        {
            for (int j = 0; j < p.length(); ++j)
            {
                if (s[i] == p[j] || p[j] == '.')
                {
                    dp[i + 1][j + 1] = dp[i][j];
                }
                else if (p[j] == '*')
                {
                    if (s[i] != p[j - 1] && p[j - 1] != '.')
                    {
                        dp[i + 1][j + 1] = dp[i + 1][j - 1];
                    }
                    else
                    {
                        dp[i + 1][j + 1] = (dp[i + 1][j] || dp[i][j + 1] || dp[i + 1][j - 1]);
                    }
                }
            }
        }
        return dp[s.length()][p.length()];
    }
};

int main()
{
    Solution so;
    cout << so.isMatch("aa", "a");
    return 0;
}
