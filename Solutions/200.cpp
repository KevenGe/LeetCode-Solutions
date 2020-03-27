#include <iostream>
#include <vector>
using namespace std;

class Solution
{
public:
    int numIslands(vector<vector<char>> &grid)
    {
        if (grid.size() == 0)
        {
            return 0;
        }
        else
        {
            int ans = 0;
            int x = grid.size();
            int y = grid[0].size();
            for (int i = 0; i < x; ++i)
            {
                for (int j = 0; j < y; ++j)
                {
                    if (grid[i][j] == '1')
                    {
                        dfs(grid, x, y, i, j);
                        ans++;
                    }
                }
            }
            return ans;
        }
    }

    void dfs(vector<vector<char>> &grid, int x, int y, int i, int j)
    {
        grid[i][j] = '0';
        if (i - 1 >= 0 && grid[i - 1][j] == '1')
        {
            dfs(grid, x, y, i - 1, j);
        }
        if (i + 1 < x && grid[i + 1][j] == '1')
        {
            dfs(grid, x, y, i + 1, j);
        }
        if (j - 1 >= 0 && grid[i][j - 1] == '1')
        {
            dfs(grid, x, y, i, j - 1);
        }
        if (j + 1 <y && grid[i][j + 1] == '1')
        {
            dfs(grid, x, y, i, j + 1);
        }
    }
};

int main()
{
    int **p = new int *[3];
    p[0] = new int[3];
    p[1] = new int[3];
    p[2] = new int[3];

    for (int i = 0; i < 3; ++i)
    {
        for (int j = 0; j < 3; ++j)
        {
            p[i][j] = i * 3 + j;
        }
        cout << endl;
    }
    for (int i = 0; i < 3; ++i)
    {
        for (int j = 0; j < 3; ++j)
        {
            cout << p[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}