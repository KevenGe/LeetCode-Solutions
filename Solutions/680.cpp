/*
 * LeetCode 680. 验证回文字符串 Ⅱ
 * Author: Keven Ge
 * Date: 2020-05-19
 */

#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    bool validPalindrome(string s) {
        int low = 0;
        int high = s.length() - 1;

        while (low <= high) {
            if (s[low] == s[high]) {
                low += 1;
                high -= 1;
            } else {
                return help(s, low + 1, high) || help(s, low, high - 1);
            }
        }
        return true;
    }

    bool help(string s, int a, int b) {
        while (a <= b) {
            if (s[a] == s[b]) {
                a += 1;
                b -= 1;
            } else {
                return false;
            }
        }
        return true;
    }
};


int main() {
    Solution so;
    cout << so.validPalindrome("cbbcc") << endl;


    return 0;
}