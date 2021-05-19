#include <iostream>

using namespace std;

class Solution {
public:
    int trailingZeroes(int n) {
        int ans = 0;
        for (int i = 5; i <= n; i++) {
            int j = i;
            while (j % 5 == 0) {
                ans += 1;
                j = j / 5;
            }
        }
        return ans;
    }
};

void runTest(){
    Solution so;
    cout << so.trailingZeroes(30) << endl;
}

int main() {
    runTest();
    return 0;
}








