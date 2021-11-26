'''
信息论/进制
(轮数 + 1) ** 猪数 >= N桶
如果 N = 1, 只有1桶。那这桶肯定有毒。pig = 0

Estimation: The number of states is exactly (T+1)^x and here is why. For each pig during T tests, it has exactly T+1 states: dies at some test #i, where 1<= i <= T) or still alive eventually. For x pigs, obviously the maximum possible number of states we could have is (T+1)^x since each is independent and one pig can not influence on another one.

执行用时：36 ms, 在所有 Python3 提交中击败了24.11% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了49.65% 的用户
通过测试用例：17 / 17
'''

class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        pig = 0
        round = minutesToTest // minutesToDie + 1
        while round ** pig < buckets:
            pig += 1
        return pig


'''
执行用时：24 ms, 在所有 Python3 提交中击败了94.33% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了21.28% 的用户
通过测试用例：17 / 17
'''
class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        round = minutesToTest // minutesToDie + 1
        return int(ceil(log(buckets, round)))


'''
执行用时：20 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了5.68% 的用户
通过测试用例：17 / 17
'''
from math import ceil, log

class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        round = minutesToTest // minutesToDie + 1
        return ceil(log(buckets) / log(round))
