// 合并区间

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool cmp(vector<int> a, vector<int> b)
{
    if (a[0] < b[0])
    {
        return true;
    }
    else if (a[0] == b[0])
    {
        return a[1] <= b[0];
    }
    return false;
}

class Solution
{
public:
    vector<vector<int>> merge(vector<vector<int>> &intervals)
    {
        sort(intervals.begin(), intervals.end(), cmp);
        vector<vector<int>> res;
        if (intervals.size() == 0)
            return res;

        res.push_back(intervals[0]);
        int size = 0;
        for (int i = 1; i < intervals.size(); ++i)
        {
            if (intervals[i][0] <= res[size][1])
            {
                if (res[size][1] < intervals[i][1])
                {
                    res[size][1] = intervals[i][1];
                }
            }
            else
            {
                res.push_back(intervals[i]);
                size++;
            }
        }
        return res;
    }
};

int main()
{
    vector<vector<int>> vec;
    vector<int> tmp;
    tmp.push_back(1);
    tmp.push_back(3);
    vec.push_back(tmp);

    vector<int> tmp2;
    tmp2.push_back(2);
    tmp2.push_back(6);
    vec.push_back(tmp2);

    vector<int> tmp3;
    tmp3.push_back(8);
    tmp3.push_back(10);
    vec.push_back(tmp3);

    vector<int> tmp4;
    tmp4.push_back(15);
    tmp4.push_back(18);
    vec.push_back(tmp4);

    Solution so;
    so.merge(vec);
    return 0;
}