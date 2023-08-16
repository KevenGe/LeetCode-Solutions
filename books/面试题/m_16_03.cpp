/*
 * LeetCode m 16.03
 * 面试题 16.03. 交点
 */


#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<double> intersection(vector<int> &start1, vector<int> &end1, vector<int> &start2, vector<int> &end2) {
        double x1 = start1[0];
        double y1 = start1[1];
        double x2 = end1[0];
        double y2 = end1[1];
        double x3 = start2[0];
        double y3 = start2[1];
        double x4 = end2[0];
        double y4 = end2[1];

        // todo 剩余部分
        vector<double> ans;
        if (x2 - x1 == 0) {
            if (x4 - x3 == 0) {
                if (x4 == x2 && !(max(y1, y2) < min(y3, y3) || min(y1, y2) > max(y3, y4))) {
                    ans.push_back(x4);
                    ans.push_back(max(min(y1, y2), min(y3, y4)));
                }
            } else {
                double y_t = ((y4 - y3) / (x4 - x3)) * (x1 - x3) + y3;
                if (y_t <= max(y1, y2) && y_t >= min(y1, y2)) {
                    ans.push_back(x1);
                    ans.push_back(y_t);
                }
            }
        } else {
            if (x4 - x3 == 0) {
                double y_t = ((y2 - y1) / (x2 - x1)) * (x3 - x1) + y1;
                if (y_t <= max(y3, y4) && y_t >= min(y3, y4)) {
                    ans.push_back(x3);
                    ans.push_back(y_t);
                }
            } else {
//                cout << (y2 - y1) / (x2 - x1) << " " << (y4 - y3) / (x4 - x3) << endl;
                if ((y2 - y1) / (x2 - x1) != (y4 - y3) / (x4 - x3)) {
                    double x_t = (y3 - y1) + ((y2 - y1) / (x2 - x1)) * x1 - ((y4 - y3) / (x4 - x3)) * x3;
                    x_t = x_t / ((y2 - y1) / (x2 - x1) - (y4 - y3) / (x4 - x3));
                    double y_t = ((y2 - y1) / (x2 - x1)) * (x_t - x1) + y1;

                    if (x_t <= max(x1, x2) && x_t >= min(x1, x2) && x_t <= max(x3, x4) && x_t >= min(x3, x4)) {
                        if (y_t <= max(y1, y2) && y_t >= min(y1, y2) && y_t <= max(y3, y4) && y_t >= min(y3, y4)) {
                            ans.push_back(x_t);
                            ans.push_back(y_t);
                        }
                    }
                } else if (y3 == ((y2 - y1) / (x2 - x1)) * (x3 - x1) + y1) {
                    if (!(min(x1, x2) > max(x3, x4) || max(x1, x2) < min(x3, x4))) {
                        ans.push_back(max(min(x1, x2), min(x3, x4)));
                        ans.push_back(max(min(y1, y2), min(y3, y4)));
                    }
                }
            }
        }
        return ans;
    }
};

int main() {
    vector<int> start1;
    start1.push_back(12);
    start1.push_back(-55);

    vector<int> end1;
    end1.push_back(59);
    end1.push_back(-60);

    vector<int> start2;
    start2.push_back(4);
    start2.push_back(-55);

    vector<int> end2;
    end2.push_back(81);
    end2.push_back(-62);

    Solution so;
    for (auto x : so.intersection(start1, end1, start2, end2)) {
        cout << x << endl;
    }
    return 0;
}