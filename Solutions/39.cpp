#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution
{
public:
    vector<vector<int>> ans;
    vector<vector<int>> combinationSum(vector<int> &candidates, int target)
    {
        vector<int> res;
        dfs(0, target, res, candidates);
        return ans;
    }

    void dfs(int i, int remain, vector<int> res, vector<int> &candidates)
    {
        if (i < candidates.size())
        {
            while (remain >= 0)
            {
                dfs(i + 1, remain, res, candidates);
                res.push_back(candidates[i]);
                remain -= candidates[i];
            }
        }
        else
        {
            if (remain == 0)
            {
                ans.push_back(res);
            }
        }
    }
};

int main()
{
    return 0;
}