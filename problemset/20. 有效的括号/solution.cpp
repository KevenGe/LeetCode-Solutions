#include <iostream>
#include <stack>
#include <string>

using namespace std;

class Solution {
public:
    bool isValid(string s) {
        stack<char> sts;
        for (char i : s) {
            if (i == '(' || i == '{' || i == '[') {
                sts.push(i);
            } else {
                if (sts.empty()) {
                    return false;
                } else {
                    if (!( (i == ')' && sts.top()=='(') || (i == '}' && sts.top()=='{') || (i == ']' && sts.top()=='[') )){
                        return false;
                    }
                    sts.pop();
                }
            }
        }
        return sts.empty();
    }
};

int main() {
    return 0;
}