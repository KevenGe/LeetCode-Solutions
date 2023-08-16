#include <iostream>
#include <limits.h>
#include <string>
#include <ctype.h>
using namespace std;

class Solution
{
public:
    int myAtoi(string str)
    {
        int res = 0;
        int state = 1;
        bool fu = false;
        for (int i = 0; i < str.length(); ++i)
        {
            if (state == 1)
            {
                if (str[i] == ' ')
                {
                    continue;
                }
                else if (str[i] == '+')
                {
                    state = 2;
                }
                else if (str[i] <= '9' && str[i] >= '0')
                {
                    res = res * 10 + int(str[i] - '0');
                    state = 2;
                }
                else if (str[i] == '-' && i + 1 < str.length() && str[i + 1] <= '9' && str[i + 1] >= '0')
                {
                    res = 0 - int(str[i + 1] - '0');
                    i++;
                    state = 2;
                    fu = true;
                }
                else
                {
                    break;
                }
            }
            else if (state == 2)
            {
                if (str[i] <= '9' && str[i] >= '0')
                {
                    int num = int(str[i] - '0');
                    if (fu)
                    {
                        num = -num;
                    }

                    if (res > INT_MAX / 10 || (res == INT_MAX / 10 && num > INT_MAX % 10))
                    {
                        res = INT_MAX;
                        break;
                    }
                    if (res < INT_MIN / 10 || (res == INT_MIN / 10 && num < INT_MIN % 10))
                    {
                        res = INT_MIN;
                        break;
                    }
                    res = res * 10 + num;
                }
                else
                {
                    break;
                }
            }
        }
        return res;
    }
};

int main()
{
    Solution so;
    cout << so.myAtoi("2147483648") << endl;
    return 0;
}