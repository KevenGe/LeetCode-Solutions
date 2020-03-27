/*
    309. 最佳买卖股票时机含冷冻期

    六个股票买卖问题
*/

#include <iostream>
#include <vector>
#include <limits.h>
#include <algorithm>
using namespace std;

class Solution
{
public:
    int maxProfit(vector<int> &prices)
    {
        if(prices.size()==0)
        {
            return 0;
        }

        int dp[100000][3][2] = {0};

        dp[0][0][0] = 0;
        dp[0][0][1] = 0;
        for (int i = 0; i < prices.size(); ++i)
        {
            for (int k = 1; k <= 2; ++k)
            {
                if (i == 0)
                {
                    dp[i][0][0] = 0;
                    dp[i][0][1] = INT_MIN;
                    dp[i][1][0] = 0;
                    dp[i][1][1] = -prices[i];
                    dp[i][2][0] = 0;
                    dp[i][2][1] = INT_MIN;
                    break;
                }
                dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i]);
                dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i]);
            }
        }
        return max(dp[prices.size() - 1][2][0], dp[prices.size() - 1][1][0]);
    }
};

int main()
{
    vector<int> vec;
    // vec.push_back(1);
    // vec.push_back(2);
    // vec.push_back(3);
    // vec.push_back(4);
    // vec.push_back(5);

    vec.push_back(3);
    vec.push_back(3);
    vec.push_back(5);
    vec.push_back(0);
    vec.push_back(0);
    vec.push_back(3);
    vec.push_back(1);
    vec.push_back(4);

    Solution so;
    cout << so.maxProfit(vec);
    return 0;
}