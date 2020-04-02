#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;


// leetcode 1111
// 栈
class Solution {
public:
    vector<int> maxDepthAfterSplit(string seq) {
        int depth = 0;
        vector<int> ans;
        for (char &ch:seq) {
            if (ch == '(') {
                ans.push_back(depth % 2);
                depth++;
            } else {
                depth--;
                ans.push_back(depth % 2);
            }
        }
        return ans;
    }
};


int main() {
    return 0;
}
