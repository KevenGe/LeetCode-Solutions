/**
 * 长亭笔试 L题
 *
 */

#include <iostream>
#include <algorithm>
#include <vector>
#include <unordered_map>
#include <string>

using namespace std;


int main() {
    int N, M;
    cin >> N >> M;
    vector<int> times(N);
    vector<vector<int>> attacks;
    unordered_map<string, int> maps;

    string attackTmp;
    for (int i = 0; i < N; i++) {
        cin >> times[i] >> attackTmp;

        for(int j=0;j<attacks.size();j++){
            attacks[j][i] = attacks[j][i-1];
        }
        if (maps.find(attackTmp) == maps.end()) {
            maps.emplace(attackTmp, maps.size());
            attacks.emplace_back(N, 0);
            cin >> attacks[maps[attackTmp]][i];
        } else {
            cin >> attacks[maps[attackTmp]][i];
            attacks[maps[attackTmp]][i] += attacks[maps[attackTmp]][i - 1];
        }
    }

//    for(auto x:attacks){
//        for(auto y:x){
//            cout << y <<" ";
//        }
//        cout << endl;
//    }

    int start;
    int end;
    string attackType;
    for (int i = 0; i < M; i++) {
        cin >> start >> end >> attackType;

        if(maps.find(attackType)==maps.end()){
            cout << 0 << endl;
            continue;
        }


        auto iter = lower_bound(times.begin(), times.end(), start);
        auto iterE = upper_bound(times.begin(), times.end(), end);

//        cout << iterE - times.begin() - 1 << endl;
//        cout << iter - times.begin() - 1<< endl;

        int endIndex = iterE - times.begin() - 1;
        int startIndex = iter - times.begin() - 1;
        if(startIndex < 0){
            cout << attacks[maps[attackType]][endIndex] << endl;
        }else{
            int res =
                    attacks[maps[attackType]][endIndex] - attacks[maps[attackType]][startIndex];
            cout << res << endl;
        }
    };
    return 0;
}