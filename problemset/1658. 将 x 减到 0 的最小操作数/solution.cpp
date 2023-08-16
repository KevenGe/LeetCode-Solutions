#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

class Solution {
 public:
  int minOperations(vector<int>& nums, int x) {
    // step 1
    int sum = 0;
    for (const int& num : nums) {
      sum += num;
    }
    sum -= x;

    // step 2
    int ans = -1;

    int l = 0;
    int r = 0;

    while (true) {
      if (sum == 0) {
        ans = max(ans, r - l);

        if (r < nums.size()) {
          sum -= nums[r];
          r += 1;
        } else {
          break;
        }
      } else if (sum > 0) {
        while (r + 1 <= nums.size() && sum > 0) {
          sum -= nums[r];
          r += 1;
        }
      } else if (sum < 0) {
        while (l < r && sum < 0) {
          sum += nums[l];
          l += 1;
        }
      }

      if ((r == nums.size() && sum > 0) || (sum < 0 && l == r)) {
        break;
      }
    }

    // step 3
    return ans == -1 ? -1 : nums.size() - ans;
  }
};

int main() {
  // Solution so;
  // vector<int> nums{1241, 8769, 9151, 3211, 2314, 8007, 3713, 5835, 2176,
  // 8227,
  //                  5251, 9229, 904,  1899, 5513, 7878, 8663, 3804, 2685,
  //                  3501, 1204, 9742, 2578, 8849, 1120, 4687, 5902, 9929,
  //                  6769, 8171, 5150, 1343, 9619, 3973, 3273, 6427, 47, 8701,
  //                  2741, 7402, 1412, 2223, 8152, 805,  6726, 9128, 2794,
  //                  7137, 6725, 4279, 7200, 5582, 9583, 7443, 6573, 7221,
  //                  1423, 4859, 2608, 3772, 7437, 2581, 975,  3893, 9172, 3,
  //                  3113, 2978, 9300, 6029, 4958, 229,  4630, 653,  1421,
  //                  5512, 5392, 7287, 8643, 4495, 2640, 8047, 7268, 3878,
  //                  6010, 8070, 7560, 8931, 76,   6502, 5952, 4871, 5986,
  //                  4935, 3015, 8263, 7497, 8153, 384,  1136};
  // cout << so.minOperations(nums, 894887480) << endl;

  // Solution so;
  // vector<int> nums{8828,  9581,  49,   9818, 9974, 9869, 9991, 10000,
  //                  10000, 10000, 9999, 9993, 9904, 8819, 1231, 6309};
  // cout << so.minOperations(nums, 134365) << endl;

  Solution so;
  vector<int> nums{500, 1, 4, 2, 3};
  cout << so.minOperations(nums, 500) << endl;

  return 0;
}