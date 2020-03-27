#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Solution
{
public:
    vector<string> ans;
    int n;
    string digitss;
    vector<string> letterCombinations(string digits)
    {
        n = digits.length();
        if (n == 0)
        {
            return ans;
        }
        digitss = digits;
        helper(0, "");
        return ans;
    }
    void helper(int i, string tmp)
    {
        if (i == n)
        {
            ans.push_back(tmp);
        }
        else
        {
            string basic = "";
            switch (digitss[i])
            {
            case '2':
                basic = "abc";
                break;
            case '3':
                basic = "def";
                break;
            case '4':
                basic = "ghi";
                break;
            case '5':
                basic = "jkl";
                break;
            case '6':
                basic = "mno";
                break;
            case '7':
                basic = "pqrs";
                break;
            case '8':
                basic = "tuv";
                break;
            case '9':
                basic = "wxyz";
                break;
            default:
                basic = "";
                break;
            }

            for (char ch : basic)
            {
                helper(i + 1, tmp + ch);
            }
        }
    }
};

int main()
{
    Solution so;

    for (string x : so.letterCombinations("7"))
    {
        cout << x << endl;
    }
    return 0;
}