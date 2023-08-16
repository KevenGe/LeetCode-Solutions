//
// Created by lenovo on 2020-09-18.
//

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool cmp(vector<int> &p1, vector<int> &p2) {
    return p1[0] < p2[0];
}

class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>> &intervals) {
        sort(intervals.begin(), intervals.end(), cmp);

    }
};

int main() {
    return 0;
}