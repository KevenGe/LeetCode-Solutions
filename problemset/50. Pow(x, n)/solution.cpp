/*
 * LeetCode 50. Pow(x, n)
 * Author: Keven Ge
 * Date: 2020-05-11
 */

#include <iostream>
#include <cmath>

using namespace std;


//class Solution {
//public:
//    double myPow(double x, int n) {
//        return pow(x,n);
//    }
//};


class Solution {
public:
    /*
     * 使用快速幂方法
     */
    double myPow(double x, int n) {
        long long n2 = n;
        bool flag = false;
        if (n2 < 0) {
            flag = true;
            n2 = -n2;
        }
        double res = 1;
        double tmp = x;
        unsigned t = 1;
        for (int i = 0; i <= 31; ++i) {
            if (t & n2) {
                res *= tmp;
            }
            tmp = tmp * tmp;
            t = t << 1;
        }

        if (flag) {
            return 1 / res;
        } else {
            return res;
        }
    }
};


int main() {
    Solution so;
    cout << so.myPow(2, -2) << endl;
    return 0;
}
