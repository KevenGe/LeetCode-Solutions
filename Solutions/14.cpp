#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

class Solution
{
public:
    int minCostClimbingStairs(vector<int> &cost)
    {
        if (cost.size() <= 2)
        {
            return 0;
        }

        int *dp = new int[cost.size()+1];
        dp[0] = 0;
        dp[1] = 0;
        for (int i = 2; i <= cost.size(); ++i)
        {
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2]);
        }
        return dp[cost.size()];
    }
};

/*
Binayr search!!! 
*/
bool binarySearch(vector<int> vec, int left, int right, int target)
{
    if (left > right)
    {
        return false;
    }

    int middle = (left + right) / 2;
    if (vec[middle] == target)
    {
        return true;
    }
    else
    {
        return binarySearch(vec, left, middle - 1, target) || binarySearch(vec, middle + 1, right, target);
    }
}

int main()
{
    vector<int> vec;
    vec.push_back(4);
    vec.push_back(2);
    vec.push_back(3);
    vec.push_back(1);
    vec.push_back(5);
    Solution so;
    cout << so.lengthOfLIS(vec) << endl;
}