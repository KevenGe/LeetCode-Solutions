//
// Created by lenovo on 2020/6/23.
//
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    string addBinary(string a, string b) {
        // The max length now.
        int len = max(a.length(), b.length());

        // swap a and b.
        if (a.length() < b.length()) {
            while(a.length() != len){
                a.insert(0, "0");
            }
        }else{
            while(b.length() != len){
                b.insert(0, "0");
            }
        }

        string ans; // answer for the end.
        int jin = 0; // In
        for (int i = len - 1; i >= 0; i--) {
            int t = (a[i] - '0') + (b[i] - '0') + jin;

            if (t == 0 || t == 1) {
                jin = 0;
                ans.insert(0, string(1, char(t + '0')));
            }else if(t == 2 || t == 3){
                jin = 1;
                ans.insert(0, string(1, char(t+'0' -2)));
            }
        }
        if(jin == 1){
            ans.insert(0, "1");
        }

        return ans;
    }
};

int main() {
    Solution so;
    cout << so.addBinary("11", "1") << endl;

    return 0;
}