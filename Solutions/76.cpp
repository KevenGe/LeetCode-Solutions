#include <iostream>
#include <string>
#include <unordered_map>
#include <climits>

using namespace std;

class Solution {
private:
    unordered_map<char, int> smaps;
    unordered_map<char, int> tmaps;

    /**
     *
     * @return
     */
    bool check() {
        for (auto iter = tmaps.begin(); iter != tmaps.end(); iter++) {
            if (!(smaps.find(iter->first) != smaps.end() && smaps.at(iter->first) >= tmaps.at(iter->first))) {
                return false;
            }
        }
        return true;
    }

    /**
     * @brief initial
     */
    void init(string &s, string &t) {
        for (string::iterator iter = t.begin(); iter != t.end(); iter++) {
            if (tmaps.find(*iter) != tmaps.end()) {
                tmaps[*iter]++;
            } else {
                tmaps.insert(unordered_map<char, int>::value_type(*iter, 1));
            }
        }
    }

public:
    string minWindow(string s, string t) {
        init(s, t);
        int l = 0, r = 0;
        string ans;
        int curLen = INT_MAX;

        while (l <= r) {
            if (check()) {
                if (r - l < curLen) {
                    ans = s.substr(l, r - l);
                    curLen = r - l ;
                }
                smaps[s[l]] --;
                l++;
            } else {
                if(smaps.find(s[r]) != smaps.end()){
                    smaps[s[r]]++;
                }else{
                    smaps.insert(unordered_map<char, int>::value_type(s[r], 1));
                }
                r++;
                if(r > s.length()){
                    break;
                }
            }
        }
        return ans;
    }
};

int main() {
    Solution so;
    cout << so.minWindow("ABCDEFA", "") << endl;
    return 0;
}
