#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
using namespace std;

class Solution
{
public:
    int findRepeatNumber(vector<int> &nums)
    {
        set<int> setss;
        for (int i = 0; i < nums.size(); ++i)
        {
            if (setss.find(nums[i]) != setss.end())
            {
                return nums[i];
            }
            else
            {
                setss.insert(nums[i]);
            }
        }
        return -1;
    }
};

int main()
{
}