#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution
{
public:
    vector<vector<int>> threeSum(vector<int> &nums)
    {
        sort(nums.begin(), nums.end());
        vector<vector<int>> res;

        if (nums.size() < 3)
            return res;

        int left = 0;
        int right;
        int middle = 1;
        while (left < nums.size() - 2)
        {
            middle = left + 1;
            right = nums.size() - 1;

            while (middle < right)
            {
                if (nums[left] + nums[middle] + nums[right] == 0)
                {
                    vector<int> res_tmp;
                    res_tmp.push_back(nums[left]);
                    res_tmp.push_back(nums[middle]);
                    res_tmp.push_back(nums[right]);
                    res.push_back(res_tmp);

                    while (middle + 1 < right && nums[middle] == nums[middle + 1])
                    {
                        middle++;
                    }
                    middle++;

                    while (middle < right - 1 && nums[right] == nums[right - 1])
                    {
                        right--;
                    }
                    right--;

                    if (nums[middle] == res_tmp[1] || nums[right] == res_tmp[2])
                    {
                        break;
                    }
                }
                else if (nums[left] + nums[middle] + nums[right] > 0)
                {
                    right--;
                }
                else
                {
                    middle++;
                }
            }

            while (left + 1 < nums.size() - 2 && nums[left] == nums[left + 1])
            {
                left++;
            }
            left++;
        }
        return res;
    }
};

int main()
{
    vector<int> vec;

    // vec.push_back(-1);
    // vec.push_back(0);
    // vec.push_back(1);
    // vec.push_back(2);
    // vec.push_back(-1);
    // vec.push_back(-4);

    // vec.push_back(0);
    // vec.push_back(0);
    // vec.push_back(0);
    // vec.push_back(0);

    vec.push_back(-2);
    vec.push_back(0);
    vec.push_back(1);
    vec.push_back(1);
    vec.push_back(2);
    Solution so;
    for (vector<int> tmp : so.threeSum(vec))
    {
        for (int x : tmp)
        {
            cout << x << " ";
        }
        cout << endl;
    }
    return 0;
}