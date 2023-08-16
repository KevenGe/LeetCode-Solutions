#include <iostream>
#include <limits.h>
using namespace std;

class Solution
{
public:
    bool isPalindrome(int x)
    {
        if ((x > 0 && x % 10 != 0) || x==0)
        {
            int x_reverse = 0;
            while (x_reverse < x)
            {
                x_reverse = x_reverse * 10 + x % 10;
                x = x / 10;
            }
            return x == x_reverse || x == x_reverse / 10;
        }
        return false;
    }
};

int main()
{
    Solution so;
    cout << so.isPalindrome(0) << endl;
    return 0;
}
