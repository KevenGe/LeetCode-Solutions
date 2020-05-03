//
// Created by lenovo on 2020/4/10.
//

/*
 * LeetCode 151
 */

#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    string reverseWords(string s) {
        if (s.empty()){
            return "";
        }


        vector<string> res;
        enum STATE{
            start, chars
        } state;

        state = start;
        string tmp;
        for(char ch:s){
            if(state == start){
                if(ch != ' '){
                    tmp = tmp + ch;
                    state = chars;
                }
            }else if (state == chars){
                if(ch != ' '){
                    tmp = tmp + ch;
                }else{
                    res.push_back(tmp);
                    tmp.clear();
                    state = start;
                }
            }
        }

        if (!tmp.empty()){
            res.push_back(tmp);
        }

        string ans;
        for(auto iter = res.rbegin(); iter !=res.rend();){
            ans += *iter;
            iter ++;
            if (iter == res.rend()){
                break;
            }else{
                ans += " ";
            }
        }
        return ans;
    }
};

int main()
{
    Solution so;
    cout << so.reverseWords(" ");
    return 0;
}