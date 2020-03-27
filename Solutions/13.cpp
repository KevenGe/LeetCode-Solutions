#include <iostream>
using namespace std;

class Solution
{
public:
    int romanToInt(string s)
    {
        int ans = 0;
        for (int i = 0; i < s.length(); ++i)
        {
            if (s[i] == 'M')
            {
                if (i - 1 >= 0 && s[i - 1] == 'C')
                {
                    ans += 800;
                }
                else
                {
                    ans += 1000;
                }
            }
            else if (s[i] == 'D')
            {
                if (i - 1 >= 0 && s[i - 1] == 'C')
                {
                    ans += 300;
                }
                else
                {
                    ans += 500;
                }
            }
            else if (s[i] == 'C')
            {
                if (i - 1 >= 0 && s[i - 1] == 'X')
                {
                    ans += 80;
                }
                else
                {
                    ans += 100;
                }
            }
            else if (s[i] == 'L')
            {
                if (i - 1 >= 0 && s[i - 1] == 'X')
                {
                    ans += 30;
                }
                else
                {
                    ans += 50;
                }
            }
            else if (s[i] == 'X')
            {
                if (i - 1 >= 0 && s[i - 1] == 'I')
                {
                    ans += 8;
                }
                else
                {
                    ans += 10;
                }
            }
            else if (s[i] == 'V')
            {
                if (i - 1 >= 0 && s[i - 1] == 'I')
                {
                    ans += 3;
                }
                else
                {
                    ans += 5;
                }
            }
            else
            {
                ans += 1;
            }
        }
        return ans;
    }
};

int main()
{
    Solution so;
    while(true)
    {
        string ans="";
        cin >> ans;
        cout << so.romanToInt(ans) << endl;
    }
    return 0;
}