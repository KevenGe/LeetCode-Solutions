#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

// class Solution
// {
// public:
//     char chars[10][10];
//     bool could_use[10][10];
//     int end;
//     vector<vector<string>> res;
//     vector<vector<string>> solveNQueens(int n)
//     {
//         this->end = n;
//         for (int i = 0; i < n; ++i)
//         {
//             fill(chars[i], chars[i] + n, '.');
//             fill(could_use[i], could_use[i] + n, true);
//         }
//         dfs(0);
//         return res;
//     }
//     void dfs(int dim)
//     {
//         if (dim == this->end)
//         {
//             vector<string> tmp;
//             for (int i = 0; i < this->end; ++i)
//             {
//                 string tmp2 = "";
//                 for (int j = 0; j < this->end; ++j)
//                 {
//                     tmp2 = tmp2 + this->chars[i][j];
//                 }
//                 tmp.push_back(tmp2);
//             }
//             this->res.push_back(tmp);
//         }
//         else
//         {
//             for (int i = 0; i < this->end; ++i)
//             {
//                 if (this->could_use[dim][i])
//                 {
//                     this->could_use[dim][i] = false;
//                     this->chars[dim][i] = 'Q';
//                     for (int j = dim + 1; j < this->end; ++j)
//                     {
//                         this->could_use[j][i] = false;

//                         if ((i - (j - dim) >= 0))
//                         {
//                             this->could_use[j][i - (j - dim)] = false;
//                         }

//                         if ((i + (j - dim) < this->end))
//                         {
//                             this->could_use[j][i + (j - dim)] = false;
//                         }
//                     }
//                     dfs(dim + 1);
//                     this->could_use[dim][i] = true;
//                     this->chars[dim][i] = '.';
//                     for (int j = dim + 1; j < this->end; ++j)
//                     {
//                         this->could_use[j][i] = true;

//                         if ((i - (j - dim) >= 0))
//                         {
//                             this->could_use[j][i - (j - dim)] = true;
//                         }

//                         if ((i + (j - dim) < this->end))
//                         {
//                             this->could_use[j][i + (j - dim)] = true;
//                         }
//                     }
//                 }
//             }
//         }
//     }
// };

class Solution
{
public:
    vector<vector<char>> chars;
    vector<vector<char>> could_use;
    int end;
    vector<vector<string>> res;
    vector<vector<string>> solveNQueens(int n)
    {
        this->end = n;
        for (int i = 0; i < n; ++i)
        {
            vector<char> chars2;
            vector<char> could_use2;
            for (int j = 0; j < n; ++j)
            {
                chars2.push_back('.');
                could_use2.push_back(true);
            }
            chars.push_back(chars2);
            could_use.push_back(could_use2);
        }
        dfs(0);
        return res;
    }
    void dfs(int dim)
    {
        if (dim == this->end)
        {
            vector<string> tmp;
            for (int i = 0; i < this->end; ++i)
            {
                string tmp2 = "";
                for (int j = 0; j < this->end; ++j)
                {
                    tmp2 = tmp2 + this->chars[i][j];
                }
                tmp.push_back(tmp2);
            }
            this->res.push_back(tmp);
        }
        else
        {
            for (int i = 0; i < this->end; ++i)
            {
                if (this->could_use[dim][i])
                {
                    this->could_use[dim][i] = false;
                    this->chars[dim][i] = 'Q';
                    for (int j = dim + 1; j < this->end; ++j)
                    {
                        this->could_use[j][i] = false;

                        if ((i - (j - dim) >= 0))
                        {
                            this->could_use[j][i - (j - dim)] = false;
                        }

                        if ((i + (j - dim) < this->end))
                        {
                            this->could_use[j][i + (j - dim)] = false;
                        }
                    }
                    dfs(dim + 1);

                    this->could_use[dim][i] = true;
                    this->chars[dim][i] = '.';
                    for (int j = dim + 1; j < this->end; ++j)
                    {
                        this->could_use[j][i] = true;

                        if ((i - (j - dim) >= 0))
                        {
                            this->could_use[j][i - (j - dim)] = true;
                        }

                        if ((i + (j - dim) < this->end))
                        {
                            this->could_use[j][i + (j - dim)] = true;
                        }
                    }
                }
            }
        }
    }
};

int main()
{
    Solution so;
    so.solveNQueens(4);
    return 0;
}