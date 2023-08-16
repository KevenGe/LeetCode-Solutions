#include <iostream>
#include <queue>
#include <vector>
using namespace std;

struct Pos
{
    int x;
    int y;
    Pos(int x_, int y_)
    {
        x = x_;
        y = y_;
    }
};

class Solution
{
public:
    int orangesRotting(vector<vector<int>> &grid)
    {
        queue<Pos> ques;
        bool find_one_bad = false;
        for (int i = 0; i < grid.size(); ++i)
        {
            for (int j = 0; j < grid[0].size(); ++j)
            {
                if (grid[i][j] == 2)
                {
                    Pos pos(i, j);
                    ques.push(pos);
                    find_one_bad = true;
                }
            }
        }

        if (!find_one_bad)
        {
            for (int i = 0; i < grid.size(); ++i)
            {
                for (int j = 0; j < grid[0].size(); ++j)
                {
                    if (grid[i][j] == 1)
                    {
                        return -1;
                    }
                }
            }
            return 0;
        }

        int res = 0;
        while (!ques.empty())
        {
            for (int i = ques.size(); i > 0; --i)
            {
                Pos pos = ques.front();
                ques.pop();
                if (pos.x - 1 >= 0 && grid[pos.x - 1][pos.y] == 1)
                {
                    grid[pos.x - 1][pos.y] = 2;
                    Pos poss(pos.x - 1, pos.y);
                    ques.push(poss);
                }

                if (pos.x + 1 < grid.size() && grid[pos.x + 1][pos.y] == 1)
                {
                    grid[pos.x + 1][pos.y] = 2;
                    Pos poss(pos.x + 1, pos.y);
                    ques.push(poss);
                }

                if (pos.y - 1 >= 0 && grid[pos.x][pos.y - 1] == 1)
                {
                    grid[pos.x][pos.y - 1] = 2;
                    Pos poss(pos.x, pos.y - 1);
                    ques.push(poss);
                }

                if (pos.y + 1 < grid[0].size() && grid[pos.x][pos.y + 1] == 1)
                {
                    grid[pos.x][pos.y + 1] = 2;
                    Pos poss(pos.x, pos.y + 1);
                    ques.push(poss);
                }
            }
            res++;
        }

        for (int i = 0; i < grid.size(); ++i)
        {
            for (int j = 0; j < grid[0].size(); ++j)
            {
                if (grid[i][j] == 1)
                {
                    return -1;
                }
            }
        }

        return res - 1;
    }
};

int main()
{
    vector<vector<int>> res;
    vector<int> res1;
    res1.push_back(2);
    res1.push_back(1);
    res1.push_back(1);

    vector<int> res2;
    res2.push_back(1);
    res2.push_back(1);
    res2.push_back(0);

    vector<int> res3;
    res3.push_back(0);
    res3.push_back(1);
    res3.push_back(1);

    res.push_back(res1);
    res.push_back(res2);
    res.push_back(res3);

    Solution so;
    cout << so.orangesRotting(res) << endl;
    return 0;
}