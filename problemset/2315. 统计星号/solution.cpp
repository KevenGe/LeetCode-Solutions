#include <iostream>
#include <string>

using namespace std;

class Solution {
 public:
  int countAsterisks(string s) {
    int starCount = 0;
    int startCount = 0;
    for (const char ch : s) {
      if (ch == '|') {
        startCount = 1 - startCount;
      } else if (startCount == 0 && ch == '*') {
        starCount += 1;
      }
    }
    return starCount;
  }
};