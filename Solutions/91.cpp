#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

class Solution
{
public:
    int numDecodings(string s)
    {
        if (s.length() == 0 || s[0] == '0')
        {
            return 0;
        }
        if (s.length() == 1)
        {
            return 1;
        }

        vector<int> dp(s.length() + 1, 0); // 前I个字符的可能性
        dp[0] = 1;
        dp[1] = 1;
        for (int i = 2; i <= s.length(); i++)
        {
            if (s[i - 2] == '0')
            {
                if (s[i - 1] == '0')
                {
                    return 0;
                }
                else
                {
                    dp[i] = dp[i - 1];
                }
            }
            else if (s[i - 2] == '1')
            {
                if (s[i - 1] == '0')
                {
                    dp[i] = dp[i - 2];
                }
                else
                {
                    dp[i] = dp[i - 1] + dp[i - 2];
                }
            }
            else if (s[i - 2] == '2')
            {
                if (s[i - 1] == '0')
                {
                    dp[i] = dp[i - 2];
                }
                else if (s[i - 1] <= '6')
                {
                    dp[i] = dp[i - 1] +  dp[i - 2];
                }
                else
                {
                    dp[i] = dp[i - 1];
                }
            }
            else
            {
                if (s[i - 1] == '0')
                {
                    return 0;
                }
                else
                {
                    dp[i] = dp[i - 1];
                }
            }
        }
        return dp[s.length()];
    }
};

int main()
{
    return 0;
}