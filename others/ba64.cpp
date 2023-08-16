/**
 * 长亭 笔试 J题
 *
 */

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

/**
 * 单个字符，获取其有效的6位数
 * @return
 */
int base64Bin(char &ch) {
    if (ch >= 'A' && ch <= 'Z') {
        return int(ch) - 'A';
    } else if (ch >= 'a' && ch <= 'z') {
        return int(ch) - 'a' + 26;
    } else if (ch >= '0' && ch <= '9') {
        return int(ch) - '0' + 52;
    } else if (ch == '+') {
        return 62;
    } else if (ch == '/') {
        return 63;
    } else if (ch == '=') {
        return 0;
    }
}

vector<int> getBinFromStr(char &ch) {
    int x = base64Bin(ch);
    vector<int> res;
    for (int i = 0; i < 6; i++) {
        if (x & 1) {
            res.push_back(1);
        } else {
            res.push_back(0);
        }
        x = x >> 1;
    }
    reverse(res.begin(), res.end());
    return res;
}

/**
 * Base 转化为相应的数组
 * @param s
 * @return
 */
vector<int> base64ToVector(string &s) {
    int n = s.length() / 4;
    vector<int> res;
    int tmp2 = pow(2, 6);
    for (int i = 0; i < s.length(); i += 4) {
        int tmp = 0;
        unsigned t1 = base64Bin(s[i]);
        unsigned t2 = base64Bin(s[i + 1]);
        unsigned t3 = base64Bin(s[i + 2]);
        unsigned
        t4 = base64Bin(s[i + 3]);

        res.push_back((t1 << 2) + (t2 >> 4));
        res.push_back(((t2 << 28)>>24) + (t3 >> 2));
        res.push_back(((t3 << 30) >> 24) + (t4));
    }

    // 处理 =
    for (int i = 0; i < 4; i++) {
        if (s[s.length() - 1 - i] == '=') {
            res.pop_back();
        } else {
            break;
        }
    }

//    for (auto x:res) {
//        cout << x << endl;
//    }

    return res;
}

char decToJ36(int x) {
    if (x < 10) {
        return char(x + '0');
    } else {
        return char(x - 10 + 'A');
    }
}

vector<int> strDivBy36(vector<int> &s) {
    vector<int> results;
    int reminder = 0;

    for (int i = 0; i < s.size(); i++) {
        int c = s[i] + reminder * 256;
        int result = c / 36;
        reminder = c % 36;
        results.push_back(result);
    }

    results.push_back(reminder);
    return results;
}

string strToJ36(vector<int> &s) {
    vector<int> results;
    for (auto x:s) {
        results.push_back(int(x));
    }

    string res = "";

    while (true) {
//        for(auto x:results){
//            cout << x << endl;
//        }

        results = strDivBy36(results);
        res = decToJ36(results.back()) + res;
        results.pop_back();

        while (results.size() != 0) {
            if (results[0] == 0) {
                results.erase(results.begin());
            } else {
                break;
            }
        }
        if (results.size() == 0) {
            break;
        }
    }
    return res;
}


int main() {
    string s;
    cin >> s;
//    s = "cGFzc3dvcmQgaXMgQWRtaW4xMjM0NTY=";
    vector<int> t = base64ToVector(s);
    cout << strToJ36(t) << endl;
    return 0;
}