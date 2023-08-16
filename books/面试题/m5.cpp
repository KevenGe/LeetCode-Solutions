//
// Created by lenovo on 2020/6/21.
//

/**
 * 剑指 Offer 05. 替换空格
 * @author Keven Ge
 */

#include <iostream>

using namespace std;

class Solution {
public:
    string replaceSpace(string s) {
        string ans;
        for (int i = 0; i < s.length(); ++i) {
            if(s[i] == ' '){
                ans.append("%20");
            }else{
                ans.append(s.substr(i, 1));
            }
        }
        return ans;
    }
};

int main() {
    Solution so;
    cout << so.replaceSpace("abc abc") << endl;
    return 0;
}
