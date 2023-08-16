#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

class Solution
{
public:
    string addStrings(string num1, string num2)
    {
        if (num1 == "0")
        {
            return num2;
        }
        if (num2 == "0")
        {
            return num1;
        }

        string ans = "";
        while(num1.length() > num2.length())
        {
            num2 = '0' + num2;
        }
        while(num1.length() < num2.length())
        {
            num1 = '0' + num1;
        }

        int adds = 0;
        for (int i = num1.length() - 1; i >= 0; --i)
        {
            int tmp = (num1[i] - '0') + (num2[i] - '0') + adds;
            ans = char(tmp % 10 + '0') + ans;
            adds = tmp / 10;
        }
        if (adds)
        {
            ans = char(adds + '0') + ans;
        }
        return ans;
    }
};

int main()
{
    Solution so;
    cout << so.addStrings("999", "111");
    return 0;
}