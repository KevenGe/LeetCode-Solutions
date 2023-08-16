#include <iostream>

using namespace std;

class Solution
{
public:
    bool isPowerOfTwo(int n)
    {
        int tmp = 1;
        for (int i = 0; i < 31; i++)
        {
            if (n == tmp)
            {
                return true;
            }
            tmp = tmp << 1;
        }
        return false;
    }
};

int main()
{
    return 0;
}