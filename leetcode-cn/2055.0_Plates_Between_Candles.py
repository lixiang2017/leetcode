'''
two passes + prefix sum
T: O(2 * len(s) + len(queries))
S: O(3 * len(s) + len(queries))

执行用时：272 ms, 在所有 Python3 提交中击败了91.41% 的用户
内存消耗：43.4 MB, 在所有 Python3 提交中击败了40.49% 的用户
通过测试用例：35 / 35
'''
class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        # for every i, left most candle postion, right most candle position
        left, right = [-1] * n, [n] * n
        total_candle, seen_left, seen_right = 0, -1, n
        # for every i, pre sum for count candles
        pre_cnt = [0] * n
        for i in range(n):
            if s[i] == '|':
                total_candle += 1
                seen_left = i 
                pre_cnt[i] = total_candle
            left[i] = seen_left
        
        for i in range(n - 1, -1, -1):
            if s[i] == '|':
                seen_right = i 
            right[i] = seen_right

        qn = len(queries)
        ans = [0] * qn 
        for j, (l, r) in enumerate(queries):
            # xxxx.|....xxxx.||...........|...xxxx
            #   right[l]             left[r]
            if left[r] > right[l]:
                interval = left[r] - right[l] + 1
                candle = pre_cnt[left[r]] - pre_cnt[right[l]] + 1
                star = interval - candle
                ans[j] = star 

        return ans 

