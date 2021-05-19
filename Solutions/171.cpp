//
// Created by lenovo on 2020-09-29.
//

#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    int titleToNumber(string s) {
        int ans = 0;
        for (int i = 0; i < s.length(); i++) {
            int num = s[i] - 'A' + 1;
            ans = ans * 26 + num;
        }
        return ans;
    }
};

int main() {
    return 0;
}