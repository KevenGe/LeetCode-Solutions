# 2043. 简易银行系统
# https://leetcode-cn.com/problems/simple-bank-system/

################################################################################
from typing import List


class Bank:
    def __init__(self, balance: List[int]):
        self.balance = balance

    def _exists(self, account: int) -> bool:
        return 1 <= account <= len(self.balance)

    def _verify(self, account: int, money: int) -> int:
        if self._exists(account):
            return self.balance[account - 1] >= money
        return False

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if (
            self._exists(account1)
            and self._exists(account2)
            and self._verify(account1, money)
        ):
            self.balance[account1 - 1] -= money
            self.balance[account2 - 1] += money
            return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        if self._exists(account):
            self.balance[account - 1] += money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        if self._exists(account) and self._verify(account, money):
            self.balance[account - 1] -= money
            return True
        return False


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)

################################################################################

