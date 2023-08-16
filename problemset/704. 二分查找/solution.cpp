#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution
{
public:
    int search(vector<int> &nums, int target)
    {
        if (nums.size() == 0 || target < nums[0] || target > nums[nums.size() - 1])
        {
            return -1;
        }

        int left = 0;
        int right = nums.size() - 1;
        int m = (left + right) / 2;
        while (left <= right)
        {
            m = (left + right) / 2;
            if (nums[m] < target)
            {
                left = m + 1;
            }
            else if (nums[m] > target)
            {
                right = m - 1;
            }
            else
            {
                return m;
            }
        }
        return -1;
    }
};

int main()
{
    return 0;
}