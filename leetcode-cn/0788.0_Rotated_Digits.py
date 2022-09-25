'''
bit mask(7进制) + brute force(暴力枚举)

执行用时：80 ms, 在所有 Python3 提交中击败了51.61% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了27.42% 的用户
通过测试用例：50 / 50
'''
class Solution:
    def rotatedDigits(self, n: int) -> int:
        choice = [0, 1, 2, 5, 6, 8, 9]
        good_choice = {2, 5, 6, 9}
        nn, digit_cnt = n, 0 
        while nn:
            nn //= 10
            digit_cnt += 1 

        ans = 0
        for mask in range(7 ** digit_cnt):
            x = 0
            isGood = False 
            indice = deque()
            while mask:
                mask, r = divmod(mask, 7)
                indice.appendleft(r)
            for r in indice:
                x *= 10
                x += choice[r]
                if choice[r] in good_choice:
                    isGood = True 
            if isGood and x <= n:
                ans += 1
        return ans
