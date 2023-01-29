#include <iostream>
#include <vector>

using namespace std;

// /**
//  * @brief 奇数偶数分开计算，复杂度稍高
//  *
//  */
// class Solution {
//  public:
//   int waysToMakeFair(vector<int>& nums) {
//     // step 1
//     vector<int> oddCum(nums.size() + 1, 0);
//     vector<int> evenCum(nums.size() + 1, 0);
//     for (int i = 0; i < nums.size(); i++) {
//       if (i % 2 == 0) {
//         evenCum[i + 1] = evenCum[i] + nums[i];
//         oddCum[i + 1] = oddCum[i];
//       } else {
//         evenCum[i + 1] = evenCum[i];
//         oddCum[i + 1] = oddCum[i] + nums[i];
//       }
//     }

//     // step 2
//     int validOps = 0;
//     for (int i = 0; i < nums.size(); i++) {
//       int evenSum =
//           (evenCum[i] - evenCum[0]) + (oddCum[nums.size()] - oddCum[i + 1]);
//       int oddSum =
//           (oddCum[i] - oddCum[0]) + (evenCum[nums.size()] - evenCum[i + 1]);

//       if (evenSum == oddSum) {
//         validOps += 1;
//       }
//     }

//     // step 3
//     return validOps;
//   }
// };

class Solution {
 public:
  int waysToMakeFair(vector<int>& nums) {
    // step 1
    int oddSum = 0;
    int evenSum = 0;
    for (int i = 0; i < nums.size(); i += 1) {
      if (i % 2 == 0) {
        evenSum += nums[i];
      } else {
        oddSum += nums[i];
      }
    }

    // step 2
    int validOps = 0;
    int oddCum = 0;
    int evenCum = 0;
    for (int i = 0; i < nums.size(); i++) {
      int afterDeleteEvenSum = 0;
      int afterDeleteOddSum = 0;

      if (i % 2 == 0) {
        afterDeleteEvenSum = evenCum + (oddSum - oddCum);
        afterDeleteOddSum = oddCum + (evenSum - evenCum - nums[i]);

        evenCum += nums[i];
      } else {
        afterDeleteEvenSum = evenCum + (oddSum - oddCum - nums[i]);
        afterDeleteOddSum = oddCum + (evenSum - evenCum);

        oddCum += nums[i];
      }

      if (afterDeleteEvenSum == afterDeleteOddSum) {
        validOps += 1;
      }
    }

    // step 3
    return validOps;
  }
};