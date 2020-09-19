//
// Created by lenovo on 2020-08-24.
//

#include <iostream>

using namespace std;

class Solution {
public:
    bool repeatedSubstringPattern(string s) {
        int n = s.length();
        for (int i = 1; i < n; i++) {
            if (n % i == 0) {
                string t = s.substr(0, i);
                if(isit(s, t)){
                    return true;
                }
            }
        }
        return false;
    }

    /**
     * 判断t是不是s的循环子串
     *
     * @param s
     * @param t
     * @return
     */
    bool isit(const string & s, const string & t){
        int sn = s.length();
        int tn = t.length();

        for(int i = 0; i < sn; i += tn){
            if(s.substr(i, tn) != t) {
                return false;
            }
        }
        return true;
    }
};

int main() {
    return 0;
}