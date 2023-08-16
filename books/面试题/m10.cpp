/**
 * @file m10.cpp
 * @author your name (you@domain.com)
 * @brief 
 * @version 0.1
 * @date 2020-08-12
 * 
 * @copyright Copyright (c) 2020
 * 
 */

#include <iostream>
using namespace std;

/**
 * @brief  NoThing.
 * 
 */
class Solution
{
private:
    int mod = 1000000007;
public:
    int fib(int n)
    {
        if (n == 0)
        {
            return 0;
        }
        else if (n == 1)
        {
            return 1;
        }
        else
        {
            int a = 0;
            int b = 1;
            int c = 0;
            for (int j = 2; j <= n; j++)
            {
                c = (a + b) % mod;
                a = b;
                b = c;
            }
            return b;
        }
    }
};

int main()
{
    return 0;
}