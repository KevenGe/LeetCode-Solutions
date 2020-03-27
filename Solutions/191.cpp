#include <iostream>
#include <vector>
using namespace std;

class Solution
{
public:
    int hammingWeight(uint32_t n)
    {
        int res = 0;
        uint32_t  n_tmp = 1;
        for (int i = 0; i < 32; ++i)
        {
            if (n & n_tmp)
            {
                res ++;
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