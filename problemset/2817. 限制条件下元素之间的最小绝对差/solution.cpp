#include <algorithm>
#include <functional>
#include <iostream>
#include <limits>
#include <set>
#include <stack>
#include <string>
#include <vector>

using namespace std;

class Solution
{
  public:
    int minAbsoluteDifference(vector<int> &nums, int x)
    {
        set<int> s{numeric_limits<int>::max() / 2, numeric_limits<int>::min() / 2};
        int ans = numeric_limits<int>::max();
        for (int i = x; i < nums.size(); i++)
        {
            s.insert(nums[i - x]);
            int y = nums[i];
            set<int>::iterator it = s.lower_bound(y);
            ans = min(ans, min(*it - y, y - *(--it)));
        }
        return ans;
    }
};

int main()
{
    Solution so;
    return 0;
}
