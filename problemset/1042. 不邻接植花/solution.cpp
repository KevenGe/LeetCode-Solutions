//
// Created by lenovo on 2020/6/8.
//

/**
 * 染色问题？
 */


#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> gardenNoAdj(int N, vector<vector<int>> &paths) {
        vector<vector<int> > vec(N);
        vector<int> res(N, 0);
        for (auto path:paths) {
            vec[path[0] - 1].push_back(path[1]);
            vec[path[1] - 1].push_back(path[0]);
        }

        for (int i = 0; i < N; ++i) {
            dfs(vec, res, i);
        }
        return res;
    }

    void dfs(vector<vector<int>> &vec, vector<int> &res, int i) {
        int color[4] = {0};
        for (auto x:vec[i]) {
            if (res[x - 1] != 0) {
                color[res[x - 1] - 1] = 1;
            }
        }
        for (int j = 0; j < 4; ++j) {
            if (color[j] == 0) {
                res[i] = j + 1;
                break;
            }
        }
    }
};

int main() {
    vector<vector<int>> vec;
    vector<int> vec1;
    vec1.push_back(1);
    vec1.push_back(2);
    vec.push_back(vec1);

    vector<int> vec2;
    vec2.push_back(3);
    vec2.push_back(4);
    vec.push_back(vec2);

//    vector<int> vec3;
//    vec3.push_back(3);
//    vec3.push_back(1);
//    vec.push_back(vec3);


    Solution so;
    for (auto x:so.gardenNoAdj(4, vec)) {
        cout << x << endl;
    }
    return 0;
}