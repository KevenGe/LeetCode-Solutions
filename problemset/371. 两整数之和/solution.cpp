//
// Created by lenovo on 2020-09-30.
//

#include <iostream>

using namespace std;

class Solution {
public:
    int getSum(int a, int b) {
        unsigned ans = 0;
        unsigned add = 0;
        do {
            ans = unsigned (a) ^ unsigned (b);
            add = unsigned (a & b);
            a = ans;
            b = add << 1;
        } while (add != 0);
        return ans;
    }
};

void runTest() {
    Solution so;
    cout << so.getSum(1, 1) << endl;
}

int main() {
    runTest();
    return 0;
}