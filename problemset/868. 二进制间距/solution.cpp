#include <algorithm>

using namespace std;

class Solution {
 public:
  int binaryGap(int n) {
    int maxDistance = 0;
    int prevIdx = -1;
    for (int i = 0; i < 32; i++) {
      if (n & (1 << i)) {
        if (prevIdx == -1) {
          prevIdx = i;
        } else {
          maxDistance = max(maxDistance, i - prevIdx);
          prevIdx = i;
        }
      }
    }

    return maxDistance;
  }
};