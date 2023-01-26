#include <iostream>
#include <sstream>
#include <string>

using namespace std;

class Solution {
 public:
  string getSmallestString(int n, int k) {
    if (n > k) {
      // it can't happened
      return "";
    }

    int zNum = (k - n) / 25;
    int bZ = (k - n) % 25;

    string ans = "";
    for (int i = 0; i < n; i++) {
      if (i > n - zNum - 1) {
        ans.push_back('z');
      } else if (i == n - zNum - 1) {
        ans.push_back(char(('a' - 1) + bZ + 1));
      } else {
        ans.push_back('a');
      }
    }

    return ans;
  }
};