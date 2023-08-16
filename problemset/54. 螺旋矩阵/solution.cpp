//
// Created by lenovo on 2020-10-01.
//

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>> &matrix) {
        vector<int> ans;
        if (matrix.empty() || matrix[0].empty()) {
            return ans;
        }

        // layer
        for (int i = 0; i <= (min(matrix.size(),matrix[0].size()) - 1) / 2; i++) {
            int left = i;
            int right = matrix[0].size() - 1 - i;
            int top = i;
            int bottom = matrix.size() - 1 - i;

            if(left == right){
                if(top == bottom){
                    ans.push_back(matrix[left][top]);
                }else{
                    // right
                    for (int j = top; j <= bottom; j++) {
                        ans.push_back(matrix[j][right]);
                    }
                    break;
                }
            }else{
                if(top == bottom){
                    // top
                    for (int j = left; j <= right; j++) {
                        ans.push_back(matrix[top][j]);
                    }
                }
                else {

                    // top
                    for (int j = left; j < right; j++) {
                        ans.push_back(matrix[top][j]);
                    }

                    // right
                    for (int j = top; j < bottom; j++) {
                        ans.push_back(matrix[j][right]);
                    }

                    // bottom
                    for (int j = right; j > left; j--) {
                        ans.push_back(matrix[bottom][j]);
                    }

                    // left
                    for (int j = bottom; j> top;j--){
                        ans.push_back(matrix[j][left]);
                    }
                }
            }
        }
        return ans;
    }
};

void runTest() {
    vector<vector<int>> vec;
    vector<int> tmp;
    tmp.push_back(1);

    vec.push_back(tmp);

    vector<int> tmp2;
    tmp2.push_back(5);
    vec.push_back(tmp2);

    vector<int> tmp3;
    tmp3.push_back(9);
    vec.push_back(tmp3);

    vector<int> tmp4;
    tmp4.push_back(9);
    vec.push_back(tmp4);

    vector<int> tmp5;
    tmp5.push_back(9);
    vec.push_back(tmp5);

    vector<int> tmp6;
    tmp6.push_back(9);
    vec.push_back(tmp6);

    vector<int> tmp7;
    tmp7.push_back(9);
    vec.push_back(tmp7);

    vector<int> tmp8;
    tmp8.push_back(9);
    vec.push_back(tmp8);

    Solution so;
    for (auto x : so.spiralOrder(vec)){
        cout << x << " ";
    }
}

int main() {
    runTest();
    return 0;
}