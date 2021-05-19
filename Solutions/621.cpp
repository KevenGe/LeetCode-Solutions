#include <iostream>
#include <vector>
#include <algorithm>
#include <stack>

using namespace std;

class Solution {
public:
    int leastInterval(vector<char> &tasks, int n) {
        struct taskNode {
            char ch;
            int times;

            taskNode() {
                times = 0;
            }
        };
        vector<taskNode> tasksVec(26, taskNode());
        for (int i = 0; i < 26; i++) {
            tasksVec[i].ch = char('A' + i);
        }

        for (char task: tasks) {
            tasksVec[int(task) - 'A'].times += 1;
        }

        sort(tasksVec.begin(), tasksVec.end(), [&](taskNode &a, taskNode &b) -> bool {
            return a.times > b.times;
        });

        //show
        for (int i = 0; i < 26; i++) {
            cout << tasksVec[i].ch << ", " << tasksVec[i].times << endl;
        }






        return 0;
    }
};

int main() {
    Solution so;
    vector<char> vec;
    vec.push_back('A');
    vec.push_back('D');
    vec.push_back('C');
    vec.push_back('D');

    cout << so.leastInterval(vec, 2) << endl;

    return 0;
}