#include <iostream>

using namespace std;

class Solution {
public:
    int hammingDistance(int x, int y) {
        uint32_t t = 1;
        int res = 0;
        for (int i = 0; i < 32; i++) {
            if ((x & t) ^ (y & t)){
                res ++;
            }
            t = t << 1;
        }
        return res;
    }
};

int main() {
    return 0;
}