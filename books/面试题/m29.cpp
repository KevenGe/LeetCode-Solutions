/* 
    面试题29：顺时针打印矩阵
 */

#include <iostream>
#include <vector>

using namespace std;

class Solution
{
public:
    vector<int> spiralOrder(vector<vector<int>> &matrix)
    {
        vector<int> res;
        for (int j = 0; j < (matrix.size() + 1) / 2; ++j)
        {
            int row = j;
            int column = j;
            int width = matrix.size() - row * 2;

            if (width == 1)
            {
                res.push_back(matrix[row][column]);
                break;
            }

            // up to right
            for (int i = 0; i < width - 1; ++i)
            {
                res.push_back(matrix[row][column + i]);
            }

            //right to button
            column = row + width - 1;
            for (int i = 0; i < width - 1; ++i)
            {
                res.push_back(matrix[row + i][column]);
            }

            //button to left
            row = row + width - 1;

            for (int i = 0; i < width - 1; ++i)
            {
                res.push_back(matrix[row][column - i]);
            }

            // left to top
            column = column - width + 1;
            for (int i = 0; i < width - 1; ++i)
            {
                res.push_back(matrix[row - i][column]);
            }
        }

        return res;
    }
};

int main()
{

    vector<int> vec1;
    vec1.push_back(1);
    vec1.push_back(2);
    vec1.push_back(3);
    vec1.push_back(4);

    vector<int> vec2;
    vec2.push_back(5);
    vec2.push_back(6);
    vec2.push_back(7);
    vec2.push_back(8);

    vector<int> vec3;
    vec3.push_back(9);
    vec3.push_back(10);
    vec3.push_back(11);
    vec3.push_back(12);

    vector<int> vec4;
    vec4.push_back(13);
    vec4.push_back(14);
    vec4.push_back(15);
    vec4.push_back(16);

    vector<vector<int>> vec;
    vec.push_back(vec1);
    vec.push_back(vec2);
    vec.push_back(vec3);
    vec.push_back(vec4);

    Solution so;
    vector<int> tmp = so.spiralOrder(vec);
    for (int i = 0; i < 16; ++i)
    {
        // for(int j=0;j<4;++j){
        //     co
        // }
        cout << tmp[i] << endl;
    }
    return 0;
}
