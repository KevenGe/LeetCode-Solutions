#include <iostream>
#include <vector>
#include <unordered_set>
#include <algorithm>

using namespace std;

class Solution
{
public:
    int longestConsecutive(vector<int> &nums)
    {
        unordered_set<int> sets;
        for (int & num : nums)
        {
            sets.insert(num);
        }

        int ans = 0;
        for (int num : nums)
        {
            if (sets.find(num - 1) == sets.end())
            {
                int cur = num;
                int len = 1;

                while (sets.find(cur + 1) != sets.end())
                {
                    cur += 1;
                    len += 1;
                }

                ans = max(ans, len);
            }
        }

        return ans;
    }
};

int main()
{
    vector<int> vec;
    vec.push_back(100);
    vec.push_back(4);
    vec.push_back(200);
    vec.push_back(1);
    vec.push_back(3);
    vec.push_back(2);

    Solution so;
    cout << so.longestConsecutive(vec) << endl;
    return 0;
}
