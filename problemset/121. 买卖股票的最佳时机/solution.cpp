#include <iostream>
#include <vector>
#include <limits.h>
using namespace std;

class Solution
{
public:
    int maxProfit(vector<int> &prices)
    {
        int buy = INT_MAX;
        int sell = INT_MIN;
        int ans = 0;
        for (int i = 0; i < prices.size(); ++i)
        {
            if (prices[i] < buy)
            {
                buy = prices[i];
                sell = prices[i];
            }
            else if (prices[i] > sell)
            {
                sell = prices[i];
            }

            if (sell - buy > ans)
            {
                ans = sell - buy;
            }
        }
        return ans;
    }
};

int main()
{
    return 0;
}