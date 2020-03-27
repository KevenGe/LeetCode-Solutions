#include <iostream>
#include <vector>
#include <algorithm>
#include <limits.h>
using namespace std;

// class Solution
// {
// public:
//     int minIncrementForUnique(vector<int> &A)
//     {
//         sort(A.begin(), A.end());
//         int stand = INT_MIN;
//         int ans = 0;
//         for (int i = 0; i < A.size(); ++i)
//         {
//             while (A[i] <= stand)
//             {
//                 A[i]++;
//                 ans++;
//             }
//             stand = A[i];
//         }
//         return ans;
//     }
// };

class Solution
{
public:
    int minIncrementForUnique(vector<int> &A)
    {
        int dp[80000];
        fill(dp, dp + 80000, 0);
        for (int a : A)
        {
            dp[a]++;
        }

        int count = 0;
        int ans = 0;
        for (int i = 0; i < 80000; ++i)
        {
            if (dp[i] >= 2)
            {
                count += dp[i] - 1;
                ans -= i * (dp[i] - 1);
            }
            else if (dp[i] == 0 && count >0)
            {
                count --;
                ans += i;
            }
        }
        return ans;
    }
};

int main()
{
    return 0;
}