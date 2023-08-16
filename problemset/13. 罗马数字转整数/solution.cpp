#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    int romanToInt(string s) {
        if (s.empty()) {
            return 0;
        } else {
            char ch = s[0];
            int val;
            int si = 1;
            if (ch == 'M') {
                val = 1000;
            } else if (ch == 'D') {
                val = 500;
            } else if (ch == 'C') {
                if (s.length() > 1) {
                    char ch2 = s[1];
                    if (ch2 == 'M') {
                        val = 900;
                        si = 2;
                    } else if (ch2 == 'D') {
                        val = 400;
                        si = 2;
                    } else {
                        val = 100;
                    }
                } else {
                    val = 100;
                }
            } else if (ch == 'L') {
                val = 50;
            } else if (ch == 'X') {
                if (s.length() > 1) {
                    char ch2 = s[1];
                    if (ch2 == 'C') {
                        val = 90;
                        si = 2;
                    } else if (ch2 == 'L') {
                        val = 40;
                        si = 2;
                    } else {
                        val = 10;
                    }
                } else {
                    val = 10;
                }
            } else if (ch == 'V') {
                val = 5;
            } else if (ch == 'I') {
                if (s.length() > 1) {
                    char ch2 = s[1];
                    if (ch2 == 'X') {
                        val = 9;
                        si = 2;
                    } else if (ch2 == 'V') {
                        val = 4;
                        si = 2;
                    } else {
                        val = 1;
                    }
                } else {
                    val = 1;
                }
            }
            return val + romanToInt(s.substr(si));
        }
    }
};

int main() {
    return 0;
}