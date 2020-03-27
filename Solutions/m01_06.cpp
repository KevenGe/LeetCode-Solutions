#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

class Solution
{
public:
    string compressString(string S)
    {
        string res = "";
        char bef_ch = '#';
        int bef_num = 1;
        for (int i = 0; i < S.length(); ++i)
        {
            if (S[i] == bef_ch)
            {
                bef_num++;
            }
            else
            {
                res += bef_ch + getss(bef_num);
                bef_ch = S[i];
                bef_num = 1;
            }
        }

        res += bef_ch + getss(bef_num);

        res = res.substr(2);

        if(res.length() < S.length())
            return res;
        else
            return S;

        return S;
    }

    string getss(int x)
    {
        string res = "";
        while (x)
        {
            int t = x % 10;
            x = x / 10;
            res = char(t + '0') + res;
        }
        return res;
    }
};

int main()
{
    Solution so;
    cout << so.compressString("aabbbccccc") << endl;
    return 0;
}