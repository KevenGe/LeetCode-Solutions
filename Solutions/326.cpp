#include <iostream>

using namespace std;

class Solution {
public:
    static bool isPowerOfThree(int n) {
        return n > 0 && 1162261467%n == 0;
    }
};

int main() {
    int t;
    for (int i = 1; i < 30; i++) {
        t = pow(3, i);
        cout << "# " << i << ": " << t << endl;
    }
    return 0;
}

