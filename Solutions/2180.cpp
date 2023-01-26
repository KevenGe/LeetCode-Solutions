class Solution {
 public:
  int countEven(int num) {
    int count = 0;
    for (int n = 1; n <= num; n++) {
      if (this->valid(n)) {
        count += 1;
      }
    }
    return count;
  }

  bool valid(int n) {
    int s = 0;
    while (n != 0) {
      s += n % 10;
      n = n / 10;
    }
    return s % 2 == 0;
  }
};