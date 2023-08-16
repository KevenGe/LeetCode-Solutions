#include <iostream>
#include <climits>
#include <stdint.h>

using namespace std;

class Solution {
public:
    int hammingWeight(uint32_t n) {
        uint32_t t = 1;
        int ans = 0;
        for(int i=0;i<32;++i){
            if(n & t){
                ans ++;
            }
            t = t << 1;
        }
        return ans;
    }
};

int main() {
    return 0;
}