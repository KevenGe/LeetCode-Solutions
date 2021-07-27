/**
 * @brief 未完成
 */

#include <iostream>
#include <climits>

using namespace std;

class Solution {
public:
    int divide(int dividend, int divisor) {
        if (dividend == 0) {
            return 0;
        }
        if (divisor == -1) {
            if (dividend > INT_MIN) {
                return -dividend;
            }
            return INT_MAX;
        }
        if (divisor == 1) {
            return dividend;
        }

        bool sign = true;
        if ((dividend > 0 && divisor < 0) || (dividend < 0 && divisor > 0)) {
            sign = false;
        }

        long a = dividend;
        a = a > 0 ? a : -a;
        long b = divisor;
        b = b > 0 ? b : -b;

        int ans = myDiv(a, b);
        ans = sign ? ans : -ans;
        return ans;
    }

    int myDiv(long a, long b) {
        if (a < b) {
            return 0;
        }

        int t = b;

        long count = 1;
        while (a >= b + b) {
            count += count;
            b += b;
        }
        return count + myDiv(a - b, t);
    }
};

void run(){
    Solution so;
    cout << so.divide(-2147483648,-2147483648) << endl;
}

int main() {
    run();
    return 0;
}