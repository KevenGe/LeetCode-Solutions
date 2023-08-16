/* 
    LeetCode 238

 */

#include <iostream>
#include <vector>
using namespace std;

class Solution
{
public:
    vector<int> productExceptSelf(vector<int> &nums)
    {
        vector<int> res(nums.size(), 1);

        int tmp = 1;
        for (int i = 0; i < nums.size(); ++i)
        {
            res[i] *= tmp;
            tmp *= nums[i];
        }

        tmp = 1;
        for (int i = nums.size() - 1; i >= 0; --i)
        {
            res[i] *= tmp;
            tmp *= nums[i];
        }

        return res;
    }
};

int main()
{
    return 0;
}