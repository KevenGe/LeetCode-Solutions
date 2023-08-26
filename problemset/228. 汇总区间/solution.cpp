#include <algorithm>
#include <iostream>
#include <queue>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
  vector<string> summaryRanges(vector<int> &nums) {
    vector<string> ans;

    {
      int startIdx = 0;
      while (startIdx < nums.size()) {
        int endNum = nums[startIdx];
        int endIdx = startIdx;
        while (endIdx + 1 < nums.size() && nums[endIdx + 1] == endNum + 1) {
          endIdx += 1;
          endNum += 1;
        }

        if (endIdx == startIdx) {
          ans.push_back(to_string(nums[startIdx]));
        } else {
          ans.push_back(to_string(nums[startIdx]) + "->" +
                        to_string(nums[endIdx]));
        }
        startIdx = endIdx + 1;
      }
    }

    return ans;
  }
};