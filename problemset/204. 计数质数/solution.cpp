#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int countPrimes(int n) {
        vector<bool> dp(n, true);
        int ans = 0;
        for (int i = 2; i < n; i++) {
            if(dp[i]){
                ans ++;
                for(int j = 2*i;j<n;j+=i){
                    dp[j] = false;
                }
            }
        }
        return ans;
    }
};

int main() {
    return 0;
}