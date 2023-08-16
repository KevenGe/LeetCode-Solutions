// /**
//  * @file 329.cpp
//  * @author your name (you@domain.com)
//  * @brief 
//  * @version 0.1
//  * @date 2020-07-27
//  * 
//  * @copyright Copyright (c) 2020
//  * 
//  * https://leetcode-cn.com/problems/longest-increasing-path-in-a-matrix/
//  */

// #include <iostream>
// #include <vector>
// #include <algorithm>
// using namespace std;

// class Solution
// {
// public:
//     int longestIncreasingPath(vector<vector<int>> &matrix)
//     {
//         /// set the array dp, and initial as 0
//         vector<vector<int>> mem(matrix.size(), vector<int>(matrix[0].size(), 0));

//         /// dfs and memory search

//         /// get the answer
//     }

//     void dfs(vector<vector<int>> &matrix, vector<vector<int>> &mem, int i, int j)
//     {
//         if (mem[i][j] == 0)
//         {
//             /// up
//             if (i - 1 > 0 && matrix[i - 1][j] > matrix[i][j])
//             {
//                 dfs(matrix, mem, i - 1, j);
//                 mem[i][j] = max(mem[i][j], mem[i - 1][j] + 1);
//             }

//             /// down
//             if (i + 1 > 0 && matrix[i - 1][j] > matrix[i][j])
//             {
//                 dfs(matrix, mem, i - 1, j);
//                 mem[i][j] = max(mem[i][j], mem[i - 1][j] + 1);
//             }

//             /// left
//             if (i - 1 > 0 && matrix[i - 1][j] > matrix[i][j])
//             {
//                 dfs(matrix, mem, i - 1, j);
//                 mem[i][j] = max(mem[i][j], mem[i - 1][j] + 1);
//             }

//             /// right
//             if (i - 1 > 0 && matrix[i - 1][j] > matrix[i][j])
//             {
//                 dfs(matrix, mem, i - 1, j);
//                 mem[i][j] = max(mem[i][j], mem[i - 1][j] + 1);
//             }
//         }
//     }
// };

// int main()
// {
//     return 0;
// }