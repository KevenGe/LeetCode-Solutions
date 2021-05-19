#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution
{
public:
    vector<vector<int>> insert(vector<vector<int>> &intervals, vector<int> &newInterval)
    {
        vector<vector<int>> ans;

        int i = 0;

        // left
        while (i < intervals.size() && intervals[i][1] < newInterval[0])
        {
            ans.push_back(intervals[i]);
            i += 1;
        }

        // middle
        while (i < intervals.size() && intervals[i][0] <= newInterval[1])
        {
            newInterval[0] = min(newInterval[0], intervals[i][0]);
            newInterval[1] = max(newInterval[1], intervals[i][1]);
            i += 1;
        }
        ans.push_back(newInterval);

        // right
        while (i < intervals.size())
        {
            ans.push_back(intervals[i]);
            i += 1;
        }

        return ans;
    }
};

int main()
{
    return 0;
}