// 丑数 就是只包含质因数 2、3 和/或 5 的正整数。

#include <iostream>

using namespace std;

class Solution
{
public:
    bool isUgly(int n)
    {
        if (n <= 0)
        {
            return false;
        }
        if (n == 1)
        {
            return true;
        }
        else if (n % 2 == 0)
        {
            return isUgly(n / 2);
        }
        else if (n % 3 == 0)
        {
            return isUgly(n / 3);
        }
        else if (n % 5 == 0)
        {
            return isUgly(n / 5);
        }
        else
        {
            return false;
        }
    }
};

int main()
{
    Solution so;
    cout << so.isUgly(1) << endl;
    return 0;
}