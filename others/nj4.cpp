/******************************************************************************
 * @brief 这是南京大学的机试第4题
 * @author Keven Ge
 * @date 2020-07-03
 *****************************************************************************/



#include <iostream>
#include <algorithm>
#include <string>
#include <set>

using namespace std;


/**
 * @brief 解决问题使用的类
 */
class Solution {
private:

    /**
     * @brief 判断是否是正回文串，如果是，返回true，否则则否
     * @param s
     * @return
     */
    static bool checkIsHuiWen(string s) {
        if (s.length() % 2 == 1) {
            for (int i = 0; i < s.length() / 2; ++i) {
                if (s[i] != s[s.length() - 1 - i]) {
                    return false;
                }
            }
            return true;
        } else {
            return false;
        }
    }

    /**
     * @brief 获取正回文子串的数量
     * @param s 字符串
     * @return 数量
     */
    static int getTrue(const string& s) {
        set<string> sets;
        for (int i = 0; i < s.length(); ++i) {
            for (int len = 1; i + len <= s.length(); len += 2) {
                string t = s.substr(i, len);
                if (sets.find(t) == sets.end() && checkIsHuiWen(t)) {
                    sets.insert(t);
                }
            }
        }
        return sets.size();
    }

    /**
     * @brief 获取非正回文串的数量
     * @param s
     * @return
     */
    static int getFalse(const string& s) {
        set<string> sets;
        for (int i = 0; i < s.length(); ++i) {
            for (int len = 1; i + len <= s.length(); len += 1) {
                string t = s.substr(i, len);
                if (sets.find(t) == sets.end() && !checkIsHuiWen(t)) {
                    sets.insert(s.substr(i, len));
                }
            }
        }
        return sets.size();
    }

public:
    /**
     * @brief 获取结果
     * @param n  字符串的长度
     * @param s  字符串
     * @return 方案的得分
     */
    static int getAnswer(int n, const string& s) {
        int ans = 0;
        for (int i = 1; i < s.length()-1; ++i) {
            int a = getTrue(s.substr(0, i));
//            cout << s.substr(0, i) << ": " << a << endl;
            int b = getFalse(s.substr(i));
//            cout << s.substr(i+1) << ": " << b << endl;
            ans = max(ans, a*b);
        }
        return ans;
    }
};


int main() {
    int n;
    string s;
    cin >> n >> s;
    Solution so;
    cout << Solution::getAnswer(n, s) << endl;
    return 0;
}