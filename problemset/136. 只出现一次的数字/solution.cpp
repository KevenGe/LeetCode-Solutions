/*
 * LeetCode 136. 只出现一次的数字
 *  应该这个题目的升级版本，原版本忘记保留了
 * Author: Keven Ge
 * Date: 2020-05-14
 */

#include <iostream>
#include <cmath>
#include <stack>
#include <unordered_map>
#include <unordered_set>
#include <climits>
#include <vector>
#include <algorithm>

using namespace std;

bool cmp(int a, int b) {
    int aa = a;
    int bb = b;
    int ai = 0;
    int bi = 0;
    while (a != 0) {
        if (a & 1) {
            ai++;
        }
        a = a >> 1;
    }
    while (b != 0) {
        if (b & 1) {
            bi++;
        }
        b = b >> 1;
    }
    if (ai != bi) {
        return ai < bi;
    } else {
        return aa < bb;
    }
}

class Solution {
public:
    vector<int> sortByBits(vector<int> &arr) {
        sort(arr.begin(), arr.end(), cmp);
        return arr;
    }
};

int main() {
    cout << cmp (2, 1) << endl;
    return 0;
}
