/*
 * m_01_07
 */

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    void rotate(vector<vector<int>> &matrix) {
        int times = matrix.size() / 2;
        for (int i = 0; i < times; ++i) {
            int lang = matrix.size() - 1 - 2 * i;
            for (int j = 0; j < lang; ++j) {
                int x1 = i;
                int y1 = i + j;
                int x2 = y1;
                int y2 = matrix.size() - 1 - i;
                int x3 = y2;
                int y3 = matrix.size() - 1 - y1;
                int x4 = y3;
                int y4 = x1;


                int tmp = matrix[x1][y1];
                matrix[x1][y1] = matrix[x4][y4];
                matrix[x4][y4] = matrix[x3][y3];
                matrix[x3][y3] = matrix[x2][y2];
                matrix[x2][y2] = tmp;
            }
        }
    }
};

int main() {
    vector<vector<int>>vec;
    vector<int> vec1;
    vec1.push_back(1);
    vec1.push_back(2);
    vec1.push_back(3);
    vec1.push_back(4);
    vec.push_back(vec1);

    vector<int> vec2;
    vec2.push_back(5);
    vec2.push_back(6);
    vec2.push_back(7);
    vec2.push_back(8);
    vec.push_back(vec2);

    vector<int> vec3;
    vec3.push_back(9);
    vec3.push_back(10);
    vec3.push_back(11);
    vec3.push_back(12);
    vec.push_back(vec3);

    vector<int> vec4;
    vec4.push_back(13);
    vec4.push_back(14);
    vec4.push_back(15);
    vec4.push_back(16);
    vec.push_back(vec4);
    for(auto vect : vec){
        for(auto int1: vect){
            cout << int1 << " ";
        }
        cout << endl;
    }

    Solution so;
    so.rotate(vec);

    for(auto vect : vec){
        for(auto int1: vect){
            cout << int1 << " ";
        }
        cout << endl;
    }
    return 0;
}