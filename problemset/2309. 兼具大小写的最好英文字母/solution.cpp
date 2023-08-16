#include <iostream>
#include <map>
#include <memory>
#include <string>

using namespace std;

class Solution {
 public:
  string greatestLetter(string s) {
    auto betterLetter = make_unique<int[]>(26);

    for (int i = 0; i < 26; i++) {
      betterLetter[i] = 0;
    }

    for (const char& ch : s) {
      if (isupper(ch) && betterLetter[ch - 'A'] / 10 != 1) {
        betterLetter[ch - 'A'] += 10;
      } else if (islower(ch) && betterLetter[ch - 'a'] % 10 != 1) {
        betterLetter[ch - 'a'] += 1;
      }
    }

    for (int i = 25; i >= 0; i--) {
      if (betterLetter[i] == 11) {
        string ans = "";
        ans.push_back(char(i + 'A'));
        return ans;
      }
    }

    return "";
  }
};