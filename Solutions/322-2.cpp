#include <iostream>
#include <algorithm>
#include <vector>
#include <limits.h>
using namespace std;

bool cmp(int a, int b)
{
    return a >= b;
}

class Solution
{
public:
    int ans = INT_MAX;
    int coinChange(vector<int> &coins, int amount)
    {
        if (amount == 0)
        {
            return 0;
        }
        sort(coins.begin(), coins.end(), cmp);
        coinChangeHelper(coins, amount, 0, 0);

        return ans == INT_MAX ? -1 : ans;
    }
    void coinChangeHelper(vector<int> &coins, int amount, int index, int count)
    {
        if (amount == 0)
        {
            ans = min(ans, count);
            return;
        }

        if (amount <= 0 || index == coins.size())
        {
            return;
        }

        for (int i = amount / coins[index]; i >= 0 && i + count <= ans; --i)
        {
            coinChangeHelper(coins, amount - i * coins[index], index + 1, count + i);
        }
    }
};

int main()
{
    Solution so;
    vector<int> vec;
    vec.push_back(1);
    vec.push_back(2);
    vec.push_back(5);

    cout << so.coinChange(vec, 11) << endl;
    return 0;
}