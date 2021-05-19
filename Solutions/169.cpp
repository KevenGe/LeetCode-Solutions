#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int majorityElement(vector<int> &nums) {
        int candi = 0;
        int count = 0;
        for (auto num:nums) {
            if (count == 0) {
                candi = num;
                count = 1;
            } else {
                if (candi == num) {
                    count += 1;
                } else {
                    count -= 1;
                }
            }
        }
        return candi;
    }
};

int main() {
    return 0;
}
