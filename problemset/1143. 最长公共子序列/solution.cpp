#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution
{
public:
    int longestCommonSubsequence(string text1, string text2)
    {

        if (text1.length() == 0)
        {
            return 0;
        }

        vector<vector<int>> dp(text2.length(), vector<int>(text1.length(), 0));

        for (int i = 0; i < text2.length(); i++)
        {
            for (int j = 0; j < text1.length(); j++)
            {
                if (i == 0)
                {
                    if (j == 0)
                    {
                        dp[i][j] = (text1[j] == text2[i]) ? 1 : 0;
                    }
                    else
                    {
                        dp[i][j] = max(dp[i][j - 1], (text1[j] == text2[i]) ? 1 : 0);
                    }
                }
                else
                {
                    if (j == 0)
                    {
                        dp[i][j] = max(dp[i - 1][j], (text1[j] == text2[i]) ? 1 : 0);
                    }
                    else
                    {
                        dp[i][j] = dp[i - 1][j - 1] + ((text1[j] == text2[i]) ? 1 : 0);
                    }
                }
            }
        }
        return dp[text2.length() - 1][text1.length()];
    }
};

int main()
{
    Solution so;
    cout << so.longestCommonSubsequence("abcde", "ace") << endl;
    return 0;
}
