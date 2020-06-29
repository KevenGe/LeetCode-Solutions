/******************************************************************************

    面试题64

    Author: Keven Ge
    Date: 2020-06-02

******************************************************************************/

#include <iostream>
using namespace std;

/******************************************************************************
class Solution
{
public:
    int sumNums(int n)
    {
        n && (n += sumNums(n - 1));
        return n;
    }
};
******************************************************************************/

class Solution
{
public:
    int sumNums(int n)
    {
        int ans = 0;
        int t = 1;
        int a = n;
        int b = n + 1;

        (b & t) && (ans += a);
        t = t << 1;
        a = a << 1;

        (b & t) && (ans += a);
        t = t << 1;
        a = a << 1;

        (b & t) && (ans += a);
        t = t << 1;
        a = a << 1;

        (b & t) && (ans += a);
        t = t << 1;
        a = a << 1;

        (b & t) && (ans += a);
        t = t << 1;
        a = a << 1;

        (b & t) && (ans += a);
        t = t << 1;
        a = a << 1;

        (b & t) && (ans += a);
        t = t << 1;
        a = a << 1;

        (b & t) && (ans += a);
        t = t << 1;
        a = a << 1;

        (b & t) && (ans += a);
        t = t << 1;
        a = a << 1;

        (b & t) && (ans += a);
        t = t << 1;
        a = a << 1;

        (b & t) && (ans += a);
        t = t << 1;
        a = a << 1;

        (b & t) && (ans += a);
        t = t << 1;
        a = a << 1;

        (b & t) && (ans += a);
        t = t << 1;
        a = a << 1;

        (b & t) && (ans += a);
        t = t << 1;
        a = a << 1;

        ans = ans >> 1;

        return ans;
    }
};

int main()
{
    Solution so;
    cout << so.sumNums(3) << endl;
    return 0;
}
