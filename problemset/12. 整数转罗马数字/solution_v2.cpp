#include <iostream>
#include <string>
using namespace std;

class Solution
{
public:
    string intToRoman(int num)
    {
        string tmp = "";
        while (num >= 1000)
        {
            tmp += "M";
            num -= 1000;
        }
        if (num >= 900)
        {
            tmp += "CM";
            num -= 900;
        }

        if (num >= 500)
        {
            tmp += "D";
            num -= 500;
        }
        if (num >= 400)
        {
            tmp += "CD";
            num -= 400;
        }

        while (num >= 100)
        {
            tmp += "C";
            num -= 100;
        }
        if (num >= 90)
        {
            tmp += "XC";
            num -= 90;
        }

        if (num >= 50)
        {
            tmp += "L";
            num -= 50;
        }
        if (num >= 40)
        {
            tmp += "XL";
            num -= 40;
        }

        while (num >= 10)
        {
            tmp += "X";
            num -= 10;
        }
        if (num >= 9)
        {
            tmp += "IX";
            num -= 9;
        }

        if (num >= 5)
        {
            tmp += "V";
            num -= 5;
        }
        if (num >= 4)
        {
            tmp += "IV";
            num -= 4;
        }

        while (num > 0)
        {
            tmp += "I";
            num -= 1;
        }

        return tmp;
    }
};

int main()
{
    Solution so;
    // cout << so.intToRoman(6) << endl;
    for (int i = 10; i >= 0; --i)
    {
        int n;
        cin >> n;
        cout << so.intToRoman(n) << endl;
    }
    return 0;
}