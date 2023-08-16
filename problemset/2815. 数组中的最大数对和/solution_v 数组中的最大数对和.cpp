#include <algorithm>
#include <functional>
#include <iostream>
#include <map>
#include <string>
#include <vector>

using namespace std;

int getMaxN(int num)
{
    int ans = 0;
    while (num > 0)
    {
        ans = max(ans, num % 10);
        num = num / 10;
    }
    return ans;
}

class Solution
{
  public:
    int maxSum(vector<int> &nums)
    {
        sort(nums.begin(), nums.end(), greater<int>());
        vector<int> maxNums(nums.size());
        for (int i = 0; i < nums.size(); i++)
        {
            maxNums[i] = getMaxN(nums[i]);
        }
        int ans = -1;
        for (int i = 0; i < nums.size(); i++)
        {
            if(nums[i] * 2 < ans)
            {
                break;
            }
            for (int j = i + 1; j < nums.size(); j++)
            {
                if (maxNums[i] != maxNums[j])
                {
                    continue;
                }
                ans = max(ans, nums[i] + nums[j]);
                break;
            }
        }
        return ans;
    }
};

int main()
{
    Solution so;
    return 0;
}