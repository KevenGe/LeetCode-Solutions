//
// Created by lenovo on 2020/6/27.
//
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


class Solution {
public:
    int partitionDisjoint(vector<int> &A) {

        int maxPos = 0;
        int maxVau = A[0];
        int curMax = A[0];

        for (int i = 0; i < A.size(); ++i) {
            curMax = max(curMax, A[i]);

            if (A[i] < maxVau) {
                maxPos = i;
                maxVau = curMax;
            }
        }

        return maxPos + 1;
    }
};

int main() {
    return 0;
}