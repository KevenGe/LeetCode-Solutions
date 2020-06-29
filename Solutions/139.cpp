#include <iostream>
#include <vector>
#include <unordered_set>
#include <algorithm>
using namespace std;

// class Solution
// {
// private:
//     unordered_set<string> strSet;
//     int strMaxLength = 0;

// public:
//     bool wordBreak(string s, vector<string> &wordDict)
//     {
//         // add to strSet.
//         // get the max length of dict.
//         for (auto x : wordDict)
//         {
//             this->strSet.insert(x);
//             this->strMaxLength = max(this->strMaxLength, int(x.length()));
//         }

//         return findIt(s);
//     }

//     bool findIt(string s)
//     {
//         if (s == "")
//         {
//             return true;
//         }

//         for (int i = 1; i <= min(int(this->strMaxLength), int(s.length())); i++)
//         {
//             if (this->strSet.find(s.substr(0, i)) != this->strSet.end())
//             {
//                 if (findIt(s.substr(i)))
//                 {
//                     return true;
//                 }
//             }
//         }
//         return false;
//     }
// };

class Solution
{
public:
    bool wordBreak(string s, vector<string> &wordDict)
    {
        auto wordDictSet = unordered_set<string>();
        for (auto word : wordDict)
        {
            wordDictSet.insert(word);
        }

        auto dp = vector<bool>(s.size() + 1);
        dp[0] = true;
        for (int i = 1; i <= s.size(); ++i)
        {
            for (int j = 0; j < i; ++j)
            {
                if (dp[j] && wordDictSet.find(s.substr(j, i - j)) != wordDictSet.end())
                {
                    dp[i] = true;
                    break;
                }
            }
        }

        return dp[s.size()];
    }
};

int main()
{
    return 0;
}