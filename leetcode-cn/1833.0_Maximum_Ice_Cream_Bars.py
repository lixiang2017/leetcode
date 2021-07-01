'''
Sort

执行用时：164 ms, 在所有 Python3 提交中击败了54.79% 的用户
内存消耗：24.9 MB, 在所有 Python3 提交中击败了7.24% 的用户
'''

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        for i in range(len(costs)):
            coins -= costs[i]
            if coins < 0:
                return i
                
        return len(costs)


'''
Counter / Hash Table

执行用时：428 ms, 在所有 Python3 提交中击败了5.01% 的用户
内存消耗：24.8 MB, 在所有 Python3 提交中击败了62.71% 的用户
'''
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        freq = [0 for _ in range(10**5 + 1)]
        for cost in costs:
            freq[cost] += 1
        
        buy = 0
        i = 1
        while coins >= i and i <= 10**5:
            curCount = min(freq[i], coins // i)
            buy += curCount
            coins -= curCount * i
            i += 1

        return buy