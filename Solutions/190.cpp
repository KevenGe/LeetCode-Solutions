#include <iostream>
#include <vector>
using namespace std;

class Solution
{
public:
    uint32_t reverseBits(uint32_t n)
    {
        uint32_t res = 0;
        uint32_t res_tmp = 1;
        uint32_t n_tmp = 1;
        for (int i = 0; i < 32; ++i)
        {
            if (n & n_tmp)
            {
                res = res | (res_tmp << (31 - i));
            }
            n_tmp = n_tmp << 1;
        }
        return res;
    }
};

int main()
{
    return 0;
}
