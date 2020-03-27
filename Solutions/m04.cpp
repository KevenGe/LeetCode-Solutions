#include <iostream>
#include <vector>
using namespace std;

class Solution
{
public:
    bool findNumberIn2DArray(vector<vector<int>> &matrix, int target)
    {
        int m = matrix.size();
        if (m == 0)
        {
            return false;
        }
        else
        {
            int n = matrix[0].size();
            if (n==0)
            {
                return false;
            }
            for (int i = 0; i < m; ++i)
            {
                if (target <= matrix[i][n - 1] && target >= matrix[i][0])
                {
                    int left = 0;
                    int right = n - 1;
                    int middle = 0;
                    while (left <= right)
                    {
                        middle = (left + right) / 2;
                        if (target < matrix[i][middle])
                        {
                            right = middle - 1;
                        }
                        else if (target > matrix[i][middle])
                        {
                            left = middle + 1;
                        }
                        else
                        {
                            return true;
                        }
                    }
                }
            }
            return false;
        }
        return false;
    }
};

int main()
{
    return 0;
}