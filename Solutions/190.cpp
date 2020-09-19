#include <iostream>

using namespace std;

class Solution {
public:
    static uint32_t reverseBits(uint32_t n) {
        uint32_t t = 1;
        uint32_t ans = 0;
        uint32_t at = 0 | t << 31;
        for (int i = 0; i < 32; i++) {
            if (t & n) {
                ans = ans | at;
            }
            t = t << 1;
            at = at >> 1;
        }
        return ans;
    }
};

int main() {
    return 0;
}