'''
执行用时：248 ms, 在所有 Python3 提交中击败了75.46% 的用户
内存消耗：40.5 MB, 在所有 Python3 提交中击败了77.30% 的用户
通过测试用例：23 / 23
'''
class Bank:

    def __init__(self, balance: List[int]):
        self.b = balance 
        self.n = len(balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if 1 <= account1 <= self.n and 1 <= account2 <= self.n and self.b[account1 - 1] >= money:
            self.b[account1 - 1] -= money 
            self.b[account2 - 1] += money 
            return True
        else:
            return False

    def deposit(self, account: int, money: int) -> bool:
        if 1 <= account <= self.n:
            self.b[account - 1] += money
            return True 
        else:
            return False 

    def withdraw(self, account: int, money: int) -> bool:
        if 1 <= account <= self.n and self.b[account - 1] >= money:
            self.b[account - 1] -= money
            return True 
        else:
            return False 

# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
