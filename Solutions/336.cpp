//
// Created by lenovo on 2020-08-06.
//

#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <unordered_set>

using namespace std;

class Solution {
private:
    unordered_map<string, int> maps;
    unordered_set<string> used;

    bool isHuiWen(const string &str) {
        for (int i = 0; i < str.size() / 2; i++) {
            if (str[i] != str[str.size() - 1 - i]) {
                return false;
            }
        }
        return true;
    }

public:
    vector<vector<int>> palindromePairs(vector<string> &words) {
        /// Initialized The Answer
        vector<vector<int>> ans;

        /// Initialized unordered_map.
        vector<string> words2(words.begin(), words.end());
        for (int i = 0; i < words2.size(); i++) {
            reverse(words2[i].begin(), words2[i].end());
            maps.emplace(words2[i], i);
        }

        /// processing.
        for (int i = 0; i < words.size(); i++) {
            if (words[i].empty()) {
                continue;
            }

            string ts = words[i];
            reverse(ts.begin(), ts.end());
            if(used.find(ts) != used.end()){

                continue;
            }
            used.insert(words[i]);

            //
            /// form left to right
            for (int j = 0; j <= words[i].length(); j++) {
                if (this->isHuiWen(words[i].substr(0, j))) {
                    if (this->maps.find(words[i].substr(j)) != this->maps.end() &&
                        this->maps[words[i].substr(j)] != i) {
                        vector<int> tmp;
                        tmp.push_back(this->maps[words[i].substr(j)]);
                        tmp.push_back(i);
                        ans.push_back(tmp);
                    }
                }
            }

            /// form left to right
            for (int j = words[i].length(); j >= 0; j--) {
                if (this->isHuiWen(words[i].substr(j))) {
                    if (this->maps.find(words[i].substr(0, j)) != this->maps.end() &&
                        this->maps[words[i].substr(0, j)] != i) {
                        vector<int> tmp;
                        tmp.push_back(i);
                        tmp.push_back(this->maps[words[i].substr(0, j)]);
                        ans.push_back(tmp);
                    }
                }
            }
        }

        return ans;
    }
};

void testSolution() {
    vector<string> t;
    t.emplace_back("ab");
    t.emplace_back("ba");
    t.emplace_back("abc");
    t.emplace_back("cba");

    Solution so;
    for (auto x:so.palindromePairs(t)) {
        cout << x[0] << " --> " << x[1] << endl;
    }
}

int main() {
    testSolution();
    return 0;
}
