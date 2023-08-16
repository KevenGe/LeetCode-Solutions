/*
 * LeetCode 292
 * 这个是LeetCode的腾讯面试题的【NIM游戏】
 */

#include <iostream>
#include <vector>
#include <climits>

using namespace std;

class Solution {
public:
    bool canWinNim(int n) {
        return n % 4 != 0;
    }
};

int main() {
    return 0;
}