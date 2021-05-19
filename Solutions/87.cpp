#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution
{
    string s1;
    string s2;
    vector<vector<int>> dp1;
    vector<vector<int>> dp2;

public:
    bool isScramble(string s1, string s2)
    {
        this->s1 = s1;
        this->s2 = s2;
        dp1.assign(32, vector<int>(26, 0));
        dp2.assign(32, vector<int>(26, 0));

        dp1[1][s1[0] - 'a'] += 1;
        dp2[1][s2[0] - 'a'] += 1;

        for (int i = 1; i <= s1.length(); i++)
        {
            for (int j = 0; j < 26; j++)
            {
                dp1[i + 1][j] = dp1[i][j];
                dp2[i + 1][j] = dp2[i][j];
            }

            dp1[i + 1][s1[i] - 'a'] += 1;
            dp2[i + 1][s2[i] - 'a'] += 1;
        }

        return isOK(0, s1.length());
    }

    bool isOK(int s, int d)
    {
        if (s == d || s + 1 == d)
        {
            return true;
        }
        else if (s + 2 == d)
        {
            bool t = (this->s1[s] == this->s2[s] && this->s1[s + 1] == this->s2[s + 1]) ||
                     (this->s1[s] == this->s2[s + 1] && this->s1[s + 1] == this->s2[s]);
            return t;
        }
        else
        {
            for (int i = s + 1; i <= d; i++)
            {
                bool isSame = true;
                for (int j = 0; j < 26; j++)
                {
                    if ((this->dp1[i][j] - this->dp1[s][j]) != (this->dp2[i][j] - this->dp2[s][j]))
                    {
                        isSame = false;
                        break;
                    }
                }

                bool t = this->isOK(i, d);
                bool t2 = this->isOK(0, i);
                if (isSame && t && t2)
                {
                    return true;
                }
            }
            return false;
        }
    }
};

int main()
{

    Solution so;
    cout << so.isScramble("rgeat", "great") << endl;
    return 0;
}