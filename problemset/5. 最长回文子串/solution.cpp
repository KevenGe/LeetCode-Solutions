/*
 * LeetCode 5. 最长回文子串
 * Author: Keven Ge
 * Date: 2020-05-21
 */

#include <iostream>
#include <string>

using namespace std;


struct fanwei {
    int l;
    int r;

    fanwei(int l_, int r_) {
        l = l_;
        r = r_;
    }

    int getLength() {
        return this->r - this->l + 1;
    }
};

class Solution {
public:
    string longestPalindrome(string s) {
        if (s.length() == 0){
            return "";
        }


        int l = 0;
        int r = 0;
        int curLength = r - l + 1;
        for (int i = 0; i < s.size(); i++) {
            fanwei t1 = gets(s, i, i);
            if (curLength < t1.getLength()) {
                l = t1.l;
                r = t1.r;
                curLength = t1.getLength();
            }
        }

        for (int i = 0; i < s.size() - 1; i++) {
            fanwei t1 = gets(s, i, i + 1);
            if (curLength < t1.getLength()) {
                l = t1.l;
                r = t1.r;
                curLength = t1.getLength();
            }
        }

        return s.substr(l, (r - l + 1));
    }

    fanwei gets(string &s, int l, int r) {
        while (l >= 0 && r < s.length()) {
            if (s[l] == s[r]) {
                l--;
                r++;
            } else {
                break;
            }
        }
        return fanwei(l + 1, r - 1);
    }
};

int main() {
    Solution so;
    cout << so.longestPalindrome("ccc") << endl;
    return 0;
}
