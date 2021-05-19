#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

class Solution
{
public:
    vector<int> grayCode(int n)
    {
        vector<int> ans(pow(2, n), 0);

        ans[0] = 0;
        ans[1] = 1;
        for (int i = 1; i < n; i++)
        {
            for (int j = pow(2, i); j < pow(2, i + 1); j++)
            {
                ans[j] = (1 << i) + ans[pow(2, i) - (j - pow(2, i)) - 1];
            }
        }
        return ans;
    }
};

int main()
{
    Solution so;
    for (auto x : so.grayCode(4))
    {
        cout << x << endl;
    }
    return 0;
}