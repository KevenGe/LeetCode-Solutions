/*
    * https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/1/array/30/

*/

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


class Solution
{
public:
    bool isValidSudoku(vector<vector<char>> &board)
    {
        //column
        for (int i = 0; i < 9; ++i)
        {
            bool nums[10] = {false};
            for (int j = 0; j < 9; ++j)
            {
                int tmp = board[i][j] - '0';
                if (tmp >= 0 && tmp <= 9)
                {
                    if (nums[tmp] == false)
                    {
                        nums[tmp] = true;
                    }
                    else
                    {
                        return false;
                    }
                }
            }
        }

        //lines

        for (int i = 0; i < 9; ++i)
        {
            bool nums[10] = {false};
            for (int j = 0; j < 9; ++j)
            {
                int tmp = board[j][i] - '0';
                if (tmp >= 0 && tmp <= 9)
                {
                    if (nums[tmp] == false)
                    {
                        nums[tmp] = true;
                    }
                    else
                    {
                        return false;
                    }
                }
            }
        }

        //fangkuai
        for (int i = 0; i < 8; i = i + 3)
        {
            for (int j = 0; j < 8; j = j + 3)
            {
                bool nums[10] = {false};
                for (int s = i; s < i + 3; s++)
                {
                    for (int t = j; t < j + 3; t++)
                    {
                        int tmp = board[s][t]-'0';
                        if (tmp >= 0 && tmp <= 9)
                        {
                            if (nums[tmp] == false)
                            {
                                nums[tmp] = true;
                            }
                            else
                            {
                                return false;
                            }
                        }
                    }
                }
            }
        }
        return true;
    }
};

int main()
{
    return 0;
}