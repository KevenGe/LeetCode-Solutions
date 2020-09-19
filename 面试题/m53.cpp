#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution
{
public:
    int search(vector<int> &nums, int target)
    {
        int start = lower_bound(nums.begin(), nums.end(), target) - nums.begin();
        int ans = 0;
        while (start != nums.size())
        {
            if (nums[start] == target)
            {
                ans++;
                start++;
            }
            else
            {
                break;
            }
        }
        return ans;
    }
};

int main()
{
    return 0;
}