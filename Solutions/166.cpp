//
// Created by lenovo on 2020-09-30.
//

#include <iostream>
#include <string>
#include <vector>
#include <unordered_set>
#include <unordered_map>

using namespace std;

class Solution {
public:
    string fractionToDecimal(long long  numerator, long long denominator) {
        int sign = 1;
        if ((numerator < 0 && denominator > 0) || (numerator > 0 && denominator < 0)) {
            sign = -1;
            numerator = numerator > 0 ? numerator : -numerator;
            denominator = denominator > 0 ? denominator : -denominator;
        }

        string ans = "";
        long long a = 0;
        long long b = 0;

        a = numerator / denominator;
        b = numerator % denominator;
        ans += to_string(a);
        ans += b == 0 ? "" : ".";

        unordered_map<int, int> aHistory;
        aHistory.emplace(numerator, -1);

        int position = to_string(a).length() + 1;

        while (b) {
            b = b * 10;
            if (aHistory.find(b) != aHistory.end()) {
                ans.insert(aHistory[b], "(");
                ans += ")";
                break;
            }
            aHistory.emplace(b, position);
            position += 1;
            a = b / denominator;
            b = b % denominator;
            ans += to_string(a);
        }
        ans = (sign == 1 ? "" : "-") + ans;
        return ans;
    }
};

void runTest() {
    Solution so;
    cout << so.fractionToDecimal(1, 3);
}

int main() {
    runTest();
    return 0;
}