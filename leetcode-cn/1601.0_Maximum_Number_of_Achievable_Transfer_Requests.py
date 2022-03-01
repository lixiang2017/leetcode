'''
二进制枚举

执行用时：6836 ms, 在所有 Python3 提交中击败了5.17% 的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了96.55% 的用户
通过测试用例：117 / 117
'''
class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        nr = len(requests)
        ans = 0
        for state in range(1, 1 << nr):
            c1 = Counter(bin(state))['1']
            if c1 <= ans:
                continue
                
            move = [0] * n 
            for i in range(nr):
                if state & (1 << i):
                    from_i, to_i = requests[i]
                    move[from_i] -= 1
                    move[to_i] += 1

            if move == [0] * n:
                ans = max(ans, c1)
        return ans

'''
c1 = state.bit_count()

执行用时：1668 ms, 在所有 Python3 提交中击败了44.83% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了96.55% 的用户
通过测试用例：117 / 117
'''
class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        nr = len(requests)
        ans = 0
        for state in range(1, 1 << nr):
            c1 = state.bit_count()
            if c1 <= ans:
                continue

            move = [0] * n 
            for i in range(nr):
                if state & (1 << i):
                    from_i, to_i = requests[i]
                    move[from_i] -= 1
                    move[to_i] += 1

            if move == [0] * n:
                ans = c1
        return ans


'''
if all(m == 0 for m in move):

执行用时：2168 ms, 在所有 Python3 提交中击败了37.93% 的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了100.00% 的用户
通过测试用例：117 / 117
'''
class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        nr = len(requests)
        ans = 0
        for state in range(1, 1 << nr):
            c1 = state.bit_count()
            if c1 <= ans:
                continue

            move = [0] * n 
            for i in range(nr):
                if state & (1 << i):
                    from_i, to_i = requests[i]
                    move[from_i] -= 1
                    move[to_i] += 1

            if all(m == 0 for m in move):
                ans = c1
        return ans


