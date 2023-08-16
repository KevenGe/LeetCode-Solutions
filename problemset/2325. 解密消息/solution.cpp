#include <map>
#include <string>

using namespace std;

class Solution {
 public:
  string decodeMessage(string key, string message) {
    map<char, char> convertMap = [](const string& key) {
      map<char, char> cm;
      int kiter = 0;
      for (const char ch : key) {
        if (int(ch) >= 'a' && int(ch) <= 'z') {
          if (cm.find(ch) == cm.end()) {
            cm[ch] = char(kiter + 'a');
            kiter += 1;
          }
        }
      }
      return cm;
    }(key);

    string ans;
    for (const char ch : message) {
      if (int(ch) >= 'a' && int(ch) <= 'z') {
        ans.push_back(convertMap[ch]);
      } else {
        ans.push_back(ch);
      }
    }
    return ans;
  }
};