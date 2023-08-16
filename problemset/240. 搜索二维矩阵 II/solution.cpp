//
// Created by lenovo on 2020-09-18.
//

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
private:
    bool search(vector<vector<int>> &matrix, int target, int t, int b, int l, int r) {
        if (t > b || l > r) {
            return false;
        }

        int rm = (t + b) / 2;
        int cm = (l + r) / 2;
        if (matrix[rm][cm] == target) {
            return true;
        } else if (matrix[rm][cm] > target) {
            return search(matrix, target, t, rm, l, cm);
        } else {
            return search(matrix, target, t, rm, cm, r)
                   || search(matrix, target, rm, b, l, cm)
                   || search(matrix, target, rm, b, cm, r);
        }
    }

public:
    bool searchMatrix(vector<vector<int>> &matrix, int target) {
        if(matrix.size() == 0){
            return false;
        }
        return this->search(matrix, target, 0, matrix.size(), 0, matrix[0].size());
    }
};

int main() {
    return 0;
}