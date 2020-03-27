#include <iostream>
#include <string>
using namespace std;

class Solution
{
public:
    string convert(string s, int numRows)
    {
        if(s.length() == 1)
            return s;
        string res = "";
        
        int n = numRows * 2 - 2;
        for (int i = 0; i < numRows; ++i)
        {
            int index = i;
            bool flag = true; // 用来标记是不是N的左部分
            while (index < s.length())
            {
                res += s[index];

                if (i == 0 || i == numRows - 1)
                {
                    index += n;
                }
                else
                {
                    if (flag)
                    {
                        index += n - 2 * i;
                        flag = false;
                    }
                    else
                    {
                        index += 2 * i;
                        flag = true;
                    }
                }
            }
        }
        return res;
    }
};

int main()
{
    Solution so;
    cout << so.convert("A", 1) << endl;
    return 0;
}