#include <iostream>
#include <vector>
using namespace std;

class Solution
{
public:
    int ans = 0;
    int maxAreaOfIsland(vector<vector<int>> &grid)
    {
        for (int i = 0; i < grid.size(); ++i)
        {
            for (int j = 0; j < grid[0].size(); ++j)
            {
                if (grid[i][j] == 1)
                {
                    dfs(grid, i, j, 1);
                }
            }
        }
        return ans;
    }

    void dfs(vector<vector<int>> &grid, int i, int j, int len)
    {
        grid[i][j] = -1;

        if (ans < len)
        {
            ans = len;
        }
        if (i - 1 >= 0)
            dfs(grid, i - 1, j, len + 1);
        if (i + 1 < grid.size())
            dfs(grid, i + 1, j, len + 1);
        if (j - 1 >= 0)
            dfs(grid, i, j - 1, len + 1);
        if (j + 1 < grid[0].size())
            dfs(grid, i, j + 1, len + 1);
    }
};

int main()
{
    vector<vector<int>> vec;

    vector<int> row1;
    row1.push_back(1);
    row1.push_back(1);
    row1.push_back(0);
    row1.push_back(0);
    row1.push_back(0);
    vec.push_back(row1);

    vector<int>
        row2;
    row2.push_back(1);
    row2.push_back(1);
    row2.push_back(0);
    row2.push_back(0);
    row2.push_back(0);
    vec.push_back(row2);

    vector<int>
        row3;
    row3.push_back(0);
    row3.push_back(0);
    row3.push_back(0);
    row3.push_back(1);
    row3.push_back(1);
    vec.push_back(row3);

    vector<int> row4;
    row4.push_back(0);
    row4.push_back(0);
    row4.push_back(0);
    row4.push_back(1);
    row4.push_back(1);
    vec.push_back(row4);

    Solution so;
    cout << so.maxAreaOfIsland(vec) << endl;
    return 0;
}