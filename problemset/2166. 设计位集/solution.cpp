#include <memory>
#include <string>

using namespace std;

class Bitset {
 private:
  int size = 0;
  unique_ptr<int[]> ptr;
  int oneNum = 0;
  int zeroNum = 0;
  int fliped = 0;

 public:
  Bitset(int size) {
    this->size = size;
    this->ptr = make_unique<int[]>(size);

    this->oneNum = 0;
    this->zeroNum = size;
    this->fliped = 0;
  }

  void fix(int idx) {
    if (this->fliped == 1) {
      if (this->ptr[idx] == 1) {
        oneNum -= 1;
        zeroNum += 1;
      }
      this->ptr[idx] = 0;
    } else {
      if (this->ptr[idx] == 0) {
        oneNum += 1;
        zeroNum -= 1;
      }
      this->ptr[idx] = 1;
    }
  }

  void unfix(int idx) {
    if (this->fliped == 1) {
      if (this->ptr[idx] == 0) {
        oneNum += 1;
        zeroNum -= 1;
      }
      this->ptr[idx] = 1;
    } else {
      if (this->ptr[idx] == 1) {
        oneNum -= 1;
        zeroNum += 1;
      }
      this->ptr[idx] = 0;
    }
  }

  void flip() { this->fliped = 1 - this->fliped; }

  bool all() {
    if (this->fliped == 1) {
      return this->zeroNum == this->size;
    } else {
      return this->oneNum == this->size;
    }
  }

  bool one() {
    if (this->fliped == 1) {
      return this->zeroNum >= 1;
    } else {
      return this->oneNum >= 1;
    }
  }

  int count() {
    if (this->fliped == 1) {
      return this->zeroNum;
    } else {
      return this->oneNum;
    }
  }

  string toString() {
    string ans = "";
    for (int i = 0; i < size; i++) {
      if ((this->ptr[i] == 1 && this->fliped == 0) ||
          (this->ptr[i] == 0 && this->fliped == 1)) {
        ans.push_back('1');
      } else {
        ans.push_back('0');
      }
    }
    return ans;
  }
};

/**
 * Your Bitset object will be instantiated and called as such:
 * Bitset* obj = new Bitset(size);
 * obj->fix(idx);
 * obj->unfix(idx);
 * obj->flip();
 * bool param_4 = obj->all();
 * bool param_5 = obj->one();
 * int param_6 = obj->count();
 * string param_7 = obj->toString();
 */