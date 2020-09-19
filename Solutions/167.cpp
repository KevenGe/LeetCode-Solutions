/**
 * @brief 求两个数值
 */

#include <algorithm>
#include <vector>

using namespace std;


class Solution {
public:
    static vector<int> twoSum(vector<int> &numbers, int target) {
        int l = 0;
        int r = numbers.size() - 1;
        vector<int> res;
        while (l < r) {
            if (numbers[l] + numbers[r] == target) {
                res.push_back(l+1);
                res.push_back(r+1);
                return res;
            } else if (numbers[l] + numbers[r] > target) {
                r--;
            } else {
                l++;
            }
        }
        return res;
    }
};

int main() {
    return 0;
}