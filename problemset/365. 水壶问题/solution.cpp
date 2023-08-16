#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution
{
public:
    bool canMeasureWater(int x, int y, int z)
    {
        if (x + y < z)
        {
            return false;
        }
        else if (x == 0 || y == 0)
        {
            return z == 0 || x + y == z;
        }
        return z % this->gcd(x, y) == 0;
    }
    int gcd(int x, int y)
    {
        for (int i = min(x, y); i >= 1; --i)
        {
            if (x % i == 0 && y % i == 0)
            {
                return i;
            }
        }
        return -1;
    }
};

int main()
{
    return 0;
}