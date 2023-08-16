#include <iostream>
#include <limits.h>
using namespace std;

class Solution
{
public:
    int reverse(int x)
    {
        int res = 0;
        while (x)
        {
            int n = x % 10;
            x = x / 10;

            if (res > INT_MAX / 10 || (res == INT_MAX / 10 && x > INT_MAX % 10))
            {
                res = -1;
                break;
            }
            if (res < INT_MIN / 10 || (res == INT_MIN / 10 && x < INT_MIN % 10))
            {
                res = -1;
                break;
            }

            res = res *10 + n;
        }
        return res;
    }
};

int main()
{
    return 0;
}