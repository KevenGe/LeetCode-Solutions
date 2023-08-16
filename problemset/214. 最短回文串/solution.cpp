//
// Created by lenovo on 2020-08-29.
//

#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    string shortestPalindrome(string s) {
        int mod = 1000000007;
        int base = 131;
        int left = 0;
        int right = 0;
        int mul = 1;
        int best = -1;
        for (int i = 0; i < s.length(); i++) {
            left = ((long long) left * base + s[i]) % mod;
            right = (right + (long long) mul * s[i]) % mod;
            mul = ((long long) mul * base) % mod;
//            cout <<"left=" << left <<", right=" << right << endl;
            if (left == right) {
                best = i;
//                cout << "best = " << best << endl;
            }
        }

        string s2 = s.substr(best + 1);
        reverse(s2.begin(), s2.end());
        return s2 + s;
    }
};

int main() {
    Solution s;
    cout << s.shortestPalindrome("abc") << endl;

//    string t = "abcde";
//    cout << t.substr(1) << endl;
//    cout << t.substr(1,2) << endl;
    return 0;
}
