/*******************************************************************************
 *
 * @file 这是LeetCode文档的注释
 * @author Keven Ge
 * @date 2020-06-30
 * @brief 题目如下
 *      307. 区域和检索 - 数组可修改
 ******************************************************************************/


#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

/**
 * @brief 树节点
 */
struct Node {
    int l;
    int r;
    int sum;

    Node() {
        this->l = 0;
        this->r = 0;
        this->sum = 0;
    }
};


/**
 * @brief 算法类
 */
class NumArray {
private:
    vector<Node> tree;
public:

    NumArray(vector<int> &nums) {
        if(nums.size() == 0){
            return;
        }

        int level = 1;
        for (level = 1; pow(2, level) < nums.size(); level++) {}


        this->tree.assign(pow(2, level) * 2, Node());
        for (int i = 0; i < nums.size(); ++i) {
            this->tree[i + pow(2, level)].sum = nums[i];
            this->tree[i + pow(2, level)].l = i;
            this->tree[i + pow(2, level)].r = i;
        }
        this->build(1, 0, nums.size() - 1);
    }

    void build(int i, int l, int r) {
        this->tree[i].l = l;
        this->tree[i].r = r;
        if (l == r) {
            this->tree[i].sum = this->tree[this->tree.size()/2 + l].sum;
        } else {
            int middle = (l + r) / 2;
            build(i * 2, l, middle);
            build(i * 2 + 1, middle + 1, r);

            this->tree[i].sum = this->tree[i * 2].sum + this->tree[i * 2 + 1].sum;
        }
    }

    void update(int i, int val) {
        if(this->tree.empty()){
            return;
        }

        this->add(1, i, val);
    }

    int sumRange(int i, int j) {
        if(this->tree.empty()){
            return 0;
        }

        return this->search(1, i, j);
    }

    int search(int i, int l, int r) {
        // 返回全部
        if (this->tree[i].l >= l && this->tree[i].r <= r) {
            return this->tree[i].sum;
        }

        if (this->tree[i].l > r || this->tree[i].r < l) {
            return 0;
        }

        int s = 0;
        if (this->tree[i].r > l) {
            s += this->search(2 * i, l, r);
        }

        if (this->tree[i].l < r) {
            s += this->search(2 * i + 1, l, r);
        }

        return s;
    }

    void add(int i, int dis, int val) {
        if (this->tree[i].l == this->tree[i].r) {
            this->tree[i].sum = val;
            return;
        }

        if (this->tree[2 * i].r >= dis) {
            this->add(2 * i, dis, val);
        } else {
            this->add(2 * i + 1, dis, val);
        }
        this->tree[i].sum = this->tree[2 * i].sum + this->tree[2 * i + 1].sum;
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * obj->update(i,val);
 * int param_2 = obj->sumRange(i,j);
 */

int main() {
//    vector<int> nums;
//    nums.push_back(-28);
//    nums.push_back(-39);
//    nums.push_back(53);
//    nums.push_back(65);
//    nums.push_back(11);
//    nums.push_back(-56);
//    nums.push_back(-65);
//    nums.push_back(-39);
//    nums.push_back(-43);
//    nums.push_back(-97);
//
//    NumArray numss(nums);
////    numss.update(9, 27);
////    numss.update(1, -82);
////    numss.update(3, -72);
//
//    cout << numss.sumRange(1, 8) << endl;


    vector<int> nums;
    nums.push_back(1);
    nums.push_back(1);
    nums.push_back(1);
    nums.push_back(1);
    nums.push_back(1);
    nums.push_back(1);
    nums.push_back(1);
    nums.push_back(1);
    nums.push_back(1);
    nums.push_back(1);
    NumArray numss(nums);


    numss.update(0, -1);
    numss.update(1, -1);
    numss.update(2, -1);
    numss.update(3, -1);
    numss.update(4, -1);
    numss.update(5, -1);
    numss.update(6, -1);
    numss.update(7, -1);
    numss.update(8, -1);
    numss.update(9, -1);
    numss.update(10, -1);
    numss.update(11, -1);

    cout << numss.sumRange(0, 9) << endl;
    cout << numss.sumRange(1, 8) << endl;
    return 0;
}