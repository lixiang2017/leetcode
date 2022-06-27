'''
66 / 68 个通过测试用例
状态：超出时间限制
'''
class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        black =  set(blacklist)
        self.white = [i for i in range(n) if i not in black]

    def pick(self) -> int:
        return choice(self.white)


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()


'''
64 / 68 个通过测试用例
状态：超出时间限制
'''
class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        self.n = n 
        self.black =  set(blacklist)

    def pick(self) -> int:
        while True:
            x = randint(0, self.n - 1)
            if x not in self.black:
                return x 


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()




'''
   n - k,                                  k
   i black, n-k-i white              k-i black, i white
   black -> white

hash table

执行用时：268 ms, 在所有 Python3 提交中击败了78.59% 的用户
内存消耗：26.1 MB, 在所有 Python3 提交中击败了24.58% 的用户
通过测试用例：68 / 68
'''

class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        self.white_cnt = n - len(blacklist)
        black = set(b for b in blacklist if b >= self.white_cnt)
        self.b2w = dict()
        white_idx = self.white_cnt
        for b in blacklist:
            if b < self.white_cnt:
                while white_idx in black:
                    white_idx += 1
                self.b2w[b] = white_idx 
                white_idx += 1   #!!!!

    def pick(self) -> int:
        x = randint(0, self.white_cnt - 1)
        return self.b2w.get(x, x)


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()


